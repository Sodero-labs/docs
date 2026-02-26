# User Guide: Robot System Parameters

This guide provides a detailed explanation of the global system parameters found in the Robot Configuration settings. These settings define the robot's physical properties and safety constraints.

---

## 1. Arm Reach

### Definition
This parameter defines the physical reach of the robot based on its kinematics. It is calculated as the radius from the **base joint's rotation axis** to the **Tool Center Point (TCP)** when the robot is fully extended.

<figure markdown="span">
    ![arm_reach_diagram](images/arm_reach_diagram.png)
    <figcaption>Diagram: Definition of Max Arm Reach</figcaption>
</figure>

### Details
- **Unit**: mm
- **Function**: This value is used to limit the joint speed effectively to prevent the TCP from exceeding safe velocities.

> **⚠️ Caution**

> * This value **must be reasonably accurate**, as it affects motion constraints.
> * However, **perfect precision is not required** — an error margin of **±10%** is acceptable.

---

## 2. Gravity Vector

### Definition
The gravity vector defines the direction and magnitude of gravitational acceleration relative to the **World Coordinate System**.

### Details
- The vector must point **in the direction of gravity** (usually downward in the Z-axis).
- The magnitude should reflect the local gravitational acceleration (approx. 9.81 m/s²).

> **⚠️ Caution**
> Be careful with the **unit**: Ensure consistent use of **mm/s²** (e.g., -9810) or **m/s²** (e.g., -9.81) depending on your global unit settings.

---

## 3. Max Payload

### Definition
Specifies the **maximum payload capacity** of the robot (Unit: g). This value defines the **upper limit for gravity compensation**, regardless of the actual payload data set in the tool configuration.

### How It Works
Even if a tool is configured with a payload that **exceeds** this value (e.g., by mistake or tool change), the system will **limit gravity compensation** to the value specified here to protect the robot.

> **⚠️ Caution**
> Always set this value according to the **robot's mechanical and control limits** to prevent incorrect torque output or safety issues.

---

## 4. Max Allowable Inertia

### Definition
Defines the moment of inertia limits for the robot's wrist joints.

> **ℹ️ Status: Future Feature**
>
> This parameter is **reserved for future use** and is currently **not operational**. Inputting any value will have **no effect** on the actuator's behavior in the current version.

---

## 5. Task Space Limits

### Definition
Defines the kinematic constraints **in task space**, i.e., relative to the robot’s **Tool Center Point (TCP)**. These limits constrain the Cartesian linear motion of the end-effector.

### Parameters

* **Max Speed**: Maximum linear velocity of the TCP when moving toward the target (Unit: mm/s or m/s).
* **Max Accel**: Maximum linear acceleration of the TCP while following the trajectory (Unit: mm/s² or m/s²).
* **Max Jerk**: Maximum linear jerk (rate of change of acceleration) of the TCP (Unit: mm/s³ or m/s³).

> **⚠️ Caution**
> These values should be defined based on:

> * The **mechanical and structural limits** of the robot.
> * The desired **task performance and safety**.
> * Excessively high values can lead to unstable or unsafe robot behavior.

---

## 6. Goal Tolerance

### Definition
This parameter defines the **arrival criteria** for the Tool Center Point (TCP).

### Usage
* When executing task-space commands (like `move_linear`), the robot is considered to have reached the target when the TCP position error is within this tolerance value.
* **Unit**: mm