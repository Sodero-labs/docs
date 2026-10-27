# Load and Configure a Map

A **map bundle** (`.nav`) is one file that carries the map of one site together with the settings to localize and navigate in it. You upload it once to the **Localizer**; the **Navigator** uses the same bundle, and **Visual odometry** uses its camera calibration. This page loads a finished bundle, checks the values for the first run and starts the nodes.

| You want to                                           | Page                                                                                                  |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Load a finished bundle, such as the warehouse example | This page                                                                                             |
| Make a bundle for your own site                       | [Create a Map from Your Site](https://docs.sodero.io/stellar-x/v2.0.1/navigation/create_map/index.md) |
| Look up every file, key and message of the format     | [Map Bundle Format](https://docs.sodero.io/stellar-x/v2.0.1/navigation/map_bundle_format/index.md)    |

Stellar Station does not build maps on the robot; there is no SLAM. A bundle is made beforehand from a 3D model or a 3D scan of the site.

______________________________________________________________________

## 1. What You Need

- **The bundle file**, for example [warehouse.nav.tgz](https://docs.sodero.io/stellar-x/v2.0.1/navigation/simulation_tutorial/files/warehouse.nav.tgz) of [Navigate in Simulation](https://docs.sodero.io/stellar-x/v2.0.1/navigation/simulation_tutorial/index.md). The Station page accepts names ending in `.tgz`; the CLI needs a name ending in `.nav`. Both are the same gzip-compressed tar, so you can copy `site.nav.tgz` to `site.nav`.
- **A Localizer node** (`sodero.localizer`) and, to drive to goals, a **Navigator node** (`sodero.navigator`), connected as in [Localization and Navigation › Set Up Navigation](https://docs.sodero.io/stellar-x/v2.0.1/navigation/overview/#3-set-up-navigation).

The bundle contains five settings files and three map files:

| File                              | Contents                                                 | Read by                                |
| --------------------------------- | -------------------------------------------------------- | -------------------------------------- |
| `meta.yaml`                       | The map ID and a description of the grid                 | Localizer and Navigator                |
| `localizer.yaml`                  | Localizer settings, including the point-cloud file       | Localizer                              |
| `navigator.yaml`                  | Navigator settings: robot size, speeds, tolerances       | Navigator                              |
| `extrinsics.yaml`                 | Where the camera is mounted on the robot                 | Localizer and Visual odometry          |
| `initial_pose.yaml`               | The starting pose of the robot on the map                | Localizer                              |
| `map/MAP_ID.ply`, `.pgm`, `.yaml` | The 3D point cloud and the 2D occupancy grid of the site | Localizer; Navigator and the map views |

______________________________________________________________________

## 2. Upload the Bundle

The Localizer and the Navigator share one bundle, so one upload to the Localizer serves both.

### Station Page

1. Stop the Localizer and the nodes that use its bundle (Navigator, Visual odometry).
1. Select the Localizer node. In the inspector's **LOCALIZER** section, click **Upload .nav** and choose `site.nav.tgz`.
1. The section shows the file name, and **NAVIGATION SETTINGS** lists the settings of the bundle.

The page checks the archive's layout. The CLI preview below checks every rule of the format, so preview a bundle you built yourself with the CLI before you upload it on the page.

### sodero CLI

```
sodero runtime node stop sodero.navigator --execute
sodero runtime node stop sodero.localizer --execute
sodero navigation get --node sodero.localizer                                     # note "sha256"
sodero maps upload site.nav --node sodero.localizer --if-sha256 SHA256            # preview: checks the bundle
sodero maps upload site.nav --node sodero.localizer --if-sha256 SHA256 --execute  # attach it
sodero runtime node start sodero.localizer --execute
sodero runtime node start sodero.navigator --execute
```

- With Visual odometry, also stop `sodero.visual_odometry` before the upload, and start it again before the Localizer.
- The file name must end in `.nav`, and the file may be at most 64 MiB.
- The preview reports the first problem it finds ([Validation Errors](https://docs.sodero.io/stellar-x/v2.0.1/navigation/map_bundle_format/#validation-errors)) and changes nothing.
- After each upload or settings change, read the SHA-256 again before the next one.

Uploading a bundle replaces all of its settings, including changes saved on the Station page or with the CLI. Copy those changes into your files before you upload a new version.

______________________________________________________________________

## 3. Check the Values for the First Run

A bundle made for another robot needs your robot's values. Check these before the first run:

| Value           | Setting                                                                                                                    | Group in **NAVIGATION SETTINGS** |
| --------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| Robot size      | `robot_radius` of `local_costmap` and `global_costmap` (the same value in both)                                            | Navigator                        |
| Speeds          | `FollowPath.desired_linear_vel` (cruise speed), `FollowPath.max_angular_vel` (turn rate), `velocity_smoother.max_velocity` | Navigator                        |
| Camera mounting | `xyz` and `quat` of the edge from `base_link` to the camera; the height is measured **from the floor**                     | Camera calibration               |
| Camera frame    | `camera_frame_id`: the **frame id** in the camera node's **CAMERA SETTINGS**                                               | Camera calibration               |
| Start pose      | `x`, `y`, `yaw` of `base_link` on the map                                                                                  | Initial pose                     |

### Change Settings

After the upload, the settings in `localizer.yaml`, `navigator.yaml`, `extrinsics.yaml` and `initial_pose.yaml` can be changed without a new bundle:

- **Station page:** select the Localizer or the Navigator node. The inspector's **NAVIGATION SETTINGS** section groups the keys your files contain as Localizer, Navigator, Camera calibration and Initial pose.
- **CLI:** `sodero navigation get --node sodero.navigator`, edit the returned `config`, then `sodero navigation apply` with its SHA-256 (see [sodero CLI](https://docs.sodero.io/stellar-x/v2.0.1/ssh_workspace/sodero_cli/index.md)).

Stop the Localizer, the Navigator and Visual odometry before you save; the new values apply when the nodes start again. The map files, `meta.yaml` and `map.file` change only with a new bundle. Every key is described in [Map Bundle Format](https://docs.sodero.io/stellar-x/v2.0.1/navigation/map_bundle_format/#files).

______________________________________________________________________

## 4. Start and Set the Initial Pose

1. Start the nodes in this order: the gateway and Strider, the camera gateway (and Visual odometry), the Localizer, the Navigator.
1. Open Strider's **Navigation** page (the **Strider** link on the Navigator's card). **Localization Status** shows **Healthy** once the camera view matches the map.
1. If the status stays **Initializing** or **Lost**, or the robot appears at the wrong place, click **Set Initial Pose**, press on the map where the robot stands and drag in the direction it faces ([Strider › Set the Initial Pose](https://docs.sodero.io/stellar-x/v2.0.1/controllers/strider/#set-the-initial-pose)).

The Localizer starts from the bundle's initial pose when it has no confirmed pose on this map. Once it has localized, it restarts from its last confirmed pose on the same `map_id`. A pose set with **Set Initial Pose**, or with the `localization.set_initial_pose` tool, replaces both. Give a changed map a new `map_id` so that an old pose is not reused.

Before you drive a real robot on a new map, check in simulation that the status reaches **Healthy** and that the robot reaches a nearby goal.

______________________________________________________________________

## 5. Troubleshooting

| Symptom or message                                                            | Cause and fix                                                                                                                                                                                        |
| ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *… the file name must end with .tar.gz or .tgz or .tar or .zip*               | A `.nav` file name on the Station page. Rename the file to `site.nav.tgz`.                                                                                                                           |
| *the localizer is running — stop it before replacing its bundle*              | Stop the Localizer, then upload again.                                                                                                                                                               |
| *Read the current navigation SHA-256 before applying a map.*                  | The SHA-256 is out of date. Run `sodero navigation get` again.                                                                                                                                       |
| The status stays **Initializing**                                             | The camera height in the extrinsics is not measured from the floor, `camera_frame_id` differs from the camera's **frame id**, or the initial pose is far off. Fix the value or set the initial pose. |
| The Localizer log shows `camera_frame_id is required` or `no_extrinsics_edge` | `extrinsics.yaml` has no `camera_frame_id`, or no edge connects the camera's **frame id** to `base_link`.                                                                                            |
| Other messages of the upload                                                  | See [Map Bundle Format › Validation Errors](https://docs.sodero.io/stellar-x/v2.0.1/navigation/map_bundle_format/#validation-errors).                                                                |
