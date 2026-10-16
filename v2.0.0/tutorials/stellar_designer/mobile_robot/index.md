# Mobile Robot (.sddm)

This tutorial builds the document of a wheeled mobile base, using the Clearpath Jackal (skid steer, four wheels) of the [Quick Start](https://docs.sodero.io/v2.0.0/get_started/quick_start/index.md). The document belongs to a Strider node (`rc.mobile_controller_manager.NAME`).

______________________________________________________________________

## Before You Start

1. On the Station, add a **Controller › Strider** node, for example `jackal`.
1. Select it and click **Edit Stellar Designer**.
1. In **Create robot definition**, choose the template that matches your drive:

| Template               | Drive                                            |
| ---------------------- | ------------------------------------------------ |
| Differential drive 2WD | Two driven wheels and casters                    |
| MiR250 differential    | Differential drive of a MiR250                   |
| Skid steer 4WD         | Four fixed driven wheels that slide when turning |
| Mecanum 4WD            | Four mecanum wheels, omnidirectional             |
| Swerve 4WD             | Four steered and driven wheels                   |
| Ackermann              | Car-like steering                                |
| Tricycle 3WD           | One steered and driven wheel, two passive wheels |

The template sets the drive type, which decides how body velocities become wheel commands. Then change its dimensions to those of your robot.

______________________________________________________________________

## Step 1: Chassis Structure

Chassis Structure of a skid-steer base

Step **01 Chassis Structure** ① shows the body and the wheels of the base.

**Body** ②:

| Field                             | Meaning                                                                      |
| --------------------------------- | ---------------------------------------------------------------------------- |
| **Template**                      | The drive type                                                               |
| **Length**, **Width**, **Height** | Outer dimensions of the body                                                 |
| **Base Origin Z**                 | Height of the robot's base frame above the floor (normally the wheel radius) |
| **Track Width**                   | Distance between the left and right wheels of a differential drive           |

**Wheels** ③ (`Wheel-fl`, `Wheel-fr`, `Wheel-rl`, `Wheel-rr`):

| Field                                    | Meaning                                                                        |
| ---------------------------------------- | ------------------------------------------------------------------------------ |
| **Role**                                 | `drive` (driven), `steer` (steered), `drive + steering`, or `caster` (passive) |
| **Radius**, **Width**                    | Wheel size                                                                     |
| **Offset X**, **Offset Y**, **Offset Z** | Wheel position relative to the base frame (X forward, Y left)                  |

**Constraints** ④ opens the wheel's drive limits in the right panel ⑥: **max_speed** and **max_accel** of the wheel.

The constraints of the front-left wheel, with its diameter and width in the 3D view

**Display** ⑤ changes the 3D view; the unit menu ⑦ changes the display units.

Skid-steer wheels slide sideways when the robot turns, so the robot turns less than the wheel speeds suggest. The skid-steer kinematics use the wheels' **Offset Y**: turn the robot in place by a known angle and increase the left and right **Offset Y** until the odometry matches the real turn. The simulated Jackal of the Quick Start, for example, uses an effective **Offset Y** of 0.441 m.

______________________________________________________________________

## Step 2: Robot System Parameters

Robot System Parameters of the Jackal

| Group           | Fields                                                                   | Meaning                                                                   |
| --------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| **ROBOT**       | Total mass, Max payload, Center of mass, Body inertia                    | Mass properties of the robot                                              |
| **ENVIRONMENT** | Gravity vector                                                           | Normally `(0, 0, -9.81) m/s²`                                             |
| **MOTION**      | Max linear speed, Max angular speed, Max linear accel, Max angular accel | Limits of the body velocity. Strider and the navigator never exceed them. |

______________________________________________________________________

## Step 3: Actuator Mapping

Four actuators driving the four wheels

Connect each actuator of the gateway to the wheel it drives (or steers), as for a manipulator ([Manipulator › Actuator Mapping](https://docs.sodero.io/v2.0.0/tutorials/stellar_designer/manipulator/#step-3-actuator-mapping)). The order must match the gateway: in the Jackal's gateway, actuator 1 is the front-left wheel, 2 front-right, 3 rear-left, 4 rear-right.

A mobile base uses the mapping only to know which actuator drives which wheel; leave the **INFLUENCE FACTOR** at `1`. The wheel kinematics already account for the left and right side. If a real wheel still turns the wrong way, invert the motor's direction in its drive, for example with the drive's polarity parameter as a start-up SDO in the [Gateway Designer](https://docs.sodero.io/v2.0.0/gateways/ethercat/#ethercat-tab).

______________________________________________________________________

## Step 4: Verification

Click **Verify**. Stellar Designer checks the chassis structure, the system parameters, the actuator mapping and the configuration files.

All checks passed: skid steer, 4 wheels, 4 actuators

**Export .sddm** saves a copy of the document to your computer.

______________________________________________________________________

## Try the Robot

Start the gateway and the Strider node, open Strider, choose **Twist**, switch the servo on and drive slowly ([Strider](https://docs.sodero.io/v2.0.0/controllers/strider/index.md)). Check that:

- **Forward** drives forward and every wheel turns the right way,
- **Turn Left** turns counterclockwise (seen from above),
- the odometry on the **Status** page matches the distance and angle actually driven.
