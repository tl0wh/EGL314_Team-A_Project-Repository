from pythonosc import udp_client
import time
import random

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

# Function to create a glitchy light show with automatic turn-off
def glitchy_light_show(receiver_ip, receiver_port, num_pixels, duration_sec):
    start_time = time.time()
    end_time = start_time + duration_sec
    brightness = 1.0
    
    while time.time() < end_time:
        current_time = time.time() - start_time
        
        # Randomly change colors
        r, g, b = random_color()
        
        # Randomly blink or flicker effect
        if random.random() < 0.2:  # 20% chance to flicker
            send_color(receiver_ip, receiver_port, 0, 0, 0)  # Turn off
            time.sleep(random.uniform(0.05, 0.2))  # Random flicker duration
            send_color(receiver_ip, receiver_port, r, g, b)  # Turn on
        
        # Send color to all pixels
        send_color(receiver_ip, receiver_port, r, g, b)
        
        # Adjust brightness periodically
        if int(current_time) % 5 == 0:
            brightness = random.uniform(0.5, 1.0)  # Random brightness between 0.5 and 1.0
        
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

# Example glitchy light show with automatic turn-off
glitchy_light_show(PI_A_ADDR, PORT, NUM_PIXELS, DURATION_SEC)
