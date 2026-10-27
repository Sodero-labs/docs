# What Is Sodero Cloud

Sodero Cloud runs the Sodero robot platform in your browser. You build a simulated place for your robots, compose their robot systems in Stellar Station, run both in the cloud and watch them live, with nothing to install.

______________________________________________________________________

## Projects, Worlds and Systems

Everything you build lives in a **project** in the Sodero Cloud portal at `https://app.sodero.io`. A project holds two kinds of file:

- **Robot Worlds**: simulated places with your robots in them, for example a warehouse with a mobile base.
- **Robot Systems**: the robot software. Each Robot System is one **Stellar Station**.

The Robot Systems of a project drive the robots in the project's active Robot World.

### Core Ideas

**Studio builds the World, the cloud simulates it, Theater shows it.** You build a Robot World in **Studio**, the World editor: bring in a scene, add robots and environments from Sodero Assets, arrange them and save. When you activate the World, Sodero Cloud simulates it. **Theater** shows the running World live in your browser, with the robots and the Stations that drive them.

**Each Robot System is a Stellar Station.** It uses a graph of nodes and Stellar Designer document types (`.gw`, `.sdd`, `.sddm`, `.sdda`). These concepts also apply to Stellar X. The available apps, menus and accepted document versions depend on the installed release ([Compatibility](https://docs.sodero.io/sodero-cloud/v1.0.0/reference/compatibility/index.md)).

**The World connects by itself.** The simulation gateways of every active Station in the project connect to the project's active World automatically. There is no Isaac Sim to install and no network to set up: each gateway finds its robot in the World by name.

______________________________________________________________________

## From Design to a Running Robot

```
flowchart TB
    D["Design<br>Stellar Designer documents"] --> W["Build the World<br>Studio"]
    W --> C["Compose<br>Stellar Station"]
    C --> R["Run and watch<br>Theater"]
    C -. ".sdr transfer:<br>check compatibility" .-> X["Stellar X<br>real hardware"]
```

**Design.** Describe each robot and its gateway in Stellar Designer documents: kinematics, wheels, limits and actuator mapping. Sodero also publishes ready-made documents in **Sodero Assets**.

**Build the World.** In [Studio](https://docs.sodero.io/sodero-cloud/v1.0.0/worlds/studio/index.md), bring in a scene or Sodero Assets, arrange them and save. The World must follow a few rules so that Stations can drive its robots ([Prepare a World for Simulation](https://docs.sodero.io/sodero-cloud/v1.0.0/worlds/prepare_world/index.md)).

**Compose.** In the [Station](https://docs.sodero.io/sodero-cloud/v1.0.0/station/overview/index.md), add gateways and controllers as nodes, connect their ports and load their documents.

**Run and watch.** On the project page, activate the World and its Robot Systems and run them ([Activate and Run](https://docs.sodero.io/sodero-cloud/v1.0.0/projects/activate_run/index.md)). Watch the World in [Theater](https://docs.sodero.io/sodero-cloud/v1.0.0/worlds/theater/index.md) and operate the robots from the controller UIs ([Strider](https://docs.sodero.io/sodero-cloud/v1.0.0/operate/strider/index.md)).

______________________________________________________________________

## Sodero Cloud and Stellar X

**Stellar X** is Sodero's motion controller for real robots. It runs the same Stellar Station on the robot, with EtherCAT for real drives ([Stellar X manual](https://docs.sodero.io/stellar-x/latest/)).

|                            | Sodero Cloud                                       | Stellar X                                                               |
| -------------------------- | -------------------------------------------------- | ----------------------------------------------------------------------- |
| Where the Station runs     | In the cloud, one per Robot System                 | On the Stellar X controller                                             |
| What it drives             | Robots simulated in the project's Robot World      | Real drives through EtherCAT, or a robot in NVIDIA Isaac Sim on your PC |
| Simulation                 | Built in: Studio, the cloud simulation and Theater | Isaac Sim with the Isaac Bridge extension, on your PC                   |
| Save a Station to a file   | **Download local copy** (`.sdr`)                   | **Export SDR**                                                          |
| Load a Station from a file | **Import file** (`.sdr`)                           | **Load SDR**                                                            |

**Move a Robot System with an `.sdr` file.** Export or download the system, then import it at the destination only after checking its Station release, document formats and required apps. Installed packages are not included. See [Compatibility](https://docs.sodero.io/sodero-cloud/v1.0.0/reference/compatibility/index.md) and [Move Robot Systems](https://docs.sodero.io/sodero-cloud/v1.0.0/projects/files/#move-robot-systems-between-stellar-x-and-sodero-cloud).

**Adapt the design for real hardware.** Controllers send commands through a gateway. Reusing a controller design on Stellar X requires a compatible release, a hardware gateway, and checks of actuator mapping, calibration, limits and sensors. Follow the device manual before enabling motion.

**Tip:** Build and test the robot system in Sodero Cloud first. When it behaves as it should in the World, take it to the real robot on Stellar X.

______________________________________________________________________

## What You Need

| You need         | Details                                                                                                                                                                                                                                             |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A browser        | Everything runs in the browser: the portal, Studio, the Station, the controller UIs and Theater.                                                                                                                                                    |
| A Sodero account | Sign in at `https://app.sodero.io` ([Sign In and Account](https://docs.sodero.io/sodero-cloud/v1.0.0/account/sign_in/index.md)).                                                                                                                    |
| Credits          | Active Robot Systems and Robot Worlds use your workspace's credits ([Credits and Usage](https://docs.sodero.io/sodero-cloud/v1.0.0/account/billing/index.md)).                                                                                      |
| Rendering        | **WebGPU** needs support from your browser, operating system and GPU. **RTX Real-time** renders in the cloud and streams the view to your device. See [Compatibility](https://docs.sodero.io/sodero-cloud/v1.0.0/reference/compatibility/index.md). |

Continue with [Key Concepts](https://docs.sodero.io/sodero-cloud/v1.0.0/get_started/key_concepts/index.md), then try the [Quick Start](https://docs.sodero.io/sodero-cloud/v1.0.0/get_started/quick_start/index.md).
