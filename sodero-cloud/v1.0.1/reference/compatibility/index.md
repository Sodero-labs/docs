# Compatibility

Sodero Cloud and Stellar X share the robot-system concepts and the document types. Each product runs its own release of Stellar Station, so their Store apps, menus, node names and accepted document versions can differ.

## Robot Documents and Apps

- Use gateway and robot documents (`.gw`, `.sdd`, `.sddm`, `.sdda`) made for the Station release you work with, such as the documents in **Sodero Assets**. Documents with old node names are refused: export them again from a current Stellar Designer ([Documents with Old Node Names](https://docs.sodero.io/sodero-cloud/v1.0.1/station/documents/#documents-with-old-node-names)).
- Do not edit the files inside a document to make a Station accept it. Export it again, or ask Sodero for a document of the current format.
- Install the apps that your nodes run from the Station's **Store** before you start the nodes ([Apps and Packages](https://docs.sodero.io/sodero-cloud/v1.0.1/station/apps/index.md)).

## Move Files Between Products

An `.sdr` file carries a Robot System between Sodero Cloud and Stellar X. It holds the graph, the documents and the settings, but not the installed packages. Before you import one, check that the destination runs a Station release that accepts its node names and documents, and that the apps its nodes need are available there. Keep the original file until the imported system works ([Move Robot Systems Between Stellar X and Sodero Cloud](https://docs.sodero.io/sodero-cloud/v1.0.1/projects/files/#move-robot-systems-between-stellar-x-and-sodero-cloud)).

A Robot World's `.sdr` opens in Sodero Cloud only.

The [Stellar X manual](https://docs.sodero.io/stellar-x/latest/) describes the Station on the controller. Use it for the concepts and the device steps; this manual's menus, such as **Store**, **Station · Edit**, **Go live** and **Station · Live**, apply to Sodero Cloud.

## Example Scene

The [Quick Start](https://docs.sodero.io/sodero-cloud/v1.0.1/get_started/quick_start/index.md) scene `jackal_warehouse.zip` contains a Clearpath Jackal and a Clearpath Dingo with their license notice. Keep the license file with the scene when you pass it on.

## Browser and Rendering

Use an up-to-date desktop browser. **WebGPU** needs support from the browser, the operating system and the GPU; when it is not available on your device, use **RTX Real-time**, which renders in the cloud and streams the picture ([Choose Rendering Mode](https://docs.sodero.io/sodero-cloud/v1.0.1/projects/activate_run/#choose-rendering-mode)).

## External Tools

- **Project VPN:** install the Sodero VPN toolkit with the command that the **Project VPN** panel shows for your operating system ([Project VPN](https://docs.sodero.io/sodero-cloud/v1.0.1/connect/project_vpn/index.md)).
- **AI agents:** connect them with the address and settings of the project's **AI agents** panel ([AI Agents](https://docs.sodero.io/sodero-cloud/v1.0.1/connect/ai_agents/index.md)).
