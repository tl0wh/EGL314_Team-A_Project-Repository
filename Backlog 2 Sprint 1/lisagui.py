# Huats 2023 oscstarterkit
# This python script demonstrate controlling Reaper (Jump to Marker 1) using a Raspberry Pi through the
# OSC messaging protocol
from pythonosc import udp_client

import tkinter as tk 
import subprocess


def send_message(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

		# Send an OSC message to the receiver
		client.send_message(address, message)

		print("Message sent successfully.")
	except:
		print("Message not sent")

# FOR INFO: IP address and port of the receiving Raspberry Pi
PI_A_ADDR = "192.168.254.162"		# wlan ip
PORT = 8000




main = tk.Tk()
var = 0


def function1():
    addr = "/action/40161" # Jump to Marker One
    msg = float(1) # Trigger TRUE Value

    send_message(PI_A_ADDR, PORT, addr, msg)
    
    
def function2():
    addr = "/action/40162" # Jump to Marker two
    msg = float(1) # Trigger TRUE Value

    send_message(PI_A_ADDR, PORT, addr, msg)
    

def function3():
    print("You have exited")
    exit()

def function4():
    addr = "/action/40163" # Jump to Marker three
    msg = float(1) # Trigger TRUE Value

    send_message(PI_A_ADDR, PORT, addr, msg)
    
  
    
def function5():
    addr = "/action/40164" # Jump to Marker Four
    msg = float(1) # Trigger TRUE Value

    send_message(PI_A_ADDR, PORT, addr, msg)
    
   
    
def function6():
    addr = "/action/40044" # Play/Stop Function in Reaper
    msg = float(1) # Trigger TRUE Value

    send_message(PI_A_ADDR, PORT, addr, msg)

    
    

#page 1
title = tk.Label(main, text ="Markers in Reaper", font="20", pady= 10)
title.grid(row=0, column=0, columnspan=6)

button1 = tk.Button(main, text="Marker1", font="20", command=function1,  background="orange")
button2 = tk.Button(main, text="Marker2", font="20", command=function2,  background="orange")
button3 = tk.Button(main, text="Exit", font="20", command=function3,  background="Green")
button4 = tk.Button(main, text="Marker3", font="20", command=function4,  background="orange")
button5 = tk.Button(main, text="Marker4", font="20", command=function5,  background="orange")
button6 = tk.Button(main, text="Play", font="20", command=function6,  background="yellow")


button1.grid(row=1, column=0)
button2.grid(row=1, column=2)
button3.grid(row=2, column=1)
button4.grid(row=3, column=0)
button5.grid(row=3, column=2)
button6.grid(row=4, column=1)



button1.config(height= 5, width=10)
button2.config(height= 5, width=10)
button3.config(height= 5, width=10)
button4.config(height= 5, width=10)
button5.config(height= 5, width=10)








main.mainloop()
