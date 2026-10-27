# Stop Controls

A robot on Stellar X can be stopped in several ways: buttons in the controller UIs and the test console, automatic stops of the gateway, and the emergency stop that you wire yourself. This page compares them, so that you know what each one does before real motors move.

**On-screen buttons are not emergency stops.** They are software functions of the controllers and the gateway, and they act only while the browser, the network, Stellar X and the drives work. Every robot with real motors needs a hardware emergency stop that removes motor power or triggers the drives' safe torque off (STO), wired as the drive manufacturer describes. Keep it within reach whenever the motors are powered.

______________________________________________________________________

## 1. Hardware Emergency Stop and STO

The hardware emergency stop and the drives' STO inputs are part of your machine, not of Stellar X. How they stop the motors depends on your wiring and on the drives. While they are active, the drives cannot be enabled: the gateway reports *Servo ON failed: drive … did not enable* ([EtherCAT Gateway › Troubleshooting](https://docs.sodero.io/stellar-x/v2.0.1/gateways/ethercat/#6-troubleshooting)). After you release them, switch the servo on again in the UI.

______________________________________________________________________

## 2. Stops in the UIs

| Control                                                                                            | What it does                                                                                                                                                                                                 | Servo afterwards | To continue                                                                                                              |
| -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **E-STOP** (Strider, top bar)                                                                      | Cancels manual driving and the navigation goal and sets the wheel speeds to zero at once. The drives stay enabled and hold zero speed. The stop latches.                                                     | On               | **Clear E-Stop** (the base switches to **Idle**), then **Twist**                                                         |
| **Stop Motion**, **Stop (Space)**, releasing a pad button (Strider, Drive page)                    | Ends manual driving (and, for **Stop Motion**, a navigation goal). The base slows down at the acceleration limits of its document.                                                                           | On               | Drive again                                                                                                              |
| Releasing a jog button or **Hold to move** (Motion Studio)                                         | The arm slows down over a short ramp and holds its position.                                                                                                                                                 | On               | —                                                                                                                        |
| **Stop** (Articulation, top bar)                                                                   | Switches the servo off and latches a stop.                                                                                                                                                                   | Off              | **Clear stop**, then **Servo on**                                                                                        |
| **Servo Off** / **Servo off** / **Servo OFF** (Strider, Motion Studio, Articulation, test console) | Disables the drives. The motors no longer hold: a base rolls out, and a joint without a brake can fall. Whether a motor brake engages depends on the drive's configuration.                                  | Off              | Switch the servo on                                                                                                      |
| **EMERGENCY STOP** (test console)                                                                  | Sends a quick stop to every drive of the gateway and switches the servo off. How a drive slows down depends on its quick stop settings. While it is active, **Servo ON** and **Fault Reset** have no effect. | Off              | Click it again to release it, then **Servo ON**. If a drive does not enable again, end the test and restart the gateway. |

Motion Studio has no on-screen emergency stop. Use the hardware emergency stop, or switch the servo off where the arm can safely lose its holding torque.

**A closed tab does not stop the robot.** Closing a UI tab or losing the network connection is not a stop command. Strider stops manual driving within about a second, but a navigation goal continues. In Motion Studio and the [test console](https://docs.sodero.io/stellar-x/v2.0.1/gateways/test_console/index.md), a motion that is running when the browser loses the page can continue. Stop the motion before you leave a UI, and use the hardware emergency stop when a UI does not respond.

______________________________________________________________________

## 3. Automatic Stops

| Situation                                                              | What happens                                                                                                                                                                                                             | To continue                                                                 |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| A controller stops sending commands while the servo is on              | The gateway keeps the last command for 3 s, then switches the servo off (*No commands from the robot controller for 3.0 s: servo turned OFF for safety.*).                                                               | Start the controller and switch the servo on                                |
| EtherCAT communication is lost                                         | The gateway switches the servo off and reports *EtherCAT communication lost*.                                                                                                                                            | Fix the cable or the drive's power, then restart the gateway                |
| A drive reports a fault                                                | The gateway reports the fault in **Gateway events**.                                                                                                                                                                     | Fix the cause, **Fault Reset** or **Error Reset**, then switch the servo on |
| Motion Studio: a joint limit, a speed or torque limit, or a collision  | Protective stop: the arm holds its position with the servo on ([Manipulator › Robot System Parameters](https://docs.sodero.io/stellar-x/v2.0.1/tutorials/stellar_designer/manipulator/#step-2-robot-system-parameters)). | **Error Reset**                                                             |
| Motion Studio: no feedback from the gateway, or a critical drive fault | Emergency stop: the controller requests a quick stop and the servo switches off.                                                                                                                                         | Stop and start the Motion Studio node                                       |
| Articulation: feedback older than 100 ms, or no new target for 200 ms  | The servo switches off and a stop latches.                                                                                                                                                                               | **Clear stop**, then **Servo on**                                           |
| Strider: no manual command for about 1 s                               | The base slows to a stop.                                                                                                                                                                                                | Drive again                                                                 |

______________________________________________________________________

## 4. Before You Power Real Motors

1. Wire and test the hardware emergency stop and the drives' STO.
1. Lift wheels off the ground, or keep the axes clear of their end stops.
1. Check each actuator alone with the [test console](https://docs.sodero.io/stellar-x/v2.0.1/gateways/test_console/index.md), at low speed.
1. Start the controller with low limits, and keep someone at the emergency stop.
