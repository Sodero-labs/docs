# StellarX Isaac Sim Extension Installation

You need a dedicated Isaac Sim extension to control robots with StellarX in the simulator.

## Download

Download StellarX_Extension from one of the following repositories and unzip it into a directory of your choice.

- link 1
- link 2
- link 3

## Extension Installation

### Dependency

Before starting, you have to install pyzmq, an open source messaging library. In the terminal, go to your installed Isaac Sim directory and enter following command.
> ./python.sh -m pip install pyzmq==27.1.0

This command will install the library inside of Isaac Sim python virtual environment. If pyzmq is successfully installed, you can proceed to next step.

### Installation

![main menu](images/isaacsim_extension_00.png){ width="1000" }  

1. When you open Isaac Sim, you'll see the above default main screen.  
&nbsp;

![window](images/isaacsim_extension_01_edit.png)  
![extensions](images/isaacsim_extension_02_edit.png)  
2. Click the 'Window' tab and select the 'Extensions' menu.
&nbsp;

![extensions window](images/isaacsim_extension_03_edit.png){ width="1000" }  
3. On the extensions window, click the button on the top-right and open the settings.
&nbsp;

![extensions settings](images/isaacsim_extension_04_edit.png){ width="1000" }  
![extensions settings](images/isaacsim_extension_05_edit.png){ width="1000" }  
4. On the settings page, scroll down and click the plus button.  
5. In the newly added row, double-click the blank box and enter the path to your downloaded extension.
&nbsp;

![extensions window](images/isaacsim_extension_06_edit.png){ width="1000" }  
6. Press Enter and go to the 'THIRD PARTY' tab. Expand the 'User' dropdown and you'll see that the new extension has been added.
&nbsp;

![extensions settings](images/isaacsim_extension_07_edit.png){ width="1000" }  
7. Select the extension and click the toggle button to enable the extension. You can turn on 'AUTOLOAD' to automatically enable the extension next time you re-open Isaac Sim.  
&nbsp;

And that's it! Your Isaac Sim is now prepared for StellarX. Follow [the next chapter](../robot_setup/index.md) to learn how to prepare a robot model.
&nbsp;
