<h1 align="center">
  Proof Of Concept 
</h1>

<p align="center">

 <i align="center">Proof Of Concept for The BlindFold Challenge ( Team A ) </i>
</p>

# System Flowchart
```mermaid
graph TD
A[Raspberry Pi A ]<--LAN/WiFi + OSC--> L[Master Laptop]
L[Master Laptop] --Running--> B[Reaper<br>DAW]
L--Running--> C[MA3<br> Lighting Console]
C --LAN SACN--> D[Hanging Lights<br>Ayrton Mistral , Magicblade , Minipanel<br> Showline ePar]
B[Reaper<br>DAW] --ASIO , LAN DanteVSC --> E[L-ISA Processor]
E--MetaData--> F[L-ISA Controller]
F --LAN Dante--> G[Mixer<br>Yamaha QL1]
G--LAN Dante--> H[Amplifier<br> Yamaha XMV8140D]
H -- Speaker Cable to 4 Way Terminal Block--> I[Speakers<br> Yamaha VXS5]
K[MIDI Controller<br>Korg Nano Controller]--MiniUSB to USB A <br> & MIDI-->J[Raspberry Pi B]
J[Raspberry Pi B]--OSC-->F[L-ISA Controller] 
```
## Asset Files:
There will be the Following Files ; Lighting MA3(.show)<br> SoundScape  L-ISA Controller(.lisa)<br>Dightal Audio Workstation Reaper(.rpp) ShowFiles<br> Located in Asset_Files in [POC](./Asset_Files/)

### Required Software:
- [Reaper DAW](https://www.reaper.fm/download.php)
- [grandMA3 on PC](https://www.malighting.com/downloads/products/grandma3/) (If you have a console , this is optional)
- [L-ISA Controller](https://www.l-acoustics.com/products/l-isa-studio/)
- L-ISA Processor (Installed with L-ISA Controller)
- [Dante Virtual Soundcard](https://my.audinate.com/support/downloads/dante-virtual-soundcard)
- [Dante Controller](https://my.audinate.com/support/downloads/dante-controller)
- [LoopMIDI](https://www.tobias-erichsen.de/software/loopmidi.html)(Needed to Link Reaper Timecode into L-ISA)

# Configuration

## Linking MIDI From Reaper to L-ISA Controller:
1. Launch LoopMIDI
2. Rename your New Profile(Yellow)
3. Click + (Green)
4. Appears Saved (Blue)
<img src="./diagrams/Loopmidi.png" >

## Reaper Side
1. Launch Reaper
2. `Control + P` to go Preferences
3. Navigate to MIDI
4. Under  , Enable Output for your LoopMidi Profile
<img src="./diagrams/rpmidi.png" >
5. Select the Timecode Track in the MasterFile
6. Navigate to the Fader at the `bottom` Corresponding to your source.
<img src="./diagrams/fader.png" >
7. Click the button Circled in Green
<img src="./diagrams/routing.png" >
8. Navigate to `MIDI Output Device`
9. Select the MIDI Profile you have just created in `LoopMIDI`

## L-ISA Side
1. Open L-ISA Controller
2. Navigate to Settings at the Top Right
<img src="./diagrams/settings.png" >
3. Go To MIDI Tab
<img src="./diagrams/MIDITab.png" >
4. Click MTC For your saved MIDI Profile
5. Head Back to Reaper and Press Play
6. Timecode at the top right will change away from 00:00:00:00
<img src="./diagrams/moving.png" >

## -Timecode Configuration is Now Complete-

