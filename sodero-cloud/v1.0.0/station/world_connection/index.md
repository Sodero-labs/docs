# Connect to the World

The Robot Systems of a project drive the robots in the project's active Robot World. Sodero Cloud makes the connection: a simulation gateway reaches the World by itself and finds its robot by name. This page shows what to set so that a robot moves.

```
flowchart LR
    subgraph RS ["Robot System"]
        C["Controller<br>sodero.mlc.jackal"] -- servo_link --> G["Simulation gateway<br>sodero.actuator_gateway.jackal<br>Robot name: jackal"]
    end
    subgraph W ["Robot World, active"]
        R["Robot prim jackal<br>joints 1 to 4"]
    end
    G -- "found by name" --> R
```

______________________________________________________________________

## 1. What Is Automatic

- **No address to set.** The simulation, camera and IMU gateways of an active Station reach the project's active World through the local simulator address, which is the default in their documents: Sodero Cloud forwards it to the World. Keep that default; a document that points to another address does not reach the World.
- **Activate in any order.** A Station that is active before the World connects once the World is up.
- **One World per project.** Only one Robot World of a project can be active at a time, and a Station never reaches a World in another project ([How Robot Worlds and Robot Systems Work Together](https://docs.sodero.io/sodero-cloud/v1.0.0/projects/files/#4-how-robot-worlds-and-robot-systems-work-together)).

______________________________________________________________________

## 2. Name the Robot

A simulation gateway drives the robot whose articulation prim has its robot name. You set the robot name on the gateway node in the Station, so that one gateway document fits any robot:

1. Select the simulation gateway node, for example `sodero.actuator_gateway.jackal`.
1. Under **Parameters**, check that **Gateway project** names its gateway document ([Documents and Settings](https://docs.sodero.io/sodero-cloud/v1.0.0/station/documents/index.md)).
1. In **Robot name**, under the document, enter the name of the robot's articulation prim, for example `jackal` for `/World/jackal`. Press `Enter`, or leave the field, to save it.

A new name applies at the gateway's next start. Without a name, the inspector says *No robot name yet: the gateway is tied to no robot in the World.* Renaming the node does not change the robot it drives.

**The robot name must be exactly the name of the robot's articulation prim in the World.**

| Station                                                                        | World                                                                               |
| ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| Gateway node `sodero.actuator_gateway.jackal` with the **Robot name** `jackal` | The robot's articulation prim `jackal`, at `/World/jackal` in the World's hierarchy |

- Names are case-sensitive: `Jackal` and `jackal` are different robots.
- A robot name uses letters, digits and `_`, and does not start with a digit.
- Every robot in the World needs a name of its own.

If the names differ, the gateway never finds its robot: it keeps waiting, and the robot does not move.

______________________________________________________________________

## 3. Match Actuators and Joints

The gateway addresses joints by actuator index. Actuator *i* drives the robot's *i*-th movable joint, revolute or prismatic, in the order of the robot's USD file; joints marked `rc:passive = true` are skipped ([Prepare a World for Simulation](https://docs.sodero.io/sodero-cloud/v1.0.0/worlds/prepare_world/#3-joints-are-actuators-in-usd-order)).

| Gateway                               | Robot in the World                                           |
| ------------------------------------- | ------------------------------------------------------------ |
| Actuators 1, 2, 3, 4 (indices 0 to 3) | The robot's 1st, 2nd, 3rd and 4th movable joint in USD order |

- Give the gateway one actuator per joint it drives. The robot document then maps the gateway's actuators to its joints or wheels ([Documents and Settings](https://docs.sodero.io/sodero-cloud/v1.0.0/station/documents/index.md)).
- The **Joints** list in Studio is alphabetical; it does not show this order.
- To drive one robot with two gateways, for example an arm and its gripper, set the gripper gateway's **DOF offset** to the index of the gripper's first joint ([Gateway Designer › Simulation Gateways](https://docs.sodero.io/stellar-x/latest/gateways/gateway_designer/#5-simulation-gateways) in the Stellar X manual).

What a robot needs in the World, such as its articulation and joint drives, is described in [Prepare a World for Simulation](https://docs.sodero.io/sodero-cloud/v1.0.0/worlds/prepare_world/index.md).

______________________________________________________________________

## 4. Several Robots and Stations

- Use one gateway and one controller per robot, each gateway with its own robot name.
- The gateways can sit in one Robot System or in several. Every active Robot System of the project connects to the same World.
- Drive each robot, or each part of a robot, from one gateway only.

______________________________________________________________________

## 5. Cameras and IMUs

- **Camera gateway** (`sodero.camera_gateway.<name>`): its camera name must be the name of the camera's prim in the World. It uses letters, digits, `_`, `-` and `.`. The World renders the robots' cameras while it is active; the first pictures can take a moment after the World starts.
- **IMU gateway** (`sodero.imu_gateway.<name>`): it reads the IMU of one robot, which you name like the robot of an actuator gateway.

The World must declare its cameras and IMUs ([Prepare a World for Simulation](https://docs.sodero.io/sodero-cloud/v1.0.0/worlds/prepare_world/index.md)).

______________________________________________________________________

## 6. Start Order

Activate the World and the Robot System and run the World ([Activate and Run](https://docs.sodero.io/sodero-cloud/v1.0.0/projects/activate_run/#how-it-works)), start the gateway before its controller ([Start and Monitor Nodes](https://docs.sodero.io/sodero-cloud/v1.0.0/station/run/index.md)), then switch the servo on in the controller's UI ([Strider](https://docs.sodero.io/sodero-cloud/v1.0.0/operate/strider/index.md), [Motion Studio](https://docs.sodero.io/sodero-cloud/v1.0.0/operate/motion_studio/index.md), [Articulation](https://docs.sodero.io/sodero-cloud/v1.0.0/operate/articulation/index.md)).

______________________________________________________________________

## 7. Troubleshooting

A gateway connects to the World, not to another node. A World that is not running, or a robot name that does not match, therefore shows neither as **Waiting binding** nor as an error in the graph: the gateway's node can look normal while the gateway waits for its robot. Select the gateway and read its **Gateway events** log ([Logs and Activity](https://docs.sodero.io/sodero-cloud/v1.0.0/station/run/#5-logs-and-activity)). It says whether the gateway is still waiting for its robot or is connected to the simulation.

| Symptom                                                        | What to check                                                                                                                                                                                       |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The gateway keeps waiting for its robot                        | The World is active and playing; it is in the same project; the gateway's **Robot name** equals the robot's prim name exactly; the gateway document keeps the default simulator address             |
| The controller stays in **Waiting binding**                    | Its `servo_link` is connected to the gateway, and the gateway runs ([Node States](https://docs.sodero.io/sodero-cloud/v1.0.0/station/run/#4-node-states))                                           |
| The servo switches on, but the robot does not move             | The gateway has as many actuators as the robot document uses. In Strider, the drive mode is **Twist**.                                                                                              |
| A wheel or joint turns the wrong way, or the wrong joint moves | Stop motion. Check the robot's joint order in USD, the actuator mapping of the robot document, the axis direction and the configured polarity. Change the document, then check one joint at a time. |
| The servo switched off by itself                               | The World may have been stopped or reset; stopping a World resets its robots' poses. Switch the servo on again.                                                                                     |
| The camera gateway shows no picture                            | The camera name equals the camera's prim name; the World plays and declares its cameras                                                                                                             |
| The robot moves slower than expected                           | In Theater, **Physics RTF** is below 1.00: the World simulates slower than real time ([Theater](https://docs.sodero.io/sodero-cloud/v1.0.0/worlds/theater/index.md))                                |
