# Learning Path

The tutorials of this documentation build on each other: first connection, a simulated robot, navigation, then real motors. Follow them in this order, or start where your project is. The first hands-on tutorial is the [Quick Start](https://docs.sodero.io/stellar-x/v2.0.0/get_started/quick_start/index.md); its [Before You Start](https://docs.sodero.io/stellar-x/v2.0.0/get_started/quick_start/#before-you-start) section lists what to prepare.

```
flowchart TB
    A["1. Connect Stellar X"] --> B["2. Quick Start<br>simulated Jackal"]
    B --> C["3. Navigate in Simulation"]
    B --> D["4. Your own robot documents"]
    D --> E["5. EtherCAT Mobile Base<br>real motors"]
    C --> F["6. Extend and automate"]
    E --> F
```

______________________________________________________________________

## 1. Connect Stellar X

| What you do                                                 | Page                                                                                                                | You need               |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| Power Stellar X, connect your PC and open the Station       | [Stellar X](https://docs.sodero.io/stellar-x/v2.0.0/hardware_setup/stellar_series/stellar_x/index.md)               | Stellar X, a LAN cable |
| Give Stellar X an address on your network                   | [Network Settings](https://docs.sodero.io/stellar-x/v2.0.0/hardware_setup/stellar_series/network_settings/index.md) | —                      |
| Learn the terms: Station, nodes, ports, gateways, documents | [Key Concepts](https://docs.sodero.io/stellar-x/v2.0.0/get_started/key_concepts/index.md)                           | —                      |

______________________________________________________________________

## 2. Drive a Simulated Robot

| What you do                                                              | Page                                                                                                               | You need                                                                                                            |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Install Isaac Sim and the Isaac Bridge extension                         | [Install Isaac Bridge](https://docs.sodero.io/stellar-x/v2.0.0/virtual_simulation/extension_installation/index.md) | A PC with an NVIDIA GPU ([Compatibility](https://docs.sodero.io/stellar-x/v2.0.0/reference/compatibility/index.md)) |
| Add a gateway and Strider, load the example documents and jog the Jackal | [Quick Start](https://docs.sodero.io/stellar-x/v2.0.0/get_started/quick_start/index.md)                            | The Quick Start's example files                                                                                     |

______________________________________________________________________

## 3. Navigate in Simulation

| What you do                                                                    | Page                                                                                                                                                                                                      | You need                                      |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| Add a camera, the Localizer and the Navigator, load the map and drive to goals | [Navigate in Simulation](https://docs.sodero.io/stellar-x/v2.0.0/navigation/simulation_tutorial/index.md)                                                                                                 | The Quick Start setup, the example map bundle |
| Load a map of your own site later                                              | [Load and Configure a Map](https://docs.sodero.io/stellar-x/v2.0.0/navigation/map_bundle/index.md), [Create a Map from Your Site](https://docs.sodero.io/stellar-x/v2.0.0/navigation/create_map/index.md) | A 3D model or scan of the site                |

______________________________________________________________________

## 4. Describe Your Own Robot

| What you do                                              | Page                                                                                                                                                                                                                    | You need                         |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| A mobile base: chassis, wheels, limits, actuator mapping | [Mobile Robot (.sddm)](https://docs.sodero.io/stellar-x/v2.0.0/tutorials/stellar_designer/mobile_robot/index.md)                                                                                                        | Your base's dimensions           |
| A manipulator: DH parameters, limits, actuator mapping   | [Manipulator (.sdd)](https://docs.sodero.io/stellar-x/v2.0.0/tutorials/stellar_designer/manipulator/index.md)                                                                                                           | Your arm's kinematics and limits |
| A robot driven joint by joint, such as a legged robot    | [Articulated Robot (.sdda)](https://docs.sodero.io/stellar-x/v2.0.0/tutorials/stellar_designer/articulation/index.md)                                                                                                   | Your robot's joints and limits   |
| The gateway of its motors                                | [Gateway Designer](https://docs.sodero.io/stellar-x/v2.0.0/gateways/gateway_designer/index.md)                                                                                                                          | Motor and drive data             |
| Try the documents in Isaac Sim first                     | [Prepare the Robot](https://docs.sodero.io/stellar-x/v2.0.0/virtual_simulation/robot_setup/index.md), [Connect to Stellar Station](https://docs.sodero.io/stellar-x/v2.0.0/virtual_simulation/connect_station/index.md) | Your robot's scene in Isaac Sim  |

______________________________________________________________________

## 5. Bring Up Real Motors

| What you do                                                 | Page                                                                                                    | You need                                          |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| Read how to stop the robot before anything moves            | [Stop Controls](https://docs.sodero.io/stellar-x/v2.0.0/hardware_setup/stop_controls/index.md)          | A wired emergency stop                            |
| Wire four EtherCAT drives, test each wheel and jog the base | [EtherCAT Mobile Base](https://docs.sodero.io/stellar-x/v2.0.0/tutorials/ethercat_mobile_base/index.md) | Four CiA 402 drives and motors, a four-wheel base |
| Move single actuators without a controller                  | [Test Console](https://docs.sodero.io/stellar-x/v2.0.0/gateways/test_console/index.md)                  | A running gateway                                 |

______________________________________________________________________

## 6. Extend and Automate

| What you do                                                           | Page                                                                                                                                                                              |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Work on the controller over SSH                                       | [SSH Workspace](https://docs.sodero.io/stellar-x/v2.0.0/ssh_workspace/overview/index.md), [sodero CLI](https://docs.sodero.io/stellar-x/v2.0.0/ssh_workspace/sodero_cli/index.md) |
| Run your own programs as nodes                                        | [Create Custom Modules](https://docs.sodero.io/stellar-x/v2.0.0/extend/custom_modules/index.md)                                                                                   |
| Connect your own camera, IMU or wheel board through the Device Bridge | [Write Device Bridge Drivers](https://docs.sodero.io/stellar-x/v2.0.0/extend/device_bridge_drivers/index.md)                                                                      |
| Let an AI coding agent do routine work                                | [AI Coding Agents](https://docs.sodero.io/stellar-x/v2.0.0/ssh_workspace/ai_agents/index.md)                                                                                      |
