from pythonosc import udp_client, osc_message_builder
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

#change the below values
if __name__ == "__main__":
    LAPTOP_IP = "192.168.0.100"		# send to laptop w grandMA3
    PORT = 8888                  # laptop w grandMA3 port number
    addr = "/gma3/cmd"

    send_message(LAPTOP_IP, PORT, addr, "FaderMaster Page 1.201 At 0")
    send_message(LAPTOP_IP, PORT, addr, "FaderMaster Page 1.202 At 0")
    send_message(LAPTOP_IP, PORT, addr, "FaderMaster Page 1.203 At 0")
    send_message(LAPTOP_IP, PORT, addr, "FaderMaster Page 1.204 At 0")
    send_message(LAPTOP_IP, PORT, addr, "FaderMaster Page 1.205 At 0")
    send_message(LAPTOP_IP, PORT, addr, "FaderMaster Page 1.206 At 0")
    send_message(LAPTOP_IP, PORT, addr, "FaderMaster Page 1.207 At 0")
    send_message(LAPTOP_IP, PORT, addr, "FaderMaster Page 1.208 At 0")
    send_message(LAPTOP_IP, PORT, addr, "FaderMaster Page 1.209 At 0")
    send_message(LAPTOP_IP, PORT, addr, "FaderMaster Page 1.210 At 0")
