# Gateway Designer

Every actuator gateway runs from a gateway document (`.gw`): the hardware type, the list of actuators, each actuator's motor and drive parameters, and the fieldbus settings. **Stellar Gateway Designer**, the part of [Stellar Designer](https://docs.sodero.io/stellar-x/v2.0.0/tutorials/stellar_designer/introduction/index.md) for `.gw` files, creates and edits these documents. It opens from an actuator gateway node on the Station.

This page covers what all gateway documents share. The settings of each hardware type follow on [Simulation Gateway](https://docs.sodero.io/stellar-x/v2.0.0/gateways/simulation/index.md) and [EtherCAT Gateway](https://docs.sodero.io/stellar-x/v2.0.0/gateways/ethercat/index.md).

______________________________________________________________________

## 1. Open the Gateway Designer

1. Select an actuator gateway node on the Station.
1. Click **Edit Stellar Gateway Designer** in the **DEFINITION** section.

The Gateway Designer opens in a new tab with the node's document. Edits are saved back to the node automatically. **Stop the gateway before you edit**; the Station refuses saves while it runs (*Gateway '…' is running — stop it in the Station, then save again.*) and while its [test console](https://docs.sodero.io/stellar-x/v2.0.0/gateways/test_console/index.md) is open (*Gateway '…' has a test console open — stop the test in the Station, then save again.*).

A simulation gateway with four actuators

| Area              | Contents                                                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Breadcrumb        | Where the document belongs: device / Station / node / file. The arrow returns to the Station.                                                                |
| Steps             | **01 Gateway setup** (actuators and their parameters) and **02 Verification**                                                                                |
| **Actuators (N)** | One card per actuator, in index order, with its brand, model and status (**Configured** / **Not configured**). **Add Actuator** adds one; **×** removes one. |
| Actuator panel    | The parameters of the selected actuator, in tabs: **Motor** and a tab for the hardware type (**EtherCAT** or **Isaac Sim**)                                  |
| Units             | `mm / g / deg` or `m / kg / radian` for display                                                                                                              |

______________________________________________________________________

## 2. Choose the Hardware Type

A new gateway node starts with an empty document. When you open it, the Gateway Designer asks for the hardware type:

Create gateway definition

| Type            | Use                                                                                                                                |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Isaac Sim** ① | A robot in NVIDIA Isaac Sim ([Simulation Gateway](https://docs.sodero.io/stellar-x/v2.0.0/gateways/simulation/index.md))           |
| **EtherCAT** ②  | CiA 402 servo drives on the EtherCAT port ([EtherCAT Gateway](https://docs.sodero.io/stellar-x/v2.0.0/gateways/ethercat/index.md)) |

Select the type and click **Next** ③, then **Create**.

To change the type of an existing gateway, click the Stellar mark at the top left and choose **Definition** › **Replace definition**. Pick the new type and click **Next** › **Replace**. Existing actuators keep their motor settings and receive the new type's hardware settings; the previous type's hardware settings are removed. This cannot be undone.

______________________________________________________________________

## 3. Add and Configure Actuators

1. Click **Add Actuator** once per motor. Actuator 1 is index 0, actuator 2 is index 1, and so on.
1. Select an actuator card. Fill in the **Motor** tab: pick the motor from the catalog (**Brand** › **Series** › **Model**) or enter its values.
1. Fill in the tab of the hardware type: **EtherCAT** (identification, SDOs, PDOs) or **Isaac Sim** (DOF offset).

### Motor Parameters

Every field of the **Motor** tab is described in [EtherCAT Gateway › Motor Tab](https://docs.sodero.io/stellar-x/v2.0.0/gateways/ethercat/#motor-tab). For simulation gateways the **Motor** tab shows only **Max torque**, **Max speed** and **Gear ratio**: the gateway limits torque commands to *Max torque × Gear ratio* and velocity commands to *Max speed ÷ Gear ratio* at the joint.

______________________________________________________________________

## 4. Verify and Export

Open **02 Verification** and click **Verify**. The Gateway Designer checks the hardware type, the actuator list, the motor parameters (for EtherCAT also the encoder resolution) and the configuration files.

All checks passed

Errors (for example a parameter that must be positive) must be fixed; warnings are advisory. Then start the gateway from the Station.

When all checks pass, **Export .gw** downloads the document as a `.gw` file, which you can import into another gateway node (**Import .gw**).

______________________________________________________________________

## 5. Simulation Gateways

For **Isaac Sim** gateways, the actuator panel has an **Isaac Sim** tab with one setting:

The Isaac Sim tab of an actuator

**DOF offset** is the first joint of the Isaac Sim articulation that this gateway drives, counted from 0 in actuator order. It applies to every actuator of the gateway: the **Isaac Sim** tab of each actuator shows the same value. Leave it at 0 when one gateway drives the whole robot.

Several gateways can share one simulated robot. For an arm with four joints and a gripper with two, as in the hint below the field (*arm 0, gripper 4*):

| Gateway | DOF offset | Drives     |
| ------- | ---------- | ---------- |
| Arm     | 0          | Joints 1–4 |
| Gripper | 4          | Joints 5–6 |

The robot's name in the scene (**Robot name**) and the address of the Isaac Sim computer (**Sim host**) are set on the Station node, not in the document ([Simulation Gateway](https://docs.sodero.io/stellar-x/v2.0.0/gateways/simulation/#2-create-a-simulation-gateway)).

Next: [Simulation Gateway](https://docs.sodero.io/stellar-x/v2.0.0/gateways/simulation/index.md) for a robot in Isaac Sim, or [EtherCAT Gateway](https://docs.sodero.io/stellar-x/v2.0.0/gateways/ethercat/index.md) for real drives.
