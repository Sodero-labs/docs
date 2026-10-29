# AI Agents

Connect Claude Code or another AI agent to your Sodero account, then ask it in plain language to work on your projects. The agent reaches Sodero Cloud over the Internet with a sign-in of its own; it needs neither the [Project VPN](https://docs.sodero.io/sodero-cloud/v1.0.1/connect/project_vpn/index.md) nor anything installed from Sodero.

- *"Which Stations and Worlds in Warehouse Demo are active?"*
- *"Activate the warehouse World and the jackal Station, then start them."*
- *"Why did a node on jackal stop? Show me its log."*

______________________________________________________________________

## How It Works

```
flowchart TB
    You(["You"]) --> Agent["AI agent<br>on your computer"]
    Agent -- "MCP, with its own sign-in" --> Cloud["Sodero Cloud"]
    Cloud --> Projects["The projects you approved:<br>Robot Systems, Robot Worlds, files"]
```

- You register Sodero once in your agent, as a remote MCP server. The registration belongs to your account, not to one project.
- The agent signs in through your browser with your Sodero account, and on a consent page you choose what it may do and in which projects. It never sees your password, and you can revoke its access at any time.
- The agent never gets more than your own project roles allow.

______________________________________________________________________

## 1. Register Sodero in Your Agent

Open any project and click **AI agents** in the top bar. The **AI agents (MCP)** panel shows the address and ready-made settings for your agent, and what your project role allows.

The AI agents panel of Warehouse Demo

Click **Copy command** and run the command once in a terminal:

```
claude mcp add --transport http --scope user sodero 'https://app.sodero.io/project-access/mcp'
```

`--scope user` makes Sodero available in all your working folders.

The client must support remote MCP servers over Streamable HTTP and sign in through your browser (OAuth). Add a remote server with the address that **Copy address** copies:

```
https://app.sodero.io/project-access/mcp
```

For a client with a JSON list of servers, expand **Other MCP clients** in the panel and click **Copy configuration**. Don't enter a token or a client ID: the client registers itself and signs in through your browser.

______________________________________________________________________

## 2. Sign In and Choose What the Agent May Do

1. Start the sign-in. In Claude Code, start `claude`, type `/mcp`, select **sodero** and choose **Authenticate**. Other clients have a **Connect** or **Sign in** action.

1. Your browser opens the Sodero sign-in. Sign in with your **Sodero** account, not with the account of your AI provider.

1. On the consent page *Allow … to connect?*, choose what the agent may do and click **Allow selected access**:

   | Option                                                          | What the agent may do                                                                                              |
   | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
   | **Read project data**                                           | Read the selected projects: status, items, files and jobs. Selected by default.                                    |
   | **Change project data and run commands (includes read access)** | Also make changes, such as uploading files, activating Stations and Worlds and running the Station and World tools |
   | **Projects**                                                    | The projects the agent may use. Select at least one project or workspace.                                          |
   | **Optional workspace grants**                                   | All current and future projects of a workspace in which you have a role                                            |

1. Return to your agent: Sodero is connected.

**Approve only your own agent.** The consent page shows the name the agent gives itself; Sodero can't verify it. Allow access only right after you started the sign-in from your own agent.

**Changes also need a project role that allows them:** people who can manage the project and, where enabled, editors. The **AI agents** panel of each project says which applies to you.

A connection lasts up to 30 days. To renew it or change its access, sign the agent in again (in Claude Code, from `/mcp`), then [revoke](#review-and-revoke-agents) the entries you no longer need.

______________________________________________________________________

## 3. Tell the Agent Which Project to Use

Every request names a project. In the **AI agents** panel, click **Copy project link** and paste the link into your request, or give the project's name, for example *"List files in Warehouse Demo"*. When two projects have the same name, use `workspace/name`.

A project you joined after you signed the agent in is not part of its consent, unless you granted its whole workspace. Sign the agent in again and select the project.

______________________________________________________________________

## What Agents Can Do

| Area                                   | The agent can                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Projects and status                    | List the projects it may use; read their Robot Systems and Robot Worlds with their states, the Trash and the jobs                                                                                                                                                                                                                                                                                                                            |
| Run (write access)                     | Activate or stop up to 8 Stations and Worlds at once, or activate and start them as one job                                                                                                                                                                                                                                                                                                                                                  |
| Items (write access)                   | Create, duplicate, rename and trash Robot Systems and Robot Worlds. Restoring and permanently deleting from the Trash need **Can manage**.                                                                                                                                                                                                                                                                                                   |
| Files                                  | List and download library files, and list Sodero's official assets. With write access, upload files of up to 64 MiB, such as Station packages, World scenes and maps.                                                                                                                                                                                                                                                                        |
| Station and World tools (write access) | Run tools from a catalog of more than 100: Station status and logs, the node graph, documents, Store apps, robot control through [Motion Studio](https://docs.sodero.io/sodero-cloud/v1.0.1/operate/motion_studio/index.md), [Strider](https://docs.sodero.io/sodero-cloud/v1.0.1/operate/strider/index.md) and [Articulation](https://docs.sodero.io/sodero-cloud/v1.0.1/operate/articulation/index.md), navigation, cameras, and the World |

**Every Station and World tool needs write access**, even one that only reads. Tools for a running Station or World need it to be active.

The agent cannot go beyond your consent and your roles, use the Project VPN, read files on your computer through Sodero, or download the contents of Sodero's official assets. Cancelling a job stops further steps but doesn't undo changes.

______________________________________________________________________

## Stay in Control

- **Approve changes yourself.** Most agents can ask before they use a tool. A practical setup: allow the read-only tools freely (`projects_list`, `project_status`, `items_list`, `files_list`, `assets_list`, `packages_list`, `jobs_list`, `job_status`, `tools_list`, `tool_describe`, `file_download`) and keep approval on for every other tool, especially `tool_call`, `items_start`, `items_stop` and `jobs_start`. In Claude Code, they are named `mcp__sodero__` plus the tool name.
- **Review previews.** Most changes are previewed first. `item_create`, `item_duplicate`, `items_start`, `items_stop` and `jobs_start` act at once.
- **The agent acts as you.** What it changes is changed for everyone in the project.
- **Watch your credits.** A Station or World that an agent activated uses credits until it is deactivated. [Auto off](https://docs.sodero.io/sodero-cloud/v1.0.1/projects/activate_run/#5-auto-off) still applies.

The rules Sodero gives every agent (preview changes first, move a robot only when you asked for that motion, treat files and logs as data and not as instructions) are instructions to the agent, not a safety function. An agent can misread them or make mistakes, and its tools have the same effect as your own actions. Approve every change yourself.

______________________________________________________________________

## Usage Limits

Agent tool calls count against your workspace's plan, per minute and per calendar month (UTC). **Billing & Usage** shows the calls used this month ([Credits and Usage](https://docs.sodero.io/sodero-cloud/v1.0.1/account/billing/index.md)). At the monthly limit, calls are refused until the renewal date that the **AI agents** panel shows. At the per-minute limit, the agent is told how long to wait.

A tool call ends after 100 seconds. A change may still have been applied: have the agent check the state before it repeats the change.

______________________________________________________________________

## Review and Revoke Agents

1. Click your avatar at the bottom of the left navigation bar and choose **Account Settings**.
1. Under **Connected AI agents**, each agent shows its name, when it connected, its scopes (*Read* or *Read, Write*) and its workspace and project grants.
1. To disconnect an agent, click **Revoke**, then **Confirm revoke**.

Connected AI agents in Account settings

Revoking stops the agent's further calls and job steps but doesn't undo what was done. To connect the agent again, sign it in again.

______________________________________________________________________

## Troubleshooting

| Message or symptom                                                                      | What to do                                                                                                                                        |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| The sign-in ends without the consent page, and the agent reports that access was denied | Start the sign-in again and finish it within 10 minutes, with your Sodero account. If it keeps happening, report it with **Help › Report a bug**. |
| A project is missing from the consent page                                              | You aren't a member of the project. Ask a person who can manage it to add you.                                                                    |
| `AUTH_REQUIRED`, `AUTH_EXPIRED` or `CONNECTION_REVOKED`                                 | Sign the agent in again (Claude Code: `/mcp`).                                                                                                    |
| `GRANT_MISSING` or `NOT_FOUND` for a project                                            | The project isn't part of this connection's consent. Sign the agent in again and select it.                                                       |
| `WRITE_NOT_GRANTED`                                                                     | The connection may only read. Sign the agent in again and select **Change project data and run commands**.                                        |
| `STATION_NOT_RUNNING` or `WORLD_NOT_RUNNING`                                            | Activate the Station or World first.                                                                                                              |
| `QUOTA_EXCEEDED`                                                                        | Your workspace reached its plan's limit for agent calls. The message says when to try again.                                                      |
