# Compatibility

Sodero Cloud and Stellar X share the robot-system concepts and the document types. Each product runs its own release of Stellar Station, so their Store apps, menus, node names and accepted document versions can differ.

## Robot Documents and Apps

Use gateway and robot documents (`.gw`, `.sdd`, `.sddm`, `.sdda`) made for the Station release you work with, such as the documents in **Sodero Assets**. The Station refuses a document in two cases:

- **An older format.** The message says that the file *uses an obsolete format*, or names an *Obsolete robot file* or an *Obsolete gateway filename* ([Documents in an Obsolete Format](https://docs.sodero.io/sodero-cloud/v1.0.0/station/documents/#documents-with-old-node-names)).
- **A robot document without `runtime.yaml`.** Robot documents (`.sdd`, `.sddm`, `.sdda`) must contain a `runtime.yaml` that names their controller. Without it, the message says *The robot document has no runtime.yaml naming its controller.*

Documents exported from a current Stellar Designer meet both rules: export older documents again and upload the new file. Do not edit the files inside a document to make a Station accept it.

Install the apps that your nodes run from the Station's **Store** before you start the nodes ([Apps and Packages](https://docs.sodero.io/sodero-cloud/v1.0.0/station/apps/index.md)).

## Move Files Between Products

An `.sdr` file carries a Robot System between Sodero Cloud and Stellar X, without its installed packages. Check the destination's Station release and apps before you import it ([Move Robot Systems Between Stellar X and Sodero Cloud](https://docs.sodero.io/sodero-cloud/v1.0.0/projects/files/#move-robot-systems-between-stellar-x-and-sodero-cloud)).

The [Stellar X manual](https://docs.sodero.io/stellar-x/latest/) describes the Station on the controller. Use it for the concepts and the device steps; this manual's menus, such as **Store**, **Station · Edit**, **Go live** and **Station · Live**, apply to Sodero Cloud.

## Example Files

- The [Quick Start](https://docs.sodero.io/sodero-cloud/v1.0.0/get_started/quick_start/index.md) scene `jackal_warehouse.zip` contains a Clearpath Jackal and a Clearpath Dingo with their license notice. Keep the license file with the scene when you pass it on.
- The Quick Start's `jackal.gw` and `jackal.sddm` are the simulation gateway document and the mobile robot document of that Jackal, made for the Station release of Sodero Cloud.

## Browser and Rendering

Use an up-to-date desktop browser. **WebGPU** needs support from the browser, the operating system and the GPU; when it is not available on your device, use **RTX Real-time**, which renders in the cloud and streams the picture ([Choose Rendering Mode](https://docs.sodero.io/sodero-cloud/v1.0.0/projects/activate_run/#choose-rendering-mode)).

## External Tools

- **Project VPN:** install the Connector with the command for your operating system under **Install Connector** in the project's **Project VPN** panel, then sign in once with `sodero login` ([Project VPN](https://docs.sodero.io/sodero-cloud/v1.0.0/connect/project_vpn/index.md)).
- **AI agents:** connect them with the address and settings of the project's **AI agents** panel ([AI Agents](https://docs.sodero.io/sodero-cloud/v1.0.0/connect/ai_agents/index.md)).
