# Prepare a World for Simulation

The Stations of a project can drive a robot in its Robot World only when the World follows a few rules. They are the rules for a robot in NVIDIA Isaac Sim on Stellar X, plus two more: a purpose for robot cameras and a schema on fixed joints. The scene of the [Quick Start](../../get_started/quick_start/index.md) follows all of them: use it as a model.

Studio has no tools to create articulations, joints, colliders or cameras. Prepare robots in a USD tool such as Isaac Sim ([Prepare the Robot](https://docs.sodero.io/stellar-x/latest/virtual_simulation/robot_setup/) in the Stellar X manual), then bring the scene into the World with **Replace scene…**. A robot in a single USD file can also come in through **Upload from PC** ([Studio](../studio/index.md#2-bring-content-in)).

---

## The Rules

| Rule | Why |
| :--- | :--- |
| **The World is Z-up, in meters, and has a PhysicsScene.** | Studio refuses Y-up scenes, and the simulation needs a physics scene. |
| **Each robot is one articulation.** Its top prim carries an **Articulation Root**. | A robot is simulated and driven as one articulation. |
| **The prim name is the robot name.** It is unique in the World and equals the **Robot name** set on the robot's simulation gateway node. | A simulation gateway finds its robot by this name. |
| **Actuators follow the USD joint order.** Actuator *i* of a gateway drives the robot's *i*-th movable joint in USD order. | The gateway addresses joints by actuator index. |
| **Robot cameras have unique names and the purpose `guide`.** | A camera gateway reads its camera by name, and Sodero renders robot cameras that have this purpose. |
| **Fixed joints carry a physics joint schema.** | A fixed joint without one takes no part in the simulation. |

---

## 1. Z-Up and a PhysicsScene

- Author the scene Z-up, in meters. Studio refuses a scene that declares Y-up: convert it before you bring it in.
- Include a **PhysicsScene** prim. Check that the **Hierarchy** in Studio shows one; the Quick Start's scene does.

---

## 2. One Articulation per Robot

- The robot's top prim carries the **Articulation Root**. A robot has exactly one.
- Its links are rigid bodies with colliders and realistic masses. Studio can correct a body's mass or density ([Studio](../studio/index.md#3-arrange-and-edit)).
- The prim's name is the robot name: letters, digits and `_`, not starting with a digit. It must be unique in the World, and case matters.
- The robot's simulation gateway node uses the same name as its **Robot name** ([Connect to the World](../../station/world_connection/index.md#2-name-the-robot)). For the example scene, the Jackal articulation is `/World/jackal`.

!!! warning "**Names must match.** If the gateway node's **Robot name** differs from the robot's prim name, the robot never moves. Rename the prim, or change the **Robot name**."

---

## 3. Actuators Follow the USD Joint Order { #3-joints-are-actuators-in-usd-order }

A simulation gateway drives the robot's joints by actuator index:

- Actuator 1 (index 0) drives the first movable joint under the robot prim, actuator 2 the second, and so on. Movable joints are revolute and prismatic joints; fixed joints are not actuators.
- The order is the order in which the robot's USD file defines the joints, for example the order of the joint prims in a `.usda` file.
- A joint marked `rc:passive = true` is not an actuator and is skipped.

The robot document maps its joints or wheels to the gateway's actuators: that mapping must match this order. Use robot documents prepared for this scene and Station release ([Compatibility](../../reference/compatibility/index.md)).

Studio's **Joints (n)** list shows a robot's joint names and their number, in alphabetical order: it does not show the actuator order.

Before normal operation, test one joint or wheel at a time with a small command and confirm that the intended part moves in the intended direction. Stop and correct the actuator mapping or axis configuration if it does not. Keep joint limits consistent with the robot model.

---

## 4. Cameras and IMUs

**Cameras.** A camera gateway reads one camera of the World by its name.

- Put each robot camera, a **Camera** prim, under the link it is mounted on, so that it moves with the robot.
- Give it a unique name. The camera gateway's camera name is this prim name: letters, digits, `_`, `-` and `.`.
- Set the camera's **purpose** to `guide`. Robot cameras need this purpose in Sodero Cloud; a camera without it is not rendered for the Station.

While the World is active, Sodero renders its robot cameras for the camera gateways of the project's Stations. Theater's loading screen shows their progress under **Robot cameras**.

**IMUs.** An IMU gateway reads an IMU on a link of the robot. Declare it on the robot prim with `rc:imuLink`, the name of the link, and `rc:imuOffset`, its position on that link in meters, as for Isaac Sim ([Prepare the Robot › IMU](https://docs.sodero.io/stellar-x/latest/virtual_simulation/robot_setup/#7-imu)).

---

## 5. Fixed Joints

A fixed joint holds a body in place, for example the base of a manipulator on the world. Give every fixed joint a physics joint schema, such as `PhysxJointAPI`. Without one, the joint takes no part in the simulation in Sodero Cloud, and a fixed-base robot falls over.

In Isaac Sim, you can set a camera's purpose and a fixed joint's schema with **Window › Script Editor**, then save the scene:

```python
import omni.usd
from pxr import PhysxSchema, UsdGeom

stage = omni.usd.get_context().get_stage()

# a robot camera: purpose guide
camera = stage.GetPrimAtPath("/World/my_robot/links/base_link/cam0")
UsdGeom.Imageable(camera).CreatePurposeAttr().Set(UsdGeom.Tokens.guide)

# the fixed joint that holds my_arm to the world: a physics joint schema
anchor = stage.GetPrimAtPath("/World/my_arm/joints/anchor")
PhysxSchema.PhysxJointAPI.Apply(anchor)
```

Replace the prim paths with those of your scene.

---

## 6. Keep the World Light

- Everything in the World is drawn, but only physics content takes part in the simulation: the physics scene, rigid bodies, colliders, joints and articulations. Give physics only to what the robots touch.
- Large scenes take longer to load. Theater reports a World that has not loaded within 3 minutes. A file you bring into Studio can be up to 1 GiB.
- Watch **Physics RTF** in Theater. Near 1.00, the simulation keeps up with real time; if it stays well below 1.00, make the World lighter.

---

## 7. Test the World in Theater

Check the World on its own before you connect Stations to it:

1. Save the World in Studio and close Studio.
2. On the project page, activate the World.
3. Open **Theater** and wait until the World, and its **Robot cameras** if it has any, have loaded.
4. Click **Start Theater**.
5. Check that:
    - the robots rest on the ground and do not fall through it or drift away;
    - a fixed-base robot stays in place;
    - **Physics RTF** is near 1.00;
    - each robot appears in **Scene assets** under the **Robot name** of its gateway node.
6. Click **Stop Theater**. To change the World, deactivate it and open it in Studio.

Next: [Connect to the World](../../station/world_connection/index.md).
