# sodero CLI

`sodero` is the command-line tool of the SSH workspace. It performs the operations of the Station page (adding nodes, connecting ports, loading settings and maps, starting nodes, calling robot tools) and prints every result as JSON, so both people and scripts or AI agents can use it.

The CLI is its own best reference:

| Command                                            | What it gives                                                |
| -------------------------------------------------- | ------------------------------------------------------------ |
| `sodero --help`                                    | All command groups                                           |
| `sodero GROUP ACTION --help`                       | Every option of one command, with defaults                   |
| `sodero capabilities`                              | The full command list, exit codes and limits as JSON         |
| `sodero tools list` / `sodero tools describe TOOL` | The robot tools of the running nodes and their input schemas |
| `sodero-help` / `sodero-help NAME`                 | The workspace guides, for example `sodero-help navigation`   |

______________________________________________________________________

## Conventions

- **JSON output.** Each command prints one JSON result on stdout. Pipe it through `python3 -m json.tool` to read it comfortably. A failure prints one JSON error on stderr: `{"error": {"code": ..., "message": ..., "details": ...}}`.
- **Preview first.** A command that changes something only previews until you add `--execute`. Read the preview, then repeat the command with `--execute`.
- **Versions.** Changes to the node graph take `--if-version N`, the `expected_version` from `sodero topology get`. Changes to settings and documents take `--if-sha256 SHA256` from the matching `get`. Each saved change returns the next value. If someone changed the Station page in the meantime, the change is refused with a conflict (exit code 6): read again and retry.
- **One Station.** On a robot, the only item is the Station `station`. `--item` defaults to it and can be left out.
- **Node IDs.** Nodes are named `rc.<kind>.<name>`, for example `rc.actuator_gateway.jackal`, `rc.mobile_controller_manager.jackal`, `rc.camera_gateway.cam0`. The localizer, navigator and visual odometry have fixed IDs: `rc.localizer`, `rc.navigator`, `rc.visual_odometry`.

### Exit Codes

| Code | Meaning                      | What to do                                            |
| ---- | ---------------------------- | ----------------------------------------------------- |
| 0    | Success                      | For an accepted change, check the returned state      |
| 1    | Other failure                | Read `error.message` and fix the cause                |
| 2    | Invalid arguments            | Check `--help`                                        |
| 3    | Authentication or permission | Reconnect; ask the robot's operator                   |
| 4    | Service unavailable          | Check the state before you repeat a change            |
| 5    | Timeout                      | Check the state; run the printed resume command       |
| 6    | Conflict                     | Read the current version or SHA-256 again, then retry |
| 7    | Busy                         | Retry after a pause                                   |
| 8    | Limit exceeded               | Reduce the size or count                              |

______________________________________________________________________

## Command Map

| Group                    | Actions                                                                        | Use                                                                        |
| ------------------------ | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| `project`                | `status`                                                                       | Station and workspace information                                          |
| `runtime`                | `status`, `logs`, `start`, `stop`, `node start`, `node stop`                   | Which nodes run, their logs; start and stop nodes                          |
| `topology`               | `catalog`, `get`, `add-node`, `connect`, `disconnect`, `remove-node`, `import` | Edit the node graph                                                        |
| `tools`                  | `list`, `describe`, `call`                                                     | Robot tools: Strider, Motion Studio, navigation, localization, documents…  |
| `navigation`             | `list`, `get`, `apply`                                                         | Settings of the camera, visual odometry, localizer and navigator           |
| `maps`                   | `upload`, `attach`                                                             | Attach `.nav` map bundles to the localizer and navigator                   |
| `locomotion`, `policies` | `list`, `get`, `apply`; `upload`                                               | Legged locomotion and IMU settings; your own ONNX walking policy           |
| `articulations`          | `get`, `configure`, `upload`                                                   | Joints and actuators of Articulation nodes                                 |
| `packages`               | `list`, `upload`, `remove`                                                     | Your own modules                                                           |
| `apps`                   | `start`, `stop`, `status`, `logs`, `call`                                      | Nodes of your own modules                                                  |
| `watch`, `camera`        | `watch`; `camera snapshot`                                                     | Sample readings for a few seconds; save a camera picture                   |
| `files`                  | `upload`                                                                       | Stage a file on the robot for `documents.apply` (kept for at most 6 hours) |
| `run`, `programs`        | `run`; `programs list`, `programs logs`                                        | Run a program in the workspace and keep its output                         |

Worlds, project items, the project Library and the official asset catalog belong to the Sodero cloud. On a robot these commands answer `NOT_AVAILABLE_ON_DEVICE`.

______________________________________________________________________

## Recipes

### Status and Logs

```
sodero runtime status                                    # every node: configured, running, its state
sodero runtime logs rc.actuator_gateway.jackal --lines 100
sodero tools call strider.get_state --input '{"target":"rc.mobile_controller_manager.jackal"}'
```

### Start and Stop Nodes

```
sodero runtime node start rc.actuator_gateway.jackal --execute          # gateway first
sodero runtime node start rc.mobile_controller_manager.jackal --execute # then its controller
sodero runtime node stop rc.mobile_controller_manager.jackal --execute
```

`sodero runtime start --execute --wait` starts every saved node, like **Start all nodes** on the Station page.

**Start all** includes nodes that drive real hardware. Start nodes one by one when the graph contains hardware you do not want to run.

### Edit the Node Graph

Every graph change needs the current version. Read it, preview, then execute:

```
sodero topology get                                       # note "expected_version", e.g. 12
sodero topology add-node --kind camera --name cam0 --if-version 12              # preview
sodero topology add-node --kind camera --name cam0 --if-version 12 --execute    # returns version 13
sodero topology connect --source rc.localizer.camera \
    --target rc.camera_gateway.cam0.camera --if-version 13 --execute
```

`sodero topology catalog` lists the node kinds (`gateway`, `strider`, `motion_studio`, `articulation`, `camera`, `imu`, `vo`, `localizer`, `navigator`, `legged_locomotion`, `legged_navigator`, `package`) with their ports. The Station must be stopped while you edit its graph, as on the Station page.

### Change Settings of Official Nodes

```
sodero navigation list
sodero navigation get --node rc.navigator > navigator.json   # the editable config and its sha256
# save the "config" part to config.json and change the values you need, then:
sodero navigation apply --node rc.navigator --config @config.json --if-sha256 SHA256            # preview
sodero navigation apply --node rc.navigator --config @config.json --if-sha256 SHA256 --execute
```

Stop the node first; the new settings apply when it starts again. These are the same settings the Station page shows in the node's inspector.

### Attach a Map

```
sodero navigation get --node rc.localizer            # its sha256
sodero maps upload /workspace/maps/warehouse.nav --node rc.localizer --if-sha256 SHA256 --execute
```

The localizer and the navigator share one map bundle, so one upload serves both. Stop both nodes first. See [Localization and Navigation](https://docs.sodero.io/v2.0.0/navigation/overview/index.md).

### Modules (Your Own Programs)

```
sodero packages upload /workspace/my-work/patrol.tar.gz --execute
sodero topology add-node --kind package --package patrol --if-version N --execute
sodero apps start NODE --execute
sodero apps logs NODE --lines 100
```

See [Modules](https://docs.sodero.io/v2.0.0/station/modules/index.md) for the package format.

### Robot Tools

```
sodero tools list                                        # tools of the running nodes, with their targets
sodero tools describe localization.set_initial_pose      # input schema
sodero tools call localization.set_initial_pose --input '{"x": -1.6, "y": 2.4, "yaw": 0.0}'            # preview
sodero tools call localization.set_initial_pose --input '{"x": -1.6, "y": 2.4, "yaw": 0.0}' --execute
```

A tool that changes something or moves the robot acts only with `--execute`. Strider and Motion Studio tools need the exact `target` (from `tools list`) when the Station has more than one robot of that kind, for example `{"mode": "TWIST", "target": "rc.mobile_controller_manager.jackal"}` for `strider.set_mode`.

### Readings and Pictures

```
sodero watch --probe rc.mobile_controller_manager.jackal --hz 5 --seconds 5
sodero camera snapshot rc.camera_gateway.cam0 --output frame.png
```
