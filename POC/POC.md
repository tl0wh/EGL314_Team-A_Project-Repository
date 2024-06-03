<h1 align="center">
  Proof Of Concept 
</h1>
<p align="center">

 <i align="center">Proof Of Concept for The BlindFold Challenge ( Team A ) </i>
</p>

# System Flowchart
```mermaid
graph TD
A[Raspberry Pi A ]--LAN/WiFi + OSC--> L[Master Laptop]
L[Master Laptop] --Running--> B[Reaper<br>DAW]
L--Running--> C[MA3<br> Lighting Console]
C --LAN SACN--> D[Hanging Lights<br>Ayrton Mistral , Magicblade , Minipanel<br> Showline ePar]
B[Reaper<br>DAW] --ASIO , LAN DanteVSC--> E[L-ISA Processor]
E--MetaData--> F[L-ISA Controller]
F --LAN Dante--> G[Mixer<br>Yamaha QL1]
G--LAN Dante--> H[Amplifier<br> Yamaha XMV8140D]
H -- Speaker Cable to 4 Way Terminal Block--> I[Speakers<br> Yamaha VXS5]
K[MIDI Controller<br>Korg Nano Controller]--MiniUSB to USB A <br> & MIDI-->J[Raspberry Pi B]
J[Raspberry Pi B]--OSC-->F[L-ISA Controller] 
```



