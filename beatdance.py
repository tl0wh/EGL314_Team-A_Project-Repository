from pythonosc import udp_client
import time
import random
import colorsys
import math

# UDP client setup
def send_color(receiver_ip, receiver_port, r, g, b):
    client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
    client.send_message("/color", [r, g, b])

def send_brightness(receiver_ip, receiver_port, brightness):
    client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
    client.send_message("/brightness", [brightness])

def send_pixel_color(receiver_ip, receiver_port, pixel_index, r, g, b):
    client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
    address = f"/color/{pixel_index}"
    client.send_message(address, [r, g, b])

# Function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Function to create a music festival light show
def festival_light_show(receiver_ip, receiver_port, num_pixels, duration_sec, bpm):
    start_time = time.time()
    end_time = start_time + duration_sec
    brightness = 1.0
    
    beat_interval = 63 / bpm  # Calculate interval between beats based on BPM
    
    while time.time() < end_time:
        current_time = time.time() - start_time
        
        # Pulsating color effect
        pulse = (1 + 0.5 * (1 + math.sin(2 * math.pi * current_time / beat_interval))) / 2
        r, g, b = [int(c * pulse) for c in random_color()]
        
        # Send color to all pixels
        send_color(receiver_ip, receiver_port, r, g, b)
        
        # Sweep through hues over time
        hue = current_time / duration_sec
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]
        
        # Send color to alternate pixels with different hues
        for i in range(0, num_pixels, 2):
            send_pixel_color(receiver_ip, receiver_port, i, r, g, b)
            send_pixel_color(receiver_ip, receiver_port, i + 1, g, b, r)
        
        # Adjust brightness periodically
        if int(current_time) % 5 == 0:
            brightness = random.uniform(0.7, 1.0)  # Random brightness between 0.7 and 1.0
        
        send_brightness(receiver_ip, receiver_port, brightness)
        
        time.sleep(0.1)  # Adjust speed of updates as needed
    
    # Turn off NeoPixels after the duration
    send_color(receiver_ip, receiver_port, 0, 0, 0)
    send_brightness(receiver_ip, receiver_port, 0.0)  # Ensure brightness is set to 0

# FOR INFO: IP address and port of the receiving Raspberry Pi 
PI_A_ADDR = "192.168.254.242"  # Change to your RPi's IP address
PORT = 2005
NUM_PIXELS = 200  # Change to match the number of NeoPixels on your strip
DURATION_SEC = 38  # Duration of the light show in seconds
BPM = 62  # Beats per minute of the music

# Example music festival light show
festival_light_show(PI_A_ADDR, PORT, NUM_PIXELS, DURATION_SEC, BPM)
