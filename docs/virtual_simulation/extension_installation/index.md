# Isaac Bridge Installation

**Isaac Bridge** is the Isaac Sim extension that connects Isaac Sim to the gateways of Stellar Station. Install it once on the computer that runs Isaac Sim.

---

## 1. Download the Extension

Isaac Bridge is open source. Download it from GitHub:

```sh
git clone https://github.com/Sodero-labs/isaac_bridge.git
```

Or download the ZIP file of the latest release from the repository page and extract it. Either way you get a folder `isaac_bridge`. Remember the folder that **contains** it, for example `~/isaac_extensions` when the extension is in `~/isaac_extensions/isaac_bridge`.

---

## 2. Add the Extension to Isaac Sim

1. Start Isaac Sim.
2. Open **Window › Extensions**.
3. Open the Extensions window's settings (the menu icon next to the search field) and add the folder that contains `isaac_bridge` to **Extension Search Paths**.
4. Search for `isaac bridge` ①.
5. Switch the extension on ②.
6. Tick **AUTOLOAD** ③, so the extension starts with Isaac Sim from now on.

<figure markdown="span">
  ![Isaac Bridge in the Extensions window](images_v2/extensions_isaac_bridge.png){ width="1000" }
  <figcaption>① search ② enable ③ autoload</figcaption>
</figure>

When the extension starts the first time, Isaac Sim installs the Python package `pyzmq` from the internet. On a computer without internet access, install it into Isaac Sim's Python yourself, from Isaac Sim's installation folder:

=== "Linux"

    ```sh
    ./python.sh -m pip install pyzmq
    ```

=== "Windows"

    ```bat
    python.bat -m pip install pyzmq
    ```

!!! info "You can also start Isaac Sim with the extension from a command line: `isaac-sim.sh --ext-folder ~/isaac_extensions --enable isaac_bridge`."

---

## 3. Open the Status Window

Open **Window › Isaac Bridge**. The window shows what the bridge serves. Before a scene plays it is mostly empty; press **Play** in Isaac Sim and it fills in:

<figure markdown="span">
  ![Isaac Bridge window](../connect_station/images/isaac_bridge_window.png){ width="560" }
  <figcaption>The Isaac Bridge status window while a scene plays</figcaption>
</figure>

| No. | Line | Meaning |
| :---: | :--- | :--- |
| 1 | **Ports** | The command (53333), state (53334) and camera (53335) ports, and **serving** when the gateways can connect. The line below shows the scene's physics and render rates. |
| 2 | **Robots** | Every robot of the scene: its name, its prim path, **bound** when the bridge controls it, and its number of joints (DOF) |
| 3 | **Cameras** | Every camera served: name, resolution, frame rate and frames sent |
| 4 | **Rescan** | Looks for robots and cameras again after you changed the scene while it plays |

The ports open when the scene plays and close when it stops.

---

## 4. Allow the Ports in the Firewall

Stellar X connects to the Isaac Sim computer on **TCP ports 53333, 53334 and 53335**. Allow them for incoming connections from Stellar X.

=== "Ubuntu (ufw)"

    ```sh
    sudo ufw allow from <Stellar X IP address> to any port 53333:53335 proto tcp
    ```

=== "Windows"

    Open **Windows Defender Firewall › Advanced settings › Inbound Rules › New Rule…**, choose **Port**, **TCP**, ports `53333-53335`, and allow the connection for your private network.

!!! warning "The bridge does not authenticate its clients: any computer that reaches these ports can command the robots of the scene. Use it on a trusted network only, and do not open the ports to the internet."

---

## 5. Update or Remove

- **Update:** run `git pull` in the `isaac_bridge` folder (or replace the folder with a newer release) and restart Isaac Sim.
- **Remove:** switch the extension off in **Window › Extensions**, untick **AUTOLOAD**, and remove its folder from **Extension Search Paths**.

The extension's README describes advanced settings, such as camera sizes and rates, which cameras to publish, and the ports.

Next: [Robot Setup](../robot_setup/index.md).
