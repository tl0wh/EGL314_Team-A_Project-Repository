import tkinter as tk
from pythonosc import udp_client, osc_message_builder
import time

def send_message2(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

		# Send an OSC message to the receiver
		client.send_message(address, message)

		print("MA3 sent successfully.")
	except:
		print("MA3 not sent")

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




#gui
def start():
    print("This is the start button")
    # Hide the start button and show the other two buttons
    starts.place_forget()
    Replays.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    Startg.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
	# REAPER
    PI_A_ADDR = "192.168.254.30"		# wlan ip
    PORT = 8000

    addr = "/action/41251" # Jump to Marker
    msg = float(1) # Trigger TRUE Value
    addr2 = "/action/1007" # Play/Stop Function in Reaper
    msg = float(1) # Trigger TRUE Value

    send_message1(PI_A_ADDR, PORT, addr, msg)
    send_message3(PI_A_ADDR, PORT, addr2, msg)

    #MA3
    if __name__ == "__main__":
        LAPTOP_IP = "192.168.254.30"		# send to laptop w grandMA3
        PORTS = 8888                     # laptop w grandMA3 port number
        addrs = "/gma3/cmd"

        send_message2(LAPTOP_IP, PORTS, addrs, "Go Sequence 24")

def Replay():
    print("Replaying instructions.....")
	    # REAPER
    PI_A_ADDR = "192.168.254.30"		# wlan ip
    PORT = 8000

    addr = "/action/41251" # Jump to Marker
    msg = float(1) # Trigger TRUE Value
    addr2 = "/action/1007" # Play/Stop Function in Reaper
    msg = float(1) # Trigger TRUE Value

    send_message1(PI_A_ADDR, PORT, addr, msg)
    send_message3(PI_A_ADDR, PORT, addr2, msg)

    #MA3
    if __name__ == "__main__":
        LAPTOP_IP = "192.168.254.30"		# send to laptop w grandMA3
        PORTS = 8888                     # laptop w grandMA3 port number
        addrs = "/gma3/cmd"

        send_message2(LAPTOP_IP, PORTS, addrs, "Go Sequence 24")

def Startgame():
# REAPER
    PI_A_ADDR = "192.168.254.30"		# wlan ip
    PORT = 8000

    addr = "/action/41255" # Jump to Marker
    msg = float(1) # Trigger TRUE Value
    addr2 = "/action/1007" # Play/Stop Function in Reaper
    msg = float(1) # Trigger TRUE Value

    send_message1(PI_A_ADDR, PORT, addr, msg)
    send_message3(PI_A_ADDR, PORT, addr2, msg)

    #MA3
    if __name__ == "__main__":
        LAPTOP_IP = "192.168.254.30"		# send to laptop w grandMA3
        PORTS = 8888                     # laptop w grandMA3 port number
        addrs = "/gma3/cmd"

        send_message2(LAPTOP_IP, PORTS, addrs, "Go Sequence 25")

main = tk.Tk()
main.geometry("600x400") # size of window

# Buttons
starts = tk.Button(main, text="Start ▶", font="20", command=start, background="Orange")
Replays = tk.Button(main, text="Replay ⟳", font="20", command=Replay, background="Orange")
Startg = tk.Button(main, text="Start The Game! 🥷🏿", font="20", command=Startgame, background="Orange")

# Initial Button placement
starts.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
starts.config(height=5, width=20)

# Initially hide the Replay and Start Game buttons
Replays.place_forget()
Replays.config(height=5, width=20)

Startg.place_forget()
Startg.config(height=5, width=20)

main.mainloop()