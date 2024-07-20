import time
from pythonosc import udp_client

def send_color(receiver_ip, receiver_port, r, g, b):
    client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
    client.send_message("/color", [r, g, b])

def send_brightness(receiver_ip, receiver_port, brightness):
    client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
    client.send_message("/brightness", [brightness])

# FOR INFO: IP address and port of the receiving Raspberry Pi
PI_A_ADDR = "192.168.254.242"  # Change to your RPi's IP address
PORT = 2005


send_color(PI_A_ADDR, PORT, 100, 100, 254)  # Change to your choice of color (255, 255, 255)
send_brightness(PI_A_ADDR, PORT, 0.3)    # Change brightness (0-1)
time.sleep(1)

send_color(PI_A_ADDR, PORT, 254, 100, 100)
send_brightness(PI_A_ADDR, PORT, 0.3)
time.sleep(1)

send_color(PI_A_ADDR, PORT, 100, 254, 100)
send_brightness(PI_A_ADDR, PORT, 0.3)
time.sleep(1)