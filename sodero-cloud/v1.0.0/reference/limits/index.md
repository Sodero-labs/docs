# Limits and Defaults

This page collects the fixed limits and the defaults you can meet in Sodero Cloud, each with the page that explains it. Your workspace's plan sets further limits, such as storage and how many Robot Systems and Robot Worlds can be active at once: **Billing & Usage** shows them ([Set by Your Plan](#set-by-your-plan)).

______________________________________________________________________

## Names

| What                                             | Limit                                                                                                                                                            | More                                                                                                          |
| ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Workspace name                                   | Up to 30 characters                                                                                                                                              | [Workspaces and People](https://docs.sodero.io/sodero-cloud/v1.0.0/account/workspaces/index.md)               |
| Project name and description                     | Name up to 20 characters, description up to 40                                                                                                                   | [Projects](https://docs.sodero.io/sodero-cloud/v1.0.0/projects/projects/#2-create-a-project)                  |
| Robot System or Robot World name and description | File name up to 20 characters, description up to 40                                                                                                              | [Robot Systems and Robot Worlds](https://docs.sodero.io/sodero-cloud/v1.0.0/projects/files/#1-create-a-file)  |
| Node name in a Station                           | Up to 60 characters; 20 for an empty draft such as **Empty gateway**. Letters, digits, `_`, `.` and `-`, starting with a letter or digit. Unique in the Station. | [Build the Graph](https://docs.sodero.io/sodero-cloud/v1.0.0/station/graph/#name-the-node)                    |
| Robot name of a simulation gateway               | Exactly the robot's articulation prim name in the World: up to 64 characters, letters, digits and `_`, not starting with a digit. Unique in the World.           | [Connect to the World](https://docs.sodero.io/sodero-cloud/v1.0.0/station/world_connection/#2-name-the-robot) |
| Password                                         | At least 8 characters                                                                                                                                            | [Sign In and Account](https://docs.sodero.io/sodero-cloud/v1.0.0/account/sign_in/index.md)                    |

______________________________________________________________________

## Projects, Files and Runs

| What                                    | Limit or default                                                                                                                                                | More                                                                                                                                            |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Active Robot Worlds per project         | 1                                                                                                                                                               | [Robot Systems and Robot Worlds](https://docs.sodero.io/sodero-cloud/v1.0.0/projects/files/#4-how-robot-worlds-and-robot-systems-work-together) |
| Active Robot Systems per project        | Any number, within your plan's limit of **Systems and Worlds running at once**                                                                                  | [Billing and Usage](https://docs.sodero.io/sodero-cloud/v1.0.0/account/billing/#limits)                                                         |
| Auto off                                | Deactivates an active Robot System or Robot World after 30 minutes without users (the default). On by default.                                                  | [Auto Off](https://docs.sodero.io/sodero-cloud/v1.0.0/projects/activate_run/#5-auto-off)                                                        |
| Files in one **Actions** selection      | Any number of Robot Systems, at most one Robot World                                                                                                            | [Several Files at Once](https://docs.sodero.io/sodero-cloud/v1.0.0/projects/activate_run/#4-several-files-at-once)                              |
| Nodes after **Activate** or **Go live** | No node starts by itself                                                                                                                                        | [Start and Monitor Nodes](https://docs.sodero.io/sodero-cloud/v1.0.0/station/run/index.md)                                                      |
| Station resources                       | Each Station gets its own share of CPU and memory from Sodero Cloud. **Resources** in the Station and the **Resource** column of the project page show its use. | [Stellar Station](https://docs.sodero.io/sodero-cloud/v1.0.0/station/overview/#4-resources)                                                     |
| Node logs in the Station                | The last 200 lines of each stream                                                                                                                               | [Logs and Activity](https://docs.sodero.io/sodero-cloud/v1.0.0/station/run/#5-logs-and-activity)                                                |

______________________________________________________________________

## Files and Uploads

| What                           | Limit                                                                                                      | More                                                                                    |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| A file in a library            | Up to 2 GiB                                                                                                | [Libraries](https://docs.sodero.io/sodero-cloud/v1.0.0/projects/libraries/#2-add-files) |
| An upload in Studio            | Up to 1 GiB per file                                                                                       | [Studio](https://docs.sodero.io/sodero-cloud/v1.0.0/worlds/studio/index.md)             |
| A file uploaded by an AI agent | Up to 1 GiB for a library file; up to 64 MiB for any other upload, such as a Station document or a package | [AI Agents](https://docs.sodero.io/sodero-cloud/v1.0.0/connect/ai_agents/#usage-limits) |

______________________________________________________________________

## Sharing and Connections

| What                               | Limit                                              | More                                                                                                  |
| ---------------------------------- | -------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Project or workspace invitation    | Valid for 7 days                                   | [Share and Collaborate](https://docs.sodero.io/sodero-cloud/v1.0.0/projects/sharing/#1-invite-people) |
| Project VPN connections            | 3 open connections per person, across all projects | [Project VPN](https://docs.sodero.io/sodero-cloud/v1.0.0/connect/project_vpn/#limits)                 |
| Length of a Project VPN connection | At most 8 hours                                    | [Project VPN](https://docs.sodero.io/sodero-cloud/v1.0.0/connect/project_vpn/#limits)                 |
| AI agent connection                | Up to 30 days, then sign the agent in again        | [AI Agents](https://docs.sodero.io/sodero-cloud/v1.0.0/connect/ai_agents/#usage-limits)               |
| AI agent tool call                 | Ends after 100 seconds                             | [AI Agents](https://docs.sodero.io/sodero-cloud/v1.0.0/connect/ai_agents/#usage-limits)               |

______________________________________________________________________

## Set by Your Plan

Your workspace's plan sets these limits. **Billing & Usage**, in the workspace menu, shows each one with what the workspace uses ([Billing and Usage](https://docs.sodero.io/sodero-cloud/v1.0.0/account/billing/index.md)):

- credits, their hourly rates and when they renew;
- **Projects** in the workspace;
- **Workspace storage** and **Project libraries**;
- **Systems and Worlds running at once**;
- **AI agent (MCP) tool calls**, **Project VPN time** and **Project VPN data** per calendar month;
- AI agent tool calls per minute, when the plan limits them (*Agents can make up to N tool calls per minute.*).

Plans differ, so this manual gives no values for them. To change the plan or add credits, contact Sodero.
