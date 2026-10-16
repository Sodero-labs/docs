# Modules

A **module** is a program packaged to run on the Station as a node. The built-in modules (gateways, controllers, navigation) come with Stellar X. You can install your own modules to add robot behaviors, task logic or custom device interfaces; they run next to the built-in ones and use the same interfaces.

______________________________________________________________________

## 1. The Modules Page

Click **Modules** in the left sidebar. The page lists the modules that the nodes of your system use.

Modules used in this system

| No. | Item                  | Description                                                                      |
| --- | --------------------- | -------------------------------------------------------------------------------- |
| 1   | **Add custom module** | Installs a module package from your PC ([Install a Module](#2-install-a-module)) |
| 2   | **TYPE**              | Gateway, Controller, Compound or Application                                     |
| 3   | **USED BY**           | How many nodes of the graph use the module                                       |

The **⋯** menu of a row offers **Module info** and, for your own modules, **Remove module**.

______________________________________________________________________

## 2. Install a Module

1. Click **Add custom module**.
1. Drop the package (`.tar.gz`) or click **Choose file**, then click **Add module**.

Installing a module package

- Uploading a package with the same name replaces the installed version. Nodes that use it keep their connections; stop and start them to run the new version.
- Built-in modules cannot be replaced.

### Add and Start the Module's Node

1. Click **Add node** and choose the type your module declares (for example **Application**). Your module appears in the list with the **CUSTOM** badge.
1. Connect its required ports, for example to a Strider's `mobile_base` or a Motion Studio's `manipulator`.
1. Right-click the node and choose **Start node**, or use **Start all nodes**.

If the module has its own web UI, a link with the module's name appears on its node card while it runs. Its logs are available in full in the inspector.

### Remove a Module

Stop and delete the nodes that use the module, then choose **Remove module** in the **⋯** menu of its row.

______________________________________________________________________

## 3. Package Format

A module package is a gzip-compressed tar archive with a `package.yaml` at its root:

```
my-module-1.0.0.tar.gz
├── package.yaml      # name, version, entry point, parameters
├── subsystem.yaml    # the node: its role and the ports it requires and provides
├── run.py            # your program (any executable)
└── ...               # your other files
```

| File             | Purpose                                                                                                                                         |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `package.yaml`   | The module's name (for example `customer.patrol`), version, the command that starts it and its parameters                                       |
| `subsystem.yaml` | The node the module creates: its role (`component`, `compound` or `application`) and its ports with their contracts                             |
| `run.py`         | Your program. It implements the node's lifecycle (initialize, start, stop) with the Stellar SDK and serves or calls the interfaces of its ports |

Limits: 64 MiB per package (128 MiB unpacked).

**Complete guide and examples.** The SSH workspace of Stellar X contains the full package guide and runnable examples, including a status module, a navigation-goal client and a custom input gateway. Run `sodero-help packages` and see `/opt/sodero/docs/examples/` ([SSH Workspace](https://docs.sodero.io/v2.0.0/ssh_workspace/overview/index.md)).

### Build and Install from the SSH Workspace

```
cp -R /opt/sodero/docs/examples/native-status /workspace/my-work/
cd /workspace/my-work/native-status
python3 run.py --self-test                     # offline check
chmod +x run.py
tar -czf ../status-module.tar.gz package.yaml subsystem.yaml run.py README.md
sodero packages upload ../status-module.tar.gz --execute
```

Then add its node on the Station page, or with `sodero topology add-node --kind package --package NAME --if-version N --execute`, and start it.

**Tip:** An AI coding agent can write, check, package and install a module for you through the SSH workspace. See [AI Coding Agents](https://docs.sodero.io/v2.0.0/ssh_workspace/ai_agents/index.md).
