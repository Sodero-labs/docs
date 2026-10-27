# Write Device Bridge Drivers

The [Device Bridge](https://docs.sodero.io/stellar-x/v2.0.1/gateways/device_bridge/index.md) runs on a small computer next to the sensors and serves their data to Stellar X. It connects any RGB-D camera, IMU or wheel board for which it has a driver: one Python class on the sensor computer. The drivers that come with the bridge, for Intel RealSense D400 cameras, the TurtleBot3 OpenCR board and simulated devices, are examples; write a driver of the same kind for your own device. Nothing on the controller is rebuilt or modified.

This page is for developers. To install the bridge and connect it to the Station, see [Device Bridge](https://docs.sodero.io/stellar-x/v2.0.1/gateways/device_bridge/index.md).

______________________________________________________________________

## 1. Driver Classes

A driver is one Python class for one piece of hardware. It subclasses `Device` and each capability the hardware has: `Camera`, `Imu` or `Wheels`. One class may provide several, as the OpenCR driver provides both `Imu` and `Wheels`. The interfaces are documented in `device_bridge/devices/base.py`, and `device_bridge/devices/simulated.py` is the smallest complete example.

| Class    | You implement                                                                                                                                                                                |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Device` | `open()`: connect, or raise an exception with a clear message. `close()`: stop and release the hardware; safe to call twice. `self.options` holds the device's configuration block.          |
| `Camera` | `camera_info()` returns `CameraInfo(width, height, fx, fy, cx, cy)` of the aligned output; `read_frame(timeout_s)` returns `RgbdFrame(rgb, depth_mm, capture_unix_ns)` or `None`             |
| `Imu`    | `read_imu()` returns `ImuSample(gyro, accel, orientation_xyzw, source_time_ns)`, or `None` when nothing is new                                                                               |
| `Wheels` | `joint_count`; `read_joints()` returns `JointState(positions, velocities, efforts, source_time_ns)` or `None`; `set_velocities(rad_per_s)`; `stop()` sets zero speed and releases the motors |

A minimal IMU driver:

```
# device_bridge/devices/my_imu.py
from device_bridge.devices.base import Device, Imu, ImuSample
import vendor_sdk  # placeholder: your IMU's SDK


class MyImu(Device, Imu):
    def open(self):
        self.sensor = vendor_sdk.open(self.options.get("port", "/dev/ttyUSB0"))
        self.last_ns = 0

    def close(self):
        if getattr(self, "sensor", None) is not None:
            self.sensor.close()
            self.sensor = None

    def read_imu(self):
        raw = self.sensor.latest()               # newest sample; never wait for one
        if raw is None or raw.timestamp_ns <= self.last_ns:
            return None                          # nothing new since the last call
        self.last_ns = raw.timestamp_ns
        return ImuSample(gyro=raw.gyro_rad_s,              # rad/s, sensor axes
                         accel=raw.accel_m_s2,             # m/s², gravity included
                         orientation_xyzw=raw.quaternion_xyzw,
                         source_time_ns=raw.timestamp_ns)  # must increase
```

Select it in the configuration as `driver: device_bridge.devices.my_imu:MyImu`, or register a short name in `DRIVERS` in `device_bridge/devices/__init__.py`. Keep your drivers in `device_bridge/devices/` so that `install.sh` copies them, and add your SDK's Python package to `requirements.txt`. `python -m unittest discover -s tests` checks the bridge end to end with the simulated devices.

Rules every driver follows:

- **Units:** radians, rad/s, m/s² with gravity included (+9.81 m/s² upward at rest), depth in millimeters as 16-bit integers (0 = no measurement), times in nanoseconds. Wheel positions are continuous and do not wrap at 2π.
- **Frames:** IMU data in the sensor's own axes, with `orientation_xyzw` the sensor's attitude in the world. Camera images in the optical frame (x right, y down, z forward), depth aligned to the RGB image, both rectified without distortion. Do not rotate data into the robot's frame; the mounting belongs in the map bundle.
- **Time:** `source_time_ns` must increase; a monotonic clock is fine. A camera's `capture_unix_ns` is the capture time on the wall clock.
- **Timing:** `read_imu` and `read_joints` return at once; `read_frame` blocks for at most its timeout. Copy images out of buffers that the SDK reuses.
- **Safety:** `stop()` must stop and release the motors. The bridge calls it when the controller switches its drive off and when commands pause for `command_timeout_s`.

______________________________________________________________________

## 2. Protocol

The Device Bridge and Isaac Bridge send the same messages over ZeroMQ on TCP. The bridge listens; the Station's gateways connect.

| Port  | Direction           | Contents                                                                           | Station node                  |
| ----- | ------------------- | ---------------------------------------------------------------------------------- | ----------------------------- |
| 53335 | bridge → controller | RGB-D frames (16-bit depth in millimeters and 8-bit RGB) and the camera intrinsics | Camera gateway                |
| 53334 | bridge → controller | IMU samples and wheel states                                                       | IMU gateway, Actuator gateway |
| 53333 | controller → bridge | Wheel commands: velocity while the drive is on, limp when it is off                | Actuator gateway              |

Every message carries the robot name, and each gateway takes only the messages of its own name. A slow link drops old frames instead of queuing them. The byte layouts are documented in [`docs/protocol.md`](https://github.com/Sodero-labs/device_bridge/blob/HEAD/docs/protocol.md) in the repository.
