# Credits and Usage

Robot Systems and Robot Worlds use credits while they are active. Credits belong to a workspace. This page explains what uses credits, how to read **Billing & Usage**, and what happens when credits run out.

---

## How Credits Work

- **Credits belong to a workspace.** Everything active in the workspace's projects uses its balance, whoever activated it, guests and AI agents included.
- **Each workspace has one plan.** Your workspace's plan sets how many credits the workspace receives, how many credits per hour each kind of use takes, and the workspace's limits. **Billing & Usage** shows them.
- **Credits renew every week or every month**, depending on the plan, on the workspace's own cycle. Unused plan credits expire at renewal; they do not roll over.
- **Extra credits from Sodero** can have their own end date. The credits that expire soonest are used first.

---

## What Uses Credits

A Robot System or Robot World uses credits by the hour **from the moment it is activated until it is deactivated**, whether or not anything runs in it and whether or not anyone uses it.

| What | Uses credits |
| :--- | :--- |
| An active Robot System or Robot World | From **Activate** to **Deactivate** |
| Each Theater viewer and each Studio session in **RTX Real-time** | While it is open. Each has its own cloud renderer. |
| The robot cameras of an active World | While the cameras are rendered |
| Views in **WebGPU** | WebGPU draws with your own computer's GPU, but your plan may still count WebGPU views |

**Billing & Usage** shows how many credits each of these uses on your workspace's plan.

!!! warning "**Stop is not Deactivate.** **Stop** ends what runs in a Robot System or Robot World but keeps it active, so it keeps using credits. Only **Deactivate**, or [Auto off](../../projects/activate_run/index.md#5-auto-off), ends the use."

Storage, AI agent tool calls and the Project VPN do not use credits; they count against your plan's [limits](#limits).

---

## The Billing & Usage Dialog

Open the workspace menu and choose **Billing & Usage**. Everyone in the workspace can open it. It shows the current workspace and updates while it is open. It calls a Robot System a *System*, a Robot World a *World*, and the time one of them is active a *run*.


The top line shows your workspace's plan and, next to **Renews**, the date of the next renewal. A red **Out of credits** badge appears when the balance is zero.

### Credits

| Row | Meaning |
| :--- | :--- |
| **credits left** | The workspace's balance: the plan credits and extra credits that are left |
| **Weekly credits** or **Monthly credits** | The credits the plan gives the workspace at each renewal |
| **Used this week** or **Used this month** | Credits used since the last renewal |
| **Used in total** | Credits used since the workspace was created |
| **Extra credits from Sodero** | The extra credits left, each with its end date. Shown only when there are some. |
| **Used beyond the balance** | Credits used after the balance reached zero, on plans that keep running. Shown only when there are some. |

Under the rows, a line gives your plan's rates: the credits per hour of a System, of a World and of each kind of renderer.

### Limits

Each meter compares what the workspace uses with what the plan allows. The bar turns yellow at 80 % and red when the limit is reached. At the limit, the action that would go over it is refused with a [message](#messages).

| Meter | What it counts |
| :--- | :--- |
| **Projects** | The workspace's projects. Projects in Trash do not count. |
| **Workspace storage** | Everything stored in the workspace's projects: files, saved versions and project libraries |
| **Project libraries** | The files in the libraries of the workspace's projects |
| **Your My Library** | Your personal **My Library**. It shows the same in every workspace; its limit comes from the plans of the workspaces you own. |
| **Systems and Worlds running at once** | The Robot Systems and Robot Worlds active right now in the workspace |

### AI Agents and Project VPN This Month

**AI agent (MCP) tool calls**, **Project VPN time** and **Project VPN data** count the workspace's use of [AI agents](../../connect/ai_agents/index.md) and of the [Project VPN](../../connect/project_vpn/index.md). They count per calendar month (UTC); the line under them gives the reset date. When a counter reaches its limit, agent tool calls are refused, or Project VPN connections end, until the reset.

### Recent Runs

The table lists the workspace's recent runs and renderers: Systems and Worlds from Activate to Deactivate, Theater viewers, Studio sessions and World camera renderers. Each row shows the name, kind and project, when it started, how long it lasted and the credits it used. A row with a green dot is still active and still using credits.

---

## When Credits Run Out

What happens at zero depends on your plan. On plans that stop at zero, the rates line ends with *When credits run out, runs stop and new runs can't start.*

| Plan | At zero credits |
| :--- | :--- |
| Stops at zero (most plans) | The **Out of credits** badge appears. What runs in the workspace's Robot Systems and Robot Worlds is stopped, and activating one fails with *This workspace has run out of credits. …* |
| Keeps running | Work goes on. Credits used beyond zero show as **Used beyond the balance** and are taken from the next credits the workspace receives. |

New plan credits arrive at the next renewal. There is no payment page in the portal: to change your workspace's plan or to add credits, contact Sodero.

---

## Save Credits

- **Deactivate when you are done.** A stopped Robot System or Robot World is still active and still uses credits.
- **Keep Auto off on.** A Robot System or Robot World that someone forgot then deactivates by itself.
- **Use WebGPU when you do not need RTX quality.** Each RTX viewer and each RTX Studio session has its own cloud renderer.
- **Check Recent runs.** Rows with a green dot are still using credits.

---

## Messages

| Message | What to do |
| :--- | :--- |
| *This workspace has run out of credits. …* | Wait for the next renewal, or contact Sodero to add credits. |
| *The PLAN plan runs at most N Systems and Worlds at once. …* | Deactivate a Robot System or Robot World, then activate the new one. Stopping it is not enough. |
| *The PLAN plan holds up to N projects in a workspace. …* | Move a project you no longer need to Trash, or contact Sodero. Also shown when you restore a project from Trash. |
| *Not enough workspace storage: …* or *Not enough room in …* | The upload does not fit. Delete files you no longer need, or contact Sodero. |
| *This workspace's plan doesn't include …* | The plan has no AI agent tool calls or no Project VPN. Contact Sodero. |
| *Limit reached: … for this month. It renews on DATE.* | The monthly allowance is used up until the date shown. |
