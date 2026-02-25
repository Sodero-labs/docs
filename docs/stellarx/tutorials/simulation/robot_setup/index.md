# Prepare Robot Model

## Using Provided Robot Models

Isaac Sim provides various robot models from popular manufacturers like Universal Robots, Unitree, Franka Robotics etc. by default.  

You can access these models by clicking `Window` -> `Browsers` -> `Isaac Sim Assets`.

![isaac sim asset](images/isaacsim_models_01.png)
![isaac sim asset](images/isaacsim_models_02.png){ width="1000" }

There should be a new tab appeared next to the `Content` tab. You may have to wait for a while for Isaac Sim to load all the assets. There are plenty of robot models here. But if you need your own robot to be implemented, please follow below general setup guide.

## Building Robot model

### Prerequisites

You can make any robot with all the shapes and sizes you'd like, but there are some rules that need to be addressed.

- The name of your robot prim must match the name from StellarX.
- Robot must contain only one [articulation root](https://docs.isaacsim.omniverse.nvidia.com/5.0.0/robot_setup_tutorials/tutorial_gui_simple_robot.html#add-articulation).
- All the links in the robot must be rigid-bodies. Collision or weight settings is not mandatory, but is recommanded for accurate physics simulation.
- Closed-loop articulation is not supported. You can [exclude](https://docs.isaacsim.omniverse.nvidia.com/5.0.0/robot_setup_tutorials/rig_closed_loop_structures.html) some joints from articulation, but this may result in inaccurate simulation result.

Most of the time, you'll be using [urdf](https://wiki.ros.org/urdf) format. If you wish to use urdf, please refer to [this guide](https://docs.isaacsim.omniverse.nvidia.com/5.0.0/importer_exporter/import_urdf.html). In this tutorial, we'll be rigging the robot ourselves. Before starting, please download the result robot model from [**3D Model Creation**](../../stellar_designer/3dmodel_creation/index.md) guide.

 - [**3D Model download link**](models/example_manipulator_assembly_vis.glb)

### Making Robot Model

<figure markdown="span">
    ![models](images/isaacsim_assembly_01.png)
</figure>
- Open up new file. From main screen, Click `File` -> `Import`.

<figure markdown="span">
    ![models](images/isaacsim_assembly_02.png){ width="1000" }
    ![models](images/isaacsim_assembly_03.png){ width="1000" }
</figure>
- Go to downloaded file's directory. Select the file and enable `Use Meter as World Unit`. Click box next to `Up-axis` and select `Z-up` and import. The result should look like bottom picture.

<figure markdown="span">
    ![models](images/isaacsim_assembly_04.png)
    ![models](images/isaacsim_assembly_05.png){ width="1000" }
    ![models](images/isaacsim_assembly_07.png){ width="1000" }
</figure>
- If you take a look at the file's directory, you'll see a new `.usd` format file with the same name. Click `File` -> `Open` and open the `.usd` file.
You'll be then able to see the full robot model.

<figure markdown="span">
    ![models](images/isaacsim_assembly_08.png)
    ![models](images/isaacsim_assembly_09.png)
</figure>
- Open up all the joint prims and you'll see the full stage tree. Right-click on the empty part of the stage and click `Create` -> `Scope`. This will create scope for organizing the stage. Create two scopes and name them `links` and `joints`. 

<figure markdown="span">
    ![models](images/isaacsim_assembly_10.png)
    ![models](images/isaacsim_assembly_11.png)
</figure>
- Drag all the links to `links` scope and delete joint prims.

<figure markdown="span">
    ![models](images/isaacsim_assembly_12.png)
    ![models](images/isaacsim_assembly_13.png)
</figure>
- Select all the links and right-click. Click `Add` -> `Physics` -> `Rigid Body` to make them rigid-bodies. You can verify it by scrolling down on the property tab.

<figure markdown="span">
    ![models](images/isaacsim_assembly_14.png)
    ![models](images/isaacsim_assembly_15.png)
</figure>
- Next, open the link prim and select mesh prim. Right-click and click `Add` -> `Physics` -> `Collider`. This will add collider to mesh and you can also verify it by scrolling down. Default collider type is `trimesh`, but since the parent prim is rigid-body, it is automatically set to `Convex Hull`. Repeat this for all the other link meshes.

<figure markdown="span">
    ![models](images/isaacsim_assembly_16_1.png)
    ![models](images/isaacsim_assembly_16_2.png)
</figure>
- Now, we need to add joints. First, select `link0` and right-click. Click `Create` -> `Physics` -> `Joint` -> `Fixed Joint`. This will create `FixedJoint` under `link0`. This joint is like an anchor that fixes base link of the robot to the world. You can see this by looking at the Body settings of `FixedJoint`. Empty Body 0 means it is fixed to world. You can explicitly set this To `/World` prim.

<figure markdown="span">
    ![models](images/isaacsim_assembly_17.png)
    ![models](images/isaacsim_assembly_18.png)
</figure>
- Next, we will add revolute joint. Select `link0` and then ctrl-click `link1`. Order matters in this part. Selecting `link1` then `link0` will result in `link0` trying to revolute relative to `link1` and not vice versa. Right-click on `link1` and click `Create` -> `Physics` -> `Joint` -> `Revolute Joint`. This will create revolute joint under `link1`.

<figure markdown="span">
    ![models](images/isaacsim_assembly_19.png)
    ![models](images/isaacsim_assembly_20.png)
</figure>
- Rename joint to `J1` for consistency. Right-click on `J1` and select `Add` -> `Physics` -> `Angular Drive`. We can only control joints with drive property, and joints without them can only move passively.

<figure markdown="span">
    ![models](images/isaacsim_assembly_21.png)
    ![models](images/isaacsim_assembly_22.png)
</figure>
- Repeat the same process for the other joints. And move them to `joints` scope.

<figure markdown="span">
    ![models](images/isaacsim_assembly_23.png)
    ![models](images/isaacsim_assembly_24.png)
</figure>
- Select all the active joints and scroll down to `Drive` property. Set `Stiffness` and `Damping` to `100000.0` and `10000.0`, resplectively. This is only to set the joints fixed when not using Stellar X. You can choose arbitrary values, only if `Stiffness` is higher than `Damping`.

<figure markdown="span">
    ![models](images/isaacsim_assembly_25.png)
</figure>
- Select `J1` and scroll down to `Revolute Joint` section. Click `Axis` and selelct Z. Repeat same process for `J4` and `J6`.

<figure markdown="span">
    ![models](images/isaacsim_assembly_26.png)
</figure>
- Finally, select FixedJoint and right-click. Select `Add` -> `Physics` -> `Articulation Root`. `Articulation Root` is what defines robot in Isaac Sim. For more information, check out [this documentation](https://docs.isaacsim.omniverse.nvidia.com/5.0.0/robot_setup_tutorials/tutorial_gui_simple_robot.html#add-articulation).

<figure markdown="span">
    ![models](images/isaacsim_assembly_27.png)
    ![models](images/isaacsim_assembly_28.png)
</figure>
And that's it! You just made your own robot model. Save and open up new file. Click `Create` -> `Environments` -> `Flat Grid`. Drag the robot model file to `Stage` on the right, and you'll see the robot in the world!

(Insert example gif here)

Change the robot's name to your StellarX's robot name and click `Play` button on the left side. Jog the robot via StellarX and you'll see the robot is moving accordingly. You can also write your own python script to move the robot at your need.

You can download final robot model below.

- [**Download link**](models/example_manipulator_assembly.usd)

## Conclusion

In this tutorial, we set up robot eligible for Isaac Sim environment. Isaac Sim is a powerful tool for robot simulation with numerous features. Check out [official Isaac Sim Documentation](https://docs.isaacsim.omniverse.nvidia.com/5.0.0/index.html) for more information. If you have questions regarding Isaac Sim, please check out [Isaac Sim Forum](https://forums.developer.nvidia.com/c/omniverse/simulation/69).
&nbsp;
