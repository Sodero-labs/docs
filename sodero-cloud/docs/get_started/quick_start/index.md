# Quick Start

Create a warehouse World, watch its simulation in Theater, then stop and deactivate it. This first exercise walks through the whole life of a World; driving its robots from a Station comes next ([Next: Connect a Robot System](#next-connect-a-robot-system)).

## Before You Start

- Sign in to [Sodero Cloud](https://app.sodero.io) with access to create a project and edit its files.
- Check the workspace's credits and active-file allowance in **Billing & Usage**.
- Download [jackal_warehouse.zip](files/jackal_warehouse.zip), the example scene with a Jackal and a Dingo. Keep the ZIP intact. It includes the accompanying Clearpath license notice.

**Credits:** an active World uses credits until you deactivate it. Studio and Theater sessions in **RTX Real-time** use credits too. Check your plan's rates before opening them ([Credits and Usage](../../account/billing/index.md)).

## Step 1: Create the Project and World { #step-1-create-the-project-and-world }

1. In **Projects**, click **+ Project**.
2. Enter `Warehouse Demo`, keep **Restricted**, and click **Create**.
3. In the project, click **New file**, choose **Robot World**, and click **Next**.
4. Enter `warehouse` as the **File Name**, then click **Create**.

<figure markdown="span">
  ![Create new file](images/new_world.png){ width="480" }
  <figcaption>Naming the new Robot World</figcaption>
</figure>

The World appears as **Inactive**. Its **Studio** link opens the editor.

## Step 2: Import and Save the Scene { #step-2-import-and-save-the-scene }

1. Click **Studio** on the World row. Choose **RTX Real-time** or **WebGPU**, then click **Open Cosmic Studio**.
2. Open the logo menu and choose **World › Replace scene…**.
3. On **This PC**, select `jackal_warehouse.zip`, click **Replace**, and confirm replacement.

    <figure markdown="span">
      ![Replace scene](images/replace_scene.png){ width="520" }
      <figcaption>The Replace scene dialog</figcaption>
    </figure>

4. Check that **Hierarchy** contains the warehouse and robots. If the old default scene remains after the replacement confirmation, reload Studio.
5. Click **Save now** and wait for *Saved just now*.

<figure markdown="span">
  ![Warehouse in Studio](images/studio_warehouse.png){ width="900" }
  <figcaption>The example scene in Studio. It contains a Jackal and a Dingo.</figcaption>
</figure>

Choose **Back to Sodero Cloud** from the logo menu to close Studio. Keep the portal tab open while using the editor.

## Step 3: Activate the World { #step-3-activate-the-world }

On the project page, set the World's **Activation** to **Active**. Wait until **Activating** changes to **Active**. Activation prepares the environment; it does not start the simulation.

## Step 4: View and Run the Simulation { #step-4-view-and-run-the-simulation }

1. Click **Theater**, choose a rendering mode, and click **Open Cosmic Theater**.
2. Wait for *Ready*. If the view fails to load, use **Retry**; repeated failures should be reported through **Help**.
3. On the project page, set the World's **Running** state to **Running**. Alternatively, the editor who has control in Theater can use **Start Theater**.
4. Select **jackal** in **Scene assets**; double-click the row to bring the camera to it.

Check that the scene loads and the robots remain on the ground. **Physics RTF** near 1.00 means the simulation keeps up with elapsed time; **FPS** describes display updates. These are different measurements. A robot does not start driving simply because the World is running.

## Step 5: Stop and End the Session { #step-5-stop-and-end-the-session }

1. Set the World's **Running** state to **Stopped**. Stopping resets its pose and clock; it is not a pause that preserves progress.
2. Set **Activation** to **Inactive** and wait for deactivation to finish.
3. Close Studio and Theater views you no longer need. In **Billing & Usage › Recent runs**, check for remaining active sessions.

Stopping a World leaves its environment active and using credits. Deactivating a World does not deactivate separate Robot Systems. End each resource that you started.

## Next: Connect a Robot System { #next-connect-a-robot-system }

To drive the robots of this World, add a Robot System to the same project:

1. Create a [Robot System](../../projects/files/index.md) in the project.
2. Install the apps its nodes run from the [Store](../../station/apps/index.md), then [add and connect the nodes](../../station/graph/index.md).
3. Go live, and [upload the gateway and robot documents](../../station/documents/index.md) while the nodes are stopped.
4. Check the [robot name and the actuator mapping](../../station/world_connection/index.md), run the World, and [start the nodes](../../station/run/index.md).
5. Drive the robot from its controller's UI: [Strider](../../operate/strider/index.md), [Motion Studio](../../operate/motion_studio/index.md) or [Articulation](../../operate/articulation/index.md).

Use gateway and robot documents made for this Station release, such as the documents in **Sodero Assets** ([Compatibility](../../reference/compatibility/index.md)).
