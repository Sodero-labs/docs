# Compatibility and Downloads

This documentation describes the versions below. With other versions, menus, messages and file formats can differ.

---

## Verified Versions

| Software | Version | Where to get it |
| :--- | :--- | :--- |
| Stellar software on Stellar X (Stellar Station, built-in nodes, Network Settings, SSH workspace) | 2.0 | Comes with Stellar X |
| NVIDIA Isaac Sim | 6.0, on Linux or Windows | [NVIDIA](https://docs.isaacsim.omniverse.nvidia.com/latest/installation/index.html){:target="_blank"} |
| Isaac Bridge | 1.0.0 | Release `v1.0.0` of [Sodero-labs/isaac_bridge](https://github.com/Sodero-labs/isaac_bridge){:target="_blank"} ([Isaac Bridge Installation](../../virtual_simulation/extension_installation/index.md)) |
| Device Bridge | No release yet: the `main` branch of 2026-10-20 | [Sodero-labs/device_bridge](https://github.com/Sodero-labs/device_bridge){:target="_blank"} ([Device Bridge](../../gateways/device_bridge/index.md)) |
| Web browser | A recent version of Chrome or Edge | — |

!!! info "After you update Isaac Bridge or the Device Bridge, check the connection again: the bridge serves its ports, and the Station's gateways log that they are connected ([Isaac Bridge Installation](../../virtual_simulation/extension_installation/index.md#3-open-the-status-window), [Device Bridge › Check from Another Computer](../../gateways/device_bridge/index.md#check-from-another-computer))."

---

## Example Files

| File | Used in | Contents | Last changed |
| :--- | :--- | :--- | :--- |
| [jackal.gw](../../get_started/quick_start/files/jackal.gw) | [Quick Start](../../get_started/quick_start/index.md) | Simulation gateway for the Jackal | 2026-10-27 |
| [jackal.sddm](../../get_started/quick_start/files/jackal.sddm) | [Quick Start](../../get_started/quick_start/index.md) | Strider document of the Jackal | 2026-10-27 |
| [jackal_warehouse.zip](../../get_started/quick_start/files/jackal_warehouse.zip) | [Quick Start](../../get_started/quick_start/index.md) | Isaac Sim scene with a Clearpath Jackal and Dingo, with their license | 2026-10-18 |
| [warehouse.nav.tgz](../../navigation/simulation_tutorial/files/warehouse.nav.tgz) | [Navigate in Simulation](../../navigation/simulation_tutorial/index.md) | Map bundle of the warehouse scene | 2026-10-16 |
| [wheels.gw](../../tutorials/ethercat_mobile_base/files/wheels.gw) | [EtherCAT Mobile Base](../../tutorials/ethercat_mobile_base/index.md) | EtherCAT gateway with four drives | 2026-10-27 |
| [base.sddm](../../tutorials/ethercat_mobile_base/files/base.sddm) | [EtherCAT Mobile Base](../../tutorials/ethercat_mobile_base/index.md) | Strider document of the four-wheel base | 2026-10-27 |
| [example_manipulator_parts.zip](../../tutorials/stellar_designer/3dmodel_creation/models/example_manipulator_parts.zip) | [3D Model Creation](../../tutorials/stellar_designer/3dmodel_creation/index.md) | 3D parts of the example arm | 2026-03-16 |
| [.blend](../../tutorials/stellar_designer/3dmodel_creation/models/example_manipulator_assembly_vis.blend), [.glb](../../tutorials/stellar_designer/3dmodel_creation/models/example_manipulator_assembly_vis.glb) | [3D Model Creation](../../tutorials/stellar_designer/3dmodel_creation/index.md) | The assembled example arm | 2026-10-18 (`.blend`), 2026-03-16 (`.glb`) |

The four `.gw` and `.sddm` examples were updated on 2026-10-27 for the current node IDs (`sodero.actuator_gateway.*`). If you downloaded them earlier, download both files of a pair again, `jackal.gw` with `jackal.sddm` or `wheels.gw` with `base.sddm`: older copies use the previous gateway IDs, and the Station can refuse them. Keep the node names of the tutorials (`jackal`, or gateway `wheels` and controller `base`), and check the `servo_link` connection before you start the nodes. If the Station refuses a document of your own as obsolete, contact [Sodero support](https://www.sodero.io/contact). The changes are listed in the [ChangeLog](../../CHANGELOG.md).

Some screenshots were taken with an earlier build and show `rc.` node IDs, for example `rc.actuator_gateway.jackal`. They are the same nodes; use the `sodero.` IDs of the text.
