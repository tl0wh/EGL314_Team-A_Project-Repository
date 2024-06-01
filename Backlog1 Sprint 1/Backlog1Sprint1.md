<h1 align="center">
  Backlog 1 Sprint 1
</h1>
<p align="center">

 <i align="center">Prepping Raspberry Pi , Open Sound Control & Creation of Grapgical User Interface </i>

 </p>

 ## Summary:
In this sprint of Backlog 1 , here anre the following tasks:


1.  Preparing Raspberry Pi
2.  Install OSC on Raspberry Pi
3.  Create a UI via tkinter
4.  Raspberry Pi to Raspberry Pi OSC Communication
5.  OSC Communication to GrandMA3 & Yamaha QL1
 


## Preppign Paspberry Pi:
Please follow the steps in the attached repository:
**[Huats Club - rpistarterkit](https://github.com/huats-club/rpistarterkit)**

<br>
After you are done setting up, Please follow these steps to create a Virtual Environment:
## Installing a virtual environment

1. To install **Python Virtualenv**

```
sudo apt install virtualenv python3-virtualenv -y
```

2. To create a new virtual environment

```
virtualenv -p /usr/bin/python3 <environment_name>
```
**Note** - the virtual environment will be a folder

3. To activate virtual environment

```
source <environment_folder>/bin/activate
```

4. To install a package

```
pip3 install python-osc
```

5. To deactivate environment

```
deactivate
```

## To copy virtual environment

1. Generate dependencies file

```
pip3 freeze > requirements.txt
```

This will generate a requirement file at the current working directory.

2. To install dependencies in new enviroment

```
source <environment_folder>/bin/activate
```

```
pip3 install -r ~/<directory>/requirements.txt
```
## References
1. Using and Copying virtual environment: Click [here](https://github.com/huats-club/mts_sensor_cookbook/blob/main/0.%20virtual_environment/venv.md).

## Installing Python-OSC on Raspberry Pi:
**Python-osc** is a Python library for sending and receiving **Open Sound Control (OSC)** messages. OSC is a protocol for communication among computers, sound synthesizers, and other multimedia devices that is widely used in the field of electronic music and multimedia applications.

Python-osc provides a convenient way to work with OSC in Python by offering functions and classes for creating OSC messages, handling OSC bundles (a collection of OSC messages), and establishing OSC communication between different devices or software applications. It supports both OSC over UDP (User Datagram Protocol) and OSC over TCP (Transmission Control Protocol) for network communication.

### To Install Python-OSC
**On Raspberry Pi**
```
pip3 install python-osc==1.8.1
```