# Create a Map from Your Site

Stellar Station does not build maps on the robot; there is no SLAM. You make the map bundle of your site beforehand, from a 3D model or a 3D scan of the site, and then upload it as described in [Load and Configure a Map](https://docs.sodero.io/stellar-x/v2.0.2/navigation/map_bundle/index.md). Every file and key of the bundle is specified in [Map Bundle Format](https://docs.sodero.io/stellar-x/v2.0.2/navigation/map_bundle_format/index.md).

The Localizer matches the camera's depth images against the 3D point cloud of the bundle to find the robot on the map. The Navigator plans paths on the 2D occupancy grid. Both describe the same site in the same coordinates.

Any point-cloud tool, such as CloudCompare or Open3D, can do the steps below.

______________________________________________________________________

## 1. Choose the Coordinate Frames

| Frame                                            | Meaning                                                                                                                          |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `map`                                            | The site: x and y horizontal, z up, the floor at z = 0, in meters. The point cloud, the grid, the initial pose and goals use it. |
| `odom`                                           | Continuous motion measured by odometry (Strider wheel odometry or Visual odometry). It drifts; the Localizer corrects the drift. |
| `base_link`                                      | The robot, **on the floor**: x forward, y left, z up.                                                                            |
| Camera optical frame, for example `cam0_optical` | x right, y down, z forward along the view.                                                                                       |

```
flowchart TB
    M["map"] -- "Localizer<br>(drift correction)" --> O["odom"]
    O -- "odometry<br>(Strider or Visual odometry)" --> B["base_link<br>(on the floor)"]
    B -- "extrinsics.yaml<br>(fixed)" --> C["cam0_optical<br>(x right, y down, z forward)"]
```

The Localizer is planar by default (`icp.planar: true`): it estimates x, y and yaw of `base_link` and holds its height, roll and pitch at zero. `base_link` therefore lies on the floor, and the camera height in `extrinsics.yaml` is its height **above the floor**.

Measure the camera's x and y from the base origin that your odometry tracks, but its z from the floor, even when your robot model places `base_link` higher, for example at the wheel axles. A height taken from a raised base puts every camera point too low by that offset: the fit error exceeds `icp.max_rmse` and the localization status stays **Initializing** (`initializing`).

______________________________________________________________________

## 2. Get a Point Cloud

Choose the `map` frame first: x and y horizontal, z up, the floor at z = 0, in meters. Then collect points on every surface the camera will see:

- **3D model:** sample points on the surfaces of the site's model, for example the USD world of your Isaac Sim scene, with normals and colors where available. When the map frame is the world frame, poses in the simulator and on the map are the same.
- **3D scan:** scan the real site with a laser scanner or by photogrammetry, and level the scan so that the floor lies at z = 0.

______________________________________________________________________

## 3. Clean and Export the PLY

1. Remove people, vehicles and other objects that move, stray points and everything outside the site.
1. Downsample to a point spacing of 2 to 5 cm, at most 2 million points; the Localizer reduces the map to `map.voxel_size` (5 cm by default) anyway.
1. Export a binary little-endian PLY with `float` x, y, z, optional normals and `uchar` colors: points only, no faces and no extra fields ([Point Cloud](https://docs.sodero.io/stellar-x/v2.0.2/navigation/map_bundle_format/#point-cloud-mapmap_idply)).

______________________________________________________________________

## 4. Make the Occupancy Grid

1. Pick the resolution (typically 0.05 m) and a rectangle that covers the cloud with a margin. Its lower-left corner is the `origin`; width and height are its size divided by the resolution, rounded up.
1. Mark a cell **occupied** (0) when it holds points in the height band the robot can hit, from just above the floor to just above the robot, for example 0.05 to 0.65 m.
1. Mark a cell **free** (254) when it holds floor points and no obstacle, and every other cell **unknown** (205).
1. Write the PGM with its top row at the largest y, then the grid YAML ([Occupancy Grid](https://docs.sodero.io/stellar-x/v2.0.2/navigation/map_bundle_format/#occupancy-grid-mapmap_idyaml-and-mapmap_idpgm)). Record the height band in `meta.yaml` as `z_slice`.

**Tip:** Compare the PGM with a top view of the point cloud. The walls must line up; a grid mirrored top to bottom was written bottom row first.

______________________________________________________________________

## 5. Write the YAML Files

Choose a map ID, name the three map files after it, and write the five YAML files: `meta.yaml`, `localizer.yaml`, `navigator.yaml`, `extrinsics.yaml` and `initial_pose.yaml` ([Files](https://docs.sodero.io/stellar-x/v2.0.2/navigation/map_bundle_format/#files)). Copy the width, height, resolution and origin of the grid into `meta.yaml` without rounding.

Start `navigator.yaml` from the file of a working bundle, such as the warehouse example of [Navigate in Simulation](https://docs.sodero.io/stellar-x/v2.0.2/navigation/simulation_tutorial/index.md), and change values only.

______________________________________________________________________

## 6. Measure the Camera Mounting

Measure the camera's optical center from `base_link`: x forward and y left from the base origin, z up from the floor. Measure its downward tilt and take the quaternion from [extrinsics.yaml](https://docs.sodero.io/stellar-x/v2.0.2/navigation/map_bundle_format/#extrinsicsyaml). Set `camera_frame_id` and the edge's `child` to the camera node's `frame_id`.

______________________________________________________________________

## 7. Pack the Bundle

```
# build/site.nav/ holds the five YAML files and map/
tar -czf site.nav.tgz -C build site.nav   # file for the Station page
cp site.nav.tgz site.nav                  # the same file, named for sodero maps upload
tar -tzf site.nav                         # every entry starts with site.nav/
```

Do not pack with `tar -czf site.nav.tgz -C build/site.nav .`: the `./` entry it adds is refused. Archive entries with hidden names, such as files some archivers add on macOS, are refused too.

______________________________________________________________________

## 8. Check the Bundle

The Station page checks the archive's layout when you upload it. The CLI preview checks every rule of the format without changing anything, so preview a new bundle from the [SSH workspace](https://docs.sodero.io/stellar-x/v2.0.2/ssh_workspace/overview/index.md) first:

```
sodero navigation get --node sodero.localizer                           # note "sha256"
sodero maps upload site.nav --node sodero.localizer --if-sha256 SHA256  # preview only, without --execute
```

The preview reports the first problem it finds ([Validation Errors](https://docs.sodero.io/stellar-x/v2.0.2/navigation/map_bundle_format/#validation-errors)).

### Checklist

- The `map` frame has the floor at z = 0, and the point cloud and the grid use the same coordinates.
- The grid files are `map/MAP_ID.pgm` and `map/MAP_ID.yaml`, and `meta.yaml` repeats their width, height, resolution and origin exactly.
- The PLY holds only x, y, z with optional normals and colors, and at most 2 million points.
- The grid YAML has exactly six keys, `negate` is 0 or 1, and `free_thresh` is below `occupied_thresh`.
- `camera_frame_id` matches the camera node's `frame_id`, the edges use `quat [x, y, z, w]`, and the camera height is measured from the floor.
- `initial_pose.yaml` gives the pose of `base_link`, with yaw in radians.
- `navigator.yaml` is complete, with your robot's `robot_radius` and speed limits.
- The archive is a gzip tar with one top folder, at most 64 MiB, and the CLI preview reports no problem.
- In simulation, the localization status reaches **Healthy** and the robot reaches a nearby goal before you drive the real robot.

Then upload the bundle: [Load and Configure a Map](https://docs.sodero.io/stellar-x/v2.0.2/navigation/map_bundle/index.md).
