# Key Concepts

This page explains the terms you meet everywhere in Sodero Cloud: workspaces and projects, Robot Systems and Robot Worlds, activation, Studio and Theater, and the parts of a Station. Read it once before the [Quick Start](https://docs.sodero.io/sodero-cloud/v1.0.0/get_started/quick_start/index.md).

______________________________________________________________________

## Workspaces and Projects

```
flowchart TB
    subgraph WS ["Workspace: people, plan, credits"]
        subgraph P ["Project: files and the people who can open them"]
            A["Robot System A<br>Stellar Station"] -- "simulation gateway" --> W["Robot World<br>simulated in the cloud"]
            B["Robot System B<br>Stellar Station"] -- "simulation gateway" --> W
        end
    end
```

| Term             | What it is                                                                                                                                                                                                               |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Workspace**    | Where a team works together: its people, its projects, its plan and its credits. You can belong to several workspaces ([Workspaces and People](https://docs.sodero.io/sodero-cloud/v1.0.0/account/workspaces/index.md)). |
| **Project**      | Robot Systems and Robot Worlds that belong together, and the people who can open them ([Projects](https://docs.sodero.io/sodero-cloud/v1.0.0/projects/projects/index.md))                                                |
| **Robot System** | A project file that is one Stellar Station ("the Station"): the robot system's nodes, documents, settings and apps                                                                                                       |
| **Robot World**  | A project file that holds a simulated place: a USD scene with the ground, the lighting, objects and robots                                                                                                               |

A project can hold several Robot Worlds, but only one of them can be active at a time. Any number of Robot Systems can be active, within your plan's limit of **Systems and Worlds running at once**, and they all drive robots in that World ([How Robot Worlds and Robot Systems Work Together](https://docs.sodero.io/sodero-cloud/v1.0.0/projects/files/#4-how-robot-worlds-and-robot-systems-work-together)).

______________________________________________________________________

## Activate and Run

Each Robot System and Robot World has its own environment in the cloud. Two columns on the project page control it, and they are separate steps:

| Column         | States                   | What it does                                                                                                                                     |
| -------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Activation** | **Inactive**, **Active** | **Activate** brings the environment up: a Station restores its saved data, a World loads its saved scene. **Deactivate** releases it.            |
| **Running**    | **Stopped**, **Running** | **Run** starts what is in an active environment: the Station's nodes, the World's simulation. **Stop** stops them; the environment stays active. |

- **Credits.** An active file uses your workspace's credits for every minute it is active, whether or not anything runs in it. Stop does not end that; Deactivate does. Studio and Theater sessions can use credits too, depending on their rendering mode ([Billing and Usage](https://docs.sodero.io/sodero-cloud/v1.0.0/account/billing/index.md)).
- **Auto off.** An active file that nobody has used for 30 minutes is deactivated automatically, unless an editor has cleared its **Auto off** box. A Station counts as used while someone has it open or works with it through an AI agent or the Project VPN; a World, while someone watches it in Theater.

Details: [Activate and Run](https://docs.sodero.io/sodero-cloud/v1.0.0/projects/activate_run/index.md).

______________________________________________________________________

## Studio and Theater

| Tool        | For                                                                                                                                                                                  | Opens while the World is |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| **Studio**  | Building the World: bring in scenes and Sodero Assets, arrange objects, set mass and joint poses, save ([Studio](https://docs.sodero.io/sodero-cloud/v1.0.0/worlds/studio/index.md)) | **Inactive**             |
| **Theater** | Watching the running World: select robots and see the Station that drives each one ([Theater](https://docs.sodero.io/sodero-cloud/v1.0.0/worlds/theater/index.md))                   | **Active**               |

Both ask first for a **rendering mode**. **RTX Real-time** draws the World on a cloud GPU; **WebGPU** draws it in your browser with your computer's GPU. The mode changes only how you see the World: the simulation is the same for everyone ([Choose Rendering Mode](https://docs.sodero.io/sodero-cloud/v1.0.0/projects/activate_run/#choose-rendering-mode)).

______________________________________________________________________

## Inside a Robot System: the Station

A **Station** is a graph of **nodes**. Each node is one program, such as a gateway, a robot controller, a navigation component or a module of your own. **Add node** offers four types:

| Type            | Purpose                                       |
| --------------- | --------------------------------------------- |
| **Gateway**     | Connects simulation or hardware to the system |
| **Controller**  | Defines a robot unit and its control          |
| **Compound**    | Combines several robot units into one system  |
| **Application** | Defines robot behaviors and task logic        |

Every node runs an **app**. Sodero's apps come from the Station's **Store**; your own module packages are added on **Modules**. A new Robot System can start with a bundle of apps, its **Starting apps** ([Apps and Packages](https://docs.sodero.io/sodero-cloud/v1.0.0/station/apps/index.md)).

The IDs of Sodero's nodes start with `sodero.`. Most of them end with a name you choose, usually the robot's:

| Node                                        | ID                                         |
| ------------------------------------------- | ------------------------------------------ |
| Actuator gateway                            | `sodero.actuator_gateway.<name>`           |
| Camera gateway                              | `sodero.camera_gateway.<name>`             |
| Mobile base controller                      | `sodero.mlc.<name>`                        |
| Manipulator controller (Motion Studio)      | `sodero.mmc.<name>`                        |
| Articulated robot controller (Articulation) | `sodero.amc.<name>`                        |
| Strider, the operator UI of a mobile base   | `sodero.strider`                           |
| Localizer, Navigator                        | `sodero.icp_localizer`, `sodero.navigator` |

### Ports

Nodes work together through **ports**. Each node card lists **REQUIRES**, the services the node needs, and **PROVIDES**, the services it offers. You connect a required port to a matching provided port; the Station refuses ports that do not match. A mobile robot such as Jackal uses two connections:

```
flowchart TB
    S["Strider<br>sodero.strider"] -- "mobile_base" --> M["Mobile base controller<br>sodero.mlc.jackal"]
    M -- "servo_link" --> G["Actuator gateway<br>sodero.actuator_gateway.jackal"]
    G -- "robot name jackal" --> W["Robot World<br>robot /World/jackal"]
```

| Requires                | Provides                             | Meaning                                       |
| ----------------------- | ------------------------------------ | --------------------------------------------- |
| Controller `servo_link` | Actuator gateway `servo_link`        | The controller drives the gateway's actuators |
| Strider `mobile_base`   | Mobile base controller `mobile_base` | Strider operates this mobile base             |

See [Build the Graph](https://docs.sodero.io/sodero-cloud/v1.0.0/station/graph/index.md).

### Gateways and Documents

A **gateway** is the only node that talks to actuators; controllers send their commands through it. In Sodero Cloud, a simulation gateway drives a robot in the project's World. On Stellar X, an EtherCAT gateway drives real drives; the controllers work the same way, in the Station release that the device runs ([Compatibility](https://docs.sodero.io/sodero-cloud/v1.0.0/reference/compatibility/index.md)).

Gateways and controllers are configured by **design documents**, which you upload into the node's **Parameters** ([Documents and Settings](https://docs.sodero.io/sodero-cloud/v1.0.0/station/documents/index.md)):

| File    | Node             | Contents                                                  |
| ------- | ---------------- | --------------------------------------------------------- |
| `.gw`   | Actuator gateway | Hardware type and actuators                               |
| `.sdd`  | `sodero.mmc`     | Manipulator: kinematics, dynamics, actuator mapping       |
| `.sddm` | `sodero.mlc`     | Mobile base: drive type, wheels, limits, actuator mapping |
| `.sdda` | `sodero.amc`     | Articulated robot: joints and actuator mapping            |

**Names must match.** A simulation gateway finds its robot in the World by name. The **Robot name** of the gateway node must be exactly the name of the robot's prim in the World, for example `jackal` for `/World/jackal`. With another name, the robot never moves. See [Connect to the World](https://docs.sodero.io/sodero-cloud/v1.0.0/station/world_connection/index.md).

______________________________________________________________________

## Glossary

| Term                  | Meaning                                                                                                           |
| --------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Workspace             | A team's space in the portal: people, projects, plan and credits                                                  |
| Project               | Robot Systems and Robot Worlds that belong together, and who can open them                                        |
| Robot System          | A project file that is one Stellar Station                                                                        |
| Stellar Station       | The application that runs a robot system as a graph of nodes. Stellar X runs it too, in the device's own release. |
| Robot World           | A project file with a simulated place and the robots in it                                                        |
| Studio                | The World editor                                                                                                  |
| Theater               | The live view of an active World                                                                                  |
| Activate, Deactivate  | Bring a file's environment up, or release it                                                                      |
| Run, Stop             | Start or stop what runs in an active environment                                                                  |
| Auto off              | Deactivates a file that nobody has used for 30 minutes                                                            |
| Credits               | What active files and rendering sessions use, from your workspace's plan                                          |
| RTX Real-time, WebGPU | The rendering modes: on a cloud GPU, or on your computer's GPU                                                    |
| Node                  | One program in the Station, such as a gateway, a controller or a module of your own                               |
| Port                  | A connection point of a node: REQUIRES (needs) or PROVIDES (offers)                                               |
| Gateway               | A node that connects controllers to actuators or sensors, simulated or real                                       |
| Controller            | A node that controls a robot unit, such as a mobile base or a manipulator                                         |
| Design document       | The configuration of a gateway or a robot controller: `.gw`, `.sdd`, `.sddm`, `.sdda`                             |
| App                   | A package from the Store that a node runs                                                                         |
| Robot name            | The name of a robot's prim in the World, set on the simulation gateway node that drives it                        |
| `.sdr`                | A Sodero file that holds one Robot System or one Robot World                                                      |
| Sodero Assets         | Robots, environments and documents published by Sodero                                                            |
