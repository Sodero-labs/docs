# Sodero Ecosystem

## A Software-Defined Robotics Platform: Build Once. Move Everywhere.

Sodero fundamentally resolves the biggest bottlenecks in traditional robot development: **Tight Hardware Coupling** and the **Sim-to-Real Gap**. By abstracting complex control environments into a standardized software layer, we provide an innovative, unified ecosystem. Developers can design robots in a virtual environment and deploy them directly to the real world without changing a single line of code.

### Core Architecture

**Causality-Aligned Simulation** Going beyond simple 3D rendering, our Reverse Digital Twin technology ensures that the control logic in the virtual environment matches the physical outcomes in reality. The same controller drives a robot in NVIDIA Isaac Sim and on real motors; only its gateway changes.

**Unified Execution Layer** Even if the robot's form factor or hardware changes, there is no need to rewrite the glue code from scratch. Every node on Stellar Station, built-in or your own, runs on one real-time runtime with standardized interfaces, so code and motions written on the Sodero platform are executed with the same semantics everywhere.

______________________________________________________________________

### What's New in 2.0

Version 2.0 turns Stellar X from a single-robot motion controller into a complete robot system on one controller:

- **Stellar Station**: build the robot system as a graph of nodes (gateways, controllers, sensors, navigation and your own modules) and run it from the browser.
- **One Stellar Designer** for every design document: manipulators (`.sdd`), mobile bases (`.sddm`), articulated robots (`.sdda`) and gateways (`.gw`).
- **Mobile robots and navigation**: Strider drives wheeled bases; the Localizer and Navigator add map-based localization and autonomous navigation.
- **Isaac Bridge**: connect robots in NVIDIA Isaac Sim to the Station over the network, with cameras and IMUs.
- **SSH Workspace and AI agents**: develop on the controller over SSH and let AI coding agents operate the Station with the `sodero` CLI.

______________________________________________________________________

### From Design to the Real Robot

The Sodero ecosystem connects the entire process, from robot design and validation to physical deployment, into a single pipeline.

```
flowchart TB
    D["Design<br>Stellar Designer"] --> S["Compose<br>Stellar Station"]
    S --> V["Simulate<br>Isaac Sim + Isaac Bridge"]
    V --> R["Run<br>Stellar X + real hardware"]
    R -. "same controller,<br>new gateway" .- V
```

**Design: Stellar Designer** A web-based design tool that defines your robot's kinematics, links, joints, wheels and actuator mapping through a GUI, and the gateway that connects the actuators, entirely hardware-free.

**Compose: Stellar Station** The control center on the controller. Add gateways and controllers as nodes, connect their ports, load their design documents and start them, all in the browser.

**Simulate: NVIDIA Isaac Sim** The Isaac Bridge extension connects a robot in Isaac Sim to the Station. The simulated robot is driven by exactly the same controller and documents as the real one.

**Run: Stellar Hardware Series** Starting with Stellar X, our industry-proven universal motion controller with an EtherCAT master, Sodero will continuously expand its physical ecosystem with next-generation lineups to support various form factors and specialized applications.

In simulation and on the real robot alike, you operate the robot from the same built-in controller UIs: **Motion Studio** for manipulators, **Strider** for mobile bases and **Articulation** for articulated and legged robots.

**Tip:** Every tool runs in the browser and is served by Stellar X itself. Connect a PC to the controller's network and open its address; there is nothing to install on your PC except Isaac Sim for simulation.

______________________________________________________________________

### Integration and Extensibility

Beyond controlling a single robot, Sodero integrates with complex system integration (SI) environments and upper-level host controllers.

**Modules** Package your own programs and install them on the Station. They run as nodes next to the built-in ones and use the same interfaces to command robots, read sensors and send navigation goals.

**SSH Workspace and the `sodero` CLI** Every Station operation is available as a command that prints JSON, for scripts, CI pipelines and AI coding agents.

Continue with [Key Concepts](https://docs.sodero.io/v2.0.0/get_started/key_concepts/index.md), then try the [Quick Start](https://docs.sodero.io/v2.0.0/get_started/quick_start/index.md).
