import tkinter as tk 

#from pythonosc import udp_client, osc_message_builder

from pythonosc import udp_client, osc_message_builder
import time 
import subprocess

def send_message1(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

		# Send an OSC message to the receiver
		client.send_message(address, message)

		print("Reaper sent successfully.")
	except:
		print("Reaper not sent")

def send_message3(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

		# Send an OSC message to the receiver
		client.send_message(address, message)

		print("Message sent successfully.")
	except:
		print("Message not sent")



main = tk.Tk()

var = 0  

def on():
    subprocess.call(["python", "test_AllOn.py"])

def off():
    subprocess.call(["python", "test_AllOff.py"])

def seq():
    subprocess.call(["python", "test.py"])

def show():
     # REAPER
    PI_A_ADDR = "192.168.254.30"		# wlan ip
    PORT = 8000

    addr = "/marker/61" # Jump to Marker
    msg = float(1) # Trigger TRUE Value
    addr2 = "/action/1007" # Play/Stop Function in Reaper
    msg = float(1) # Trigger TRUE Value

    send_message1(PI_A_ADDR, PORT, addr, msg)
    send_message3(PI_A_ADDR, PORT, addr2, msg)

    print("Playing Freebird")
    subprocess.call(["python", "LaserShowHardCode.py"])
	subprocess.call(["python", "./Neopixel/beatdance.py"])

      
    



on = tk.Button(main, text="On", font="20", command=on , background="Orange")

off = tk.Button(main, text="Off", font="20", command=off, background= "Orange")

seq = tk.Button(main, text="Seq", font="20", command=seq, background= "Orange")

show = tk.Button(main, text="Show", font="20", command=show, background= "Orange")

on.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

off.grid(row=1, column=3, columnspan=2, pady=10, padx=10)

seq.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

show.grid(row=2, column=3, columnspan=2, pady=10, padx=10)

on.config(height=6, width=12)

off.config(height=6, width=12)

seq.config(height=6, width=12)

show.config(height=6, width=12)

main.mainloop()