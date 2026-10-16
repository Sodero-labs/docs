# Isaac Bridge Installation

**Isaac Bridge** is the Isaac Sim extension that connects Isaac Sim to the gateways of Stellar Station. Install it once on the computer that runs Isaac Sim.

______________________________________________________________________

## 1. Download the Extension

Isaac Bridge is open source. Download it from GitHub:

```
git clone https://github.com/Sodero-labs/isaac_bridge.git
```

Or download the ZIP file of the latest release from the repository page and extract it. Either way you get a folder `isaac_bridge`. Remember the folder that **contains** it, for example `~/isaac_extensions` when the extension is in `~/isaac_extensions/isaac_bridge`.

______________________________________________________________________

## 2. Add the Extension to Isaac Sim

1. Start Isaac Sim.
1. Open **Window › Extensions**.
1. Open the Extensions window's settings (the menu icon next to the search field) and add the folder that contains `isaac_bridge` to **Extension Search Paths**.
1. Search for `isaac bridge` ①.
1. Switch the extension on ②.
1. Tick **AUTOLOAD** ③, so the extension starts with Isaac Sim from now on.

① search ② enable ③ autoload

When the extension starts the first time, Isaac Sim installs the Python package `pyzmq` from the internet. On a computer without internet access, install it into Isaac Sim's Python yourself, from Isaac Sim's installation folder:

```
./python.sh -m pip install pyzmq
```

```
python.bat -m pip install pyzmq
```

You can also start Isaac Sim with the extension from a command line: `isaac-sim.sh --ext-folder ~/isaac_extensions --enable isaac_bridge`.

______________________________________________________________________

## 3. Open the Status Window

Open **Window › Isaac Bridge**. The window shows what the bridge serves. Before a scene plays it is mostly empty; press **Play** in Isaac Sim and it fills in:

The Isaac Bridge status window while a scene plays

| No. | Line        | Meaning                                                                                                                                                                |
| --- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Ports**   | The command (53333), state (53334) and camera (53335) ports, and **serving** when the gateways can connect. The line below shows the scene's physics and render rates. |
| 2   | **Robots**  | Every robot of the scene: its name, its prim path, **bound** when the bridge controls it, and its number of joints (DOF)                                               |
| 3   | **Cameras** | Every camera served: name, resolution, frame rate and frames sent                                                                                                      |
| 4   | **Rescan**  | Looks for robots and cameras again after you changed the scene while it plays                                                                                          |

The ports open when the scene plays and close when it stops.

______________________________________________________________________

## 4. Allow the Ports in the Firewall

Stellar X connects to the Isaac Sim computer on **TCP ports 53333, 53334 and 53335**. Allow them for incoming connections from Stellar X.

```
sudo ufw allow from <Stellar X IP address> to any port 53333:53335 proto tcp
```

Open **Windows Defender Firewall › Advanced settings › Inbound Rules › New Rule…**, choose **Port**, **TCP**, ports `53333-53335`, and allow the connection for your private network.

The bridge does not authenticate its clients: any computer that reaches these ports can command the robots of the scene. Use it on a trusted network only, and do not open the ports to the internet.

______________________________________________________________________

## 5. Update or Remove

- **Update:** run `git pull` in the `isaac_bridge` folder (or replace the folder with a newer release) and restart Isaac Sim.
- **Remove:** switch the extension off in **Window › Extensions**, untick **AUTOLOAD**, and remove its folder from **Extension Search Paths**.

The extension's README describes advanced settings, such as camera sizes and rates, which cameras to publish, and the ports.

Next: [Robot Setup](https://docs.sodero.io/v2.0.0/virtual_simulation/robot_setup/index.md).
