# Device Bridge

Stellar X connects to the rest of the robot through network ports only. Sensors that need USB, such as an Intel RealSense depth camera or a USB IMU, therefore go on a small computer next to them: a Raspberry Pi, another single-board computer or a PC. The **Device Bridge** runs on that computer. It reads the devices and serves their data to the controller over the LAN.

The bridge speaks the same network protocol as Isaac Bridge, so the controller's built-in Camera gateway, IMU gateway, Visual odometry, Localizer and Navigator connect to real sensors the same way as to a simulated robot: they connect to the sensor computer instead of the Isaac Sim computer. Real sensors still need their own values: camera intrinsics, mounting and synchronized clocks.

Use the Device Bridge when:

- the robot carries a USB camera or IMU, which cannot plug into the controller;
- the motor board of a small robot sits on USB as well (for example the TurtleBot3 OpenCR board) and the controller should drive it.

Drives on the controller's EtherCAT port do not need the bridge, and neither does a simulated robot.

| You want to                                                                                    | Page                                                                                                               |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Connect a RealSense D400 camera, a TurtleBot3 OpenCR board, or try the bridge without hardware | This page: install the bridge and use its built-in drivers                                                         |
| Connect another camera, IMU or wheel board                                                     | [Write Device Bridge Drivers](https://docs.sodero.io/v2.0.0/extend/device_bridge_drivers/index.md), then this page |

The Device Bridge is an open-source program. Nothing changes on the controller when you install it or add a driver.

______________________________________________________________________

## 1. Architecture

```
flowchart TB
    subgraph SC ["Sensor computer"]
        DB(["Device Bridge"])
        RS["RealSense<br>depth camera"] --> DB
        IU["USB IMU"] --> DB
        MB["Motor board<br>(optional)"] <--> DB
    end
    subgraph SX ["Stellar X · Stellar Station"]
        CG["Camera gateway"]
        IG["IMU gateway"]
        AG["Actuator gateway<br>(optional)"]
        VO["Visual odometry"]
        LO["Localizer"]
        NV["Navigator"]
        ST["Strider"]
    end
    DB -->|"53335 · RGB-D frames"| CG
    DB -->|"53334 · IMU samples"| IG
    DB <-->|"53333 commands · 53334 joint states"| AG
    CG --> VO
    IG --> VO
    CG --> LO
    VO -->|odometry| LO
    LO -->|"localization · map"| NV
    NV -->|mobile_base| ST
    AG <-->|servo_link| ST
```

The bridge **listens** on three ports and the controller's gateways **connect** to it, exactly as they connect to the simulator. Every message carries the bridge's `robot_name`, and each gateway takes the data published under the name it is configured with. Without the optional wheel stream, Strider drives the robot's own base through an EtherCAT Actuator gateway as usual.

______________________________________________________________________

## 2. Requirements

| Item            | Requirement                                                                                                                                                                                                            |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sensor computer | A Raspberry Pi, another single-board computer or a PC next to the sensors, running 64-bit Linux with systemd (for example Debian 12, Raspberry Pi OS or Ubuntu). A RealSense camera needs a USB 3 port.                |
| Python          | Python 3.8 or later. The installer creates its own environment; when the system Python cannot load the RealSense SDK (for example Debian 12 on 64-bit ARM), it installs a standalone Python 3.10 by itself.            |
| Internet        | During installation only, to download the Python packages                                                                                                                                                              |
| Network         | The sensor computer and Stellar X on the same LAN; a wired link is recommended                                                                                                                                         |
| Clocks          | Synchronized to within about 20 ms while frames carry their capture time (the default)                                                                                                                                 |
| Firewall        | Inbound TCP ports 53333–53335 on the sensor computer open to the controller                                                                                                                                            |
| IMU address     | Only for an IMU stream: the controller's IMU gateway connects to a sensor address that Sodero support sets for the unit. Ask Sodero support to set it to the sensor computer before you connect the IMU ([IMU](#imu)). |

**Bandwidth.** RGB-D frames travel uncompressed: about 61 Mbit/s at 424 × 240 and 15 fps, about 185 Mbit/s at 640 × 480 and 15 fps, and about 370 Mbit/s at 640 × 480 and 30 fps. IMU samples and wheel messages add only a few Mbit/s. Use a wired link, ideally Gigabit Ethernet, for the higher settings.

**Clock synchronization.** With `send_capture_time: true` (the default), every frame carries its capture time. The controller accepts a frame only when that time is at most 20 ms ahead of its own clock and at most 2 s old, so run NTP (for example chrony) to keep both computers on the same time. If you cannot synchronize the clocks, set `send_capture_time: false`: the controller then uses each frame's arrival time, as with the simulator. This needs no clock agreement and costs the network delay in accuracy.

**Tip:** On a sensor computer that runs ufw, open the ports for the controller with `sudo ufw allow from ROBOT_ADDRESS to any port 53333:53335 proto tcp`.

______________________________________________________________________

## 3. Install and Run

1. **Get the source** on the sensor computer:

   ```
   git clone https://github.com/Sodero-labs/device_bridge.git
   cd device_bridge
   ```

   You can also copy the `device_bridge` folder to the sensor computer by other means, for example with `scp -r` from your PC.

1. **Choose a configuration.** Copy the example closest to your hardware, for example `cp config/turtlebot3_d435.yaml config/my_robot.yaml`, and edit it as described in [Configuration File](#configuration-file). `config/turtlebot3_d435.yaml` serves a RealSense D435 and the IMU of a TurtleBot3 OpenCR board, with the wheel stream prepared but commented out; `config/simulated.yaml` needs no hardware.

1. **Install and start** the service:

   ```
   sudo deploy/install.sh config/my_robot.yaml
   ```

   The installer copies the program and your configuration to `/opt/sodero-device-bridge` (as `config.yaml`), creates a Python environment there and installs the `sodero-device-bridge` service. The service starts now and at every boot, and restarts 3 seconds after an error. It runs as the user who called `sudo`, with access to serial ports, USB devices and cameras.

1. **Follow the log** with `journalctl -u sodero-device-bridge -f` and look for the lines in [Log Lines](#log-lines).

1. **Check the streams** from another computer, as described in [Check from Another Computer](#check-from-another-computer).

To change a setting later, edit `/opt/sodero-device-bridge/config.yaml` and run `sudo systemctl restart sodero-device-bridge`.

Running `install.sh` again, for example after `git pull`, replaces `/opt/sodero-device-bridge/config.yaml` with the file you pass. Keep your configuration in your own file and pass it every time.

### Configuration File

The configuration names the robot, lists the devices on this computer and states which stream each device feeds. Every stream is optional; the bridge opens only the ports of the streams you configure.

```
robot_name: tb3              # the controller finds this robot's data under this name

network:                     # optional; these are the defaults
  bind: 0.0.0.0              # every interface, or this computer's LAN address
  command_port: 53333        # controller -> bridge: wheel commands
  state_port: 53334          # bridge -> controller: IMU samples and wheel states
  camera_port: 53335         # bridge -> controller: RGB-D frames and intrinsics

state_poll_hz: 200           # optional; how often the IMU and wheel devices are read

devices:                     # the hardware, each under a name you choose
  d435:
    driver: realsense        # a built-in driver
    serial: auto             # every other key is an option of the driver
    width: 424
    height: 240
    fps: 15
  opencr:
    driver: turtlebot3_opencr
    port: /dev/turtlebot3_opencr
    max_linear_speed: 0.15   # m/s
    max_angular_speed: 1.0   # rad/s

streams:                     # what the controller receives
  camera:
    device: d435
    frame_id: cam0_optical   # the camera frame named in the map bundle
    send_capture_time: true  # needs synchronized clocks; false = arrival time
  imu:
    device: opencr           # one device can feed several streams
  wheels:                    # only when the controller drives these wheels
    device: opencr
    command_timeout_s: 0.5   # stop the wheels when commands pause this long
```

| Key                                | Default        | Description                                                                                                                                            |
| ---------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `robot_name`                       | required       | Name under which the bridge publishes. The Station's gateways use the same name.                                                                       |
| `network.bind`                     | `0.0.0.0`      | Address the bridge listens on. Enter the sensor computer's LAN address to restrict it to one interface.                                                |
| `network.camera_port`              | `53335`        | RGB-D frames. Must match the Camera gateway's **Port**.                                                                                                |
| `network.state_port`               | `53334`        | IMU samples and wheel states. Keep the default: the IMU and Actuator gateways expect it.                                                               |
| `network.command_port`             | `53333`        | Wheel commands. Keep the default.                                                                                                                      |
| `state_poll_hz`                    | `200`          | How often the IMU and wheel drivers are polled, per second                                                                                             |
| `devices.<name>.driver`            | required       | A [built-in driver](#4-built-in-drivers) or your own class as `package.module:Class`. All other keys of the block are passed to the driver as options. |
| `streams.camera.device`            | —              | The device that provides the camera                                                                                                                    |
| `streams.camera.frame_id`          | `cam0_optical` | Optical frame name sent with each frame, 1 to 15 bytes                                                                                                 |
| `streams.camera.send_capture_time` | `true`         | Send each frame's capture time. `false`: the controller uses the arrival time.                                                                         |
| `streams.imu.device`               | —              | The device that provides the IMU                                                                                                                       |
| `streams.wheels.device`            | —              | The device that drives the wheels. Leave the stream out when the controller drives its own base.                                                       |
| `streams.wheels.command_timeout_s` | `0.5`          | Stop the wheels when commands pause this long, in seconds                                                                                              |

Unknown keys are refused, so a typo stops the bridge with a clear message instead of being ignored. The configuration needs at least one device and one stream, and each stream must name a listed device that provides it.

**Tip:** Choose a `robot_name` of lowercase letters, digits and underscores that starts with a letter, such as `tb3`. Every Station node accepts such a name, so the gateway nodes can carry the same name.

### Log Lines

After a start with `config/turtlebot3_d435.yaml` (camera and IMU, no wheel stream), the log shows these lines (time stamps left out):

```
INFO device_bridge: device 'd435' (realsense) is open
INFO device_bridge: device 'opencr' (turtlebot3_opencr) is open
INFO device_bridge.bridge: camera 424x240 fx=303.22 fy=303.26 cx=216.20 cy=123.18 frame_id=cam0_optical (use these intrinsics in the controller's camera settings)
INFO device_bridge.bridge: serving robot 'tb3' on 0.0.0.0 (camera 53335, state 53334, command -)
INFO device_bridge: camera_pair 15.0/s, imu_state 50.0/s, sim_state 0.0/s, sim_command 0.0/s
```

| Line                                                              | Meaning                                                                                           |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `device '…' (…) is open`                                          | The driver has connected to its hardware.                                                         |
| `camera 424x240 fx=… fy=… cx=… cy=…`                              | The camera's resolution and intrinsics. Enter them in the Camera gateway (see [Camera](#camera)). |
| `serving robot 'tb3' on … (camera 53335, state 53334, command -)` | The robot name and the ports served. `-` marks a stream that is not configured.                   |
| `camera_pair 15.0/s, imu_state 50.0/s, …`                         | Message rates, every 10 seconds. `sim_command` counts the commands received from the controller.  |

If the configuration or a device fails, the log shows one `ERROR` line that names the problem, and the service tries again 3 seconds later.

### Check from Another Computer

`listen` receives the streams the way the controller does. Run it from a copy of the source on any computer on the same network, for example your PC:

```
cd device_bridge
python3 -m venv .venv && . .venv/bin/activate
pip install numpy pyzmq PyYAML
python -m device_bridge.listen SENSOR_COMPUTER_ADDRESS --robot tb3
```

It prints one line per message kind with its rate and latest values, for example:

```
camera_info     1.0/s  width=424 height=240 fx=303.217 fy=303.257 cx=216.198 cy=123.175
camera_pair    15.0/s  424x240, depth valid 91%, median 1480 mm, capture age 9 ms (meaningful with synchronized clocks)
imu_state      50.0/s  gyro [+0.002, -0.001, +0.000] rad/s, |accel| 9.80 m/s^2
```

To test the wheels, add `--wheels` with one speed per wheel in rad/s, for example `--wheels 1.0 1.0 --seconds 2`. `listen` drives them for `--seconds` and then releases them the way the controller does.

`--wheels` moves the robot. Lift the wheels off the ground or give the robot room, and stop the Station's Actuator gateway for this robot first.

### Try Without Hardware

`config/simulated.yaml` serves a test-pattern camera, a slowly turning IMU and two ideal wheels under the robot name `tb3`. Use it to try the network, the Station's gateway settings and `listen` before the hardware is ready. Install it as a service, or run it in the foreground in the environment from the previous section:

```
sudo deploy/install.sh config/simulated.yaml     # as a service
python -m device_bridge config/simulated.yaml    # or in the foreground; stop with Ctrl+C
```

______________________________________________________________________

## 4. Built-in Drivers

| Driver                 | Provides                     | Options (default)                                                                                                                                               |
| ---------------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `realsense`            | Camera                       | `serial` (`auto`), `width` (`424`), `height` (`240`), `fps` (`15`)                                                                                              |
| `turtlebot3_opencr`    | IMU and wheels (left, right) | `port` (`/dev/turtlebot3_opencr`), `poll_hz` (`100`, 20 to 100), `max_linear_speed` (`0.15` m/s, at most 0.22), `max_angular_speed` (`1.0` rad/s, at most 2.84) |
| `simulated_camera`     | Camera                       | `width` (`424`), `height` (`240`), `fps` (`15`)                                                                                                                 |
| `simulated_imu`        | IMU                          | `rate_hz` (`100`), `yaw_rate` (`0.1` rad/s)                                                                                                                     |
| `simulated_wheels`     | Wheels                       | `joints` (`2`), `rate_hz` (`100`)                                                                                                                               |
| `package.module:Class` | What the class provides      | Your own driver ([Write Device Bridge Drivers](https://docs.sodero.io/v2.0.0/extend/device_bridge_drivers/index.md))                                            |

- **`realsense`** reads Intel RealSense D400 cameras through the RealSense SDK and is tested with the D435. Depth is aligned to the color image, so both share the color camera's intrinsics. With `serial: auto`, exactly one camera must be connected; with several cameras, enter the serial number.
- **`turtlebot3_opencr`** drives the OpenCR board of a TurtleBot3 Burger running the ROBOTIS TurtleBot3 ROS 2 firmware. The board is both the wheel controller and the IMU, and its serial port can have only one owner, so one device feeds both the `imu` and the `wheels` stream. Wheel speeds are scaled down together to the configured limits, which keeps the path's curvature. If the bridge stops talking to the board, the firmware stops the wheels by itself within 0.5 s. Set `port` to the board's serial device (for example `/dev/ttyACM0`) when the default device name does not exist on your system.
- **`simulated_camera`**, **`simulated_imu`** and **`simulated_wheels`** stand in for hardware: a moving color pattern in front of a flat wall 2 m away, a level sensor turning slowly about its z axis, and joints that follow their velocity commands exactly.

______________________________________________________________________

## 5. Connect It on the Station Page

Start with the bridge running and `listen` showing its streams, then open the Station page (`http://ROBOT_ADDRESS`). The steps use the robot name `tb3`; use your bridge's `robot_name` instead.

**Names must match.** The Camera gateway's **Camera name**, the IMU gateway's **Robot in World** and the Actuator gateway's **Robot name** must all be exactly the bridge's `robot_name`. Each gateway takes only the data published under its name.

### Camera

1. Click **Add node**, choose **Gateway** › **Camera gateway** and name it after the robot, for example `tb3` (node `rc.camera_gateway.tb3`).

1. In the **CAMERA GATEWAY** section of the inspector, enter:

   - **Camera name**: the bridge's `robot_name` (`tb3`). The bridge publishes its camera under the robot name; it has no separate camera name.
   - **Camera host**: `SENSOR_COMPUTER_ADDRESS`.
   - **Port**: `53335`, or the bridge's `network.camera_port`.

1. Enter the resolution and intrinsics from the bridge's `camera …` log line. A new Camera gateway computes its intrinsics from a field of view, as for a simulated camera, so for intrinsics its **CAMERA SETTINGS** show *horizontal fov deg* but not fx, fy, cx and cy. Load the calibrated values once with **Upload yaml** while the node is stopped:

   ```
   camera_gateway:
     camera:
       type: isaac_zmq              # the simulator's stream format, which the bridge speaks
       frame_id: cam0_optical       # the bridge's streams.camera.frame_id
       width: 424                   # resolution from the log line
       height: 240
       fps: 15
       isaac:
         robot_name: tb3            # Camera name: the bridge's robot_name
         host: SENSOR_COMPUTER_ADDRESS
         port: 53335
       intrinsics:
         mode: manual               # use fx, fy, cx, cy instead of a field of view
         fx: 303.22
         fy: 303.26
         cx: 216.20
         cy: 123.18
   ```

   After the upload, **CAMERA SETTINGS** shows these values and you can change them there later. Check that **Camera name**, **Camera host** and **Port** show your values.

1. Click **Start**.

Intrinsics belong to one resolution. After you change the bridge's `width`, `height` or camera, enter the new values from its log line.

**Tip:** In the [SSH workspace](https://docs.sodero.io/v2.0.0/ssh_workspace/overview/index.md), `sodero camera snapshot rc.camera_gateway.tb3 --output frame.png` saves a picture from the gateway.

### IMU

1. Click **Add node**, choose **Gateway** › **IMU gateway** and name it after the robot (`tb3`).
1. In **IMU SETTINGS**, check that **Robot in World** is the bridge's `robot_name` (a new IMU gateway starts with its node name) and click **Save settings**.
1. Start the gateway.

The IMU gateway has no address field: it connects to the sensor address that Sodero support sets for the unit ([Requirements](#2-requirements)).

### Wheels (Optional)

Only when the bridge serves a `wheels` stream:

1. Add an **Actuator gateway** and load a simulation `.gw` (`hardware.type: simulation`) whose joints are the bridge's wheels, in the same order (`turtlebot3_opencr`: left, then right).
1. In its **TARGET** section, click **Change**, enter **Robot name** `tb3` and **Sim host** `SENSOR_COMPUTER_ADDRESS`, and click **Done**.
1. Add **Strider** with your base's `.sddm` and connect its `servo_link` to the Actuator gateway's `servo_link`.
1. Drive slowly at first, with the wheels off the ground.

The bridge stops and releases the wheels when the controller switches its drive off and when commands pause for longer than `command_timeout_s`. Keep someone ready to stop the robot during the first runs.

### Navigation and Mounting

1. Add **Visual odometry**, **Localizer** and **Navigator** and connect them as for any robot: the Camera gateway's `camera` to Visual odometry and the Localizer, the IMU gateway's `imu` to Visual odometry, Visual odometry's (or Strider's) `odometry` to the Localizer, the Localizer's `localization` and `map` to the Navigator, and Strider's `mobile_base` to the Navigator.
1. Upload the map bundle (`.nav`) once to the Localizer. The Navigator uses the same shared bundle ([Load and Configure a Map](https://docs.sodero.io/v2.0.0/navigation/map_bundle/index.md)).

The bridge sends camera and IMU data in the sensors' own frames. Where the sensors sit on the robot, their mounting extrinsics, belongs in the map bundle ([Load and Configure a Map](https://docs.sodero.io/v2.0.0/navigation/map_bundle/#3-check-the-values-for-the-first-run)): measure the mounting and enter it there, and do not rotate data inside a driver. Keep the bridge's `frame_id`, the Camera gateway's *frame id* and the camera frame of the map bundle the same (default `cam0_optical`).

______________________________________________________________________

## 6. Troubleshooting

| Symptom                                                                                                          | Cause                                                                                                                                                                                                         | Fix                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| The service restarts every few seconds and the log shows one `ERROR` line                                        | A configuration or device problem named in that line, such as an unknown key, a stream without its device, `RealSense … is not connected` or `no reply from the board`                                        | Fix the configuration or the connection, then restart the service                                               |
| `listen` prints `no messages from … for robot '…'`                                                               | The bridge is not running, `--robot` differs from `robot_name`, or a firewall blocks the ports                                                                                                                | Check `systemctl status sodero-device-bridge`, use the name from the `serving robot` line, open TCP 53333–53335 |
| Camera gateway: `Waiting for simulator at …:53335`                                                               | Wrong **Camera host** or **Port**, no camera stream, or a firewall                                                                                                                                            | Compare with the `serving robot` line and run `listen` from another computer                                    |
| Camera gateway: `… publishes frames of camera(s) 'tb3' but none of camera '…'`                                   | **Camera name** differs from `robot_name`                                                                                                                                                                     | Set **Camera name** to `robot_name`, then Stop and Start                                                        |
| Camera gateway: `Frames … are stale or carry capture times that do not match this Station's clock (clock skew?)` | The clocks differ: frames look more than 20 ms in the future or more than 2 s old                                                                                                                             | Synchronize the clocks with NTP, or set `send_capture_time: false` and restart the bridge                       |
| Visual odometry drifts or the Localizer does not fit the map                                                     | Field-of-view intrinsics instead of the calibrated ones, or values for another resolution                                                                                                                     | Upload the intrinsics from the bridge's log line for the current resolution                                     |
| The IMU gateway does not start: `Start the project World to provide the simulation IMU endpoint.`                | No simulator/sensor address is configured for the unit                                                                                                                                                        | Ask Sodero support to set it to the sensor computer                                                             |
| The IMU gateway runs, but no IMU data arrives                                                                    | **Robot in World** differs from `robot_name`, the bridge has no `imu` stream (`state -`), or the unit's address points to another computer                                                                    | Fix the name or the stream; check the address with Sodero support                                               |
| The wheels do not move                                                                                           | No `wheels` stream (`command -`), a different **Robot name**, commands that are not velocity commands (`modes … are not velocity control`), or the OpenCR motor power is off (`wheel motors are not powered`) | Add the stream, fix the name, drive Strider in **Twist** mode, switch on the motor power                        |
| The wheels stop while driving; log: `no wheel command for 0.50 s: wheels stopped`                                | The safety watchdog: commands paused longer than `command_timeout_s`                                                                                                                                          | Use a wired link; raise `command_timeout_s` only with care                                                      |
| The `camera_pair` rate stays below `fps`                                                                         | Not enough bandwidth (Wi-Fi), a USB 2 port or a busy sensor computer                                                                                                                                          | Use a wired link and a USB 3 port, or lower `width`, `height` or `fps`                                          |
| **Camera host** cannot be edited                                                                                 | The camera address is set for this unit                                                                                                                                                                       | Ask Sodero support to point it at the sensor computer                                                           |
