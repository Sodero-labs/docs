# Compatibility

Sodero Cloud and Stellar X share robot-system concepts and document types. Their deployed Station versions, installed apps and operator interfaces can differ.

## Before You Configure a Robot

1. Check that the required app is available in the current Station's **Store** and can be installed for this environment.
2. Use gateway and robot documents exported for that Station version. An app listing or an upload confirmation alone does not confirm that the controller is ready to operate.
3. After going live, check the selected documents, port connections and node states before issuing motion commands.
4. Open an operator UI only when the running app provides its link or **Open …** action. If unavailable, stop here and contact Sodero for supported packages and instructions.

The controller chapters describe their functions when these prerequisites are met. The Quick Start covers World creation and viewing; it does not require a controller UI.

## Move Files Between Products

An `.sdr` is a transfer container, not a guarantee of compatibility with every Station release. Check document format, node names, required apps and destination architecture before importing. Installed packages are not included in the file.

A Robot World's `.sdr` is for Sodero Cloud. For a Robot System, follow [Import an .sdr File](../../projects/files/index.md#2-import-an-sdr-file) and the destination product's documentation. Keep the original backup until the imported system has been checked.

Cloud instructions use **Store**, **Station · Edit**, **Go live** and **Station · Live**. A Stellar X manual for an earlier device release may use different menus and node names. Use it for the concepts and device-specific steps that match your installed version; do not copy old graph identifiers into Cloud unchanged.

## Example Scene and Robot Documents

The [Quick Start](../../get_started/quick_start/index.md) includes a warehouse scene and its accompanying license notice. A scene alone does not configure its robot controller.

Obtain compatible `.gw`, `.sdd`, `.sddm` or `.sdda` documents from the current product's supported asset collection or from Sodero. Keep required metadata and license notices intact. Do not edit an archive's internal files to force acceptance by a different Station version.

## Browser and Rendering

Use an up-to-date supported browser. **WebGPU** requires browser, operating-system and GPU support; a browser version number alone does not guarantee availability. **RTX Real-time** renders in the cloud and needs a working streaming connection. Check the rendering choices available on your device.

## External Tools

Install Project VPN only when the portal offers an installer for your operating system. Follow the prompts of that release. Connect AI agents using the endpoint and configuration shown in the project's **AI agents** panel.
