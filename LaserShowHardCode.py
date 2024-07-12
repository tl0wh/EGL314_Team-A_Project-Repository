from pythonosc import udp_client
import time 

bpm = 69
d_sec = 30 / bpm

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
x = int(0)
addr = "/print"

msg = [
    "11, 1, 1", ## _ Start
    "11, 2, 1",
    "2, 1, 1",
    "2, 2, 1",
    "5, 1, 1",
    "5, 2, 1",
    "8, 1, 1",
    "8, 2, 1",
    "11, 1, 0",
    "11, 2, 0",
    "2, 1, 0",
    "2, 2, 0",
    "5, 1, 0",
    "5, 2, 0",
    "8, 1, 0",
    "8, 2, 0",## + END
    "12, 2, 1",## X Start
    "12, 1, 1",
    "3, 2, 1",
    "3, 1, 1",
    "7, 2, 1",
    "7, 1, 1",
    "10, 1, 1",
    "10, 2, 1",
    "12, 2, 0",
    "12, 1, 0",
    "3, 2, 0",
    "3, 1, 0",
    "7, 2, 0",
    "7, 1, 0",
    "10, 1, 0",
    "10, 2, 0", ## X END
    "11, 1, 1",## STAR START
    "11, 2, 1",
    "1, 2, 1",
    "1, 1, 1",
    "3, 2, 1",
    "3, 1, 1",
    "7, 2, 1",
    "7, 1, 1",
    "9, 2, 1",
    "9, 1, 1",
    "11, 1, 0",
    "11, 2, 0",
    "1, 2, 0",
    "1, 1, 0",
    "3, 2, 0",
    "3, 1, 0",
    "7, 2, 0",
    "7, 1, 0",
    "9, 2, 0",
    "9, 1, 0",## STAR END
    "12, 2, 1",## ODD
	"12, 1, 1",
    "2, 1, 1",
	"2, 2, 1",
    "4, 2, 1",
	"4, 1, 1",
    "6, 2, 1",
	"6, 1, 1",
    "8, 1, 1",
	"8, 2, 1",
    "10, 1, 1",
    "10, 2, 1", # ODD END
    "1, 2, 1", # Even start
	"1, 1, 1",
    "3, 2, 1",
	"3, 1, 1",
    "5, 1, 1",
	"5, 2, 1",
    "7, 2, 1",
	"7, 1, 1",
    "9, 2, 1",
	"9, 1, 1",
    "11, 1, 1",
	"11, 2, 1",# Even END
    # All On at the end
    




]

while y <1000:
    send_message(PI_A_ADDR, PORT, addr, msg[y])
    y +=1
    time.sleep(d_sec)


