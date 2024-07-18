from pythonosc import udp_client

def send_message(receiver_ip, receiver_port, address, message):
    try:
        # Create an OSC client to send messages
        client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
        
        # Send an OSC message to the receiver
        client.send_message(address, message)
        
        print("Message sent successfully.")
    except Exception as e:
        print(f"Message not sent: {e}")

# FOR INFO: IP address and port of the receiving Raspberry Pi
PI_A_ADDR = "192.168.1.100"  # wlan ip
PORT = 2000

# Example usage: sending a regular message
addr = "/print"
msg = "salutations from pi_B"
send_message(PI_A_ADDR, PORT, addr, msg)

# Example usage: sending a command to start the light show
start_script = """
import time
import board
import neopixel
import random

NUM_PIXELS = 300
PIXEL_PIN = board.D18
pixels = neopixel.NeoPixel(PIXEL_PIN, NUM_PIXELS, auto_write=False)

def clear_pixels():
    pixels.fill((0, 0, 0))
    pixels.show()

def theater_chase(color, wait, iterations):
    for j in range(iterations):
        for q in range(3):
            for i in range(0, NUM_PIXELS, 3):
                pixels[i + q] = color
            pixels.show()
            time.sleep(wait)
            for i in range(0, NUM_PIXELS, 3):
                pixels[i + q] = (0, 0, 0)

def shooting_star(color, speed):
    for _ in range(50):
        pixel = random.randint(0, NUM_PIXELS - 1)
        pixels[pixel] = color
        pixels.show()
        time.sleep(0.05)
        pixels[pixel] = (0, 0, 0)
        pixels.show()
        time.sleep(speed)

def play_light_show():
    try:
        for _ in range(5):
            pixels.fill((255, 0, 0))
            pixels.show()
            time.sleep(0.2)
            pixels.fill((0, 0, 0))
            pixels.show()
            time.sleep(0.2)

        shooting_star((255, 255, 255), 0.1)

        for _ in range(5):
            theater_chase((0, 0, 255), 0.05, 4)
            time.sleep(0.5)
    except KeyboardInterrupt:
        clear_pixels()
    finally:
        clear_pixels()

play_light_show()
"""

# Send the light show script to be executed
send_message(PI_A_ADDR, PORT, "/execute_script", start_script)
