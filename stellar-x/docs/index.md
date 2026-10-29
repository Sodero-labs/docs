---
comments: false
show_intro: true
---



# Stellar X Documentation
<p>Set up the Stellar X controller, build your robot system in Stellar Station and operate robots in simulation and on real hardware.</p>

### Get Started
<div class="box-container">
  <a href="get_started/quick_start" class="card-box">
    <img src="https://unpkg.com/lucide-static@0.577.0/icons/rocket.svg" class="external-icon" alt="Icon">
    <h4>Quick Start</h4>
    <p>Build your first robot system on Stellar X and drive a simulated robot in about 15 minutes.</p>
  </a>
  <a href="tutorials/learning_path" class="card-box">
    <img src="https://unpkg.com/lucide-static@0.577.0/icons/route.svg" class="external-icon" alt="Icon">
    <h4>Learning Path</h4>
    <p>The tutorials in order: first connection, a simulated robot, navigation, then real motors.</p>
  </a>
  <a href="hardware_setup/stellar_series/stellar_x" class="card-box">
    <img src="https://unpkg.com/lucide-static@0.577.0/icons/cpu.svg" class="external-icon" alt="Icon">
    <h4>Hardware & Network</h4>
    <p>Power, network connection and stop controls of the Stellar X controller.</p>
  </a>
</div>

### Build the System
<div class="box-container">
  <a href="station/overview" class="card-box">
    <img src="https://unpkg.com/lucide-static@0.577.0/icons/layout-dashboard.svg" class="external-icon" alt="Icon">
    <h4>Stellar Station</h4>
    <p>Build the robot system as a graph of nodes, load design documents, run nodes and follow their logs.</p>
  </a>
  <a href="tutorials/stellar_designer/introduction" class="card-box">
    <img src="https://unpkg.com/lucide-static@0.577.0/icons/boxes.svg" class="external-icon" alt="Icon">
    <h4>Stellar Designer</h4>
    <p>Describe your robot and its gateway: kinematics, limits, safety and actuator mapping.</p>
  </a>
  <a href="gateways/overview" class="card-box">
    <img src="https://unpkg.com/lucide-static@0.577.0/icons/cable.svg" class="external-icon" alt="Icon">
    <h4>Gateways & Sensors</h4>
    <p>Connect EtherCAT drives, simulated robots, cameras and IMUs, and test actuators.</p>
  </a>
</div>

### Simulate and Operate
<div class="box-container">
  <a href="virtual_simulation/introduction" class="card-box">
    <img src="https://unpkg.com/lucide-static@0.577.0/icons/square-mouse-pointer.svg" class="external-icon" alt="Icon">
    <h4>Simulation</h4>
    <p>Drive robots in NVIDIA Isaac Sim with the same controllers and controller documents as the real robot.</p>
  </a>
  <a href="controllers/strider" class="card-box">
    <img src="https://unpkg.com/lucide-static@0.577.0/icons/gamepad-2.svg" class="external-icon" alt="Icon">
    <h4>Operate Robots</h4>
    <p>Jog mobile bases, manipulators and articulated robots with Strider, Motion Studio and Articulation.</p>
  </a>
  <a href="navigation/overview" class="card-box">
    <img src="https://unpkg.com/lucide-static@0.577.0/icons/map.svg" class="external-icon" alt="Icon">
    <h4>Localization & Navigation</h4>
    <p>Localize the robot on a map with its camera and drive it to goals around obstacles.</p>
  </a>
</div>

### Extend & Automate
<div class="box-container">
  <a href="ssh_workspace/overview" class="card-box">
    <img src="https://unpkg.com/lucide-static@0.577.0/icons/square-terminal.svg" class="external-icon" alt="Icon">
    <h4>SSH Workspace</h4>
    <p>A Linux workspace on the controller with the sodero command-line tool.</p>
  </a>
  <a href="ssh_workspace/ai_agents" class="card-box">
    <img src="https://unpkg.com/lucide-static@0.577.0/icons/bot.svg" class="external-icon" alt="Icon">
    <h4>AI Coding Agents</h4>
    <p>Let an AI coding agent inspect and configure the robot system, with your approval for each change.</p>
  </a>
  <a href="extend/custom_modules" class="card-box">
    <img src="https://unpkg.com/lucide-static@0.577.0/icons/puzzle.svg" class="external-icon" alt="Icon">
    <h4>Create Custom Modules</h4>
    <p>Add your own applications and devices to the Station as nodes.</p>
  </a>
</div>

### Reference & Support
<div class="box-container">
  <a href="https://www.sodero.io/contact" class="card-box">
    <img src="https://unpkg.com/lucide-static@0.577.0/icons/headset.svg" class="external-icon" alt="Icon">
    <h4>Contact Support</h4>
    <p>Reach out directly to our robotics engineering team for technical assistance or product inquiries.</p>
  </a>
  <a href="CHANGELOG" class="card-box">
    <img src="https://unpkg.com/lucide-static@0.577.0/icons/clock.svg" class="external-icon" alt="Icon">
    <h4>ChangeLog</h4>
    <p>Release notes and documentation revisions, including changes to the example files.</p>
  </a>
  <a href="https://github.com/Sodero-labs/docs/discussions" class="card-box">
    <img src="https://unpkg.com/lucide-static@0.577.0/icons/github.svg" class="external-icon" alt="Icon">
    <h4>GitHub Discussions</h4>
    <p>Join the global Sodero community to ask questions, share technical insights, and discuss ideas.</p>
  </a>
</div>

<style>

.md-sidebar--secondary {
  visibility: hidden;
}

.box-container {
  display: flex;
  gap: 10px;
  margin-bottom: 30px;
  flex-wrap: wrap;
}

.card-box {
  flex: 1 1 0px;
  width: 0;
  padding: 12px 12px;
  border: 1px solid #333;
  border-bottom: 1px solid #333 !important; 
  border-radius: 6px;
  text-decoration: none !important;
  color: inherit !important;
  background-color: transparent;
  box-shadow: none !important;
}

.external-icon {
  width: 18px;
  height: 18px;
  margin-bottom: 0;
  filter: invert(100%) sepia(4%) saturate(151%) hue-rotate(174deg) brightness(101%) contrast(92%);
}

.card-box:hover {
    border-color: #f1f2f3;     
    border-bottom: 1px solid #f1f2f3 !important; 
}

.card-box h4 {
  padding: 0;
  margin: 0;
  padding-bottom: 0px;
  margin-bottom: 0px;
  line-height: 1.2;
}

.card-box p {
  padding: 0;
  margin: 0;
  padding-bottom: 0px;
  margin-bottom: 20px;
  font-size: 14px;
  color: #b4bac0;
}

</style>