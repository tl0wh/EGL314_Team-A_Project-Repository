import time
from pythonosc import udp_client

def send_color(receiver_ip, receiver_port, r, g, b):
    client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
    client.send_message("/color", [r, g, b])

def send_brightness(receiver_ip, receiver_port, brightness):
    client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
    client.send_message("/brightness", [brightness])

def send_off_message(receiver_ip, receiver_port):
    client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
    client.send_message("/off", [])

# FOR INFO: IP address and port of the receiving Raspberry Pi
PI_A_ADDR = "192.168.254.242"  # Change to your RPi's IP address
PORT = 2005

bpm = 62
beat_delay = 60 / bpm
total_duration = 30  
end_time = time.time() + total_duration

colors = [
    (255, 0, 0),   # Red
    (0, 255, 0),   # Green
    (0, 0, 255),   # Blue
    (255, 255, 0), # Yellow
    (0, 255, 255), # Cyan
    (255, 0, 255)  # Magenta
]

brightness_levels = [0.1, 0.3, 0.5, 0.7, 1.0]

while time.time() < end_time:
    for color in colors:
        for brightness in brightness_levels:
            if time.time() >= end_time:
                break
            send_color(PI_A_ADDR, PORT, *color)
            send_brightness(PI_A_ADDR, PORT, brightness)
            time.sleep(beat_delay)
            
# Turn off all LEDs after the light show
send_off_message(PI_A_ADDR, PORT)
