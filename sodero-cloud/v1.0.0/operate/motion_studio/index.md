# Motion Studio

**Motion Studio** is the operator UI for manipulators. The manipulator controller node, `sodero.mmc.<name>`, runs the arm's real-time controller: kinematics, dynamics, trajectory generation and safety limits, from the arm's `.sdd` document. Motion Studio belongs to that node. It shows the arm in 3D, jogs it, defines tools and teaches poses.

______________________________________________________________________

## 1. Set Up the Nodes

1. In the Station's **Store**, install `sodero.actuator_gateway` and `sodero.mmc` ([Apps and Packages](https://docs.sodero.io/sodero-cloud/v1.0.0/station/apps/index.md)).
1. Add the gateway and the manipulator controller, and connect the controller's `servo_link` to the gateway ([Build the Graph](https://docs.sodero.io/sodero-cloud/v1.0.0/station/graph/index.md)).
1. Upload the gateway's `.gw` and the controller's `.sdd` document ([Documents and Settings](https://docs.sodero.io/sodero-cloud/v1.0.0/station/documents/index.md)).
1. Set the gateway's **Robot name** and check the actuator mapping ([Connect to the World](https://docs.sodero.io/sodero-cloud/v1.0.0/station/world_connection/index.md)).
1. Run the World, go live, then start the gateway and the controller, in this order ([Start and Monitor Nodes](https://docs.sodero.io/sodero-cloud/v1.0.0/station/run/index.md)).

______________________________________________________________________

## 2. Open Motion Studio

On the Live page, right-click the running `sodero.mmc.<name>` node and choose **Open …** ([Start and Monitor Nodes](https://docs.sodero.io/sodero-cloud/v1.0.0/station/run/#3-start-restart-or-stop-one-node)). Motion Studio opens in a new tab. If its session expires, open it again from the node.

______________________________________________________________________

## 3. Screen Layout

| Item                   | Description                                                                                  |
| ---------------------- | -------------------------------------------------------------------------------------------- |
| Pages                  | **Home**, **Tool** and **Pose**                                                              |
| 3D view                | The arm in its current pose, with the 3D model of its `.sdd`                                 |
| **Joint Status**       | Per joint: position, target position, velocity, target velocity, effort and residual effort  |
| **TCP Status**         | Position and orientation of the tool center point (TCP), and its linear and angular velocity |
| **Active Tool Status** | The active tool's TCP offset, center of mass and payload mass                                |
| **Filters**            | Shows or hides the cards of the Home page                                                    |

### Header

| Item                  | Description                                                                                                                                                                                       |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Robot and role        | The controller node, and whether this window has control (*Pilot - Control Active*)                                                                                                               |
| **Manual** / **Auto** | **Manual** limits the linear speed of the TCP in the controller's own motions and jogs, 0.25 m/s by default; it does not limit rotations or **Hand** mode. **Auto** runs at the programmed speed. |
| Feed rate             | Speed override in percent (10–150 %), applied to motion in progress                                                                                                                               |
| **Error Reset**       | Clears a protective stop (a joint at its limit, a speed or torque limit, a detected collision) and resets drive faults. Switch the servo on again afterwards.                                     |
| Units                 | `mm / g / deg` or `m / kg / radian`                                                                                                                                                               |
| **Jog**               | Opens the jog panel                                                                                                                                                                               |
| **Command log**       | Commands sent from this window                                                                                                                                                                    |
| **Alarm**             | Active alarms and notifications                                                                                                                                                                   |

The mark at the top left opens the menu, with **File** to import and export tools and poses.

______________________________________________________________________

## 4. Jog the Arm

Click **Jog** in the header to open the jog panel.

1. Switch **Servo On**.
1. In **JOG OPTION**, choose the **Mode**:
   - **Joint**: move one joint at a time (J1…Jn).
   - **Base**: move the tool in the robot's base frame (X, Y, Z, RX, RY, RZ).
   - **Tool**: move the tool in its own frame.
   - **Hand**: hand guiding, for a real arm. The arm compensates gravity and the jog buttons are disabled.
1. Choose **Continuous** (moves while you hold a button) or **Step** (5° or 10 mm per click), and the **Speed**: 50 %, 100 % or 150 %, about 0.04, 0.1 and 0.2 m/s at the tool.
1. Hold **−** or **+** next to a joint or axis in **JOG CONTROL**. The motion stops when you release the button.

The **POSE** section of the panel shows the current TCP pose and joint positions.

**Stop the motion before you leave the UI.** A continuous jog stops when the release of the button reaches the controller. If the browser or the connection fails while you jog, do not assume that the arm has stopped: stop the controller node in the Station and check in Theater that the arm stands still. For a real arm, see [Stop Controls](https://docs.sodero.io/stellar-x/latest/hardware_setup/stop_controls/) in the Stellar X manual.

______________________________________________________________________

## 5. Tools

The **Tool** page defines the tools mounted on the flange.

1. Click **+** to add a tool, and rename it with the pencil icon, for example `gripper`.
1. Enter the **TOOL CENTER POINT**: the TCP position and orientation relative to the flange. The calculator icon opens **TCP Calibration**, which computes the TCP from 3–10 poses that touch the same point.
1. Enter the **PAYLOAD PROPERTIES**: center of mass, inertia and mass. The calculator icon opens **Payload Calibration**.
1. Click **Save**, or **Save and Apply** to make it the active tool at once. **Set as active tool** activates a saved tool.

A wrong payload makes hand guiding and collision detection unreliable. Set the mass and center of mass of every tool you mount.

______________________________________________________________________

## 6. Poses

The **Pose** page stores named poses.

1. Jog the arm to the pose, then click the camera icon (**Save Current Pose**). Or click **+** (**Add pose**) and fill in the values.
1. Select the pose in the list. **POSE DATA** shows its TCP pose and joint positions; **Set from current** copies the current pose into it.
1. Under **TEST MOVE**, choose **Joint** or **Linear** motion and hold **Hold to move**. The arm moves to the pose only while you hold the button.
1. Click **Save**.

Saved poses appear as markers in the 3D view. Right-click a pose to copy, duplicate or delete it. **File** in the menu exports and imports tools and poses.

______________________________________________________________________

## 7. Program the Arm

Motion Studio is for setup and teaching. Programs run outside it and use the same controller:

| From            | How                                                                                                                                                                |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AI agents       | The `station.motion` tools: state, servo, moves, stops and fault reset ([AI Agents](https://docs.sodero.io/sodero-cloud/v1.0.0/connect/ai_agents/index.md))        |
| Your own module | A module node on the Station, connected to the manipulator controller node ([Apps and Packages](https://docs.sodero.io/sodero-cloud/v1.0.0/station/apps/index.md)) |
| Your own tools  | The Station API, through the [Project VPN](https://docs.sodero.io/sodero-cloud/v1.0.0/connect/project_vpn/index.md)                                                |

**From simulation to a real arm.** The arm's `.sdd` document, its tools and poses, and your programs carry over to a real arm on Stellar X, which uses an EtherCAT gateway instead of the simulation gateway. A real arm needs its own checks first: see [Motion Studio](https://docs.sodero.io/stellar-x/latest/controllers/motion_studio/) in the Stellar X manual.
