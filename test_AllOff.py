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
    
    "3, 2, 0",
    "3, 1, 0",
	"2, 1, 0",
    "2, 2, 0",
	"1, 2, 0",
	"1, 1, 0",
    "4, 2, 0",
    "4, 1, 0",
	"5, 1, 0",
    "5, 2, 0",
	"6, 2, 0",
	"6, 1, 0",
    "7, 2, 0",
    "7, 1, 0",
	"8, 1, 0",
    "8, 2, 0",
	"9, 2, 0",
	"9, 1, 0",
	"10, 1, 0",
	"10, 2, 0",
    "11, 1, 0",
    "11, 2, 0",
	"12, 2, 0",
	"12, 1, 0",
	
	]
while y <1000:
	send_message(PI_A_ADDR, PORT, addr, msg[y])
	y +=1
	time.sleep(0.5)


