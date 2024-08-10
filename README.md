<h1 align="center">
  Project S.O.N.I.C - The Blindfold Challenge
</h1>
<h1 align="center">
  <img src="./asset/nyp.png" width = 350px height=170px>
</h1>

<p align="center">
  <i align="center">Train to be a ninja with the use of modern technologies</i>
</p>

<h2 align = "center">
  A Project By:<br>
  <a href="https://github.com/tl0wh"><img src="https://avatars.githubusercontent.com/u/169418560?v=4" title="tl0wh" width="40" height="40"></a>
  <a href="https://github.com/AhSohs"><img src="https://avatars.githubusercontent.com/u/167286697?v=4" title="AhSohs" width="40" height="40"></a>
  <a href="https://github.com/srylqwerty"><img src="https://avatars.githubusercontent.com/u/167286875?v=4" title="srylqwerty" width="40" height="40"></a>
  <a href="https://github.com/dariensiew"><img src="https://avatars.githubusercontent.com/u/167286885?v=4" title="dariensiew" width="40" height="40"></a>

</h2>


<p align="center">
  <a href="https://github.com/tl0wh/EGL314_Team-A_Project-Repository/commits/main"><img src="https://img.shields.io/github/last-commit/tl0wh/EGL314_Team-A_Project-Repository.svg?style=for-the-badge"/></a>
</p>

## Overview
Project S.O.N.I.C (Sensory Observation Ninja Immersive Challenge) is an experiential/exploratory initiative designed to blend the ancient "ninja training techniques" with modern technologies. Students are to design a range of interactive stations that simulate ninja training scenarios, designed to test and enhance your listening abilities, reaction times and strategic thinking. The stations include:
1. Stealth Walking
2. **The Blindfold Challenge** (Team A)
3. Art Of Hearing
4. Reaction Training
5. Memory Sequence
6. Graduation Sequence
<p>
  In this repository, the focus will be strictly on Station 2 - The Blindfold Challenge.
</p>

## Station 2 - The Blindfold Challenge
The “Blindfold Challenge”, where your vision takes a 
backseat and your ears take the lead<br>
Participants are blindfolded and must navigate 
through a course guided solely by sounds.<br>
Participants must avoid contacting obstacles 
placed throughout the course for a successful 
attempt.<br>

One Person  Blindfolded , 'Ninja Cadet'<br>
One Person on MIDI Controller guiding  , 'Trainer'<br>



## Technical Summary

<ul>
  <li>L-Acoustics' L-ISA to provide auditory cues for navigation.</li>
  <li>GrandMA3 Incoporated Lighting as the 'Maze' , Walking through the shadows of the light</li>
  <li>Multi Participant Game. One Blindfolded, the other guiding via a Korg NanoKontrol2 MIDi Controller</li>
</ul>


# System Flowchart
```mermaid
graph TD
A[Raspberry Pi A ]<--LAN/WiFi + OSC--> L[Master Laptop]
L[Master Laptop] --Running--> B[Reaper<br>DAW]
L--Running--> C[MA3<br> Lighting Console]
C --LAN SACN--> D[Hanging Lights<br>Ayrton Mistral , Magicblade , Minipanel<br> Showline ePar]
B[Reaper<br>DAW] <--ASIO , LAN DanteVSC --> E[L-ISA Processor]
E<--Spatial MetaData--> F[L-ISA Controller]
F <--LAN Dante--> G[Mixer<br>Yamaha QL1]
G<--LAN Dante--> H[Amplifier<br> Yamaha XMV8140D]
H -- Speaker Cable to 4 Way EuroBlock Terminal Block--> I[Speakers<br> Yamaha VXS5]
K[MIDI Controller<br>Korg Nano Controller]--MiniUSB to USB A <br> & MIDI-->J[Raspberry Pi B]
J[Raspberry Pi B]<--OSC-->F[L-ISA Controller] 
```

## Asset Files:
There will be the Following Files ; Lighting MA3(.show)<br> SoundScape  L-ISA Controller(.lisa)<br>Dightal Audio Workstation Reaper(.rpp) ShowFiles<br> Finalised files are located in Asset_Files in [Final](./Final_Presentation/Asset_Files/)

### Required Software:
- [Reaper DAW](https://www.reaper.fm/download.php)
- [grandMA3 on PC](https://www.malighting.com/downloads/products/grandma3/) (If you have a console , this is optional)
- [L-ISA Controller](https://www.l-acoustics.com/products/l-isa-studio/)
- L-ISA Processor (Installed with L-ISA Controller)
- [Dante Virtual Soundcard](https://my.audinate.com/support/downloads/dante-virtual-soundcard)
- [Dante Controller](https://my.audinate.com/support/downloads/dante-controller)
- [LoopMIDI](https://www.tobias-erichsen.de/software/loopmidi.html)(Needed to Link Reaper Timecode into L-ISA)



## Tutorials:
- **[Backlog 1 Sprint 1](./Backlog%201%20Sprint%201/Backlog1Sprint1.md)** - OSC Installation on Raspberry Pi, Creation of a UI via tkinter, OSC Communication to various devices

- **[Backlog 2 Sprint 1](./Backlog%202%20Sprint%201/Backlog2Sprint1.md)** - OSC Reaper Combined. GUI For Control

- **[Backlog 2 Sprint 2](./Backlog2Sprint2/Backlog2Sprint2.md)** - OSC Reaper & MA3 Combined. GUI For Control

- **[POC](./POC/POC.md)** - Proof Of Concept , Initial Presentation of a Working Gameplay

- **[MVP](./MVP/MVP.md)** - Minimum Viable Project , Refined Gameplay + Introduction of Laser Modules & NeoPixel

- **[Final Presentation](./Final_Presentation/Final.md)** - Final Presentation for Overall Project with Enhanced Quality of Life changes,Code Changes, Added NeoPixel, Reduced Lasers 




## References and Sources:
- **[Huats Club - rpistarterkit](https://github.com/huats-club/rpistarterkit)** - Configuring and preparing a new Raspberry Pi
- **[Huats Club - oscstarterkit](https://github.com/huats-club/oscstarterkit)** - Introductions to Python Open Sound Control for AV
- **[Huats Club - mts_sensor_cookbook](https://github.com/huats-club/mts_sensor_cookbook)** - Basics for Sensors, MIDI Controller.

### Credits
Team A Would like to specially thank, **Mr. Fu YongWei** from **Nanyang Polytechnic** for overseeing our project phase and supplying us with base-source codes.