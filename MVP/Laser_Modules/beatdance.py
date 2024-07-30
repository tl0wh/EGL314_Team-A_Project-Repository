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

def blink_color(NUM_PIXELS, color, blink_duration):
    blink_end_time = time.time() + blink_duration
    while time.time() < blink_end_time:
        # Blink color
        colors = [color] * NUM_PIXELS
        send_color_array_truss(colors)
        time.sleep(0.1)  # Short on time
        # Turn off
        colors = [(0, 0, 0)] * NUM_PIXELS
        send_color_array_truss(colors)
        time.sleep(0.1)  # Short off time

def gradual_on(NUM_PIXELS, duration):
    step_delay = duration / NUM_PIXELS
    for i in range(NUM_PIXELS + 1):  # Include the final state where all pixels are on
        colors = [(255, 255, 255) if j < i else (0, 0, 0) for j in range(NUM_PIXELS)]
        send_color_array_truss(colors)
        time.sleep(step_delay)
    # Turn off the Truss LEDs right after the gradual on effect completes
    send_off_truss()

def blink_sequence(NUM_PIXELS, duration):
    end_time = time.time() + duration
    colors_sequence = [
        (255, 0, 0),  # Red
        (0, 0, 255),  # Blue
        (0, 255, 0),  # Green
        (255, 20, 147)  # Dark Pink
    ]
    
    while time.time() < end_time:
        for color in colors_sequence:
            blink_color(NUM_PIXELS, color, 0.5)  # Blink each color for 0.5 seconds

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

def random_sparkle(NUM_PIXELS, chance_of_sparkle, speed_delay, duration):
    end_time = time.time() + duration
    green_sparkle_start_time = time.time() + 12  # Time to start adding green sparkles
    blue_sparkle_start_time = time.time() + 17  # Time to start adding blue sparkles
    red_sparkle_start_time = time.time() + 22  # Time to start adding red sparkles
    pink_sparkle_start_time = time.time() + 27  # Time to start adding dark pink sparkles
    
    while time.time() < end_time:
        colors = [(0, 0, 0)] * NUM_PIXELS
        for i in range(NUM_PIXELS):
            if randint(0, 100) < chance_of_sparkle:
                # Generate random colors
                r = randint(200, 255)
                g = randint(100, 150)
                b = randint(0, 50)
                colors[i] = (r, g, b)
            
            # Add green sparkles after 12 seconds
            if time.time() > green_sparkle_start_time and randint(0, 100) < chance_of_sparkle:
                colors[i] = (0, 255, 0)  # Green sparkles
            
            # Add blue sparkles after 17 seconds
            if time.time() > blue_sparkle_start_time and randint(0, 100) < chance_of_sparkle:
                colors[i] = (0, 0, 255)  # Blue sparkles
            
            # Add red sparkles after 22 seconds
            if time.time() > red_sparkle_start_time and randint(0, 100) < chance_of_sparkle:
                colors[i] = (255, 0, 0)  # Red sparkles
            
            # Add dark pink sparkles after 27 seconds
            if time.time() > pink_sparkle_start_time and randint(0, 100) < chance_of_sparkle:
                colors[i] = (255, 20, 147)  # Dark pink sparkles
        
        # Update Balloon Neopixels
        send_color_array_balloon(colors)
        
        # Check if it's time for Truss to blink colors
        current_time = time.time()
        if green_sparkle_start_time < current_time < green_sparkle_start_time + 1:
            blink_color(NUM_PIXELS_TRUSS, (0, 255, 0), 1)  # Blink green for 1 second
        elif blue_sparkle_start_time < current_time < blue_sparkle_start_time + 1:
            blink_color(NUM_PIXELS_TRUSS, (0, 0, 255), 1)  # Blink blue for 1 second
        elif red_sparkle_start_time < current_time < red_sparkle_start_time + 1:
            blink_color(NUM_PIXELS_TRUSS, (255, 0, 0), 1)  # Blink red for 1 second
        elif pink_sparkle_start_time < current_time < pink_sparkle_start_time + 1:
            blink_color(NUM_PIXELS_TRUSS, (255, 20, 147), 1)  # Blink dark pink for 1 second
        
        time.sleep(speed_delay / 1000.0)

def meteor_effect(NUM_PIXELS, duration, speed, meteor_size):
    end_time = time.time() + duration
    position = 0
    
    while time.time() < end_time:
        # Create meteor effect
        colors = [(0, 0, 0)] * NUM_PIXELS
        for i in range(position, position + meteor_size):
            if i < NUM_PIXELS:
                colors[i] = (128, 0, 128)  # Purple color
        
        send_color_array_balloon(colors)
        time.sleep(speed)
        
        # Clear the effect
        colors = [(0, 0, 0)] * NUM_PIXELS
        send_color_array_balloon(colors)
        time.sleep(speed)
        
        # Move meteor position
        position += 1
        if position >= NUM_PIXELS:
            position = 0  # Loop the meteor effect

if __name__ == "__main__":
    try:
        # Configuration
        NUM_PIXELS_TRUSS = 170  # Adjusted to 170 pixels for Truss
        NUM_PIXELS_BALLOON = 101  # Adjusted to 101 pixels for Balloon
        chance_of_sparkle = 10
        speed_delay = 50  # milliseconds
        duration = 45  # duration of initial effects in seconds
        meteor_size = 15  # Size of the meteor effect
        meteor_speed = 0.03  # Speed of the meteor effect (faster)

        # Start the sparkle effect in a separate thread
        sparkle_thread = Thread(target=random_sparkle, args=(NUM_PIXELS_BALLOON, chance_of_sparkle, speed_delay, duration))
        sparkle_thread.start()

        # Gradually turn on Truss NeoPixels over 45 seconds
        gradual_on(NUM_PIXELS_TRUSS, duration)

        # Turn off all NeoPixels after the gradual effect ends
        send_off_truss()
        send_off_balloon()

        # Start the meteor effect and final blinking sequence immediately after turning off
        meteor_duration = 5  # Duration for meteor effect and final blinking sequence
        meteor_thread = Thread(target=meteor_effect, args=(NUM_PIXELS_BALLOON, meteor_duration, meteor_speed, meteor_size))
        meteor_thread.start()

        # Final blinking sequence for Truss NeoPixels
        blink_thread = Thread(target=blink_sequence, args=(NUM_PIXELS_TRUSS, meteor_duration))
        blink_thread.start()

        # Wait for both effects to finish
        meteor_thread.join()
        blink_thread.join()

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
