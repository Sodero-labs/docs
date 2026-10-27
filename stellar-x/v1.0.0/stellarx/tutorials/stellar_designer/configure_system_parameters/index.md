# Tutorial: Building a Simple 2-Bar Robot - Robot System Parameters

In this tutorial, we will configure the global parameters for the robot, including arm reach, gravity, and payload settings. Please follow the steps below and input the values as specified for this example project.

______________________________________________________________________

## 1. Arm Reach Setup

We need to define the total reach of the robot. For this example, the total length from the base to the Tool Center Point (TCP) corresponds to **600 mm**.

- **Input Value**:
  - Max Arm Reach: `600` mm

Setting Max Arm Reach

______________________________________________________________________

## 2. Gravity Vector Setup

Set the gravitational acceleration relative to the World Coordinate System. In our setup, gravity acts downwards along the negative Z-axis.

- **Input Value**:
  - X: `0` mm/s²
  - Y: `0` mm/s²
  - Z: `-9,810` mm/s²

Setting Gravity Vector

______________________________________________________________________

## 3. Max Payload Setup

Set the maximum weight capacity. For this example, we will use a value of **10,000 g**.

- **Input Value**:
  - Max Payload: `10,000` g

Setting Max Payload

> **Note on this Example:** Since this specific robot operates on a plane parallel to the ground, gravity creates no load (torque) on the actuators. However, we input this value for completeness.

______________________________________________________________________

## 4. Max Allowable Inertia

This feature is currently reserved for future use. Set the value to 0.

- **Input Value**:
  - Max Allowable Inertia: `0` g/mm²

Setting Max Allowable Inertia

______________________________________________________________________

## 5. Task Space Limits

Configure the kinematic limits for the Task Space (TCP motion). Enter the values exactly as shown in the image below:

- **Input Value**:
  - Max Speed: `1,000` mm/s
  - Max Accel: `5,000` mm/s²
  - Max Jerk: `50,000` mm/s²

Setting Task Space Limits

______________________________________________________________________

## 6. Goal Tolerance

Define the arrival criteria for the TCP. Set the values as shown below:

- **Input Value**:
  - Position Goal Tolerance: `5` mm
  - Orientation Goal Tolerance: `0.5729577951308232` deg

Setting Goal Tolerance

______________________________________________________________________

## Summary

You have successfully configured the global system parameters.

- **Next Step**: Proceed to [Step 3: Actuator Mapping](https://docs.sodero.io/v1.0.0/stellarx/tutorials/stellar_designer/map_actuators/index.md) to connect these settings to physical motors.
