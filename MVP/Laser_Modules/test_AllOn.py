# Huats 2023 oscstarterkit
from pythonosc import udp_client
import time 

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
PI_A_ADDR = "192.168.254.49"		# wlan ip
PORT = 2000
y = int(0)
addr = "/print"

msg = [

    "2, 1, 1",
	"2, 2, 1",
    "5, 1, 1",
	"5, 2, 1",
    "8, 1, 1",
	"8, 2, 1",
	"11, 1, 1",
	"11, 2, 1",

	]
while y <1000:
	send_message(PI_A_ADDR, PORT, addr, msg[y])
	y +=1
	time.sleep(0.1)


