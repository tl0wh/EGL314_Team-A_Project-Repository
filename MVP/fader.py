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

# Function to create a light show for "Freebird" segment
def freebird_light_show(receiver_ip, receiver_port, num_pixels, duration_sec):
    start_time = time.time()
    end_time = start_time + duration_sec
    brightness = 1.0
    
    while time.time() < end_time:
        current_time = time.time() - start_time
        
        # Calculate hue based on time progression
        hue = current_time / duration_sec
        
        # Apply hue to RGB colors
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]
        
        # Send color to all pixels
        send_color(receiver_ip, receiver_port, r, g, b)
        
        # Pulsating brightness effect
        pulse = (1 + 0.5 * (1 + math.sin(2 * math.pi * current_time / duration_sec))) / 2
        brightness = pulse
        
        send_brightness(receiver_ip, receiver_port, brightness)
        
        time.sleep(0.05)  # Adjust speed of updates as needed
    
    # Turn off NeoPixels after the duration
    send_color(receiver_ip, receiver_port, 0, 0, 0)
    send_brightness(receiver_ip, receiver_port, 0.0)  # Ensure brightness is set to 0

# FOR INFO: IP address and port of the receiving Raspberry Pi 
PI_A_ADDR = "192.168.254.242"  # Change to your RPi's IP address
PORT = 2005
NUM_PIXELS = 200  # Change to match the number of NeoPixels on your strip
DURATION_SEC = 38  # Duration of the light show in seconds

# Example light show for "Freebird" segment
freebird_light_show(PI_A_ADDR, PORT, NUM_PIXELS, DURATION_SEC)
