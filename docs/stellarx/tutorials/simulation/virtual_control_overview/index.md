Virtual Control via Simulation

Virtual control is achieved by communicating with a simulated robot instead of a physical EtherCAT slave. By transmitting target commands to the simulator and receiving state values in return, you can treat and operate the robot within the simulator exactly as you would a real one.

Using the controller configured through **Step 1** and **Step 2** (dynamics from Step 3 are not considered for the controller side), you can control a robot with specific kinematics and dynamics in the simulated world.

This process allows you to:
- Verify if your kinematics settings are accurate.
- Observe how a robot with those specific dynamics reacts to the controller. For example, if proper torque compensation is applied when switching to direct teaching mode, the robot will maintain its position without sagging.

Currently, we support communication with **Isaac Sim**. This seamless integration is made possible through an Isaac Sim extension called **Stellar Bridge**.