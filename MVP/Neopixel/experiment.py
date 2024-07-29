from pythonosc import udp_client
import time
from random import randint

# Define the OSC server IP and port
SERVER_IP = "192.168.254.102"  # Change to your RPi's IP address
SERVER_PORT = 2006

# Create OSC client
client = udp_client.SimpleUDPClient(SERVER_IP, SERVER_PORT)

def send_color_array(colors):
    address = "/color_array"
    flattened_colors = [color for rgb in colors for color in rgb]
    client.send_message(address, flattened_colors)
    print(f"Sent color array: {flattened_colors}")

def send_brightness(brightness):
    client.send_message("/brightness", brightness)
    print(f"Sent brightness {brightness}")

def send_off():
    client.send_message("/off", [])
    print("Sent off message")

def random_sparkle(NUM_PIXELS, chance_of_sparkle, speed_delay):
    while True:
        colors = [(0, 0, 0)] * NUM_PIXELS
        for i in range(NUM_PIXELS):
            if randint(0, 100) < chance_of_sparkle:
                # Generate random orangish colors
                r = randint(200, 255)
                g = randint(100, 150)
                b = randint(0, 50)
                colors[i] = (r, g, b)
        
        send_color_array(colors)
        time.sleep(speed_delay / 1000.0)

if __name__ == "__main__":
    try:
        # Configuration
        NUM_PIXELS = 101  # Adjusted to 101 pixels
        chance_of_sparkle = 10
        speed_delay = 50  # milliseconds

        # Start the sparkle effect
        random_sparkle(NUM_PIXELS, chance_of_sparkle, speed_delay)

    except KeyboardInterrupt:
        # Turn off the NeoPixels on exit
        send_off()
        print("Client stopped")
    except Exception as e:
        print(f"Error: {e}")
        send_off()
