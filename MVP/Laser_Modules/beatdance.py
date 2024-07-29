from pythonosc import udp_client
import time
from random import randint
from threading import Thread

# Define the OSC server IPs and ports
TRUSS_SERVER_IP = "192.168.254.242"  # Change to your Truss RPi's IP address
TRUSS_SERVER_PORT = 2005

BALLOON_SERVER_IP = "192.168.254.102"  # Change to your Balloon RPi's IP address
BALLOON_SERVER_PORT = 2006

# Create OSC clients
truss_client = udp_client.SimpleUDPClient(TRUSS_SERVER_IP, TRUSS_SERVER_PORT)
balloon_client = udp_client.SimpleUDPClient(BALLOON_SERVER_IP, BALLOON_SERVER_PORT)

# Functions for Truss Neopixel
def send_color_array_truss(colors):
    address = "/color_array"
    flattened_colors = [color for rgb in colors for color in rgb]
    truss_client.send_message(address, flattened_colors)
    print(f"Sent color array to Truss: {flattened_colors}")

def send_brightness_truss(brightness):
    truss_client.send_message("/brightness", brightness)
    print(f"Sent brightness to Truss: {brightness}")

def send_off_truss():
    truss_client.send_message("/off", [])
    print("Sent off message to Truss")

# Functions for Balloon Neopixel
def send_color_array_balloon(colors):
    address = "/color_array"
    flattened_colors = [color for rgb in colors for color in rgb]
    balloon_client.send_message(address, flattened_colors)
    print(f"Sent color array to Balloon: {flattened_colors}")

def send_brightness_balloon(brightness):
    balloon_client.send_message("/brightness", brightness)
    print(f"Sent brightness to Balloon: {brightness}")

def send_off_balloon():
    balloon_client.send_message("/off", [])
    print("Sent off message to Balloon")

def gradual_on(NUM_PIXELS, duration):
    step_delay = duration / NUM_PIXELS
    for i in range(NUM_PIXELS + 1):  # Include the final state where all pixels are on
        colors = [(255, 255, 255) if j < i else (0, 0, 0) for j in range(NUM_PIXELS)]
        send_color_array_truss(colors)
        time.sleep(step_delay)

def random_sparkle(NUM_PIXELS, chance_of_sparkle, speed_delay, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        colors = [(0, 0, 0)] * NUM_PIXELS
        for i in range(NUM_PIXELS):
            if randint(0, 100) < chance_of_sparkle:
                # Generate random orangish colors
                r = randint(200, 255)
                g = randint(100, 150)
                b = randint(0, 50)
                colors[i] = (r, g, b)
        
        # Update Balloon Neopixels
        send_color_array_balloon(colors)
        time.sleep(speed_delay / 1000.0)

if __name__ == "__main__":
    try:
        # Configuration
        NUM_PIXELS_TRUSS = 170  # Adjusted to 170 pixels for Truss
        NUM_PIXELS_BALLOON = 101  # Adjusted to 101 pixels for Balloon
        chance_of_sparkle = 10
        speed_delay = 50  # milliseconds
        duration = 45  # duration of both effects in seconds

        # Initialize all pixels to off for Balloon
        off_colors = [(0, 0, 0)] * NUM_PIXELS_BALLOON
        send_color_array_balloon(off_colors)

        # Start the sparkle effect in a separate thread
        sparkle_thread = Thread(target=random_sparkle, args=(NUM_PIXELS_BALLOON, chance_of_sparkle, speed_delay, duration))
        sparkle_thread.start()

        # Gradually turn on Truss NeoPixels over 45 seconds
        gradual_on(NUM_PIXELS_TRUSS, duration)

        # Wait for the sparkle effect to finish
        sparkle_thread.join()

        # Turn off all NeoPixels after the effects are done
        send_off_truss()
        send_off_balloon()

    except KeyboardInterrupt:
        # Turn off all NeoPixels on exit
        send_off_truss()
        send_off_balloon()
        print("Client stopped")
    except Exception as e:
        print(f"Error: {e}")
        send_off_truss()
        send_off_balloon()
