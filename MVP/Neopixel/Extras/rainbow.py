from pythonosc import udp_client
import colorsys
import time

# UDP client setup
receiver_ip = "192.168.254.242"  # Change to your RPi's IP address
receiver_port = 2005
client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

# Function to send pixel color via UDP
def send_pixel_color(pixel_index, r, g, b):
    address = f"/color/{pixel_index}"
    client.send_message(address, [r, g, b])

# Function to create a rainbow color wheel (similar to the Neopixel example)
def wheel(pos):
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    else:
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)

# Function to display a rainbow cycle using UDP messages
def rainbow_cycle_udp(num_pixels, wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            r, g, b = wheel(pixel_index & 255)
            send_pixel_color(i, r, g, b)
        time.sleep(wait)

# Example usage
NUM_PIXELS = 200  # Change to match the number of NeoPixels on your strip

try:
    while True:
        # Display the rainbow cycle via UDP
        rainbow_cycle_udp(NUM_PIXELS, 0.01)

except KeyboardInterrupt:
    # Clean up or handle interruption
    pass
