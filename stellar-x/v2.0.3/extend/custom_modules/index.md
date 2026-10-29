# Create Custom Modules

A module is your own program packaged to run on the Station as a node, next to the built-in gateways and controllers. This page describes the package and how to build and install one from the [SSH workspace](https://docs.sodero.io/stellar-x/v2.0.3/ssh_workspace/overview/index.md). To install a finished package from your PC and manage installed modules, see [Modules](https://docs.sodero.io/stellar-x/v2.0.3/station/modules/index.md).

______________________________________________________________________

## 1. Package Format

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
| `subsystem.yaml` | The node the module creates: its role (`gateway`, `component`, `compound` or `app`) and its ports with their contracts                          |
| `run.py`         | Your program. It implements the node's lifecycle (initialize, start, stop) with the Station SDK and serves or calls the interfaces of its ports |

Limits: 64 MiB per package (128 MiB unpacked).

**Complete guide and examples.** The SSH workspace of Stellar X contains the full package guide and runnable examples, including a status module, a navigation-goal client and a custom input gateway. Run `sodero-help packages` and see `/opt/sodero/docs/examples/` ([SSH Workspace](https://docs.sodero.io/stellar-x/v2.0.3/ssh_workspace/overview/index.md)).

______________________________________________________________________

## 2. Build and Install from the SSH Workspace

The Station SDK is not installed in the SSH workspace. Import it only in the code that runs on the Station, and give your program an offline `--self-test` to check it in the workspace, as the example does.

```
mkdir -p /workspace/my-work
cp -R /opt/sodero/docs/examples/native-status /workspace/my-work/
cd /workspace/my-work/native-status
python3 run.py --self-test                     # offline check
chmod +x run.py
tar -czf ../status-module.tar.gz package.yaml subsystem.yaml run.py README.md
sodero packages upload ../status-module.tar.gz --execute
```

Then add its node on the Station page ([Modules › Add and Start the Module's Node](https://docs.sodero.io/stellar-x/v2.0.3/station/modules/#add-and-start-the-modules-node)), or with `sodero topology add-node --kind package --package NAME --if-version N --execute`, and start it. `NAME` is the `name` in `package.yaml`; `N` is the graph version that `sodero topology get` returns ([sodero CLI](https://docs.sodero.io/stellar-x/v2.0.3/ssh_workspace/sodero_cli/index.md)).

**Tip:** An AI coding agent can write, check, package and install a module for you through the SSH workspace. See [AI Coding Agents](https://docs.sodero.io/stellar-x/v2.0.3/ssh_workspace/ai_agents/index.md).
