# Backup and Restore

The whole Station (its node graph, design documents, settings and Station data) can be saved to one **`.sdr`** file and loaded again on the same or another Stellar X. Use it to back up a working system, to copy a system to another robot, or to bring a Station built in Sodero Cloud onto a robot.

______________________________________________________________________

## 1. Export the Station

Click **Export SDR** in the Runtime toolbar. Pending edits are saved first, then the browser downloads a file named after the Station, for example `stellar-x.sdr`.

The file contains:

| Part            | Contents                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------ |
| Runtime graph   | All nodes and their connections                                                                  |
| Robot documents | The `.sdd`, `.sddm` and `.sdda` documents of the controllers                                     |
| Station data    | Gateway documents (`.gw`), settings of sensor and navigation nodes, maps and other Station state |

Installed module packages are not part of the file; they stay on the controller.

**Tip:** Export the Station before larger changes, such as importing a new document over a working one or loading another `.sdr`.

______________________________________________________________________

## 2. Load an `.sdr` File

1. Stop all nodes (**Start all nodes** menu › **Stop all nodes**).
1. Click **Load SDR**, drop the file or click **Choose file**.
1. Click **Load and restart**.

Loading an .sdr file

The Station replaces its graph, robot documents and Station data with the file's content and restarts. The page shows *Restarting the Station with …* and reloads when the Station is back, usually within a minute. The nodes are not started; start them when you need them.

- Installed modules stay installed.
- If the file cannot be loaded, the Station keeps its data and the dialog says why.

Loading is refused while any node runs: *Stop all nodes before loading a .sdr.*

### Files That Cannot Be Loaded

| Message                                                              | Cause                                                             |
| -------------------------------------------------------------------- | ----------------------------------------------------------------- |
| *This .sdr holds a simulation, not a Station.*                       | The file is a World (simulation) export. Open it in Sodero Cloud. |
| *This robot does not have enough free disk space to load this .sdr.* | The unpacked file is too large for the controller's storage.      |
