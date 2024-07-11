from pythonosc import udp_client

def send_off_message(receiver_ip, receiver_port):
    client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
    client.send_message("/off", [])

# FOR INFO: IP address and port of the receiving Raspberry Pi
PI_A_ADDR = "192.168.254.242"  # Change to your RPi's IP address
PORT = 2005

# Send off message to turn off all LEDs
send_off_message(PI_A_ADDR, PORT)
