# ChangeLog

v2.0.3

2026.10.29

## v2.0.3

#### Documentation and Navigation

- The navigation follows the order of use: [Learning Path](https://docs.sodero.io/stellar-x/v2.0.3/tutorials/learning_path/index.md) is under **Get Started**, and **Simulation** comes before **Operate Robots**.
- The [Quick Start](https://docs.sodero.io/stellar-x/v2.0.3/get_started/quick_start/index.md) and [EtherCAT Mobile Base](https://docs.sodero.io/stellar-x/v2.0.3/tutorials/ethercat_mobile_base/index.md) begin with the tutorial itself; the notes on the example files are in [Compatibility and Downloads](https://docs.sodero.io/stellar-x/v2.0.3/reference/compatibility/#example-files).
- [Isaac Bridge Installation](https://docs.sodero.io/stellar-x/v2.0.3/virtual_simulation/extension_installation/#5-update-or-remove): update steps for a copy cloned from a release tag.
- Fixed the address of `llms-full.txt` in [AI Coding Agents](https://docs.sodero.io/stellar-x/v2.0.3/ssh_workspace/ai_agents/#give-the-agent-the-documentation) and the links to [Create Custom Modules](https://docs.sodero.io/stellar-x/v2.0.3/extend/custom_modules/index.md).

v2.0.2

2026.10.27

## v2.0.2

#### Documentation

- [Navigate in Simulation](https://docs.sodero.io/stellar-x/v2.0.3/navigation/simulation_tutorial/#step-2-add-the-camera-gateway): added a comparison of the camera gateway defaults (60° field of view, 15 fps) with the Jackal example settings (90°, 5 fps), the exact inspector field labels, and the stop/save/restart sequence for an existing setup.
- [Sensors and Cameras](https://docs.sodero.io/stellar-x/v2.0.3/gateways/sensors_and_cameras/#camera-settings): explained automatic image-size detection and why a visible camera image does not establish correct calibration for localization. Added troubleshooting for a Localizer that remains Initializing, Relocalizing or Lost.

v2.0.1

2026.10.27

## v2.0.1

#### Documentation and Example Files

This is a Stellar X documentation release, not a change to the software installed on your controller.

- Updated `jackal.gw`, `jackal.sddm`, `wheels.gw` and `base.sddm` to use current `sodero.actuator_gateway.*` IDs. Download both files of each pair again; the Station can refuse older copies. Robot geometry, actuator order, EtherCAT settings and safety limits are unchanged. See [Compatibility and Downloads](https://docs.sodero.io/stellar-x/v2.0.3/reference/compatibility/#example-files).
- Aligned gateway, camera, IMU and Navigator node IDs in the tutorials, connection diagrams and CLI examples.

v2.0.0

2026.10.16

## v2.0.0

#### New

- **Stellar Station.** Build the robot system as a graph of nodes in the browser: gateways, controllers, sensors, navigation and your own modules. Load design documents into nodes, start and stop nodes, follow their logs, and back up the whole Station in one file. See [Stellar Station](https://docs.sodero.io/stellar-x/v2.0.3/station/overview/index.md).
- **Gateways.** Actuator gateways for EtherCAT drives and robots in NVIDIA Isaac Sim, created in the new **Gateway Designer** (`.gw`). Camera and IMU gateways for simulated and real sensors; the **Device Bridge** serves real RGB-D cameras and IMUs. See [Gateways](https://docs.sodero.io/stellar-x/v2.0.3/gateways/overview/index.md).
- **Strider.** Controller and web UI for wheeled mobile bases: differential, skid steer, mecanum, swerve and Ackermann drives (`.sddm`). See [Strider](https://docs.sodero.io/stellar-x/v2.0.3/controllers/strider/index.md).
- **Articulation.** Joint-level controller for legged robots, humanoids and other articulated robots (`.sdda`). See [Articulation](https://docs.sodero.io/stellar-x/v2.0.3/controllers/articulation/index.md).
- **Localization and navigation.** Camera-based localization on a map and autonomous navigation to goals, configured by one map bundle (`.nav`). See [Localization and Navigation](https://docs.sodero.io/stellar-x/v2.0.3/navigation/overview/index.md).
- **Isaac Bridge.** Extension for Isaac Sim 6.0 that connects Isaac Sim to the Station's gateways: several robots per scene, cameras and IMUs. See [Simulation](https://docs.sodero.io/stellar-x/v2.0.3/virtual_simulation/introduction/index.md).
- **SSH Workspace.** A Linux workspace on the controller with the `sodero` command-line tool and support for AI coding agents. See [SSH Workspace](https://docs.sodero.io/stellar-x/v2.0.3/ssh_workspace/overview/index.md).
- **Network Settings.** A settings page on port 3000 for the LAN address and SSH access. See [Network Settings](https://docs.sodero.io/stellar-x/v2.0.3/hardware_setup/stellar_series/network_settings/index.md).

#### Changed

- **Stellar Designer** opens from a controller node on the Station and edits that node's document: manipulators (`.sdd`), mobile robots (`.sddm`) and articulated robots (`.sdda`). Motor and EtherCAT settings moved to the Gateway Designer.
- **Stellar Motion Studio** has a new interface with the Home, Tool and Pose pages. Programs run from the SSH Workspace or as modules on the Station.

#### Documentation Revisions

The software version stays 2.0.0; these are revisions of this documentation and its example files ([Compatibility and Downloads](https://docs.sodero.io/stellar-x/v2.0.3/reference/compatibility/index.md)).

- **2026.10.21.** New pages: [Learning Path](https://docs.sodero.io/stellar-x/v2.0.3/tutorials/learning_path/index.md), [Test Console](https://docs.sodero.io/stellar-x/v2.0.3/gateways/test_console/index.md), [Stop Controls](https://docs.sodero.io/stellar-x/v2.0.3/hardware_setup/stop_controls/index.md) and [Compatibility and Downloads](https://docs.sodero.io/stellar-x/v2.0.3/reference/compatibility/index.md). The map bundle page is split into [Load and Configure a Map](https://docs.sodero.io/stellar-x/v2.0.3/navigation/map_bundle/index.md), [Create a Map from Your Site](https://docs.sodero.io/stellar-x/v2.0.3/navigation/create_map/index.md) and [Map Bundle Format](https://docs.sodero.io/stellar-x/v2.0.3/navigation/map_bundle_format/index.md); writing Device Bridge drivers and building modules moved to **Extend & Automate**. The LAN ports and the test console conditions are described the same way on every page. Example files: `jackal.sddm` and `base.sddm` no longer carry run-time settings that the controller does not use. Copies downloaded before this date keep working.
- **2026.10.21.** [EtherCAT Mobile Base](https://docs.sodero.io/stellar-x/v2.0.3/tutorials/ethercat_mobile_base/index.md): a step that tests each wheel with the test console before Strider drives them.
- **2026.10.20.** New tutorial [EtherCAT Mobile Base](https://docs.sodero.io/stellar-x/v2.0.3/tutorials/ethercat_mobile_base/index.md) with the example files `wheels.gw` and `base.sddm`.
- **2026.10.19.** The Quick Start files `jackal.gw` and `jackal.sddm` use the current document format. If the Station refuses a copy you downloaded before this date, download the files again.

v1.0.0

2026.03.16

## v1.0.0

#### Release

- Stellar Designer for manipulators, Stellar Motion Studio, and NVIDIA Isaac Sim integration. The v1 documentation remains available in the version selector.
