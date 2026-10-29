# SSH Workspace

Stellar X includes a development workspace that you reach over SSH. It runs on the controller itself, next to Stellar Station but separated from real-time control. It still shares the controller's memory and storage, so avoid very large builds while the robot is moving.

From the workspace you can:

- inspect and change the Station with the `sodero` command-line tool: nodes, connections, design documents, settings, maps and packages;
- read the status and logs of every node, as the Station page shows them, and call robot tools such as Strider, Motion Studio and navigation;
- write and test your own programs and install them on the Station as modules;
- let an AI coding agent do all of the above for you (see [AI Coding Agents](../ai_agents/index.md)).

!!! info "The workspace performs the same operations as the Station page: a node added with `sodero topology add-node` is the same node you would add with **Add node**."

---

## 1. Register Your SSH Key

The workspace accepts SSH keys only; there is no password sign-in. Register the public key of every computer that should connect, in the **SSH ACCESS** card of the robot's Network Settings page (`http://ROBOT_ADDRESS:3000`): copy the key command for your operating system, run it on your computer, paste the line it prints and click **Add key**. The steps and the commands are in [Network Settings › SSH Access](../../hardware_setup/stellar_series/network_settings/index.md#2-ssh-access).

To revoke a computer's access, click the trash icon next to its key on the same page.

---

## 2. Connect

The **SSH workspace** card on the Network Settings page shows the command with a **Copy** button:

```sh
ssh -p 2222 sodero@192.168.60.18
```

Replace the address with your robot's address. The user name is always `sodero` and the port is always `2222`.

!!! idea "**Tip:** Save a host alias"
    Add this to `~/.ssh/config` on your computer, so that `ssh stellar-x` is enough:

    ```text
    Host stellar-x
        HostName 192.168.60.18
        Port 2222
        User sodero
    ```

Check where you are before you change anything:

```sh
sodero project status
sodero runtime status
```

Stellar X has a single Station, with the ID `station`. Every command uses it by default, so you never need `--item`.

---

## 3. What Is in the Workspace

| Path | Contents |
| :--- | :--- |
| `/workspace` | Your files. They stay on the robot across restarts and software updates. |
| `/workspace/README.md` | The workspace guide: terms, a five-minute start and the guide map |
| `/workspace/AGENTS.md` | Operating rules for AI coding agents ([AI Coding Agents](../ai_agents/index.md)) |
| `/opt/sodero/docs/` | All workspace guides and examples, read-only. Also linked as `/workspace/docs`. |

| Tool | Purpose |
| :--- | :--- |
| `sodero` | Station command-line tool ([sodero CLI](../sodero_cli/index.md)) |
| `sodero-help` | Prints the guides: `sodero-help` lists them, `sodero-help navigation` opens one |
| Python 3.12 | With numpy, PyYAML, requests, aiohttp and onnxruntime |
| `git`, `gcc`, `make`, `scp`, `sftp` | Standard development tools |

!!! info "The robot's workspace has **no Internet access**. Copy the dependencies your code needs from your computer (for example as wheel files) with `scp`."

---

## 4. Copy Files

Use `scp` or any SFTP client with the same address, user and port:

```sh
# Once: create a folder for your work on the robot
ssh -p 2222 sodero@192.168.60.18 mkdir -p /workspace/my-work

# From your computer to the robot
scp -P 2222 my_robot.gw sodero@192.168.60.18:/workspace/my-work/

# From the robot to your computer
scp -P 2222 sodero@192.168.60.18:/workspace/my-work/result.json .
```

---

## 5. Use VS Code

VS Code's **Remote - SSH** extension connects with the same command.

1. In VS Code settings, set `remote.SSH.localServerDownload` to `always`. The robot has no Internet access, so VS Code copies its server from your computer.
2. Run **Remote-SSH: Add New SSH Host...** from the Command Palette and enter `ssh -p 2222 sodero@192.168.60.18`.
3. Run **Remote-SSH: Connect to Host...**, choose the robot's address and open the folder `/workspace`.

The first connection copies the VS Code server (about 230 MB) and takes a minute or two. Later connections take seconds.

---

## 6. Rules of the Road

- **Preview first.** A `sodero` command that changes something only previews until you add `--execute`. Read the preview, then repeat the command with `--execute`.
- **The robot is real equipment.** A command with `--execute` can start nodes or move the robot. Run it only when the surroundings are clear and someone who can stop the robot is present.
- **Stop a node before you change it.** The Station refuses changes to a running node. Stop it, apply the change, start it again.

Where to go next:

| Task | Where |
| :--- | :--- |
| Command reference and examples | [sodero CLI](../sodero_cli/index.md) |
| Let an AI agent work on the robot | [AI Coding Agents](../ai_agents/index.md) |
| Load a whole design document (`.gw`, `.sdd`, `.sddm`, `.sdda`) | Station page: [Design Documents](../../station/design_documents/index.md) |
| Write your own module | [Create Custom Modules](../../extend/custom_modules/index.md) |
