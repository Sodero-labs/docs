# Theater

Theater shows an active Robot World live in your browser: the simulation as it runs, the robots in it and the Stations that drive them. Its browser tab is titled *Cosmic Theater*.

______________________________________________________________________

## 1. Open Theater

1. Activate the World on the project page ([Activate and Run](https://docs.sodero.io/sodero-cloud/v1.0.0/projects/activate_run/index.md)).
1. Click **Theater** in the World's **Actions** column. The link is available once the World is **Active** and its live view is ready.
1. In **Choose rendering mode**, pick **RTX Real-time** or **WebGPU** and click **Open Cosmic Theater** ([Choose Rendering Mode](https://docs.sodero.io/sodero-cloud/v1.0.0/projects/activate_run/#choose-rendering-mode)). Theater opens in a new tab.
1. From Studio, **Enter Theater** activates the World if needed and opens it here ([Studio](https://docs.sodero.io/sodero-cloud/v1.0.0/worlds/studio/#7-enter-theater)).
1. While the World loads, Theater shows the progress, including **Robot cameras** when the World has cameras. The first time a scene opens in **RTX Real-time**, the renderer prepares it, which can take several minutes.
1. Opening Theater does not play the World: **Run** on the project page or **Start Theater** plays it ([Start and Stop](#start-and-stop)).
1. Watching counts as use of the World: an active World that nobody watches in Theater is deactivated by Auto off after 30 minutes.

______________________________________________________________________

## 2. The Theater Window

| Area             | What it holds                                                                                                                                                                                                                                                                      |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Header**       | The project and World names; the status, *Ready* once the World is shown; the renderer menu (**RTX Real-Time** ▾ or **WebGPU** ▾); a timer; **Start Theater** or **Stop Theater**; **Resources** ▾; **Share** (link icon); the **Active users** who are watching                   |
| **Scene assets** | The top levels of the World, with **Search assets** and the number of assets. **Hide panel** folds it away.                                                                                                                                                                        |
| **Viewport**     | The running World. **Perspective** ▾ holds camera presets (Perspective, Top, Bottom, Front, Back, Left, Right). **View** ▾ holds **Grid**, **Quality** (resolution and frame rate), **Fit** and **Presentation mode**, which shows the viewport full screen until you press `Esc`. |
| **Readout**      | At the bottom of the viewport, for example *1920x1080 · 60 FPS · Physics RTF 1.00*                                                                                                                                                                                                 |
| **Runtime**      | The Station that drives the selected robot ([Select a Robot](#4-select-a-robot))                                                                                                                                                                                                   |

**Physics RTF** is the real-time factor of the simulation: simulated time divided by wall-clock time, measured over about five seconds. At 1.00 the simulation keeps up with real time; *—* means there is no fresh measurement. **FPS** is the rate at which the picture is drawn.

The renderer menu switches your view to the other rendering mode. The current picture stays until the new one is ready. The choice applies to your view only; the simulation is the same for everyone.

### Start and Stop

**Start Theater** plays the World's simulation and **Stop Theater** stops it. One viewer controls them: the first person with edit access who opened Theater. For the others, the button is dimmed and they watch. Members with **Can view** always watch. While the World is not playing, viewers who watch see the status *Ready · Paused*.

Theater plays and stops only the simulation; it does not start or stop any Station. **Run** and **Stop** on the project page act on the files you select there, the World and its Stations alike ([Activate and Run](https://docs.sodero.io/sodero-cloud/v1.0.0/projects/activate_run/#2-run-and-stop)).

______________________________________________________________________

## 3. Move the Camera

The camera moves as in Studio: right-drag to look around, the wheel to move closer or farther, middle-drag to pan and `Alt` + left-drag to orbit ([Keys and Camera](https://docs.sodero.io/sodero-cloud/v1.0.0/worlds/studio/#6-keys-and-camera)). Each viewer has their own camera.

| Key       | Action                                                                             |
| --------- | ---------------------------------------------------------------------------------- |
| `F`       | Frame the selection, or the whole World when nothing is selected                   |
| `Shift+F` | Follow the selection. A *Tracking* chip appears; **Stop** on it ends the tracking. |
| `Esc`     | Stop following; leave presentation mode                                            |

Right-click a row in **Scene assets** for **Focus** and **Focus and Track**.

______________________________________________________________________

## 4. Select a Robot

1. Click a robot in the viewport, or its row in **Scene assets**. Double-click the row to bring the camera to the robot.
1. In **RTX Real-time**, a card appears above the robot with its name and **Open Station**, followed by the Robot System that drives it. In both modes, right-clicking the robot's row in **Scene assets** offers **Open Station** as well.
1. **Open Station** opens that Robot System's live Station in a new tab. Members with **Can view** get a page they can only look at.

The **Runtime** dock opens on the right by itself when you select a robot that a Station drives. It shows that Station's graph, read-only, with the state of each node, so you can see at a glance whether the gateway and the controller are running.

- **Widen Runtime** makes the dock wider, and **Hide Runtime** closes it. **Show Runtime** in a row's right-click menu opens it again.
- The zoom buttons and **Fit view** at the bottom arrange the graph.
- When no Station drives the robot, the card or the menu says so, for example *No Station is running in this project.*

______________________________________________________________________

## 5. Several Viewers

- Everyone who opens an active World watches the same simulation. **Active users** in the header shows who is watching.
- Each person chooses their own rendering mode and moves their own camera.
- Each viewer in **RTX Real-time** has a cloud renderer of their own, which uses credits; a viewer in **WebGPU** draws with their own computer's GPU ([Credits and Usage](https://docs.sodero.io/sodero-cloud/v1.0.0/account/billing/index.md)).
- **Share** shows the link to this Theater, and **Copy** copies it. The link opens for people who are signed in and have access to the project ([Share and Collaborate](https://docs.sodero.io/sodero-cloud/v1.0.0/projects/sharing/index.md)).

______________________________________________________________________

## 6. What Theater Does Not Do

- It does not edit the World. Deactivate the World and open it in [Studio](https://docs.sodero.io/sodero-cloud/v1.0.0/worlds/studio/index.md).
- It does not start or stop Stations; use **Run** and **Stop** on the project page, or the Station itself.
- It has no recording or screenshot button. To capture the view, use your operating system's screenshot or screen-recording tools.

______________________________________________________________________

## 7. Troubleshooting

| Message                                                          | What to do                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| *Unable to load World*, with a reason                            | Click **Retry**.                                                                                                                                                                                                                                 |
| *No saved World yet*                                             | The World has no scene. Deactivate it, build the scene in Studio and save it.                                                                                                                                                                    |
| *Preparing the RTX renderer*                                     | The first time a scene opens in **RTX Real-time**, the renderer prepares it. Wait; this can take several minutes.                                                                                                                                |
| *RTX needs free GPU resources. …*                                | The cloud GPUs are busy. Wait, or close Theater and open it again in **WebGPU**.                                                                                                                                                                 |
| *The World did not finish loading in 3 minutes. …*               | The World is very large, or the renderer cannot open it. Click **Retry**; if it fails again, make the World lighter ([Prepare a World for Simulation](https://docs.sodero.io/sodero-cloud/v1.0.0/worlds/prepare_world/#6-keep-the-world-light)). |
| *Physics connection failed, retrying*                            | Wait: Theater retries by itself.                                                                                                                                                                                                                 |
| *Your sign-in expired. Open this World again from Sodero Cloud.* | Open Theater again from the project page.                                                                                                                                                                                                        |
| *No Station is running in this project.*                         | No Robot System of the project is active. Activate the one that drives the robot.                                                                                                                                                                |
| **Start Theater** is dimmed                                      | Another viewer controls the simulation, or your role is **Can view**.                                                                                                                                                                            |
| *View access: you can look but not change this project.*         | Your role is **Can view**. Ask a manager for **Can edit**.                                                                                                                                                                                       |
