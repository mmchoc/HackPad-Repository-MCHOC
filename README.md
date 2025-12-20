# SideDuck Macropad 

SideDuck is a 9 key macropad that utilizes KMK firmware and a keyboard matrix circuit. This macropad includes 2 SK6812 MINI-E LEDs as well as customizable LED features including a reactive ripple effect. 


It serves as an extension to my 60% keyboard providing my setup with individual arrow keys as well as a delete key 

## Features 

- 2 SK6812 MINI-E LEDs
- Breathe and Reactive LED feature
- Home Key as the Layer-Tap Key 
- 9 Keys

## CAD Model 

2-Piece case that fits together utilizing 4 M3 Bolts and heatset inserts. 

<img width="500" height="858" alt="Screenshot 2025-12-19 175734" src="https://github.com/user-attachments/assets/3d98de25-a427-4a63-a511-867ce5f1a663" />

The case model was made in Fusion360 

## PCB 
This is my PCB that utilizes a matrix circuit to reduce the amount of ports tied to each switch. Every switch organized in rows and columns with their respective diodes and connected to the XIAO RP2040 respectively. 



This is my Schematic 


<img width="500" height="664" alt="Screenshot 2025-12-19 174946" src="https://github.com/user-attachments/assets/53483391-e0dc-4123-932c-2cb46a1fab6b" />

This is my PCB 


<img width="500" height="682" alt="Screenshot 2025-12-19 175013" src="https://github.com/user-attachments/assets/bc6e9a4a-a098-4b61-a8ad-34d7ca0b9ffe" />

## Firmware Overview 
This macropad uses KMK firmware for everything 
- The home key acts as a Layer-Tap Key
- LED choices of Off, Reactive, and Breathe mode

## BOM:

- 9x Cherry MX Switches
- 9x Blank DSA Keycaps
- 4x M3x5x4 Heatset inserts
- 4x M3x16mm SHCS Bolts
- 9x 1N4148 DO-35 Diodes
- 2x SK6812 MINI-E LEDs
- 1x XIAO RP2040
- 1x Case (Two 3D printed parts) 
