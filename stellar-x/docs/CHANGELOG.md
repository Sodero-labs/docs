# Changelog

<div class="changelog-container" markdown="1">

<div class="version-block" markdown="1">

<div class="version-info" markdown="1">

<div class="display-version">v2.0.0</div>
<div class="display-date">2026.10.30</div>

</div>

<div class="version-content" markdown="1">

## v2.0.0 { #v2-0-0 }

#### New

* **Stellar Station.** Build the robot system as a graph of nodes in the browser: gateways, controllers, sensors, navigation and your own modules. Load design documents into nodes, start and stop nodes, follow their logs, and back up the whole Station in one file. See [Stellar Station](station/overview/index.md).
* **Gateways.** Actuator gateways for EtherCAT drives and robots in NVIDIA Isaac Sim, created in the new **Gateway Designer** (`.gw`). Camera and IMU gateways for simulated and real sensors; the **Device Bridge** serves real RGB-D cameras and IMUs. See [Gateways](gateways/overview/index.md).
* **Strider.** Controller and web UI for wheeled mobile bases: differential, skid steer, mecanum, swerve and Ackermann drives (`.sddm`). See [Strider](controllers/strider/index.md).
* **Articulation.** Joint-level controller for legged robots, humanoids and other articulated robots (`.sdda`). See [Articulation](controllers/articulation/index.md).
* **Localization and navigation.** Camera-based localization on a map and autonomous navigation to goals, configured by one map bundle (`.nav`). See [Localization and Navigation](navigation/overview/index.md).
* **Isaac Bridge.** Extension for Isaac Sim 6.0 that connects Isaac Sim to the Station's gateways: several robots per scene, cameras and IMUs. See [Simulation](virtual_simulation/introduction/index.md).
* **SSH Workspace.** A Linux workspace on the controller with the `sodero` command-line tool and support for AI coding agents. See [SSH Workspace](ssh_workspace/overview/index.md).
* **Network Settings.** A settings page on port 3000 for the LAN address and SSH access. See [Network Settings](hardware_setup/stellar_series/network_settings/index.md).

#### Changed

* **Stellar Designer** opens from a controller node on the Station and edits that node's document: manipulators (`.sdd`), mobile robots (`.sddm`) and articulated robots (`.sdda`). Motor and EtherCAT settings moved to the Gateway Designer.
* **Stellar Motion Studio** has a new interface with the Home, Tool and Pose pages. Programs run from the SSH Workspace or as modules on the Station.

#### Documentation

* This documentation describes the Stellar X 2.0 software. The pages follow the order of use: [Learning Path](tutorials/learning_path/index.md) and [Quick Start](get_started/quick_start/index.md), then hardware, Stellar Station, gateways and sensors, Stellar Designer, simulation, operation and navigation.
* Example files ([Compatibility and Downloads](reference/compatibility/index.md#example-files)): `jackal.gw` and `jackal.sddm` for the [Quick Start](get_started/quick_start/index.md), `wheels.gw` and `base.sddm` for the [EtherCAT Mobile Base](tutorials/ethercat_mobile_base/index.md) tutorial, and the map bundle of [Navigate in Simulation](navigation/simulation_tutorial/index.md). If the Station refuses a copy you downloaded earlier, download the file again.

</div>

</div>

<div class="version-block" markdown="1">

<div class="version-info" markdown="1">

<div class="display-version">v1.0.0</div>
<div class="display-date">2026.03.16</div>

</div>

<div class="version-content" markdown="1">

## v1.0.0 { #v1-0-0 }

#### Release

* Stellar Designer for manipulators, Stellar Motion Studio, and NVIDIA Isaac Sim integration.

</div>

</div>

</div>
