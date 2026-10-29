# Map Bundle Format

This page specifies the map bundle (`.nav`) completely: its layout, every file, every accepted key with its type, range and default, and the messages of the bundle check. It is a reference for people who build bundles. To load a finished bundle, see [Load and Configure a Map](https://docs.sodero.io/stellar-x/v2.0.3/navigation/map_bundle/index.md); to make a bundle for your own site, see [Create a Map from Your Site](https://docs.sodero.io/stellar-x/v2.0.3/navigation/create_map/index.md).

The frames `map`, `odom`, `base_link` and the camera's optical frame are explained in [Create a Map from Your Site › Coordinate Frames](https://docs.sodero.io/stellar-x/v2.0.3/navigation/create_map/#1-choose-the-coordinate-frames).

______________________________________________________________________

## Bundle Layout

```
site.nav/              optional top folder, any name
├── meta.yaml          map ID and a description of the grid
├── localizer.yaml     Localizer settings, including the point-cloud file
├── navigator.yaml     Navigator settings: robot size, speeds, tolerances
├── extrinsics.yaml    camera mounting on the robot
├── initial_pose.yaml  starting pose of the robot on the map
└── map/
    ├── MAP_ID.ply     3D point cloud of the site
    ├── MAP_ID.pgm     2D occupancy grid image
    └── MAP_ID.yaml    grid resolution, origin and thresholds
```

| File                                                    | Read by                              |
| ------------------------------------------------------- | ------------------------------------ |
| `meta.yaml`                                             | Localizer and Navigator (the map ID) |
| `localizer.yaml`, `initial_pose.yaml`, `map/MAP_ID.ply` | Localizer                            |
| `navigator.yaml`                                        | Navigator                            |
| `extrinsics.yaml`                                       | Localizer and Visual odometry        |
| `map/MAP_ID.pgm`, `map/MAP_ID.yaml`                     | Navigator and the map views          |

- **All eight files are required**, and no other file is accepted. `MAP_ID` is the `map_id` of `meta.yaml`: the Localizer and the Navigator open the grid files by this name.
- **Archive:** a gzip-compressed tar. The files sit at its root or in one top folder, which is dropped on upload. The file name does not change the format: `site.nav` and `site.nav.tgz` can be the same file.
- **Limits:** the archive and its unpacked contents at most 64 MiB each, each YAML file at most 1 MiB, at most 128 archive entries including folders.
- **Names:** at most 160 characters of letters, digits, `_`, `-`, `.` and `/`; no hidden names (starting with `.`) and no links. Map files sit directly in `map/` and end in `.ply`, `.pgm` or `.yaml` (`.yml` is refused).
- **YAML:** plain mappings with unique keys; unknown keys are refused. Quote dates and times, and write exponents with a decimal point: `1.0e-6` is a number, `1e-6` is read as text.

______________________________________________________________________

## Files

### meta.yaml

| Key                                                                                                                                                     | Type             | Unit      | Meaning                                                                                              | Example               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | --------- | ---------------------------------------------------------------------------------------------------- | --------------------- |
| `schema_version`                                                                                                                                        | integer          | —         | Always `1`                                                                                           | `1`                   |
| `map_id`                                                                                                                                                | text             | —         | Map name: letters, digits, `_`, `.`, `-`, starting with a letter, at most 64 characters              | `warehouse`           |
| `frame_id`                                                                                                                                              | text             | —         | Map frame (default `map`)                                                                            | `map`                 |
| `created`, `z_slice`                                                                                                                                    | text, [min, max] | —, m      | Optional: creation time (quoted) and the height band used for the grid                               | `[0.05, 0.65]`        |
| `source`                                                                                                                                                | mapping          | —         | Optional provenance: `ply` (a file name, not a path), `ply_sha256`, `points`, `bbox_min`, `bbox_max` | `ply: warehouse.ply`  |
| `grid.image`, `grid.yaml`                                                                                                                               | text             | —         | `map/MAP_ID.pgm` and `map/MAP_ID.yaml`                                                               | `map/warehouse.pgm`   |
| `grid.width`, `grid.height`                                                                                                                             | integer          | cells     | Exactly the size of the PGM                                                                          | `500`, `620`          |
| `grid.resolution`                                                                                                                                       | number           | m/cell    | Exactly the `resolution` of the grid YAML                                                            | `0.05`                |
| `grid.origin`                                                                                                                                           | [x, y, yaw]      | m, m, rad | Exactly the `origin` of the grid YAML                                                                | `[-12.5, -12.5, 0.0]` |
| `tool`, `solid_footprints`, `grid.min_points`, `grid.padding`, `grid.mark_unknown`, `grid.points_in_slice`, `grid.occupied_cells`, `grid.unknown_cells` | any              | —         | Optional, informational                                                                              |                       |

```
schema_version: 1
map_id: warehouse
created: '2026-01-15T09:00:00Z'
z_slice: [0.05, 0.65]
grid:
  image: map/warehouse.pgm
  yaml: map/warehouse.yaml
  resolution: 0.05
  width: 500
  height: 620
  origin: [-12.5, -12.5, 0.0]
```

### Occupancy Grid: map/MAP_ID.yaml and map/MAP_ID.pgm

The grid uses the standard occupancy-grid map format: a gray image and a YAML file with exactly these six keys (a key such as `mode` is refused).

| Key                              | Type        | Unit      | Meaning                                                                                         | Example               |
| -------------------------------- | ----------- | --------- | ----------------------------------------------------------------------------------------------- | --------------------- |
| `image`                          | text        | —         | File name of the PGM, without a folder                                                          | `warehouse.pgm`       |
| `resolution`                     | number      | m/cell    | Cell size, 0.001 to 100                                                                         | `0.05`                |
| `origin`                         | [x, y, yaw] | m, m, rad | Lower-left corner of the image in `map`; keep yaw at `0.0`                                      | `[-12.5, -12.5, 0.0]` |
| `negate`                         | 0 or 1      | —         | `1` inverts the gray values                                                                     | `0`                   |
| `occupied_thresh`, `free_thresh` | number      | 0 to 1    | Occupancy above the first is an obstacle, below the second is free; `free_thresh` must be lower | `0.65`, `0.196`       |

```
image: warehouse.pgm
resolution: 0.05
origin: [-12.5, -12.5, 0.0]
negate: 0
occupied_thresh: 0.65
free_thresh: 0.196
```

- **Image:** binary `P5` or ASCII `P2` PGM, maximum value 255, at most 16 million pixels. After the header, a P5 file holds exactly width × height bytes.
- **Values:** the occupancy of a pixel is `(255 − value) / 255` with `negate: 0`. With the thresholds above, write **0** for obstacles, **254** for free floor and **205** for unknown space.
- **Rows:** row 0 is the top of the map, the largest y. The pixel in column `c` and row `r` of an image `height` rows tall is the cell centered at `x = origin_x + (c + 0.5) × resolution`, `y = origin_y + (height − r − 0.5) × resolution`. The warehouse grid, 500 × 620 cells of 0.05 m, covers x from −12.5 m to 12.5 m and y from −12.5 m to 18.5 m.

### Point Cloud: map/MAP_ID.ply

- **Format:** `format binary_little_endian 1.0` (recommended) or `format ascii 1.0`, with an ASCII header in LF line endings that ends in `end_header`.
- **Contents:** one `element vertex` with 1 to 2,000,000 points. The properties are `x`, `y`, `z` (required), `nx`, `ny`, `nz` and `red`, `green`, `blue` (optional), each of type `float`, `double` or `uchar` (also written `float32`, `float64`, `uint8`). `comment` lines are allowed; faces, other elements or properties (alpha, intensity, scalar fields) and lines such as `obj_info` are refused. The warehouse header has `element vertex 1405083`, then `property float x`, `y`, `z`, `nx`, `ny`, `nz` and `property uchar red`, `green`, `blue`.
- **Values:** meters in the `map` frame, finite and at most 1,000,000 in magnitude. Normals, when present, must not be zero. Colors are optional (`uchar` 0 to 255 or `float` 0 to 1); without them the Localizer matches geometry only.
- **Size:** binary `float` coordinates with normals and colors take 27 bytes per point, so 2 million points use about 54 MB of the 64 MiB limit. Use `float`, not `double`.

### extrinsics.yaml

| Key               | Type         | Unit | Meaning                                                                                                                                | Example                     |
| ----------------- | ------------ | ---- | -------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| `camera_frame_id` | text         | —    | The camera's optical frame: the `frame_id` in the camera node's **CAMERA SETTINGS**, at most 15 characters. Required by the Localizer. | `cam0_optical`              |
| `edges`           | list         | —    | 1 to 32 fixed transforms; a frame is the `child` of one edge at most                                                                   |                             |
| `parent`, `child` | text         | —    | Frame names                                                                                                                            | `base_link`, `cam0_optical` |
| `xyz`             | [x, y, z]    | m    | Position of the child in the parent frame                                                                                              | `[0.22, 0.0, 0.468]`        |
| `quat`            | [x, y, z, w] | —    | Orientation of the child in the parent frame; the squares sum to 1 within 0.01                                                         | `[-0.5, 0.5, -0.5, 0.5]`    |

```
camera_frame_id: cam0_optical
edges:
  - parent: base_link
    child: cam0_optical
    xyz: [0.22, 0.0, 0.468]       # 0.22 m ahead of base_link, 0.468 m above the floor
    quat: [-0.5, 0.5, -0.5, 0.5]  # level, looking forward
```

Rotations are written only as `quat` in the order `[x, y, z, w]`; an edge with `rpy` is refused. Edges may form a chain, for example `base_link` → `mast` → `cam0_optical`, but no loop, and they must connect the camera frame to `base_link`. For a camera that looks forward, tilted down by θ, `quat = [-a, a, -b, b]` with `a = (cos(θ/2) + sin(θ/2)) / 2` and `b = (cos(θ/2) − sin(θ/2)) / 2`:

| Tilt θ | 0° (level)               | 10°                                  | 20°                                  | 30°                                  |
| ------ | ------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `quat` | `[-0.5, 0.5, -0.5, 0.5]` | `[-0.5417, 0.5417, -0.4545, 0.4545]` | `[-0.5792, 0.5792, -0.4056, 0.4056]` | `[-0.6124, 0.6124, -0.3536, 0.3536]` |

### initial_pose.yaml

| Key      | Type   | Unit         | Meaning                                           | Example             |
| -------- | ------ | ------------ | ------------------------------------------------- | ------------------- |
| `x`, `y` | number | m            | Position of `base_link` (not the camera) in `map` | `-1.5984`, `2.3881` |
| `yaw`    | number | rad, −π to π | Heading; `0` faces the +x axis of the map         | `0.0`               |

```
x: -1.5984
y: 2.3881
yaw: 0.0
```

The Localizer starts from this pose when it has no confirmed pose on this map. Once it has localized, it restarts from its last confirmed pose on the same `map_id`. A pose set with **Set Initial Pose** on Strider's Navigation page, or with the `localization.set_initial_pose` tool, replaces both. Give a changed map a new `map_id` so that an old pose is not reused.

### localizer.yaml

Only `map.file` is required; a key you leave out keeps its default. An excerpt of the warehouse file:

```
map:
  file: map/warehouse.ply
  voxel_size: 0.05
icp:
  device: CPU:0
  lambda: 1.0
  max_correspondence_dist: 0.12
  max_iterations: 20
sensor: {depth_min: 0.3, depth_max: 10.0}
status: {degrade_after_s: 5.0, lost_after_s: 60.0, accept_streak: 1}
publish:
  obstacles: {z_min: 0.08, z_max: 0.65}
```

#### Map and Frames

| Key                                        | Default                    | Meaning                                                               |
| ------------------------------------------ | -------------------------- | --------------------------------------------------------------------- |
| `map.file`                                 | required                   | The point cloud, `map/MAP_ID.ply`. It changes only with a new bundle. |
| `map.voxel_size`                           | `0.05` m                   | The cell size that the map and the camera points are reduced to       |
| `frames.map`, `frames.odom`, `frames.base` | `map`, `odom`, `base_link` | Frame names; keep the defaults, which the Navigator also uses         |

#### Matching

| Key                                                      | Default            | Meaning                                                                                                     |
| -------------------------------------------------------- | ------------------ | ----------------------------------------------------------------------------------------------------------- |
| `icp.planar`                                             | `true`             | Estimate x, y and yaw only (wheeled robots); `false` also estimates height, roll and pitch (walking robots) |
| `icp.device`                                             | `CPU:0`            | `CPU:0`, or `CUDA:0` for a GPU                                                                              |
| `icp.rate_hz`                                            | `10` Hz            | Localization rate                                                                                           |
| `icp.max_iterations`                                     | `50`               | Iterations per camera frame                                                                                 |
| `icp.lambda`                                             | `0.968`            | Weight of geometry against color, 0 to 1; `1.0` matches geometry only                                       |
| `icp.max_correspondence_dist`                            | `0.1` m            | Match distance while tracking                                                                               |
| `icp.init_max_correspondence_dist`                       | `0.3` m            | Match distance while initializing or relocalizing                                                           |
| `icp.min_fitness`                                        | `0.3`              | A pose is accepted when at least this share of camera points matches the map…                               |
| `icp.max_rmse`                                           | `0.05` m           | …within this fit error                                                                                      |
| `icp.max_jump_m`, `icp.max_jump_rad`                     | `1.0` m, `0.5` rad | Largest accepted correction against the odometry prediction                                                 |
| `icp.deg_ratio`, `icp.deg_min_info`, `icp.deg_threshold` | `0.05`, `5.0`, `0` | Handling of directions the view cannot observe, such as along a corridor                                    |

**Advanced matching.** Keep these at their defaults: `icp.max_solve_points` `0`, `icp.robust_delta` `0`, `icp.relative_fitness` `1.0e-6`, `icp.relative_rmse` `1.0e-6`, `icp.min_structural_fitness` `0`, `icp.rmse_growth_factor` `1.05`, `icp.sigma_depth` `0.01`, `icp.cov_inflation` `4.0`, `icp.recovery_radius_m` `0.4`, `icp.recovery_yaw_rad` `0.5`.

#### Camera Points

| Key                                    | Default          | Meaning                               |
| -------------------------------------- | ---------------- | ------------------------------------- |
| `sensor.depth_min`, `sensor.depth_max` | `0.2` m, `6.0` m | Depth range of the camera points used |

#### Localization Status

| Key                                               | Default           | Meaning                                                                                             |
| ------------------------------------------------- | ----------------- | --------------------------------------------------------------------------------------------------- |
| `status.accept_streak`, `status.init_min_fitness` | `3`, `0.7`        | Accepted fits in a row, each with at least this fitness, needed to become **Healthy** (`localized`) |
| `status.degrade_after_s`, `status.lost_after_s`   | `2.0` s, `10.0` s | Time without an accepted fit before **Degraded** (`degraded`) and before **Lost** (`lost`)          |
| `status.degrade_fitness`                          | `0.5`             | Fitness below which the state degrades                                                              |
| `status.clock_skew_ms`                            | `200` ms          | Largest camera-to-odometry lag                                                                      |
| `status.odometry_stale_s`                         | `3.0` s           | Odometry silence before the input reconnects                                                        |

#### Recovery After Lost

| Key                                                                                             | Default                        | Meaning                                                            |
| ----------------------------------------------------------------------------------------------- | ------------------------------ | ------------------------------------------------------------------ |
| `recovery.auto_reseed`                                                                          | `true`                         | After **Lost**, retry automatically around the last confirmed pose |
| `recovery.lost_wait_s`, `recovery.attempts`, `recovery.attempt_timeout_s`, `recovery.spacing_s` | `3.0` s, `5`, `5.0` s, `1.0` s | Schedule of the retries                                            |
| `recovery.radius_step_m`, `recovery.max_radius_m`, `recovery.yaw_jitter_rad`                    | `0.3` m, `1.0` m, `0.17` rad   | Search area of the retries                                         |

#### Outputs and Live Obstacles

| Key                                                            | Default            | Meaning                                                                               |
| -------------------------------------------------------------- | ------------------ | ------------------------------------------------------------------------------------- |
| `publish.pose_hz`, `publish.status_hz`, `publish.obstacles_hz` | `20`, `1`, `10` Hz | Output rates                                                                          |
| `publish.obstacles.z_min`, `publish.obstacles.z_max`           | `0.10` m, `0.30` m | Height band above the floor whose camera points mark live obstacles for the Navigator |
| `publish.obstacles.ground_relative`                            | `false`            | `true` measures the band from the floor seen in each image                            |
| `publish.obstacles.size_cells`, `publish.obstacles.resolution` | `48`, `0.05` m     | Live obstacle grid around the robot, at most 48 × 48 cells                            |
| `publish.obstacles.decay_s`                                    | `2.0` s            | How long a mark lasts                                                                 |

#### Odometry Input and Global Search

| Key                     | Default     | Meaning                                                                                                                                                                                                               |
| ----------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `odometry.frame_policy` | `match`     | `match` uses only odometry from `odom` to `base_link`; `any` accepts a single source under any frame names                                                                                                            |
| `odometry.recovery`     | `auto`      | Keep `auto`                                                                                                                                                                                                           |
| `odometry.source`       | empty       | Empty follows the node connected to the Localizer's `odometry` port                                                                                                                                                   |
| `global_search.*`       | see meaning | Grid of the `localization.global_search_*` tools: `xy_step_m` 1.0, `yaw_step_deg` 15, `coarse_radius_m` 1.2, `sample_radius_m` 6.0, `timeout_s` 120, `max_candidates` 100000, `shortlist` 32, `ambiguity_margin` 0.08 |

### navigator.yaml

The sections are `bt_navigator`, `planner_server`, `controller_server`, `local_costmap`, `global_costmap`, `behavior_server`, `velocity_smoother` and `navigator`; section and key names follow Nav2 conventions. An excerpt of the warehouse file:

```
controller_server:
  general_goal_checker: {xy_goal_tolerance: 0.1, yaw_goal_tolerance: 0.1}
  FollowPath: {desired_linear_vel: 0.3, max_angular_vel: 0.5}
local_costmap:
  global_frame: odom
  rolling_window: true
  width: 4
  height: 4
  robot_radius: 0.34
  inflation_layer: {inflation_radius: 0.6}
global_costmap: {global_frame: map, robot_radius: 0.34}
velocity_smoother:
  max_velocity: [0.3, 0.0, 0.5]
  min_velocity: [-0.2, 0.0, -0.5]
navigator: {drive: diff}
```

- **Write the complete file.** Start from the `navigator.yaml` of a working bundle, such as the warehouse example of [Navigate in Simulation](https://docs.sodero.io/stellar-x/v2.0.3/navigation/simulation_tutorial/index.md), and change values only. A key you leave out falls back to a built-in value that may not suit your robot; without `robot_radius` the Navigator does not start.
- **Text values are fixed:** frame names, `plugin` entries and plugin lists keep their values. The one choice is `navigator.drive`: `diff` or `holonomic`.
- **Numbers** are 0 to 1,000,000, except the entries of `min_velocity` and `max_decel`, which may be negative. Velocity lists have three entries: `[x m/s, y m/s, yaw rad/s]`.
- **Robot size** is a circle, `robot_radius`; a polygon `footprint` is refused.

The **Template** column lists the values of the reference navigator configuration, which defines the accepted keys. They are a starting point for your own values, not the built-in values used for a key you leave out.

#### Robot Size and Costmaps

| Key                                                                           | Template                               | Meaning                                                                                                   |
| ----------------------------------------------------------------------------- | -------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `local_costmap.robot_radius`, `global_costmap.robot_radius`                   | `0.42` m                               | Radius around `base_link` that covers the robot; required, the same value in both                         |
| `*.inflation_layer.inflation_radius`, `*.inflation_layer.cost_scaling_factor` | `0.75` m, `3.0`                        | Distance from obstacles within which paths cost more, and how fast that cost falls off                    |
| `local_costmap.width`, `local_costmap.height`, `local_costmap.resolution`     | `6` m, `6` m, `0.05` m                 | Size and cell size of the local window around the robot; the global costmap follows the grid's resolution |
| `*.obstacle_layer.enabled`, `*.obstacle_layer.decay_s`                        | `true`; `2.0` s local, `10.0` s global | Add the Localizer's live obstacles, and how long they are kept                                            |

#### Planning

| Key                                      | Template | Meaning                                    |
| ---------------------------------------- | -------- | ------------------------------------------ |
| `planner_server.GridBased.tolerance`     | `0.5` m  | How far from a blocked goal a path may end |
| `planner_server.GridBased.allow_unknown` | `true`   | Plan through unknown cells                 |
| `planner_server.GridBased.use_astar`     | `false`  | A\* instead of Dijkstra                    |

#### Path Following

| Key                                                                                               | Template                 | Meaning                                                                 |
| ------------------------------------------------------------------------------------------------- | ------------------------ | ----------------------------------------------------------------------- |
| `controller_server.controller_frequency`                                                          | `20.0` Hz                | Control rate                                                            |
| `controller_server.FollowPath.desired_linear_vel`, `controller_server.FollowPath.max_angular_vel` | `1.2` m/s, `0.825` rad/s | Cruise speed and turn rate limit                                        |
| `controller_server.FollowPath.lookahead_dist`, `min_lookahead_dist`, `max_lookahead_dist`         | `1.5`, `0.6`, `1.8` m    | Look-ahead distance on the path                                         |
| `controller_server.FollowPath.use_rotate_to_heading`, `rotate_to_heading_min_angle`               | `true`, `0.785` rad      | Turn in place toward the path when the heading error exceeds this angle |
| `controller_server.FollowPath.allow_reversing`                                                    | `false`                  | Drive backwards along the path                                          |
| `controller_server.FollowPath.use_holonomic_lateral`, `max_lateral_vel`                           | `false`, `0.2` m/s       | Move sideways (with `navigator.drive: holonomic`)                       |

#### Goals and Progress

| Key                                                                                      | Template             | Meaning                                                           |
| ---------------------------------------------------------------------------------------- | -------------------- | ----------------------------------------------------------------- |
| `controller_server.general_goal_checker.xy_goal_tolerance`, `yaw_goal_tolerance`         | `0.25` m, `0.25` rad | Arrival tolerance                                                 |
| `controller_server.progress_checker.required_movement_radius`, `movement_time_allowance` | `0.5` m, `10.0` s    | The robot must move this far within this time, or recovery starts |

#### Velocity Limits and Recovery Moves

| Key                                                                | Template                               | Meaning                                                 |
| ------------------------------------------------------------------ | -------------------------------------- | ------------------------------------------------------- |
| `velocity_smoother.max_velocity`, `velocity_smoother.min_velocity` | `[1.2, 0, 0.825]`, `[-0.1, 0, -0.825]` | Velocity limits                                         |
| `velocity_smoother.max_accel`, `velocity_smoother.max_decel`       | `[0.25, 0, 1.2]`, `[-0.5, 0, -1.6]`    | Acceleration limits; deceleration entries are 0 or less |
| `behavior_server.spin.angle`                                       | `1.5708` rad                           | Turn of the spin recovery                               |
| `behavior_server.backup.distance`, `behavior_server.backup.speed`  | `0.15` m, `0.1` m/s                    | Back-up recovery                                        |
| `behavior_server.wait.duration`                                    | `2.0` s                                | Wait recovery                                           |

#### Navigator Node

| Key                                                            | Template         | Meaning                                                                       |
| -------------------------------------------------------------- | ---------------- | ----------------------------------------------------------------------------- |
| `navigator.drive`                                              | `diff`           | `diff` (differential and skid steer) or `holonomic`                           |
| `navigator.require_base_ready`                                 | `true`           | Accept goals only while the base is enabled, free of faults and in twist mode |
| `navigator.odom_max_age_s`, `navigator.localization_max_age_s` | `0.5` s, `1.0` s | Stop when odometry or the map pose is older than this                         |
| `navigator.recovery_rounds`                                    | `2`              | Recovery rounds before a goal fails                                           |
| `navigator.replan_period_s`                                    | `1.0` s          | How often the route is checked and replanned when blocked                     |
| `navigator.preempt_on_new_goal`                                | `true`           | A new goal replaces the active one; `false` refuses it as busy                |

______________________________________________________________________

## Validation Errors

`KEY` stands for the path of a setting, for example `localizer.icp.max_rmse` or `extrinsics.edges.0`.

| Message                                                                                                                                                        | Cause                                                                                                             | Fix                                                                                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `Use a gzip .nav archive no larger than 64 MiB.`, `Navigation data exceeds 64 MiB.`                                                                            | Not gzip-compressed (zip, plain tar), or too large                                                                | Pack with `tar -czf`; fewer points, `float` instead of `double`                                   |
| `Unsafe, duplicate or unsupported navigation archive member.`                                                                                                  | A `./` entry, hidden name, link, unsupported character, name over 160 characters or more than 128 entries         | Pack the folder by name; remove hidden files and links                                            |
| `A .nav bundle needs meta, localizer, navigator, extrinsics and initial_pose YAML files.`                                                                      | A YAML file is missing, or the files sit in more than one top folder                                              | Add the file; use one top folder                                                                  |
| `Navigation bundles accept only their five YAML documents and map PLY/PGM/YAML data.`, `Include exactly the referenced PLY, PGM and occupancy YAML map files.` | An extra or unreferenced file, a `.yml` or upper-case extension, or a folder inside `map/`                        | Remove it, or fix the reference                                                                   |
| `The localizer must reference a PLY contained in map/.`, `Metadata grid references must identify bundled map data.`                                            | `map.file`, `grid.image` or `grid.yaml` does not name a bundled file                                              | Use `map/MAP_ID.ply`, `map/MAP_ID.pgm`, `map/MAP_ID.yaml`                                         |
| `Metadata grid dimensions, resolution and origin must match its occupancy data.`                                                                               | `meta.yaml` differs from the PGM size or the grid YAML                                                            | Copy the values exactly                                                                           |
| `Occupancy image or threshold values are inconsistent.`                                                                                                        | The grid YAML `image` names another file, or `free_thresh` is not below `occupied_thresh`                         | Fix the name (no folder) or the thresholds                                                        |
| `map: unknown or missing fields.`                                                                                                                              | The grid YAML has an extra key such as `mode`, or lacks one                                                       | Use exactly the six keys                                                                          |
| `Use a P2/P5 PGM with at most 16 million pixels and maximum 255.`, `PGM pixel count does not match its dimensions.`                                            | Not an 8-bit PGM, too many pixels, or missing or extra bytes                                                      | Save an 8-bit P5 PGM                                                                              |
| `PLY must contain only point vertices, optional normals and RGB.`, `PLY requires XYZ and 1–2 million points.`                                                  | Faces, other elements or properties, an `obj_info` line, no x, y, z, or too many points                           | Export points only, with supported properties; downsample                                         |
| `PLY requires a bounded LF header.`, `PLY point data length is inconsistent.`                                                                                  | CRLF line endings, or point data that does not match the header                                                   | Export again with LF line endings                                                                 |
| `Use plain YAML data types.`, `Each YAML document must be a mapping.`, `Invalid YAML document.`                                                                | An unquoted date or time (for example in `created`), an empty file or a syntax error                              | Quote dates and times; fix the file                                                               |
| `KEY: number outside supported bounds.`                                                                                                                        | A value out of range, or a number read as text, such as `1e-6`                                                    | Use the ranges on this page; write `1.0e-6`                                                       |
| `KEY: unknown or missing fields.`                                                                                                                              | A misspelled or unsupported key, such as `rpy` in an edge or `footprint` in a costmap                             | Use only the keys on this page                                                                    |
| `KEY: unsupported value.`                                                                                                                                      | A fixed text value changed, `negate` other than 0 or 1, or an unknown `drive`                                     | Restore the value                                                                                 |
| `KEY: invalid text.`, `KEY: invalid list length.`                                                                                                              | A name with unsupported characters or not starting with a letter; a list with the wrong number of entries         | Use letters, digits, `_`, `.` and `-`; 3 entries for `xyz`, `origin` and velocities, 4 for `quat` |
| `Calibration edges require unique children and unit quaternions.`, `Calibration frames must not contain a cycle.`                                              | A frame is the child of two edges, a parent equals its child, `quat` is not unit length, or the edges form a loop | One edge per child, chained from `base_link`; normalize `quat`                                    |
| `Minimum depth must be below maximum depth.`, `Lost timeout must follow degraded timeout.`, `Obstacle height bounds are inverted.`                             | An inconsistent pair of values                                                                                    | Correct the pair                                                                                  |
| `Navigation metadata requires schema_version: 1.`, `Unknown navigation metadata field.`, `Metadata source.ply must be a filename, not a path.`                 | Wrong version, an unknown key or a folder in `meta.yaml`                                                          | Use the keys above; write file names only                                                         |
| `Read the current navigation SHA-256 before applying a map.`                                                                                                   | The SHA-256 is out of date                                                                                        | Run `sodero navigation get` again                                                                 |
| `Use the matching document extension, node ID, current SHA-256 and execute flag.`                                                                              | The CLI file name does not end in `.nav`                                                                          | Rename the file, for example to `site.nav`                                                        |
| `… the file name must end with .tar.gz or .tgz or .tar or .zip`                                                                                                | A `.nav` file name on the Station page                                                                            | Rename the file to `site.nav.tgz`                                                                 |
| `the localizer is running — stop it before replacing its bundle`                                                                                               | Upload on the Station page while the Localizer runs                                                               | Stop the Localizer                                                                                |

Two problems appear only when the Localizer starts, in its log (`sodero runtime logs sodero.localizer`): `camera_frame_id is required` when `extrinsics.yaml` has no `camera_frame_id`, and `no_extrinsics_edge` when no edge connects the camera node's `frame_id` to `base_link`.
