# Tutorial: Building a Simple 2-Bar Robot - Robot System Parameters

In this tutorial, we will configure the global parameters for the robot, including arm reach, gravity, and payload settings. Please follow the steps below and input the values as specified for this example project.

---

## 1. Arm Reach Setup
We need to define the total reach of the robot. For this example, the total length from the base to the Tool Center Point (TCP) corresponds to **600 mm**.

* **Input Value**: `600`

<figure markdown="span">
    ![arm_reach](images/arm_reach.png)
    <figcaption>Setting Max Arm Reach</figcaption>
</figure>

---

## 2. Gravity Vector Setup
Set the gravitational acceleration relative to the World Coordinate System. In our setup, gravity acts downwards along the negative Z-axis.

* **Input Values**:
    * X: `0`
    * Y: `0`
    * Z: `-9,810` (unit: mm/s²)

<figure markdown="span">
    ![gravity_vector](images/gravity_vector.png)
    <figcaption>Setting Gravity Vector</figcaption>
</figure>

---

## 3. Max Payload Setup
Set the maximum weight capacity. For this example, we will use a value of **10,000 g**.

* **Input Value**: `10,000`

<figure markdown="span">
    ![max_payload](images/max_payload.png)
    <figcaption>Setting Max Payload</figcaption>
</figure>

> **Note on this Example:**
> Since this specific robot operates on a plane parallel to the ground, gravity creates no load (torque) on the actuators. However, we input this value for completeness.

---

## 4. Max Allowable Inertia
This feature is currently reserved for future use. Set the value to 0.

* **Input Value**: `0`

<figure markdown="span">
    ![max_allowable_inertia](images/max_allowable_inertia.png)
    <figcaption>Setting Max Allowable Inertia</figcaption>
</figure>

---

## 5. Task Space Limits
Configure the kinematic limits for the Task Space (TCP motion). Enter the values exactly as shown in the image below:

<figure markdown="span">
    ![task_space_limits](images/task_space_limits.png)
    <figcaption>Setting Task Space Limits</figcaption>
</figure>

---

## 6. Goal Tolerance
Define the arrival criteria for the TCP. Set the values as shown below:

<figure markdown="span">
    ![goal_tolerance](images/goal_tolerance.png)
    <figcaption>Setting Goal Tolerance</figcaption>
</figure>

---

## Summary
You have successfully configured the global system parameters.
* **Next Step**: Proceed to the **Actuator Mapping** section to connect these settings to physical motors.