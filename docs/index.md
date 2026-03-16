---
comments: false
show_intro: true
---



# Sodero Documents
<p> get an overview of sedero's products features, intergrations, and how to use them. </p>

### Getting Started
<div class="box-container">
  <a href="get_started/sodero_ecosystem" class="card-box">
    <img src="https://unpkg.com/lucide-static@latest/icons/chart-column.svg" class="external-icon" alt="Icon">
    <h4>Sodero EcoSystem</h4>
    <p>Explore the core SDR architecture and the seamless workflow from design to real-world execution.</p>
  </a>
  <!-- <a href="/docs/" class="card-box">
    <img src="https://unpkg.com/lucide-static@latest/icons/download.svg" class="external-icon" alt="Icon">
    <h4>Download Docker Image</h4>
    <p>Download our free Docker image containing our software optimized exclusively for Isaac Sim integration.</p>
  </a> -->
  <a href="hardware_setup/stellar_series/stellar_x" class="card-box">
    <img src="https://unpkg.com/lucide-static@latest/icons/cpu.svg" class="external-icon" alt="Icon">
    <h4>Hardware Setup</h4>
    <p>Step-by-step guide for power connection, network configuration, and initial setup of the physical robotics controller.</p>
  </a>
</div>


### Learn & Tutorials
<div class="box-container">
  <a href="tutorials/stellar_designer/introduction" class="card-box">
    <img src="https://unpkg.com/lucide-static@latest/icons/boxes.svg" class="external-icon" alt="Icon">
    <h4>Stellar Designer</h4>
    <p>Design your own robot. Intuitively define kinematics, links, and joint settings.</p>
  </a>
  <a href="tutorials/stellar_designer/robot_structure" class="card-box">
    <img src="https://unpkg.com/lucide-static@latest/icons/network.svg" class="external-icon" alt="Icon">
    <h4 >Stellar Motion Studio</h4>
    <p> Create robot poses and safely test precise motion trajectories using our intuitive interface.</p>
  </a>
  <a href="tutorials/stellar_designer/introduction" class="card-box">
    <img src="https://unpkg.com/lucide-static@latest/icons/rocket.svg" class="external-icon" alt="Icon">
    <h4>Starting Tutorial</h4>
    <p>A beginner-friendly guide covering the complete workflow from robot configuration to physical deployment.</p>
  </a>
</div>

### Development & Extention
<div class="box-container">
  <a href="manual/apis" class="card-box">
    <img src="https://unpkg.com/lucide-static@latest/icons/braces.svg" class="external-icon" alt="Icon">
    <h4>API Reference</h4>
    <p>A comprehensive dictionary of the Sodero API, providing detailed parameter information.</p>
  </a>
  <a href="manual/remote_control/understanding_remote_control" class="card-box">
    <img src="https://unpkg.com/lucide-static@latest/icons/radio.svg" class="external-icon" alt="Icon">
    <h4>Remote Control</h4>
    <p>Seamless external integration for Sodero hardware using language-agnostic RPCs.</p>
  </a>
  <a href="tutorials/simulation/introduction" class="card-box">
    <img src="https://unpkg.com/lucide-static@latest/icons/square-mouse-pointer.svg" class="external-icon" alt="Icon">
    <h4>NVIDIA Isaac Sim</h4>
    <p>Guide to integrating NVIDIA Isaac Sim and synchronizing Sim-to-Real environments for seamless execution.</p>
  </a>
</div>

### Development & Extention
<div class="box-container">
  <a href="https://www.sodero.io" class="card-box">
    <img src="https://unpkg.com/lucide-static@latest/icons/headset.svg" class="external-icon" alt="Icon">
    <h4>Contact Support</h4>
    <p>Reach out directly to our robotics engineering team for technical assistance or product inquiries.</p>
  </a>
  <a href="CHANGELOG" class="card-box">
    <img src="https://unpkg.com/lucide-static@latest/icons/clock.svg" class="external-icon" alt="Icon">
    <h4>ChangeLog</h4>
    <p> Detailed release notes on new features, bug fixes, and updates across the Sodero platform.</p>
  </a>
  <a href="https://github.com/Sodero-labs/docs/discussions" class="card-box">
    <img src="https://unpkg.com/lucide-static@latest/icons/github.svg" class="external-icon" alt="Icon">
    <h4>Github Discussions</h4>
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