# Sodero Ecosystem

Sodero connects robot design, simulation and operation on one controller. You describe the robot in Stellar Designer, run it on Stellar X with the built-in controllers, and drive it in NVIDIA Isaac Sim or on real motors through a gateway.

The same controller and application structure can be reused in simulation and on supported hardware. Before operating the physical robot, configure its gateway and verify actuator mapping, calibration, limits and sensor settings.

---

## Core Architecture

**Gateways separate controllers from hardware.** Controllers never talk to hardware directly. A gateway connects them to EtherCAT drives, to a robot in NVIDIA Isaac Sim, or to sensors, so the same controller and controller document can drive a simulated robot and a real one.

**One Station runs every node.** Gateways, controllers, navigation and your own modules run as nodes of one Station on Stellar X. They are connected through ports with defined interfaces, so built-in nodes and your own work together in the same way on every robot.

---

## From Design to the Real Robot

The Sodero ecosystem connects the entire process, from robot design and validation to physical deployment, into a single pipeline.

```mermaid
flowchart TB
    D["Design<br>Stellar Designer"] --> S["Compose<br>Stellar Station"]
    S --> V["Simulate<br>Isaac Sim + Isaac Bridge"]
    V --> R["Run<br>Stellar X + real hardware"]
    R -. "same controller,<br>EtherCAT gateway" .- V
```

**Design: Stellar Designer.** A web-based tool for defining your robot's kinematics, links, joints, wheels and actuator mapping, and the gateway that connects its actuators, without any hardware.

**Compose: Stellar Station.** The control center on the controller. Add gateways and controllers as nodes, connect their ports, load their design documents and start them, all in the browser.

**Simulate: NVIDIA Isaac Sim.** The Isaac Bridge extension connects a robot in Isaac Sim to the Station. The simulated robot is driven by the same controller and controller document as the real one, through a simulation gateway instead of an EtherCAT gateway.

**Run: Stellar X.** The motion controller with an EtherCAT master that runs the Station and its nodes. On the real robot, its EtherCAT gateway drives the servo drives, after you have checked the actuator mapping, calibration and limits on the hardware.

In simulation and on the real robot alike, you operate the robot from the same built-in controller UIs: **Motion Studio** for manipulators, **Strider** for mobile bases and **Articulation** for articulated and legged robots.

!!! idea "**Tip:** The Station, Stellar Designer and the controller UIs run in the browser and are served by Stellar X itself: connect a PC to the controller's network and open its address. Other software is installed only where you use it: Isaac Sim with the Isaac Bridge extension for simulation, an SSH client for the SSH workspace, and the Device Bridge on a computer next to its sensors."

!!! info "**Sodero Cloud.** The same Stellar Station, design documents and controller UIs also run in Sodero Cloud, where robots are simulated in Robot Worlds in the browser instead of Isaac Sim on your PC. See the [Sodero Cloud manual](https://docs.sodero.io/sodero-cloud/latest/)."

---

## Integration and Extensibility

Beyond controlling a single robot, Sodero works with your own programs and tools.

**Modules.** Package your own programs and install them on the Station. They run as nodes next to the built-in ones and use the same interfaces to command robots, read sensors and send navigation goals.

**SSH Workspace and the `sodero` CLI.** Every Station operation is available as a command that prints JSON, for scripts, CI pipelines and AI coding agents.

---

Continue with [Key Concepts](../key_concepts/index.md), then follow the [Learning Path](../../tutorials/learning_path/index.md).
