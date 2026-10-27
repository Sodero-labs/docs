# Quick Start

Create a warehouse World, view its simulation in Theater, then stop and deactivate it. This first exercise introduces the complete World lifecycle. Robot driving is a separate task that requires a configured Station and an available controller app.

## Before You Start

- Sign in to [Sodero Cloud](https://app.sodero.io) with access to create a project and edit its files.
- Check the workspace's credits and active-file allowance in **Billing & Usage**.
- Download [jackal_warehouse.zip](https://docs.sodero.io/sodero-cloud/v1.0.0/get_started/quick_start/files/jackal_warehouse.zip), the example scene with a Jackal and a Dingo. Keep the ZIP intact. It includes the accompanying Clearpath license notice.

**Credits:** an active World uses credits until you deactivate it. Studio and Theater sessions in **RTX Real-time** use credits too. Check your plan's rates before opening them ([Credits and Usage](https://docs.sodero.io/sodero-cloud/v1.0.0/account/billing/index.md)).

## Step 1: Create the Project and World

1. In **Projects**, click **+ Project**.
1. Enter `Warehouse Demo`, keep **Restricted**, and click **Create**.
1. In the project, click **New file**, choose **Robot World**, and click **Next**.
1. Enter `warehouse` as the **File Name**, then click **Create**.

The World appears as **Inactive**. Its **Studio** link opens the editor.

## Step 2: Import and Save the Scene

1. Click **Studio** on the World row. Choose **RTX Real-time** or **WebGPU**, then click **Open Cosmic Studio**.
1. Open the logo menu and choose **World › Replace scene…**.
1. On **This PC**, select `jackal_warehouse.zip`, click **Replace**, and confirm replacement.
1. Check that **Hierarchy** contains the warehouse and robots. If the old default scene remains after the replacement confirmation, reload Studio.
1. Click **Save now** and wait for *Saved just now*.

The example scene in Studio. It contains a Jackal and a Dingo.

Choose **Back to Sodero Cloud** from the logo menu to close Studio. Keep the portal tab open while using the editor.

## Step 3: Activate the World

On the project page, set the World's **Activation** to **Active**. Wait until **Activating** changes to **Active**. Activation prepares the environment; it does not start the simulation.

## Step 4: View and Run the Simulation

1. Click **Theater**, choose a rendering mode, and click **Open Cosmic Theater**.
1. Wait for *Ready*. If the view fails to load, use **Retry**; repeated failures should be reported through **Help**.
1. On the project page, set the World's **Running** state to **Running**. Alternatively, the editor who has control in Theater can use **Start Theater**.
1. Select **jackal** in **Scene assets**; double-click the row to bring the camera to it.

Check that the scene loads and the robots remain on the ground. **Physics RTF** near 1.00 means the simulation keeps up with elapsed time; **FPS** describes display updates. These are different measurements. A robot does not start driving simply because the World is running.

## Step 5: Stop and End the Session

1. Set the World's **Running** state to **Stopped**. Stopping resets its pose and clock; it is not a pause that preserves progress.
1. Set **Activation** to **Inactive** and wait for deactivation to finish.
1. Close Studio and Theater views you no longer need. In **Billing & Usage › Recent runs**, check for remaining active sessions.

Stopping a World leaves its environment active and using credits. Deactivating a World does not deactivate separate Robot Systems. End each resource that you started.

## Next: Connect a Robot System

Use the following sequence when compatible controller apps and robot documents are available:

1. Create a [Robot System](https://docs.sodero.io/sodero-cloud/v1.0.0/projects/files/index.md) in the same project.
1. Check its [Store apps](https://docs.sodero.io/sodero-cloud/v1.0.0/station/apps/index.md), then [add and connect nodes](https://docs.sodero.io/sodero-cloud/v1.0.0/station/graph/index.md).
1. Go live without starting the nodes. [Upload and confirm the robot documents](https://docs.sodero.io/sodero-cloud/v1.0.0/station/documents/index.md).
1. Confirm the [robot name and actuator mapping](https://docs.sodero.io/sodero-cloud/v1.0.0/station/world_connection/index.md), run the World, and [start the nodes](https://docs.sodero.io/sodero-cloud/v1.0.0/station/run/index.md).
1. If the running controller provides an operator UI, follow [Strider](https://docs.sodero.io/sodero-cloud/v1.0.0/operate/strider/index.md), [Motion Studio](https://docs.sodero.io/sodero-cloud/v1.0.0/operate/motion_studio/index.md), or [Articulation](https://docs.sodero.io/sodero-cloud/v1.0.0/operate/articulation/index.md).

Use documents supplied or exported for the Station version you are using. Check [Compatibility](https://docs.sodero.io/sodero-cloud/v1.0.0/reference/compatibility/index.md) before moving files from Stellar X.
