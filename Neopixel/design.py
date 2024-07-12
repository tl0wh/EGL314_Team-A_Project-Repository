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

while True:
    # Sequence as provided
    send_color(PI_A_ADDR, PORT, 255, 10, 50)
    send_brightness(PI_A_ADDR, PORT, 0.3)
    time.sleep(0.5)

    send_color(PI_A_ADDR, PORT, 0, 0, 0)
    send_brightness(PI_A_ADDR, PORT, 0.3)
    time.sleep(1)

    send_color(PI_A_ADDR, PORT, 255, 10, 50)
    send_brightness(PI_A_ADDR, PORT, 0.3)
    time.sleep(0.5)

    send_color(PI_A_ADDR, PORT, 0, 0, 0)
    send_brightness(PI_A_ADDR, PORT, 0.3)
    time.sleep(1)

    send_color(PI_A_ADDR, PORT, 255, 10, 50)
    send_brightness(PI_A_ADDR, PORT, 0.3)
    time.sleep(1)

    send_color(PI_A_ADDR, PORT, 0, 0, 0)
    send_brightness(PI_A_ADDR, PORT, 0.3)
    time.sleep(1)

    send_color(PI_A_ADDR, PORT, 255, 10, 50)
    send_brightness(PI_A_ADDR, PORT, 0.3)
    time.sleep(3)

    send_color(PI_A_ADDR, PORT, 255, 10, 50)
    send_brightness(PI_A_ADDR, PORT, 1)
    time.sleep(3)

    send_color(PI_A_ADDR, PORT, 0, 0, 0)
    send_brightness(PI_A_ADDR, PORT, 0.3)
    time.sleep(1)