# Tutorial: Building a Simple 2-Bar Robot - Virtual Verification

In the previous chapter, we mapped the theoretical robot structure to the actual hardware. Now that the mapping is complete, we will verify the robot's movement through a virtual simulation before deploying it to the real hardware.

> **Prerequisite:** This tutorial assumes that the EtherCAT slaves (servo drivers) are properly configured, connected, and ready for operation.

**Goal:** Verify the `test_robot` configuration via simulation and activate the EtherCAT Master for real-world control.

Virtual Verification Interface

______________________________________________________________________

## Step 1: Virtual Verification

First, we must verify that the appropriate parameters were entered in the previous steps.

1. Click the **Activate Simulation** button.
1. The system will verify the robot parameters. Once verified, the simulation will start automatically.

### Verification Results

If there are no issues with the parameters, the system log will display a success message.

> **Status:** `Activate Simulation Success`

Simulation Success Log

______________________________________________________________________

## Step 2: Jog Control & Monitoring

Once the simulation is active, you can manually control the robot to check its behavior.

1. Locate the **Jog Panel** on the right side of the screen.
1. Click **Servo On** to enable motor control.
1. Use the **Jog Control** buttons to move the robot joints.

Jog Control Panel

### Monitoring Command Values

As you move the robot, you can monitor the target values being sent to the servo drivers in real-time.

Actuator Command Preview

______________________________________________________________________

## Step 3: Real Robot Activation (EtherCAT)

After verifying the motion in the simulator, we will activate the EtherCAT Master to operate the real robot.

1. Click the **Apply** button located at the top right of the screen.

Location of the Apply Button

1. A confirmation dialog will appear.
1. Check the box to confirm that you have verified the target values via simulation.
1. Click **Apply** to proceed.

Safety Confirmation Checkbox

______________________________________________________________________

## Step 4: Final Validation

The system will attempt to initialize the EtherCAT communication.

### Scenario A: Success

If successful, the logs will show the connection details, and a **Go to Motion Studio** button will appear in the top right corner.

EtherCAT Connection Success

### Scenario B: Failure

If the connection fails, the log will display the specific reason (e.g., communication timeout, parameter mismatch).

Error Log Example

> **Troubleshooting:** If you encounter an error, correct the indicated parameters in the previous sections, return to the **Virtual Verification** page, and repeat the process.

______________________________________________________________________

## Setup Complete

Once the connection is successful, click **Go to Motion Studio** to enter the main control interface.

Motion Studio Interface

Congratulations! You have successfully completed the **Real Robot Setup** for your 2-bar robot.

In the next chapter, we will introduce the features and capabilities of [**Motion Studio**](https://docs.sodero.io/v1.0.0/stellarx/tutorials/stellar_motion_studio/about_stellar_motion_studio/index.md).
