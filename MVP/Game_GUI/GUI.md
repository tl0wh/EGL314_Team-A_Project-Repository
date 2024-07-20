<h1 align="center">
  Minimum Viable Product 
</h1>

<p align="center">

 <i align="center">Minimum Viable Product Presentation for The BlindFold Challenge ( Team A ) </i>
</p>

<h2 align="center">
  Operational Guide for GUIs in Game
</h2>
In this game , there will be <u><b>2</b> GUIs.</u><br>
<b>Note that: 1 Laptop has to be deployed for Each GUI</b>
<h3>1. Master GUI for Operational Team <br></h3>
<img src="../diagrams/Master_GUI.png" > <br>
<h3>2. GUI for Participant<br></h3>
<img src="../diagrams/PlayerGUI_Start.png" > <br>
<img src="../diagrams/pgui_main.png" > <br>
<img src="../diagrams/pgui_end.png" > <br>

## Breaking Down Operational GUI:
<img src="../diagrams/Master_GUI_Annotated.png">

### This is the Master GUI.<br> Each button will be tied to 2 different functions;<br> 1 to fire sequences in MA3<br> 1 to fire Audio in Reaper
## Components
### - In the <u>Red</u>
<img src="../diagrams/Mgui-red.png"></img>
- `Murugan Light`<br>
-Bring Guests to our Station
- `Intro` <br>
-Voiced Over Game Introduction
- `Outro` <br> 
-Voice Over Concluding Station

### - In the <u>Blue</u>
<img src="../diagrams/Mgui_blue.png"></img>
- `Demo Stage`<br>
-Demonstration Level of Game
- `Map`<br>
 -Level 1 Easy Stage of Game
- `Lvl2`<br>
 -Level 2 Hard Stage of Game

### - In the <u>Green</u>
<img src="../diagrams/Mgui_green.png"></img>
- `Lose`<br>
-Fired when Ninja 1 <b>Loses</b>

- `Clear`<br>
-Fired when Ninja 1 <b>Advances</b>


- `Sequence 32`<br>
-Spare Function

### - In the <u>Yellow</u>
<img src="../diagrams/Mgui_yellow.png"></img>
- `Go`<br>
-Go to <b>Next Cue</b> in MA3

- `Off Sequence`<br>
-Off All<b> Active Running Sequences</b> in MA3

- `Off Everything`<br>
-Off All<b> Active Running Sequences</b> in MA3<br>
-Stops <b>Audio Playback</b> in Reaper

- `Clear`<br>
-Clear All <b>Running Presets</b> in MA3


- `Play/Pause`<br>
-Toggle <b>Audio Playback</b> in Reaper

## --Breakdown of Operational GUI is Now Complete--
<br>
<br>

## Breaking Down Participant GUI:
### This is Participant GUI<br> They Can Fire the Intro & Start the Easy Level from This GUI<br><br>Each button is also tied to 2 different functions;<br> 1 to fire sequences in MA3<br> 1 to fire Audio in Reaper
## Components:

### - In the Start Page
<img src = "../diagrams/PlayerGUI_Start.png"></img>
- `Start`<br>
-Starts Introduction 

### - In the Main Page
<img src = "../diagrams/pgui_main.png"></img>
- `Replay`<br>
-Replays Introduction
- `Start The Game!`<br>
-Starts Level 1 Easy Stage of Game

### - In the Ending Page
<img src = "../diagrams/pgui_end.png"></img>



