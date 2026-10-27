# Quick Start

Updated example pair (2026-10-27)

Download both the `.gw` and `.sddm` files from this page again if you have older copies. They use the current `sodero.*` node IDs; older screenshots may still show `rc.*`. See [Compatibility and Downloads](https://docs.sodero.io/stellar-x/v2.0.1/reference/compatibility/#example-files).

You will build a small robot system on Stellar X and drive a simulated **Clearpath Jackal** in NVIDIA Isaac Sim with Strider. It takes about 15 minutes once Stellar X is on your network and Isaac Sim with the Isaac Bridge extension is installed (see **Before You Start**). You will:

1. add an actuator gateway and a Strider controller on Stellar Station,
1. load their design documents,
1. connect Isaac Sim, and
1. jog the robot from the browser.

```
flowchart TB
    B["Your browser<br>Stellar Station · Strider"]
    subgraph SX ["Stellar X"]
        S["Strider<br>sodero.mlc.jackal"] -- servo_link --> G["Actuator gateway<br>sodero.actuator_gateway.jackal"]
    end
    I["Isaac Sim + Isaac Bridge<br>robot /World/jackal"]
    B --> S
    G -- "LAN · TCP 53333–53335" --> I
```

______________________________________________________________________

## Before You Start

| You need                   | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Stellar X                  | Powered on and reachable from your PC ([Stellar X › Network Configuration](https://docs.sodero.io/stellar-x/v2.0.1/hardware_setup/stellar_series/stellar_x/#4-network-configuration), [Network Settings](https://docs.sodero.io/stellar-x/v2.0.1/hardware_setup/stellar_series/network_settings/index.md)). In this guide its address is `192.168.60.18`, an example address on a lab network; use your controller's address instead, for example `10.0.0.1` on a direct cable. |
| A PC with NVIDIA Isaac Sim | Isaac Sim 6.0 with the Isaac Bridge 1.0.0 extension installed and enabled ([Isaac Bridge Installation](https://docs.sodero.io/stellar-x/v2.0.1/virtual_simulation/extension_installation/index.md)), on the same network as Stellar X. In this guide its address is `192.168.60.20`.                                                                                                                                                                                            |
| Example files              | [jackal.gw](https://docs.sodero.io/stellar-x/v2.0.1/get_started/quick_start/files/jackal.gw) (gateway), [jackal.sddm](https://docs.sodero.io/stellar-x/v2.0.1/get_started/quick_start/files/jackal.sddm) (Strider) and [jackal_warehouse.zip](https://docs.sodero.io/stellar-x/v2.0.1/get_started/quick_start/files/jackal_warehouse.zip) (Isaac Sim scene, 6 MB). Download all three and extract the scene.                                                                    |

______________________________________________________________________

## Step 1: Add the Gateway

1. Open `http://192.168.60.18` in your browser.

1. Click **Add node**, choose **Gateway** ①, then **Actuator gateway** ② and click **Next** ③.

   Gateway › Actuator gateway

1. Name it `jackal` ① and click **Add node** ②.

______________________________________________________________________

## Step 2: Load the Gateway Document

1. Select the new node `sodero.actuator_gateway.jackal`. In its inspector, click the upload icon in **DEFINITION** (**Import .gw**).

1. On **From your PC** ①, choose `jackal.gw` ② and click **Import** ③.

1. In **TARGET**, click **Change** and set the two values:

   - **Robot name**: `jackal`. It must equal the robot's prim name in Isaac Sim (`/World/jackal`).
   - **Sim host**: the IP address of your Isaac Sim PC.

   Click **Done**.

If the robot name differs from the prim name in Isaac Sim, the gateway waits forever and the robot never moves.

______________________________________________________________________

## Step 3: Add Strider and Connect It

1. Click **Add node**, choose **Controller** ① › **Strider** ② and click **Next** ③. Name it `jackal` and click **Add node**.
1. Select `sodero.mlc.jackal` and click the upload icon in **DEFINITION** (**Import .sddm**). On **From your PC** ①, choose `jackal.sddm` ② and click **Import** ③.
1. Connect the two nodes: drag from the Strider's `servo_link` (left edge) to the gateway's `servo_link` (right edge), or click **Auto-connect** next to `servo_link` in the Strider's inspector.

The gateway and Strider connected through servo_link

______________________________________________________________________

## Step 4: Play the Scene in Isaac Sim

1. Open `jackal_warehouse.usd` in Isaac Sim (**File › Open**). The scene contains a Clearpath Jackal at `/World/jackal` and a Clearpath Dingo at `/World/dingo_d` in a warehouse.
1. Press **Play**.
1. Open **Window › Isaac Bridge**. It shows the ports as **serving** and `jackal … bound, 4 DOF`.

Isaac Bridge status: ① ports serving ② robots bound ③ cameras ④ Rescan

The Isaac Sim PC must accept TCP connections from Stellar X on ports 53333–53335. Allow them in its firewall ([Isaac Bridge Installation](https://docs.sodero.io/stellar-x/v2.0.1/virtual_simulation/extension_installation/#4-allow-the-ports-in-the-firewall)).

**Tip:** To use your own robot instead, prepare its scene as described in [Robot Setup](https://docs.sodero.io/stellar-x/v2.0.1/virtual_simulation/robot_setup/index.md): its articulation prim name is its robot name, and its joints, in order, are the gateway's actuators.

**Tip:** If you will continue with [Navigate in Simulation](https://docs.sodero.io/stellar-x/v2.0.1/navigation/simulation_tutorial/index.md), start Isaac Sim with the camera setting of its [Step 1](https://docs.sodero.io/stellar-x/v2.0.1/navigation/simulation_tutorial/#step-1-prepare-isaac-sim) now. Then you do not need to restart Isaac Sim later.

______________________________________________________________________

## Step 5: Start the Nodes

1. Select the gateway and click **Start node**. Wait until its state is **Operating**.
1. Select the Strider and click **Start node**.

In the gateway's **LOGS** (stream **Gateway events**) you see the connection to Isaac Sim:

```
Gateway sodero.actuator_gateway.jackal starting: simulation, 4 actuator(s), 1.0 ms cycle.
Simulation: robot 'jackal', simulator at 192.168.60.20; waiting for it to start.
Simulator connected.
```

______________________________________________________________________

## Step 6: Jog the Robot with Strider

1. In the Strider node's inspector, click **Strider** in **CONTROL**. Strider opens in a new tab.
1. Open the **Drive** page (gamepad icon in the left rail).
1. Under **Drive Mode**, click **Twist** ①.
1. Under **Servo / Safety**, switch **Servo On** ②.
1. Press and hold **Forward (W)** on the pad ⑤. The robot drives while you hold the button and stops when you release it. **Turn Left (A)**, **Turn Right (D)** and **Backward (S)** work the same way.

Strider's Drive page: ① Twist ② Servo On ③ Live switch for the keyboard ④ speed limits ⑤ drive pad ⑥⑦ stop and emergency stop ⑧ readiness

**Tip:** Switch on **Live** ③ in **Manual Drive** to drive with the keyboard: **W**/**S** forward and back, **A**/**D** turn, **Space** stops.

The simulated Jackal after a short drive and turn

When you are done, switch the servo off and click **Idle** under **Drive Mode**.

______________________________________________________________________

## What's Next

| Next step                                                  | Page                                                                                                                                                                                                         |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Let the Jackal localize itself on a map and drive to goals | [Navigate in Simulation](https://docs.sodero.io/stellar-x/v2.0.1/navigation/simulation_tutorial/index.md)                                                                                                    |
| Learn every part of the Station page                       | [Stellar Station](https://docs.sodero.io/stellar-x/v2.0.1/station/overview/index.md)                                                                                                                         |
| Build your own robot documents                             | [Stellar Designer](https://docs.sodero.io/stellar-x/v2.0.1/tutorials/stellar_designer/introduction/index.md), [Gateway Designer](https://docs.sodero.io/stellar-x/v2.0.1/gateways/gateway_designer/index.md) |
| Move from simulation to real motors                        | [EtherCAT Mobile Base](https://docs.sodero.io/stellar-x/v2.0.1/tutorials/ethercat_mobile_base/index.md), [EtherCAT Gateway](https://docs.sodero.io/stellar-x/v2.0.1/gateways/ethercat/index.md)              |
| Let an AI coding agent do it for you                       | [AI Coding Agents](https://docs.sodero.io/stellar-x/v2.0.1/ssh_workspace/ai_agents/index.md)                                                                                                                 |
