# Sodero Ecosystem

## A Software-Defined Robotics Platform: Build Once. Move Everywhere.
Sodero fundamentally resolves the biggest bottlenecks in traditional robot development: **Tight Hardware Coupling** and the **Sim-to-Real Gap**. By abstracting complex control environments into a standardized software layer, we provide an innovative, unified ecosystem. Developers can now design robots in a virtual environment and deploy them directly to the real world without changing a single line of code.

### Core Architecture

**Causality-Aligned Simulation**
  Going beyond simple 3D rendering, our Reverse Digital Twin technology ensures that the control logic in the virtual environment perfectly matches the physical outcomes in reality. Success in simulation guarantees success in the real world.
**Unified Execution Layer**
  Even if the robot's form factor or hardware changes, there is no need to rewrite the glue code from scratch. All codes and motions written on the Sodero platform are executed with perfectly standardized semantics.

### The Build-Teach-Run Workflow
The Sodero ecosystem connects the entire process—from robot design and validation to physical deployment—into a single, seamless pipeline.

**Build: Stellar Designer** A web-based control design tool that allows you to intuitively define your robot's kinematics, links, and joint parameters via a GUI, entirely hardware-free.
**Create: Stellar Motion Studio** An intuitive motion generation interface where you can create precise trajectories and safely test poses without writing complex code.
**Simulate: Virtual Controller & NVIDIA Isaac Sim** A free, Docker-based virtual controller that runs instantly without complex host OS configurations. Integrated with NVIDIA Isaac Sim, it enables perfect pre-validation even without physical hardware.
**Run: Stellar Hardware Series** Starting with Stellar X, our industry-proven universal motion controller, Sodero will continuously expand its physical ecosystem with next-generation lineups (e.g., Stellar Y, Z) to support various form factors and specialized applications.

!!! idea "**Tip:** Stellar Designer and Motion Studio operate in a browser-native environment. Start designing your own robot immediately without installing heavy software on your PC."



### Infinite Extensibility
Beyond controlling a single robot, Sodero supports flexible integration with complex SI (System Integration) environments and upper-level host controllers.

**Language-Agnostic SDK (stellarx_remote)** Built on an independent RPC (Remote Procedure Call) architecture, our SDK allows you to integrate upper-level controllers using your preferred programming language, such as C++, Python, or Rust.
**Unified API Experience** The API used for internal simulation testing is structurally identical to the one used for external remote control. Apply the code you wrote in the virtual environment directly to your production deployment without any modifications.
 