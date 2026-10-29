# Connect to Stellar Station

With Isaac Bridge installed and the robot prepared, point the Station's gateways at Isaac Sim and drive the robot.

______________________________________________________________________

## 1. Play the Scene

1. Open the scene in Isaac Sim and press **Play**.
1. Open **Window › Isaac Bridge** and check that the ports are **serving** and your robot is **bound**.

① ports serving ② robots bound ③ cameras served ④ Rescan

______________________________________________________________________

## 2. Set the Gateways on the Station

Set the Station nodes to match Isaac Sim:

| Isaac Sim                    | Station node                  | Field                                                                              |
| ---------------------------- | ----------------------------- | ---------------------------------------------------------------------------------- |
| Robot `jackal`               | Actuator gateway (simulation) | **TARGET › Robot name** `jackal`                                                   |
| The Isaac Sim computer       | Actuator gateway (simulation) | **TARGET › Sim host**: the computer's IP address                                   |
| Camera `cam0`                | Camera gateway                | **Camera name** `cam0`, **Camera host**: the computer's IP address, **Port** 53335 |
| Robot `jackal` (with an IMU) | IMU gateway                   | **Robot in World** `jackal`                                                        |

The IMU gateway has no host field: it connects to the simulator address configured for your controller, which Sodero support sets ([Sensors and Cameras](https://docs.sodero.io/stellar-x/v2.0.3/gateways/sensors_and_cameras/#2-imu-gateway)).

**The Robot name on the Station must be exactly the robot's prim name in Isaac Sim.** Names are case-sensitive. If they differ, the gateway keeps waiting and the robot never moves.

Robot name and Sim host of a simulation gateway

How to create the gateways and their documents: [Simulation Gateway](https://docs.sodero.io/stellar-x/v2.0.3/gateways/simulation/index.md), [Sensors and Cameras](https://docs.sodero.io/stellar-x/v2.0.3/gateways/sensors_and_cameras/index.md).

______________________________________________________________________

## 3. Start and Drive

1. Start the gateways, then the controllers ([Running Nodes](https://docs.sodero.io/stellar-x/v2.0.3/station/running_nodes/index.md)).
1. Each simulation gateway logs *Simulator connected.*
1. Open the controller's UI, switch the servo on, and jog: [Strider](https://docs.sodero.io/stellar-x/v2.0.3/controllers/strider/index.md) for mobile bases, [Motion Studio](https://docs.sodero.io/stellar-x/v2.0.3/controllers/motion_studio/index.md) for manipulators.

The Jackal jogged from Strider

______________________________________________________________________

## 4. Stop, Pause and Play

The gateways treat Isaac Sim like a power supply of real drives:

| In Isaac Sim                            | Result                                                                                                                                                                                                                                                                                                                     |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Pause**                               | The robots stay where they are. The gateways see the simulator stop and switch the servo off; switch it on again after you resume.                                                                                                                                                                                         |
| **Stop**, then **Play**                 | A new session: the robots start again at their authored pose, as after a power cycle. Switch the servo on again.                                                                                                                                                                                                           |
| Editing the scene while it plays        | Takes effect at the next **Play**, or click **Rescan** in the Isaac Bridge window                                                                                                                                                                                                                                          |
| Closing Isaac Sim and starting it again | The gateways lose the simulator, and the controllers stop the robots. When the scene plays again, restart the robot's nodes from the toolbar: **Stop all nodes**, then **Start all nodes** ([Running Nodes](https://docs.sodero.io/stellar-x/v2.0.3/station/running_nodes/#2-start-all-nodes)). Switch the servo on again. |

After the simulation restarts, the robot is back at its starting pose, but the Localizer may still hold its last pose. If Strider's Navigation page shows a wrong pose, set the initial pose again.

______________________________________________________________________

## 5. Several Robots

One scene can hold several robots. Add one gateway (and controller) per robot on the Station, each with its own **Robot name**. All gateways use the same Isaac Sim computer and ports; the status window lists every robot it serves.

A robot can also be driven by several gateways, for example an arm and its gripper. Each gateway drives its own range of joints, set by its **DOF offset** ([Gateway Designer](https://docs.sodero.io/stellar-x/v2.0.3/gateways/gateway_designer/#5-simulation-gateways)).

______________________________________________________________________

## 6. Real-Time Performance

The simulation runs in real time while the computer keeps up with the render rate. The controllers follow the simulation's time, but camera-based localization runs on wall-clock time, so a simulation that runs slower than real time degrades localization.

- Use moderate camera sizes and frame rates; each camera is rendered in addition to the viewport.
- Close viewports and windows you do not need.
- Do not run other heavy GPU programs (such as training) on the same computer at the same time.
- Keep the clocks of both computers synchronized (NTP). The camera gateway accepts frames at most 20 ms ahead of and 2 s behind its own clock. If you cannot synchronize them, start Isaac Sim with `RC_CAMERA_CAPTURE_TIME=0`: the camera gateway then stamps each frame when it arrives.

______________________________________________________________________

## 7. Troubleshooting

| Symptom                                                                                       | Cause and fix                                                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The status window does not show **serving**                                                   | Another program (for example a second Isaac Sim) holds ports 53333–53335. Close it and press **Play** again.                                                                                                                        |
| Gateway log stays at *waiting for it to start*                                                | Isaac Sim is not playing, **Sim host** is wrong, or a firewall blocks the ports ([Isaac Bridge Installation](https://docs.sodero.io/stellar-x/v2.0.3/virtual_simulation/extension_installation/#4-allow-the-ports-in-the-firewall)) |
| Isaac Sim console: *'sim_command' for 'X', which is no robot or tracked object of this stage* | The gateway's **Robot name** `X` is not the prim name of a robot in the scene                                                                                                                                                       |
| The robot is listed but never **bound**                                                       | It is not a valid PhysX articulation, or its name is used twice ([Robot Setup](https://docs.sodero.io/stellar-x/v2.0.3/virtual_simulation/robot_setup/#9-check-the-robot))                                                          |
| Camera gateway: *publishes frames of camera(s) … but none of camera …*                        | The camera gateway's **Camera name** is not the camera's prim name                                                                                                                                                                  |
| Camera gateway: frames *stale* or with capture times that do not match                        | The clocks of the two computers differ. Synchronize them, or start Isaac Sim with `RC_CAMERA_CAPTURE_TIME=0` so that the camera gateway uses arrival times.                                                                         |
| The robot moves too fast or too slow                                                          | The computer cannot keep up with the render rate. Lower camera sizes or rates, or close viewports.                                                                                                                                  |

The Isaac Sim console shows the bridge's messages, prefixed with the robot or camera name.
