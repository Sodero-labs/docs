# Stellar X API Documentation

## Index

- **[API](#api)**
  - **[A. Initialization and Default State](#a-initialization-and-default-state)**
    - [is_ready](#is_ready)
    - [get_status](#get_status)
    - [get_operating_status](#get_operating_status)
    - [get_error_status](#get_error_status)
    - [get_alarm](#get_alarm)
    - [reset_trigger](#reset_trigger)
  - **[B. Operational Mode](#b-operational-mode)**
    - [get_operational_mode](#get_operational_mode)
    - [set_operational_mode](#set_operational_mode)
    - [set_direct_teaching_on_off](#set_direct_teaching_on_off)
  - **[C. Collision Detection](#c-collision-detection)**
    - [set_collision_detection_sensitivity](#set_collision_detection_sensitivity)
    - [set_post_collision_mode](#set_post_collision_mode)
    - [get_collision_joint_status](#get_collision_joint_status)
    - [reset_collision_state](#reset_collision_state)
  - **[D. Movement and Control](#d-movement-and-control)**
    - [set_servo_on_off](#set_servo_on_off)
    - [stop](#stop)
    - [pause](#pause)
    - [resume](#resume)
    - [move_jog](#move_jog)
    - [move_home](#move_home)
    - [move_joint](#move_joint)
    - [move_linear](#move_linear)
    - [move_circle](#move_circle)
    - [check_finish](#check_finish)
    - [set_feed_rate](#set_feed_rate)
    - [get_feed_rate](#get_feed_rate)
  - **[E. Program Execution](#e-program-execution)**
    - [execute_internal_program](#execute_internal_program)
    - [stop_executing_internal_program](#stop_executing_internal_program)
  - **[F. Joint and Pose Status](#f-joint-and-pose-status)**
    - [get_trajectory_status](#get_trajectory_status)
    - [get_actual_joint_velocity_utilization](#get_actual_joint_velocity_utilization)
    - [get_actual_joint_position](#get_actual_joint_position)
    - [get_actual_joint_velocity](#get_actual_joint_velocity)
    - [get_actual_joint_effort](#get_actual_joint_effort)
    - [get_residual_effort](#get_residual_effort)
    - [get_actual_pose](#get_actual_pose)
    - [get_actual_twist](#get_actual_twist)
    - [get_actual_wrench](#get_actual_wrench)
    - [get_actual_tcp_wrench](#get_actual_tcp_wrench)
    - [get_target_joint_position](#get_target_joint_position)
    - [get_target_joint_velocity](#get_target_joint_velocity)
    - [get_target_joint_effort](#get_target_joint_effort)
    - [get_target_pose](#get_target_pose)
    - [get_target_twist](#get_target_twist)
    - [get_target_wrench](#get_target_wrench)
    - [get_joint_temperature](#get_joint_temperature)
    - [get_default_joint_limit](#get_default_joint_limit)
    - [get_user_joint_limit](#get_user_joint_limit)
    - [get_current_joint_limit](#get_current_joint_limit)
    - [set_user_joint_limit](#set_user_joint_limit)
    - [set_user_joint_limit_on_off_state](#set_user_joint_limit_on_off_state)
    - [get_current_user_joint_limit_on_off_state](#get_current_user_joint_limit_on_off_state)
  - **[G. Configuration Changes (TCP, Payload)](#g-configuration-changes-tcp-payload)**
    - [get_tcp](#get_tcp)
    - [get_payload](#get_payload)
    - [set_tcp](#set_tcp)
    - [set_payload](#set_payload)
    - [set_tcp_with_bank](#set_tcp_with_bank)
    - [set_payload_with_bank](#set_payload_with_bank)
  - **[H. Bank Data Management](#h-bank-data-management)**
    - [get_tcp_bank_data](#get_tcp_bank_data)
    - [add_tcp_bank_data](#add_tcp_bank_data)
    - [update_tcp_bank_data](#update_tcp_bank_data)
    - [remove_tcp_bank_data](#remove_tcp_bank_data)
    - [get_payload_bank_data](#get_payload_bank_data)
    - [add_payload_bank_data](#add_payload_bank_data)
    - [update_payload_bank_data](#update_payload_bank_data)
    - [remove_payload_bank_data](#remove_payload_bank_data)
    - [get_pose_bank_data](#get_pose_bank_data)
    - [add_pose_bank_data](#add_pose_bank_data)
    - [update_pose_bank_data](#update_pose_bank_data)
    - [remove_pose_bank_data](#remove_pose_bank_data)
  - **[I. Kinematics Computation](#i-kinematics-computation)**
    - [solve_forward_kinematics](#solve_forward_kinematics)
    - [solve_inverse_kinematics](#solve_inverse_kinematics)
  - **[J. TCP and Payload Measurement](#j-tcp-and-payload-measurement)**
    - [calculate_tcp](#calculate_tcp)
    - [measure_payload_start](#measure_payload_start)
    - [append_pose_wrench_sample](#append_pose_wrench_sample)
    - [remove_pose_wrench_sample](#remove_pose_wrench_sample)
    - [get_pose_wrench_sample_list](#get_pose_wrench_sample_list)
    - [calculate_payload](#calculate_payload)

---

## API

From this point onward, the main functions of the Stellar X API are categorized and explained by functionality.

### General Notes

- **Rotation Representation:**  
  Stellar X API uses the **Rotation Vector convention** as its orientation convention.

- **Function Argument Passing:**  
  Stellar X API **does not support positional arguments**, so argument names (**keyword arguments**) must be explicitly specified when providing inputs.

- **Function Return Values:**
  All functions invoked via the remote library include, as the first element of their return value, a bool indicating the communication status with Stellar X. For example, the `is_ready` function, which originally returns a bool, will return a value structured as `[True, <return value of is_ready>]` when called through Stellar X. Here, the first element, `True`, indicates that communication with Stellar X was successful. Therefore, please refer to the **second element** (index 1) of the return value as the final result of any function.
  If something goes wrong and the function returns `False`, the second element of the return value is error code in `str` type.

- **Units:**  
  - **Pose:** Position is expressed in meters (m), and rotation in radians (rad)  
  - **Joint Vector:** radians (rad)  
  - **Force/Torque:** Force is expressed in newtons (N), and torque in newton-meters (Nm)  
  - **Miscellaneous:** Mass is expressed in kilograms (kg), the center of mass in meters (m), and inertia in kg·m²

---

### A. Initialization and Default State

#### `is_ready`

**Signature:**  
```python
def is_ready(self) -> bool
```

**Usage:**  
```python
robot.is_ready()
```

**Description:**  
Checks whether the robot is currently in an operable state.
Returns `False` if the robot cannot operate due to conditions such as an emergency stop or collision detection, and `True` if it is in a normal state.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type | Description                                  |
|-------------|----------------------------------------------|
| `bool`      | `True` if robot is operational, else `False` |

**Example Output:**
```python
[True, True] # The second element corresponds to the return value of is_ready.
```


---

#### `get_status`

**Signature:**  
```python
def get_status(self) -> Dict
```

**Usage:**  
```python
robot.get_status()
```

**Description:**  
Returns a dictionary containing the robot’s overall status information.
It includes various details such as error status, motion status, and servo status.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type | Description                                                    |
|-------------|----------------------------------------------------------------|
| `dict`      | A dictionary containing the robot’s overall status information |

**Example Output:**
```python
# The second element corresponds to the return value of get_status.
[True,
 {'count_down_time': -2111.9530835214264,
  'error_status': {'alarm': {'alarm_code': '', 'alarm_description': ''},
                   'collision_detected': False,
                   'drive_error': False,
                   'emergency': False,
                   'joint_limit': False,
                   'not_following': False,
                   'processing_overload': False,
                   'safe_guard': False,
                   'self_collision': False,
                   'total_error': False},
  'internal_io_status': {'in': [1, 1, 8, 0, 0, 0, 0, 0],
                         'out': [1, 1, 0, 0, 0, 0, 0, 0]},
  'joint_temperature': [0, 0, 0, 0, 0, 0, 0],
  'model': None,
  'motion_pause_resume_state': 1,
  'operation_status': {'auto_mode': False,
                       'free_drive_mode': False,
                       'manual_mode': True,
                       'moving': False,
                       'paused': False,
                       'program': False,
                       'ready': True,
                       'remote_mode': False,
                       'safety_controller_check_enable': False,
                       'safety_controller_normal': False,
                       'strict_operation_policy': True},
  'serial_number': None,
  'servo_status': {'servo_drive_coe_mode_of_operation': [8, 8, 8, 0, 0, 0, 0],
                   'servo_drive_coe_pds': [4, 4, 4, -1, -1, -1, -1],
                   'servo_drive_error': [0, 0, 0, 0, 0, 0, 0],
                   'servo_on': True},
  'trajectory_status': {'actual_joint_effort': [35.00772476196289,
                                                6.51925802230835e-08,
                                                1.4901161193847656e-07,
                                                0.0,
                                                0.0,
                                                0.0,
                                                0.0],
                        'actual_joint_position': [0.21831373870372772,
                                                  -0.03177299723029137,
                                                  -0.8192387819290161,
                                                  0.0,
                                                  0.0,
                                                  0.0,
                                                  0.0],
                        'actual_joint_velocity': [0.0,
                                                  0.0,
                                                  0.0,
                                                  0.0,
                                                  0.0,
                                                  0.0,
                                                  0.0],
                        'actual_pose': [0.15463924134614646,
                                        0.1716203457161464,
                                        0.5038137387037277,
                                        0.0,
                                        0.0,
                                        2.2905808744304856],
                        'actual_twist': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                        'actual_wrench': [0, 0, 0, 0, 0, 0],
                        'collision_joint_status': [0, 0, 0, 0, 0, 0, 0],
                        'feed_rate': 1.0,
                        'joint_temperature': [],
                        'residual_effort': [37.087829138037115,
                                            -0.0,
                                            -0.0,
                                            0.0,
                                            0.0,
                                            0.0,
                                            0.0],
                        'target_joint_effort': [0, 0, 0, 0, 0, 0, 0],
                        'target_joint_position': [0.21831373870372772,
                                                  -0.03177299723029137,
                                                  -0.8192387819290161,
                                                  0.0,
                                                  0.0,
                                                  0.0,
                                                  5.325169965892e-310],
                        'target_joint_velocity': [1.3155372962047583e-53,
                                                  1.3572550297507825e-56,
                                                  -2.194467079681263e-55,
                                                  0.0,
                                                  0.0,
                                                  0.0,
                                                  0.0],
                        'target_pose': [0.15463924134614646,
                                        0.1716203457161464,
                                        0.5038137387037277,
                                        0.0,
                                        0.0,
                                        2.2905808744304856],
                        'target_twist': [3.752118437230104e-56,
                                         3.7035264430471718e-56,
                                         1.3155372962047583e-53,
                                         0.0,
                                         0.0,
                                         -2.058741576706185e-55],
                        'target_wrench': [0, 0, 0, 0, 0, 0],
                        'time_stamp': 2190.5200000013933}}]
```
---

#### `get_operating_status`

**Signature:**  
```python
def get_operating_status(self) -> Dict
```

**Usage:**  
```python
robot.get_operating_status()
```

**Description:**  
Returns a dictionary containing the robot’s operational state (automatic/manual, direct teaching, motion pause, etc.).

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type | Description                                                       |
|-------------|-------------------------------------------------------------------|
| `dict`      | A dictionary that includes flags related to the operational state |

**Example Output:**
```python
[True,
 {'auto_mode': False,
  'free_drive_mode': False,
  'manual_mode': True,
  'moving': False,
  'paused': False,
  'program': False,
  'ready': True,
  'remote_mode': False,
  'safety_controller_check_enable': False,
  'safety_controller_normal': False,
  'strict_operation_policy': True}]
```


---

#### `get_error_status`

**Signature:**  
```python
def get_error_status(self) -> Dict
```

**Usage:**  
```python
robot.get_error_status()
```

**Description:**  
Returns comprehensive error information provided by the manufacturer, including collisions, emergency events, and other error details.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type | Description                                                |
|-------------|------------------------------------------------------------|
| `dict`      | A dictionary containing error status and alarm information |

**Example Output:**
```python
[True,
 {'alarm': {'alarm_code': '', 'alarm_description': ''},
  'collision_detected': False,
  'drive_error': False,
  'emergency': False,
  'joint_limit': False,
  'not_following': False,
  'processing_overload': False,
  'safe_guard': False,
  'self_collision': False,
  'total_error': False}]
```
---

#### `get_alarm`

**Signature:**  
```python
def get_alarm(self) -> Dict
```

**Usage:**  
```python
robot.get_alarm()
```

**Description:**  
Returns the most recent alarm code and its description provided by the manufacturer.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type | Description                                                     |
|-------------|-----------------------------------------------------------------|
| `dict`      | A dictionary containing the last alarm code and its description |

**Example Output:**
```python
[True, {'alarm_code': '', 'alarm_description': ''}]
```


---

#### `reset_trigger`

**Signature:**  
```python
def reset_trigger(self) -> bool
```

**Usage:**  
```python
robot.reset_trigger()
```

**Description:**  
Clears errors caused by conditions such as an emergency stop or a collision.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type | Description                                                                                                                              |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `bool`      | Returns True if the command is successfully issued and False if it fails (this does not indicate whether the error was actually cleared) |

**Example Output:**
```python
[True, True]
```

---

### B. Operational mode

#### `get_operational_mode`

**Signature:**  
```python
def get_operational_mode(self) -> str
```

**Usage:**  
```python
robot.get_operational_mode()
```

**Description:**  
Returns the current operation mode.  
Returns "AUTO" for automatic mode and "MANUAL" for manual mode.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type | Description            |
|-------------|------------------------|
| `str`       | `"AUTO"` or `"MANUAL"` |

**Example Output:**
```python
[True, 'AUTO']
```

---

#### `set_operational_mode`

**Signature:**  
```python
def set_operational_mode(self, *, operational_mode: str) -> bool
```

**Usage:**  
```python
robot.set_operational_mode(operational_mode='AUTO')
```

**Description:**  
Sets the robot’s operation mode. In MANUAL mode, the TCP speed is limited to 250 mm/sec.

**Parameters:**

| Parameter          | Type  | Description            |
|--------------------|-------|------------------------|
| `operational_mode` | `str` | `"AUTO"` or `"MANUAL"` |

**Return Value:**

| Return Type | Description  |
|-------------|--------------|
| `bool`      | Returns `True` |

**Example Output:**
```python
[True, True]
```

---

#### `set_direct_teaching_on_off`

**Signature:**  
```python
def set_direct_teaching_on_off(self, state: bool) -> bool
```

**Usage:**  
```python
robot.set_direct_teaching_on_off(state=True)
```

**Description:**  
Used to switch to direct teaching mode.  
If `state` is `True`, the robot switches to direct teaching mode; if `False`, it switches to position control mode.

**Parameters:**

| Parameter | Type   | Description                                                                      |
|-----------|--------|----------------------------------------------------------------------------------|
| `state`   | `bool` | `True`: switch to direct teaching mode, `False`: switch to position control mode |

**Return Value:**

| Return Type      | Description     |
|------------------|-----------------|
| `bool` or `None` |  Returns `True` |

**Example Output:**
```python
[True, True]
```

---

### C. Collision Detection

#### `set_collision_detection_sensitivity`

**Signature:**  
```python
def set_collision_detection_sensitivity(self, *, sensitivity: float) -> bool
```

**Usage:**  
```python
robot.set_collision_detection_sensitivity(sensitivity=100)
```

**Description:**  
Sets the collision detection sensitivity to a value between 0 and 100.  

**Parameters:**

| Parameter    | Type    | Description                                  |
|--------------|---------|----------------------------------------------|
| `sensitivity`| `float` | 0 (very insensitive) to 100 (very sensitive) |

**Return Value:**

| Return Type | Description    |
|-------------|----------------|
| `bool`      | Returns `True` |

**Example Output:**
```python
[True, True]
```
---

#### `set_post_collision_mode`

**Signature:**  
```python
def set_post_collision_mode(self, *, mode: int) -> bool
```

**Usage:**  
```python
robot.set_post_collision_mode(mode=2)
```

**Description:**  
Sets the mode the robot will switch to when a collision occurs.  

- `0` : Servo Off (motor power off)  
- `1` : Free Drive (free drive mode)  
- `2` : Pause (pause at the current state)  

**Parameters:**

| Parameter | Type  | Description                             |
|-----------|-------|-----------------------------------------|
| `mode`    | `int` | Post-collision operation mode (0, 1, 2) |

**Return Value:**

| Return Type | Description                        |
|-------------|------------------------------------|
| `bool`      | Whether the setting was successful |

**Example Output:**
```python
[True, True]
```

---

#### `get_collision_joint_status`

**Signature:**  
```python
def get_collision_joint_status(self) -> list[int]
```

**Usage:**  
```python
robot.get_collision_joint_status()
```

**Description:**  
Returns the collision status of each joint. Each element indicates 0 (normal) or 1 (collision).

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type | Description                                                 |
|-------------|-------------------------------------------------------------|
| `list[int]` | Collision status for each joint (0 = normal, 1 = collision) |

**Example Output:**
```python
[True, [0, 0, 0, 0, 0, 0, 0]]
# Example: collision detected on joint 2
[True, [0, 0, 1, 0, 0, 0, 0]]
```

---

#### `reset_collision_state`

**Signature:**  
```python
def reset_collision_state(self) -> bool
```

**Usage:**  
```python
robot.reset_collision_state()
```

**Description:**  
Resets the collision detection status.
After this call, the values returned by `get_collision_joint_status` are reset to 0.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type | Description                      |
|-------------|----------------------------------|
| `bool`      | Whether the reset was successful |

**Example Output:**
```python
[True, True]
```

---

### D. Movement and Control

#### `set_servo_on_off`

**Signature:**  
```python
def set_servo_on_off(self, *, state: bool) -> bool
```

**Usage:**  
```python
robot.set_servo_on_off(state=True)
```

**Description:**  
Turns the motor power on or off.

**Parameters:**

| Parameter | Type   | Description                           |
|-----------|--------|---------------------------------------|
| `state`   | bool   | `True`: power on, `False`: power off. |

**Return Value:**

| Return Type | Description    |
|-------------|----------------|
| `bool`      | Returns `True` |

**Example Output:**
```python
[True, True]
```

---

#### `stop`

**Signature:**  
```python
def stop(self, *, ramp_time: float = -1) -> bool
```

**Usage:**  
```python
robot.stop()
```

**Description:**  
Stops the motion currently in progress.
`ramp_time` is the deceleration time, and the robot switches to manual mode after stopping.

**Parameters:**

| Parameter   | Type    | Description       | Default Value |
|-------------|---------|-------------------|---------------|
| `ramp_time` | `float` | Deceleration time | -1            |

**Return Value:**

| Return Type | Description    |
|-------------|----------------|
| `bool`      | Returns `True` |

**Example Output:**
```python
[True, True]
```

---

#### `pause`

**Signature:**  
```python
def pause(self, *, ramp_time: float = -1) -> bool
```

**Usage:**  
```python
robot.pause()
```

**Description:**  
Pauses the current motion.

**Parameters:**

| Parameter   | Type    | Description       | Default Value |
|-------------|---------|-------------------|---------------|
| `ramp_time` | `float` | Deceleration time | -1            |

**Return Value:**

| Return Type | Description    |
|-------------|----------------|
| `bool`      | Returns `True` |

**Example Output:**
```python
[True, True]
```

---

#### `resume`

**Signature:**  
```python
def resume(self, *, ramp_time: float = -1) -> bool
```

**Usage:**  
```python
robot.resume()
```

**Description:**  
Resumes a paused motion.

**Parameters:**

| Parameter   | Type    | Description             | Default Value |
|-------------|---------|-------------------------|---------------|
| `ramp_time` | `float` | Time required to resume | -1            |

**Return Value:**

| Return Type | Description    |
|-------------|----------------|
| `bool`      | Returns `True` |

**Example Output:**
```python
[True, True]
```

---

#### `move_jog`

**Signature:**  
```python
def move_jog(self, *, mode: int, type: int, index: int, direction: int, speed_level: int) -> bool
```

**Usage:**  
```python
robot.move_jog(mode=0, type=0, index=5, direction=-1, speed_level=1)
```

**Description:**  
A jog function with the following parameters:
- `mode`: 0 = Joint jog, 1 = Task jog (base coordinate frame), 2 = Task jog (tool coordinate frame)
- `type`: 0 = Continuous jog, 1 = Tick jog
- `index`: 0–5 for joint jog, or one of [x, y, z, rx, ry, rz] for task jog
- `direction`: 1 = positive direction, -1 = negative direction
- `speed_level`: 1–10 (speed level)
When used, the robot switches to manual mode, and returns True on success.

**Parameters:**

| Parameter     | Type  | Description                                                                    |
|---------------|-------|--------------------------------------------------------------------------------|
| `mode`        | `int` | 0: Joint jog, 1: Task jog (base), 2: Task jog (tool)                           |
| `type`        | `int` | 0: Continuous jog, 1: Tick jog                                                 |
| `index`       | `int` | Joint number (0–5) for joint jog, or one of [x, y, z, rx, ry, rz] for task jog |
| `direction`   | `int` | 1: Positive direction, -1: Negative direction                                  |
| `speed_level` | `int` | 1–10 (speed level)                                                             |

**Return Value:**

| Return Type | Description                                                 |
|-------------|-------------------------------------------------------------|
| `bool`      | Returns `True` if the command succeeds, `False` if it fails |

**Example Output:**
```python
[True, True]
```

---

#### `move_home`

**Signature:**  
```python
def move_home(self) -> bool
```

**Usage:**  
```python
robot.move_home()
```

**Description:**  
Moves the robot to its home pose.
The robot moves using the move_joint command to the default pose specified in Motion Studio.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type | Description    |
|-------------|----------------|
| `bool`      | Returns `True` |

**Example Output:**
```python
[True, True]
```

---

#### `move_joint`

**Signature:**  
```python
def move_joint(self, *, waypoints: list[dict]) -> tuple[bool, float]
```

**Usage:**  
```python
robot.move_joint(waypoints=[
    {'q': [0, 0, 1.0], 'vel': 0.5, 'acc': 0.5, 'radius': 0.0},
    {'q': [0, -1, math.pi/2.0], 'vel': 0.5, 'acc': 0.5, 'radius': 0.0}
])
```

**Description:**  
Moves sequentially through waypoints using a joint command.
Each waypoint consists of q (joint angles, rad), vel (velocity, rad/sec), acc (acceleration, rad/sec²), and radius (blending radius).

**Parameters:**

| Parameter  | Type          | Description                                                                                             |
|------------|---------------|---------------------------------------------------------------------------------------------------------|
| `waypoints`| `list[dict]` | A list of waypoint dictionaries. Each dict: `{'q': [...], 'vel': float, 'acc': float, 'radius': float}` |

**Return Value:**

| Return Type | Description                                                 |
|-------------|-------------------------------------------------------------|
| `bool`      | Returns `True` if the command succeeds, `False` if it fails |

**Example Output:**
```python
[True, (True, 0.0)]
```

---

#### `move_linear`

**Signature:**  
```python
def move_linear(self, *, waypoints: list[dict]) -> tuple[bool, float]
```

**Usage:**  
```python
robot.set_ignore_orientation_for_ik_on_off_state(state=True) # Solves inverse kinematics while ignoring orientation.

robot.move_linear(waypoints=[
    {'pose': [0.3, 0.2, 0.3, 0, 0, 0], 'vel': 0.1, 'acc': 0.1, 'radius': 0.01},
    {'pose': [0.4, 0.3, 0.3, 0, 0, 0], 'vel': 0.1, 'acc': 0.1, 'radius': 0.01},
    {'pose': [0.3, 0.1, 0.3, 0, 0, 0], 'vel': 0.1, 'acc': 0.1, 'radius': 0.0}
])
```

**Description:**  
Moves sequentially through waypoints along a linear path using a linear command.
`pose` is specified as `[x, y, z, rx, ry, rz]` (m, rad).

**Parameters:**

| Parameter  | Type          | Description                                                                                                |
|------------|---------------|------------------------------------------------------------------------------------------------------------|
| `waypoints`| `list[dict]` | A list of waypoint dictionaries. Each dict: `{'pose': [...], 'vel': float, 'acc': float, 'radius': float}` |

**Return Value:**

| Return Type | Description                                                 |
|-------------|-------------------------------------------------------------|
| `bool`      | Returns `True` if the command succeeds, `False` if it fails |

**Example Output:**
```python
[True, (True, 0.0)]
```

---

#### `move_circle`

**Signature:**  
```python
def move_circle(
    self,
    *,
    pose: list[float],
    via_position: list[float],
    arc_angle: float = -1,
    orientation_fix: bool = False,
    vel: float = -1,
    acc: float = -1
) -> tuple[bool, float]
```

**Usage:**  
```python
robot.move_circle(
    pose=[0.2, 0.2, 0.4, 0, 0.0, 0],
    via_position=[0.3, 0.3, 0.3],
    arc_angle=-1,
    orientation_fix=True,
    vel=0.1,
    acc=0.1
)
```

**Description:**  
Starting from the current position, performs an arc motion that passes through a specified via position and reaches the final pose.
- If `arc_angle` is negative, the robot moves to the target pose and then stops.
- If `arc_angle` is greater than 0, the robot rotates by the specified angle.
- If `orientation_fix` is `True`, the starting orientation is fixed; if `False`, the orientation is interpolated and rotated.

**Parameters:**

| Parameter         | Type          | Description                                                                                                                                 |
|-------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| `pose`            | `list[float]` | Final target pose `[x, y, z, rx, ry, rz]` (m, rad)                                                                                          |
| `via_position`    | `list[float]` | Via position `[x, y, z]` (m)                                                                                                                |
| `arc_angle`       | `float`       | Arc angle (rad), default is -1 (a negative value such as -1 means the robot draws an arc through the via position to reach the target pose) |
| `orientation_fix` | `bool`        | `True`: fix the starting orientation, `False`: interpolate and rotate                                                                       |
| `vel`             | `float`       | Velocity (m/sec)                                                                                                                            |
| `acc`             | `float`       | Acceleration (m/sec²)                                                                                                                       |

**Return Value:**

| Return Type | Description                                   |
|-------------|-----------------------------------------------|
| `bool`      | Returns `True` on success, `False` on failure |

**Example Output:**
```python
[True, (True, 0.0)]
```

---

#### `check_finish`

**Signature:**  
```python
def check_finish(self, *, finish_mode: str = 'FINE') -> bool
```

**Usage:**  
```python
robot.check_finish()
```

**Description:**  
Checks whether the current motion has reached its target.

**Parameters:**

| Parameter     | Type  | Description                                                                                                                                                                 |
|---------------|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `finish_mode` | `str` | `'FINE'`: Checks whether the robot has actually reached the target position based on encoder values.<br>`'ROUGH'`: Returns `True` once the planned trajectory is completed |

**Return Value:**

| Return Type | Description                                                      |
|-------------|------------------------------------------------------------------|
| `bool`      | Returns `True` if the target has been reached, `False` otherwise |

**Example Output:**
```python
[True, True]
```

---
#### `set_feed_rate`

**Signature:**  
```python
def set_feed_rate(self, *, feed_rate: float) -> bool
```

**Usage:**  
```python
robot.set_feed_rate(feed_rate=0.5)
```

**Description:**  
Sets the feed rate (speed ratio) (0.1 ≤ feed_rate ≤ 1.5 )
It serves the same function as the feed rate adjustment slider on the web interface and is applied starting from subsequent commands.

**Parameters:**

| Parameter  | Type    | Description                  |
|------------|---------|------------------------------|
| feed_rate  | `float` | 0.1 ≤ feed_rate ≤ 1.5        |

**Return Value:**

| Return Type | Description                                   |
|-------------|-----------------------------------------------|
| `bool`      | Returns `True` on success, `False` on failure |

**Example Output:**
```python
[True, True]
```

---

#### `get_feed_rate`

**Signature:**  
```python
def get_feed_rate(self) -> Union[float, None]
```

**Usage:**  
```python
robot.get_feed_rate()
```

**Description:**  
Returns the currently configured feed rate value.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type       | Description             |
|-------------------|-------------------------|
| `float` or *None* | Current feed rate value |

**Example Output:**
```python
[True, 0.5]
```

---

### E. Program Execution

#### `execute_internal_program`

**Signature:**  
```python
def execute_internal_program(self, *, program_id: str) -> bool
```

**Usage:**  
```python
robot.execute_internal_program(program_id='default_script')
```

**Description:**  
Executes a program on the web interface.
Be careful: if `program_id` contains whitespace characters, it may be interpreted as a different name.

**Parameters:**

| Parameter    | Type  | Description                     |
|--------------|-------|---------------------------------|
| `program_id` | `str` | Title of the program to execute |

**Return Value:**

| Return Type | Description                                   |
|-------------|-----------------------------------------------|
| `bool`      | Returns `True` on success, `False` on failure |

**Example Output:**
```python
[True, True]
```

---

#### `stop_executing_internal_program`

**Signature:**  
```python
def stop_executing_internal_program(self) -> bool
```

**Usage:**  
```python
robot.stop_executing_internal_program()
```

**Description:**  
Stops the internal program that is currently running.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type | Description                          |
|-------------|--------------------------------------|
| `bool`      | Returns True if the command succeeds |

**Example Output:**
```python
[True, True]
```


---

### F. Joint and Pose Status

#### `get_trajectory_status`

**Signature:**  
```python
def get_trajectory_status(self) -> Dict
```

**Usage:**  
```python
robot.get_trajectory_status()
```

**Description:**  
Returns a dictionary containing joint and task status information.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type | Description                                                                             |
|-------------|-----------------------------------------------------------------------------------------|
| `dict`      | A dictionary that includes state information such as joints, pose, velocity, and torque |

**Example Output:**
```python
[True,
 {'actual_joint_effort': [-1.0968292951583862,
                          -51.081275939941406,
                          -45.3602180480957,
                          4.267107009887695,
                          -1.883137583732605,
                          -0.9523519277572632,
                          0.0],
  'actual_joint_position': [0.5585400483113837,
                            0.00565151755594642,
                            1.4713047563692259,
                            -0.0005265977459574519,
                            1.3927553526495569,
                            0.5563672084675018,
                            0.0],
  'actual_joint_velocity': [-0.15509339720423812,
                            -0.0005539124095640995,
                            -0.13436095443408028,
                            -0.0,
                            -0.1067753992308215,
                            -0.14942199592583263,
                            0.0],
  'actual_pose': [0.5306729125976563,
                  0.3697042236328125,
                  0.5142694702148437,
                  0.0009823458193079307,
                  2.9034452644463578,
                  0.209994957089481],
  'actual_twist': [0.11467050170898438,
                   -0.04673583221435547,
                   0.09596857452392578,
                   0.09351894066084204,
                   -0.2264775160767786,
                   -0.011254475074188227],
  'actual_wrench': [4.989142894744873,
                    7.498985290527344,
                    4.928271770477295,
                    -2.98199725151062,
                    1.9668713808059692,
                    -1.2975391149520874],
  'collision_joint_status': [],
  'feed_rate': 1.0,
  'joint_temperature': [-273.1499938964844,
                        -273.1499938964844,
                        -273.1499938964844,
                        -273.1499938964844,
                        -273.1499938964844,
                        -273.1499938964844],
  'residual_effort': [0.8374617099761963,
                      3.030996799468994,
                      -2.037428140640259,
                      -0.42755478620529175,
                      0.2849666178226471,
                      0.8491820693016052,
                      0.0],
  'target_joint_effort': [-0.0006173491710796952,
                          -48.9547119140625,
                          -42.57754898071289,
                          3.9992575645446777,
                          0.5115765333175659,
                          0.04202323779463768,
                          0.0],
  'target_joint_position': [0.5576234881327193,
                            0.005693802000183883,
                            1.470586368665177,
                            -0.0005339404243809096,
                            1.3921602693039785,
                            0.5555522811739375,
                            0.0],
  'target_joint_velocity': [-0.15382716397444632,
                            -0.0015707040628272875,
                            -0.12981693582413256,
                            0.00014729390681101397,
                            -0.1081821391752502,
                            -0.15325579940732664,
                            0.0],
  'target_pose': [0.5312263793945312,
                  0.3694648742675781,
                  0.5146617431640625,
                  0.0011285743791562448,
                  2.902426837258773,
                  0.21047647170812725],
  'target_twist': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
  'target_wrench': [],
  'time_stamp': 1739615796.9633026}]
```

---

#### `get_actual_joint_velocity_utilization`

**Signature:**  
```python
def get_actual_joint_velocity_utilization(self) -> list[float]
```

**Usage:**  
```python
robot.get_actual_joint_velocity_utilization()
```

**Description:**  
Returns the ratio of the current speed of each joint relative to its maximum speed.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type   | Description                                                    |
|---------------|----------------------------------------------------------------|
| `list[float]` | A list of joint speed utilization ratios. (ex: [-0.0727, ...]) |

**Example Output:**
```python
[True,
 [-0.0727253278096517,
  -0.0003424342100818952,
  -0.041764473915100096,
  -0.0,
  -0.027298683590359158,
  -0.0391118409898546]]
```

---

#### `get_actual_joint_position`

**Signature:**  
```python
def get_actual_joint_position(self) -> Union[list[float], None]
```

**Usage:**  
```python
robot.get_actual_joint_position()
```

**Description:**  
Returns the current actual angle (rad) of each joint (the first six joints are used).

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type             | Description                      |
|-------------------------|----------------------------------|
| `list[float]` or *None* | A list of joint angles (radians) |

**Example Output:**
```python
[True,
 [0.5563801913778158,
  0.005630928511917395,
  1.4695007310468062,
  -0.0005240696284607344,
  1.391253063478643,
  0.5542385105186878,
  0.0]]
```

---

#### `get_actual_joint_velocity`

**Signature:**  
```python
def get_actual_joint_velocity(self) -> Union[list[float], None]
```

**Usage:**  
```python
robot.get_actual_joint_velocity()
```

**Description:**  
Returns the actual velocity (rad/sec) of each joint.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type             | Description                              |
|-------------------------|------------------------------------------|
| `list[float]` or *None* | A list of joint velocities (radians/sec) |

**Example Output:**
```python
[True,
 [-0.15476, -0.000773, -0.13366, 2.58e-06, -0.10626, -0.15581, 0.0]]
```

---

#### `get_actual_joint_effort`

**Signature:**  
```python
def get_actual_joint_effort(self) -> Union[list[float], None]
```

**Usage:**  
```python
robot.get_actual_joint_effort()
```

**Description:**  
Returns the torque applied to each joint (Nm) (control torque).

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type             | Description                  |
|-------------------------|------------------------------|
| `list[float]` or *None* | A list of joint torques (Nm) |

**Example Output:**
```python
[True,
 [-0.40564, -50.26886, -44.47928, 4.25959, -1.94794, -1.00433, 0.0]]
```

---

#### `get_residual_effort`

**Signature:**  
```python
def get_residual_effort(self) -> Union[list[float], None]
```

**Usage:**  
```python
robot.get_residual_effort()
```

**Description:**  
Returns the external torque acting on each joint (Nm).

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type             | Description                     |
|-------------------------|---------------------------------|
| `list[float]` or *None* | A list of external torques (Nm) |

**Example Output:**
```python
[True,
 [0.69302, 2.92925, -2.20712, -0.43450, 0.25531, 0.84002, 0.0]]
```

---

#### `get_actual_pose`

**Signature:**  
```python
def get_actual_pose(self) -> Union[list[float], None]
```

**Usage:**  
```python
robot.get_actual_pose()
```

**Description:**  
Returns the current TCP pose `[x, y, z, rx, ry, rz]` (m, rad).  
(Note: the rotation convention is not ZYZ; it uses the rotation vector representation.)

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type             | Description                                |
|-------------------------|--------------------------------------------|
| `list[float]` or *None* | TA list representing the TCP pose (m, rad) |

**Example Output:**
```python
[True,
 [0.53338, 0.36857, 0.51652, 0.0009746, 2.89784, 0.21278]]
```

---

#### `get_actual_twist`

**Signature:**  
```python
def get_actual_twist(self) -> Union[list[float], None]
```

**Usage:**  
```python
robot.get_actual_twist()
```

**Description:**  
Returns the current TCP twist `[vel_x, vel_y, vel_z, vel_rx, vel_ry, vel_rz]` (m/sec, rad/sec).

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type             | Description                                        |
|-------------------------|----------------------------------------------------|
| `list[float]` or *None* | A list representing the TCP twist (m/sec, rad/sec) |

**Example Output:**
```python
[True,
 [0.11384, -0.04760, 0.09602, 0.08997, -0.22732, -0.00501]]
```

---

#### `get_actual_wrench`

**Signature:**  
```python
def get_actual_wrench(self) -> Union[list[float], None]
```

**Usage:**  
```python
robot.get_actual_wrench()
```

**Description:**  
Returns the force/torque acting on the TCP in the base coordinate frame (N, Nm).

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type             | Description                                      |
|-------------------------|--------------------------------------------------|
| `list[float]` or *None* | A list representing the TCP force/torque (N, Nm) |

**Example Output:**
```python
[True,
 [5.12109, 7.16200, 5.31352, -2.89485, 2.06011, -1.27893]]
```

---

#### `get_actual_tcp_wrench`

**Signature:**  
```python
def get_actual_tcp_wrench(self) -> Union[list[list[float], float], None]
```

**Usage:**  
```python
robot.get_actual_tcp_wrench()
```

**Description:**  
Returns the force/torque acting on the TCP in the tool coordinate frame along with a timestamp.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type             | Description                        |
|-------------------------|------------------------------------|
| `list[float]` or *None* | [TCP force/torque list, timestamp] |

**Example Output:**
```python
[True,
 [[-5.86882, 8.02504, -2.71073, 3.23542, 1.82216, 0.85161],
  1739615797.0013]]
```

---

#### `get_target_joint_position`

**Signature:**  
```python
def get_target_joint_position(self) -> Union[list[float], None]
```

**Usage:**  
```python
robot.get_target_joint_position()
```

**Description:**  
Returns the target joint angles (rad).

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type             | Description                             |
|-------------------------|-----------------------------------------|
| `list[float]` or *None* | A list of target joint angles (radians) |

**Example Output:**
```python
[True,
 [0.55239, 0.00564, 1.46617, -0.0005289, 1.38848, 0.55034, 0.0]]
```

---

#### `get_target_joint_velocity`

**Signature:**  
```python
def get_target_joint_velocity(self) -> Union[list[float], None]
```

**Usage:**  
```python
robot.get_target_joint_velocity()
```

**Description:**  
Returns the target joint velocities (rad/sec).

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type             | Description                                 |
|------------------------ |---------------------------------------------|
| `list[float]` or *None* | A list of target joint velocities (rad/sec) |

**Example Output:**
```python
[True,
 [-0.15383, -0.0015707, -0.12982, 0.0001473, -0.10818, -0.15326, 0.0]]
```

---

#### `get_target_joint_effort`

**Signature:**  
```python
def get_target_joint_effort(self) -> Union[list[float], None]
```

**Usage:**  
```python
robot.get_target_joint_effort()
```

**Description:**  
Returns the target joint torques (Nm).

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type             | Description                         |
|-------------------------|-------------------------------------|
| `list[float]` or *None* | A list of target joint torques (Nm) |

**Example Output:**
```python
[True,
 [-0.00061735, -48.95471, -42.57755, 3.99926, 0.51158, 0.042023, 0.0]]
```

---

#### `get_target_pose`

**Signature:**  
```python
def get_target_pose(self) -> Union[list[float], None]
```

**Usage:**  
```python
robot.get_target_pose()
```

**Description:**  
Returns the target TCP pose [x, y, z, rx, ry, rz] (m, rad).

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type             | Description                                      |
|-------------------------|--------------------------------------------------|
| `list[float]` or *None* | A list representing the target TCP pose (m, rad) |

**Example Output:**
```python
[True,
 [0.53619, 0.36737, 0.51881, 0.0011658, 2.89209, 0.21556]]
```

---

#### `get_target_twist`

**Signature:**  
```python
def get_target_twist(self) -> Union[list[float], None]
```

**Usage:**  
```python
robot.get_target_twist()
```

**Description:**  
Returns the target TCP twist `[vel_x, vel_y, vel_z, vel_rx, vel_ry, vel_rz]` (m/sec, rad/sec).

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type             | Description                                               |
|-------------------------|-----------------------------------------------------------|
| `list[float]` or *None* | A list representing the target TCP twist (m/sec, rad/sec) |

**Example Output:**
```python
[True, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
```

---

#### `get_target_wrench`

**Signature:**  
```python
def get_target_wrench(self) -> Union[list[float], None]
```

**Usage:**  
```python
robot.get_target_wrench()
```

**Description:**  
Returns the target TCP wrench.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type             | Description                               |
|-------------------------|-------------------------------------------|
| `list[float]` or *None* | A list representing the target TCP wrench |

**Example Output:**
```python
[True, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
```

---

#### `get_joint_temperature`

**Signature:**  
```python
def get_joint_temperature(self) -> Union[list[float], None]
```

**Usage:**  
```python
robot.get_joint_temperature()
```

**Description:**  
Returns the temperature (°C) of each joint.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type             | Description                       |
|-------------------------|-----------------------------------|
| `list[float]` or *None* | A list of joint temperatures (°C) |

**Example Output:**
```python
[True,
 [-273.15, -273.15, -273.15, -273.15, -273.15, -273.15]]
```

---

#### `get_default_joint_limit`

**Signature:**  
```python
def get_default_joint_limit(self, *, joint_index: int) -> list[float, float]
```

**Usage:**  
```python
robot.get_default_joint_limit(joint_index=0)
```

**Description:**  
Returns the system (model) default joint limits.
These are **default values** independent of any user-defined limits.

**Parameters:**

| Parameter     | Type  | Description                    |
|---------------|-------|--------------------------------|
| `joint_index` | `int` | Joint index (0-based) to query |

**Return Value:**

| Return Type           | Description          |
|-----------------------|----------------------|
| `list[float, float]` | (negative, positive) |

**Example Output:**
```python
[True, [0.0, 0.225]]
```

---

#### `get_user_joint_limit`

**Signature:**  
```python
def get_user_joint_limit(self, *, joint_index: int) -> Union[list[float, float], None]
```

**Usage:**  
```python
robot.get_user_joint_limit(joint_index=0)
```

**Description:**  
Returns the **user-defined joint limits** set by the user.
Returns `None` if no user-defined limits are configured.

**Parameters:**

| Parameter     | Type  | Description                    |
|---------------|-------|--------------------------------|
| `joint_index` | `int` | Joint index (0-based) to query |

**Return Value:**

| Return Type                     | Description                  |
|---------------------------------|------------------------------|
| `list[float, float]` or *None*  | (negative, positive) or *None* |

**Example Output:**
```python
[True, [-2.0, 2.0]]
# or
[True, None]
```

---

#### `get_current_joint_limit`

**Signature:**  
```python
def get_current_joint_limit(self, *, joint_index: int) -> list[float, float]
```

**Usage:**  
```python
robot.get_current_joint_limit(joint_index=0)
```

**Description:**  
Returns the joint limits that are **currently in effect**.
If user-defined limits are enabled, the user limits are applied; otherwise, the default limits are used.

**Parameters:**

| Parameter     | Type  | Description                    |
|---------------|-------|--------------------------------|
| `joint_index` | `int` | Joint index (0-based) to query |

**Return Value:**

| Return Type           | Description          |
|-----------------------|----------------------|
| `list[float, float]` | (negative, positive) |

**Example Output:**
```python
[True, [0.0, 0.225]]
```

---

#### `set_user_joint_limit`

**Signature:**  
```python
def set_user_joint_limit(self, *, joint_index: int, negative_limit: float, positive_limit: float) -> bool
```

**Usage:**  
```python
robot.set_user_joint_limit(joint_index=0, negative_limit=-2.0, positive_limit=2.0)
```

**Description:**  
Stores the **user-defined limit values** for a specific joint.
**Note:** This only saves the values; to apply them, you must enable them using `set_user_joint_limit_on_off_state(state=True)`.

**Parameters:**

| Parameter        | Type    | Description                  |
|------------------|---------|------------------------------|
| `joint_index`    | `int`   | Target joint index (0-based) |
| `negative_limit` | `float` | Negative direction limit     |
| `positive_limit` | `float` | Positive direction limit     |

**Return Value:**

| Return Type | Description                        |
|-------------|------------------------------------|
| `bool`      | Whether the setting was successful |

**Example Output:**
```python
[True, True]
```

---

#### `set_user_joint_limit_on_off_state`

**Signature:**  
```python
def set_user_joint_limit_on_off_state(self, *, state: bool) -> bool
```

**Usage:**  
```python
# 사용자 리밋 적용 활성화
robot.set_user_joint_limit_on_off_state(state=True)
```

**Description:**  
Enables or disables the application of user-defined limits globally.
If `True`, the user-defined limits are reflected in `get_current_joint_limit`.

**Parameters:**

| Parameter | Type   | Description               |
|-----------|--------|---------------------------|
| `state`   | `bool` | Enable state (True/False) |

**Return Value:**

| Return Type | Description                        |
|-------------|------------------------------------|
| `bool`      | Whether the setting was successful |

**Example Output:**
```python
[True, True]
```

---

#### `get_current_user_joint_limit_on_off_state`

**Signature:**  
```python
def get_current_user_joint_limit_on_off_state(self) -> Union[bool, None]
```

**Usage:**  
```python
robot.get_current_user_joint_limit_on_off_state()
```

**Description:**  
Returns the current user-defined limit application state.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type      | Description                         |
|------------------|-------------------------------------|
| `bool` or *None* | Enable state (True/False) or `None` |

**Example Output:**
```python
[True, True]
```

---


### G. Configuration Changes (TCP, Payload)

#### get_tcp

**Signature:**  
```python
def get_tcp(self) -> Union[list[float], None]
```

**Usage:**  
```python
robot.get_tcp()
```

**Description:**  
Returns the currently set TCP offset values.
The return value is a list in the form `[x, y, z, rx, ry, rz]` (units: m, rad), where the orientation is represented using the rotation vector convention.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type             | Description                                         |
|-------------------------|-----------------------------------------------------|
| `list[float]` or *None* | A list of TCP offset values ([x, y, z, rx, ry, rz]) |

**Example Output:**
```python
[True, [0.0, 0.0, 0.2, 0.0, 0.0, 0.0]]
```

---

#### `get_payload`

**Signature:**  
```python
def get_payload(self) -> Union[list[float, list[float], list[float]], None]
```

**Usage:**  
```python
robot.get_payload()
```

**Description:**  
Returns the currently configured payload information.
The return value is in the form `[mass, center_of_mass, inertia]`, where  
- mass: kg  
- center_of_mass: [x, y, z] (m)  
- inertia: [Ixx, Iyy, Izz, Ixy, Iyz, Ixz] (kg·m²) 

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type                                       | Description                                            |
|---------------------------------------------------|--------------------------------------------------------|
| `list[float, list[float], list[float]]` or *None* | payload information: `[mass, center_of_mass, inertia]` |

**Example Output:**
```python
[True,
 [1.7330000400543213,
  [-0.045, -0.009, 0.085],
  [0.0038488577120006084,
   0.0038488577120006084,
   0.0038488577120006084,
   0.0,
   0.0,
   0.0]]]
```


---

#### `set_tcp`

**Signature:**  
```python
def set_tcp(self, *, tcp: list[float]) -> bool
```

**Usage:**  
```python
robot.set_tcp(tcp=[0.0, 0.0, 0.2, math.pi/2.0, 0, 0])
```

**Description:**  
Sets the TCP offset with respect to the flange coordinate frame.
When providing arguments, the argument name `tcp` must be explicitly specified.
The list should be formatted as `[x, y, z, rx, ry, rz]` (units: m, rad).
**Note:** This function cannot be used when the servo is turned off in AUTO mode.

**Parameters:**

| Parameter | Type          | Description                      |
|-----------|---------------|----------------------------------|
| `tcp`     | `list[float]` | `[x, y, z, rx, ry, rz]` (m, rad) |

**Return Value:**

| Return Type | Description                                      |
|-------------|--------------------------------------------------|
| `bool`      | Returns `True` on success and `False` on failure |

**Example Output:**
```python
[True, True]
```

---

#### `set_payload`

**Signature:**  
```python
def set_payload(self, *, payload: dict) -> bool
```

**Usage:**  
```python
robot.set_payload(payload={'mass': 1.733, 'center_of_mass': [-0.045, 0.009, 0.085], 'inertia': [0, 0, 0, 0, 0, 0]})
```

**Description:**  
Sets the payload information
- mass: kg  
- center_of_mass: [x, y, z] (m)  
- inertia: [Ixx, Iyy, Izz, Ixy, Ixz, Iyz] (kg·m²)  
**Note:** This function cannot be used when the servo is turned off in AUTO mode.

**Parameters:**

| Parameter | Type  | Description                                                    |
|-----------|-------|----------------------------------------------------------------|
| `payload` | `dict`| payload information. Keys: `mass`, `center_of_mass`, `inertia` |

**Return Value:**

| Return Type | Description                                      |
|-------------|--------------------------------------------------|
| `bool`      | Returns `True` on success and `False` on failure |

**Example Output:**
```python
[True, True]
```

---

#### `set_tcp_with_bank`

**Signature:**  
```python
def set_tcp_with_bank(self, *, name: str) -> bool
```

**Usage:**  
```python
robot.set_tcp_with_bank(name='default_tool')
```

**Description:**  
Applies the TCP information stored in the Tool tab of the web teaching interface to the robot.
This function sets only the TCP and does not modify the payload information.

**Parameters:**

| Parameter | Type  | Description     |
|-----------|-------|-----------------|
| `name`    | `str` | tool bank title |

**Return Value:**

| Return Type | Description                                      |
|-------------|--------------------------------------------------|
| `bool`      | Returns `True` on success and `False` on failure |

**Example Output:**
```python
[True, True]
```

---

#### `set_payload_with_bank`

**Signature:**
```python
def set_payload_with_bank(self, *, name: str) -> bool
```

**Usage:**  
```python
robot.set_payload_with_bank(name='default_tool')
```

**Description:**  
Applies the payload information stored in the Tool tab of the web teaching interface using the specified index.
This function sets only the payload and does not modify the TCP information.

**Parameters:**

| Parameter | Type | Description     |
|-----------|------|-----------------|
| `name`    | `str`  | tool bank title |

**Return Value:**

| Return Type | Description                                      |
|-------------|--------------------------------------------------|
| `bool`      | Returns `True` on success and `False` on failure |

**Example Output:**
```python
[True, True]
```

---

### H. Bank Data Management

#### `get_tcp_bank_data`

**Signature:**  
```python
def get_tcp_bank_data(self, *, name: str) -> list[bool, list[str], str, list[float]]
```

**Usage:**
```python
robot.get_tcp_bank_data(name='default_tool')
```

**Description:**  
Loads the TCP information registered in the web teaching interface.
The return value is (status, hash tag, description, TCP offset list).

**Parameters:**

| Parameter | Type | Description                   |
|-----------|------|-------------------------------|
| `name`    | `str`  | Tool title of the TCP to load |

**Return Value:**

| Return Type                               | Description                                      |
|-------------------------------------------|--------------------------------------------------|
| `list[bool, list[str], str, list[float]]` | (status, hash tag, description, TCP offset list) |

**Example Output:**
```python
[True, [True, [], '', [0, 0, 0.123, 0, 0, 0]]]
```

---

#### `add_tcp_bank_data`

**Signature:**  
```python
def add_tcp_bank_data(self, *, name: str, hashtags: list[str], tcp: list[float], description: str = "") -> bool
```

**Usage:**  
```python
robot.add_tcp_bank_data(
    name="gripper",
    hashtags=["endtool", "default"],
    tcp=[0.0, 0.0, 0.150, 0, 0, 0],
    description="basic gripper tool"
)
```

**Description:**  
Adds new TCP information to the tool bank in the web teaching interface.
**Note:** If a TCP with the same name already exists, this function returns False.
To modify an existing TCP, use `update_tcp_bank_data`.

**Parameters:**

| Parameter     | Type          | Description                                            |
|---------------|---------------|--------------------------------------------------------|
| `name`        | `str`         | Name of the TCP to save                                |
| `hashtags`    | `list[str]`   | list of hash tags to associate with the TCP            |
| `tcp`         | `list[float]` | TCP offset list `[x, y, z, rx, ry, rz]` (m, rad)       |
| `description` | `str`         | TCP description (optional, default is an empty string) |

**Return Value:**

| Return Type | Description                                      |
|-------------|--------------------------------------------------|
| `bool`      | Returns `True` on success and `False` on failure |

**Example Output:**
```python
[True, True]
```

---

#### `update_tcp_bank_data`

**Signature:**  
```python
def update_tcp_bank_data(self, *, name: str, hashtags: list[str], tcp: list[float], description: str = "") -> bool
```

**Usage:**  
```python
robot.update_tcp_bank_data(
    name="gripper",
    hashtags=["endtool", "v2"],
    tcp=[0.0, 0.0, 0.180, 0, 0, 0],
    description="updated gripper tool"
)
```

**Description:**  
Updates an existing registered TCP information.

**Parameters:**

| Parameter     | Type          | Description                                            |
|---------------|---------------|--------------------------------------------------------|
| `name`        | `str`         | Name of the TCP to modify                              |
| `hashtags`    | `list[str]`   | New list of hash tags to apply                         |
| `tcp`         | `list[float]` | New TCP offset `[x, y, z, rx, ry, rz]` (m, rad)        |
| `description` | `str`         | New description (optional, default is an empty string) |

**Return Value:**

| Return Type | Description                                      |
|-------------|--------------------------------------------------|
| `bool`      | Returns `True` on success and `False` on failure |

**Example Output:**
```python
[True, True]
```

---

#### `remove_tcp_bank_data`

**Signature:**  
```python
def remove_tcp_bank_data(self, *, name: str) -> bool
```

**Usage:**  
```python
robot.remove_tcp_bank_data(name="gripper")
```

**Description:**  
Deletes the specified TCP from the tool bank in the web teaching interface.

**Parameters:**

| Parameter | Type  | Description               |
|-----------|-------|---------------------------|
| `name`    | `str` | Name of the TCP to delete |

**Return Value:**

| Return Type | Description                                      |
|-------------|--------------------------------------------------|
| `bool`      | Returns `True` on success and `False` on failure |

**Example Output:**
```python
[True, True]
```

---

#### `get_payload_bank_data`

**Signature:**  
```python
def get_payload_bank_data(self, *, name: str) -> list[bool, list[str], str, Dict]
```

**Usage:**  
```python
robot.get_payload_bank_data(name="default_tool")
```

**Description:**  
Loads the payload information registered in the web teaching interface.
The return value is (status, hash tag, description, payload information dictionary).

**Parameters:**

| Parameter | Type  | Description                 |
|-----------|-------|-----------------------------|
| `name`    | `str` | Name of the payload to load |

**Return Value:**

| Return Type                         | Description                                                     |
|-------------------------------- ----|-----------------------------------------------------------------|
| `list[bool, list[str], str, dict]` | (status, hash tag, description, payload information dictionary) |

**Example Output:**
```python
[True, [True, [], '', {'mass': 0.2, 'center_of_mass': [0.1, -0.01, 0], 'inertia': [0, 0, 0, 0, 0, 0]}]]
```

---

#### `add_payload_bank_data`

**Signature:**  
```python
def add_payload_bank_data(self, *, name: str, hashtags: list[str], description: str, payload: dict) -> bool
```

**Usage:**  
```python
robot.add_payload_bank_data(
    name="vacuum_payload",
    hashtags=["vacuum", "tool"],
    description="vacuum tool payload",
    payload={
        "mass": 1.2,
        "center_of_mass": [0, 0, 0.08],
        "inertia": [0.005, 0, 0, 0.005, 0, 0.005]
    }
)
```

**Description:**  
Adds new payload information to the Payload bank in the web teaching interface.
**Note:** If a payload with the same name already exists, this function returns `False`.
To modify an existing payload, use `update_payload_bank_data`.

**Parameters:**

| Parameter     | Type        | Description                                                                                                   |
|---------------|-------------|---------------------------------------------------------------------------------------------------------------|
| `name`        | `str`       | Name of the payload to save                                                                                   |
| `hashtags`    | `list[str]` | list of hash tags to associate with the payload                                                               |
| `description` | `str`       | Payload description                                                                                           |
| `payload`     | `dict`      | Payload information `{ "mass": float, "center_of_mass": [x,y,z], "inertia": [ixx, ixy, ixz, iyy, iyz, izz] }` |

**Return Value:**

| Return Type | Description                                      |
|-------------|--------------------------------------------------|
| `bool`      | Returns `True` on success and `False` on failure |

**Example Output:**
```python
[True, True]
```

---

#### `update_payload_bank_data`

**Signature:**  
```python
def update_payload_bank_data(self, *, name: str, hashtags: list[str], description: str, payload: dict) -> bool
```

**Usage:**  
```python
robot.update_payload_bank_data(
    name="vacuum_payload",
    hashtags=["vacuum", "tool", "rev2"],
    description="updated vacuum tool payload",
    payload={
        "mass": 1.3,
        "center_of_mass": [0, 0, 0.09],
        "inertia": [0.006, 0, 0, 0.006, 0, 0.006]
    }
)
```

**Description:**  
Updates existing registered payload information.

**Parameters:**

| Parameter     | Type        | Description                                                                                 |
|---------------|-------------|---------------------------------------------------------------------------------------------|
| `name`        | `str`       | Name of the payload to modify                                                               |
| `hashtags`    | `list[str]` | New list of hash tags to apply                                                              |
| `description` | `str`       | New description                                                                             |
| `payload`     | `dict`      | Upated payload information `{ "mass": float, "center_of_mass": [x,y,z], "inertia": [...] }` |

**Return Value:**

| Return Type | Description                                      |
|-------------|--------------------------------------------------|
| `bool`      | Returns `True` on success and `False` on failure |

**Example Output:**
```python
[True, True]
```

---

#### `remove_payload_bank_data`

**Signature:**  
```python
def remove_payload_bank_data(self, *, name: str) -> bool
```

**Usage:**  
```python
robot.remove_payload_bank_data(name="vacuum_payload")
```

**Description:**  
Deletes the specified payload information from the Payload bank in the web teaching interface.

**Parameters:**

| Parameter | Type  | Description                   |
|-----------|-------|-------------------------------|
| `name`    | `str` | Name of the payload to delete |

**Return Value:**

| Return Type | Description                                      |
|-------------|--------------------------------------------------|
| `bool`      | Returns `True` on success and `False` on failure |

**Example Output:**
```python
[True, True]
```

---

#### `get_pose_bank_data`

**Signature:**  
```python
def get_pose_bank_data(self, *, name: str) -> list[bool, list[str], str, list[float], list[float]]
```

**Usage:**  
```python
robot.get_pose_bank_data(name="home_pose")
```

**Description:**  
Loads the pose information registered in the web teaching interface.
The return value is (status, hash tag, description, pose list, joint list).

**Parameters:**

| Parameter | Type  | Description              |
|-----------|-------|--------------------------|
| `name`    | `str` | Name of the pose to load |

**Return Value:**

| Return Type                                            | Description                                                        |
|--------------------------------------------------------|--------------------------------------------------------------------|
| `list[bool, list[str], str, list[float], list[float]]` | (status, hash tag, description, [x, y, z, rx, ry, rz], joint list) |

**Example Output:**
```python
[True, [True, [], '', [0.688218505859375, -0.05760165786743164, 0.6952191772460937, 1.209862261852436, 1.2082374332873191, 1.2083641231430755], [0, 0, 1.5707963267948966, 0, 1.5707963267948966, 0, 0]]]
```

---

#### `add_pose_bank_data`

**Signature:**  
```python
def add_pose_bank_data(
    self,
    *,
    name: str,
    hashtags: list[str],
    description: str,
    pose: list[float],
    joint_positions: list[float]
) -> bool
```

**Usage:**  
```python
robot.add_pose_bank_data(
    name="pick_pose",
    hashtags=["pick", "object"],
    description="pick position",
    pose=[0.2, 0.1, 0.15, 0, 3.14, 0],
    joint_positions=[0.1, -1.2, 1.4, 0, 1.57, 0]
)
```

**Description:**  
Adds new pose information to the Pose bank in the web teaching interface.
**Note:** If a pose with the same name already exists, this function returns `False`.
To modify an existing pose, use `update_pose_bank_data`.

**Parameters:**

| Parameter         | Type          | Description                                    |
|-------------------|---------------|------------------------------------------------|
| `name`            | `str`         | Name of the pose to save                       |
| `hashtags`        | `list[str]`   | list of hash tags to associate with the pose   |
| `description`     | `str`         | Pose description                               |
| `pose`            | `list[float]` | Pose offset `[x, y, z, rx, ry, rz]` (m, rad)   |
| `joint_positions` | `list[float]` | list of joint values corresponding to the pose |

**Return Value:**

| Return Type | Description                                      |
|-------------|--------------------------------------------------|
| `bool`      | Returns `True` on success and `False` on failure |

**Example Output:**
```python
[True, True]
```

---

#### `update_pose_bank_data`

**Signature:**  
```python
def update_pose_bank_data(
    self,
    *,
    name: str,
    hashtags: list[str],
    description: str,
    pose: list[float],
    joint_positions: list[float]
) -> bool
```

**Usage:**  
```python
robot.update_pose_bank_data(
    name="pick_pose",
    hashtags=["pick", "object", "rev2"],
    description="updated pick pose",
    pose=[0.25, 0.1, 0.18, 0, 3.14, 0],
    joint_positions=[0.15, -1.25, 1.45, 0, 1.57, 0]
)
```

**Description:**  
Updates existing registered pose information.

**Parameters:**

| Parameter         | Type          | Description                                      |
|-------------------|---------------|--------------------------------------------------|
| `name`            | `str`         | Name of the pose to modify                       |
| `hashtags`        | `list[str]`   | New list of hash tags to apply                   |
| `description`     | `str`         | New description                                  |
| `pose`            | `list[float]` | New pose offset `[x, y, z, rx, ry, rz]` (m, rad) |
| `joint_positions` | `list[float]` | New list of joint values to apply                |

**Return Value:**

| Return Type | Description                                      |
|-------------|--------------------------------------------------|
| `bool`      | Returns `True` on success and `False` on failure |

**Example Output:**
```python
[True, True]
```

---

#### `remove_pose_bank_data`

**Signature:**  
```python
def remove_pose_bank_data(self, *, name: str) -> bool
```

**Usage:**  
```python
robot.remove_pose_bank_data(name="pick_pose")
```

**Description:**  
Deletes the specified pose information from the Pose bank in the web teaching interface.

**Parameters:**

| Parameter | Type  | Description                |
|-----------|-------|----------------------------|
| `name`    | `str` | Name of the pose to delete |

**Return Value:**

| Return Type | Description                                      |
|-------------|--------------------------------------------------|
| `bool`      | Returns `True` on success and `False` on failure |

**Example Output:**
```python
[True, True]
```

---

### I. Kinematics Computation

#### `solve_forward_kinematics`

**Signature:**  
```python
def solve_forward_kinematics(
    self,
    *,
    target_q: list[float],
    tcp: list[float] | None = None
) -> list[bool, list[float] | None]
```

**Usage:**  
```python
robot.solve_forward_kinematics(
    target_q=[
        0.7365882795706941,
        0.2465629272153449,
        1.2036360278436509
    ]
)
```

**Description:**  
Computes the TCP pose using the given joint angles (`target_q`).
The return value is composed of (calculation success status, TCP pose).

**Parameters:**

| Parameter  | Type          | Description                |
|------------|---------------|----------------------------|
| `target_q` | `list[float]` | Joint angle list (rad)     |
| `tcp`      | `list[float]` | TCP offset (default: None) |

**Return Value:**

| Return Type               | Description                            |
|---------------------------|----------------------------------------|
| `list[bool, list[float]]` | (calculation success status, TCP pose) |

**Example Output:**
```python
[True,
 [True,
  [0.50103, 0.49837, 0.57559, -0.0043026, -3.14136, -0.0004011]]]
```

---

#### `solve_inverse_kinematics`

**Signature:**  
```python
def solve_inverse_kinematics(
    self,
    *,
    target_p: list[float],
    seed_q: list[float] | None = None,
    tcp: list[float] | None = None
) -> list[int, list[float] | None]
```

**Usage:**  
```python
robot.set_ignore_orientation_for_ik_on_off_state(state=True) # Solves inverse kinematics while ignoring orientation.
robot.solve_inverse_kinematics(
    target_p=[0.3, 0.3, 0.3, 0, 0, 0],
    seed_q=[0, 0, 0]
)
```

**Description:**  
Computes the joint angles required to reach the target pose (`target_p`).
If `seed_q` is provided as an option, a solution close to it is returned.
As with forward kinematics, the TCP argument is not used.

**Parameters:**

| Parameter  | Type          | Description                             |
|------------|---------------|----------------------------------------------|
| `target_p` | `list[float]` | Target pose `[x, y, z, rx, ry, rz]` (m, rad) |
| `seed_q`   | `list[float]` | (Optional) Initial joint angles (rad)        |
| `tcp`      | `list[float]` | (Optional) TCP offset; omit or pass None     |

**Return Value:**

| Return Type              | Description                    |
|--------------------------|--------------------------------|
| `list[int, list[float]]` | (error code, joint angle list) |

**Example Output:**
```python
[True, 
[0, [0.014500000000000035, 0.1878823471042462, -1.7235809182862791, 0.0, 0.0, 0.0, 0.0]]]
```

---

### J. TCP and Payload Measurement

#### `calculate_tcp`

**Signature:**  
```python
def calculate_tcp(self, *, sample_pose_list: list[list[float]]) -> listlist[bool, list[float], float]
```

**Usage:**  
```python
robot.calculate_tcp(sample_pose_list=[
    [0.55893, 0.11289, 0.44632, 0.06411, -2.94076, 1.07034],
    [0.45922, 0.11287, 0.40890, 0.26171, 2.31932, -0.86081],
    [0.45910, -0.13073, 0.42216, 0.85044, 2.45128, 1.11725]
])
```

**Description:**  
Calculates the TCP offset and error based on multiple sample poses.
The sample poses must be pivoted poses measured with a zero TCP (flange coordinate frame).

**Parameters:**

| Parameter          | Type                | Description                                                    |
|--------------------|---------------------|----------------------------------------------------------------|
| `sample_pose_list` | `list[list[float]]` | list of sample pose values, each pose: `[x, y, z, rx, ry, rz]` |

**Return Value:**

| Return Type                      | Description                                                |
|----------------------------------|------------------------------------------------------------|
| `list[bool, list[float], float]` | (calculation success status, TCP offset list, error value) |

**Example Output:**
```python
[True, [True, [-7.01592e-06, 3.11402e-06, 0.19998], 1.17771e-05]]
```

---

#### `measure_payload_start`

**Signature:**  
```python
def measure_payload_start(self) -> bool
```

**Usage:**  
```python
robot.measure_payload_start()
```

**Description:**  
Sets the TCP and payload to zero and initializes the measurement buffer for payload measurement.
After executing this function, no separate termination command is required.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type | Description    |
|-------------|----------------|
| `bool`      | Returns `True` |

**Example Output:**
```python
[True, True]
```

---

#### `append_pose_wrench_sample`

**Signature:**  
```python
def append_pose_wrench_sample(self) -> bool
```

**Usage:**  
```python
robot.append_pose_wrench_sample()
```

**Description:**  
Adds the current pose and end-effector wrench data to the measurement buffer.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type | Description               |
|-------------|---------------------------|
| `bool`      | Returns `True` on success |

**Example Output:**
```python
[True, True]
```

---

#### `remove_pose_wrench_sample`

**Signature:**  
```python
def remove_pose_wrench_sample(self) -> bool
```

**Usage:**  
```python
robot.remove_pose_wrench_sample()
```

**Description:**  
Removes the most recently added pose–wrench data from the measurement buffer.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type | Description                                 |
|-------------|---------------------------------------------|
| `bool`      | Returns `True` if the removal is successful |

**Example Output:**
```python
[True, True]
```

---

#### `get_pose_wrench_sample_list`

**Signature:**  
```python
def get_pose_wrench_sample_list(self) -> list[float]
```

**Usage:**  
```python
robot.get_pose_wrench_sample_list()
```

**Description:**  
Returns the pose–wrench data currently stored in the measurement buffer.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| *None*    |      | N/A         |

**Return Value:**

| Return Type   | Description                       |
|---------------|-----------------------------------|
| `list[float]` | A list of pose–wrench sample data |

**Example Output:**
```python
[True, []]
```

---

#### `calculate_payload`

**Signature:**  
```python
def calculate_payload(self, *, sample_pose_wrench_list: Optional[list[float]] = None) -> list[bool, float, list[float]]
```

**Usage:**  
```python
robot.calculate_payload()
```

**Description:**  
Calculates the payload based on the internal measurement buffer (or a provided list of pose–wrench samples).
The return value is composed of (calculation success status, mass (float), center of mass [x, y, z]).

**Parameters:**

| Parameter                        | Type          | Description                                                                      |
|----------------------------------|---------------|----------------------------------------------------------------------------------|
| `sample_pose_wrench_list` (opt.) | `Optional[list[float]` | Pose–wrench sample data list (optional; if omitted, the internal buffer is used) |

**Return Value:**

| Return Type                      | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| `list[bool, float, list[float]]` | (calculation success status, mass, center of mass [x, y, z]) (units: kg, m) |

**Example Output:**
```python
[True, [False, 0, [0.0, 0.0, 0.0]]]
```
---
