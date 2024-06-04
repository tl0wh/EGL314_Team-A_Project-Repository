# Tutorial_for_MA3_Control_via_Python_OSC
Here we are trying to control "GrandMA3" via "Python OSC" to fire the Lighting Sequences for our game

The resources in this tutorial are tested with the following hardware
1. Computer running **grandMA3 onPC (Version)** and **Reaper**
2. **grandMA3 onPC CommandWing**
3. **Raspberry Pi4 with python OSC**

## System Flowchart
```mermaid
graph LR
A[Raspberry Pi] <--LAN--> B[Router]
B <--LAN--> C[grandMA3 on PC<br>use this IP Address(1)]
B <--LAN--> C[Reaper on PC<br> use this IP Address(2)]
```
## Configuration guide for grandMA3 onPC

Please refer to the **setup guide** for instructions specific to configuring **OSC control** on the **grandMA3 onPC software**.

[setupguide_link](./GrandMA3_OSC_setupguide.pdf)


## OSC Support on grandMA3
For more instruction in **OSC for grandMA3**, please refer to this [link](https://help2.malighting.com/Page/grandMA3/remote_inputs_osc/en/1.8).


## Configuration (Reaper)

1. Go to **Reaper Preference** using the shortcut `Ctrl+P`
2. Navigate to **Control/OSC/Web** (green box)
3. Click on `Add` to configure a new OSC device 

![alt text](diagram/reaper_preference.png)

*Reaper Preference Windows*

4. Configure new **OSC Device** as shown in the picture below

![alt text](diagram/reaper_osc_device.png)




## Installation / Operation
In this example, we will be using a **Raspberry Pi** to control **grandMA3 on PC**. and **Reaper**.

1. Create a file directory (in this example we will call the folder `team_ctrl`)
```
mkdir team_ctrl
```

2. Copy the respective python file into the folder `~/grandma`
```
guiPage1.py
guiPage2.py
guiPage3.py

```

3. Edit the **IP Address(1) and Port Number(1)** (`line 18 and 19`) of the **computer** running **grandMA3 on PC** in `guiPage3.py`
```
LAPTOP_IP = "192.168.0.100"		# send to laptop w grandMA3
PORT = 8000                     # laptop w grandMA3 port number
```

 4. Edit the **IP Address(1)**I of the **Laptop (running Reaper)**in the respective python files

 - Multiple Lines of `guiPage2.py`
```
PI_A_ADDR = "10.10.10.10"
```



## Identifying OSC Commands in Reaper

2 weeks ago

L-ISA documentation
In this tutorial, we are using the *Action List* in **Reaper**. In Reaper, the *Action List* is a comprehensive catalogue of commands and functions that you can execute within the softwaer. It covers basic features such as playback controls to complex scripting operations. 
2 weeks ago

added reaper

To view *Action List* navigate to `Actions -> Show action list...`

Look out for `Command ID` (right click to unhide)

![alt text](diagram/reaper_action_list.png)

*Reaper Action List*



5. Execute `guiPage1.py`. If the file is executed successfully, The Stored Sequence on the MA will Go.
```
python3 guiPage1.py
```