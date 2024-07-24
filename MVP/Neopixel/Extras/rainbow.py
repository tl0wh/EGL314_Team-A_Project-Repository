import board
import neopixel
import time
import random

# Define constants
NUM_PIXELS = 170
PIN_STRIP1 = board.D18
MAX_BRIGHTNESS = 0.5
METEOR_COLOR = (255, 0, 0)  # Red
BOUNCE_COLOR = (0, 255, 0)  # Green
BACKGROUND_COLOR = (0, 0, 0)  # Off

# Create a NeoPixel object
pixels_strip1 = neopixel.NeoPixel(PIN_STRIP1, NUM_PIXELS, auto_write=False)

def clear_strip():
    pixels_strip1.fill(BACKGROUND_COLOR)
    pixels_strip1.show()

def meteor_effect(duration=10):
    start_time = time.time()
    while time.time() - start_time < duration:
        for i in range(NUM_PIXELS):
            # Clear strip and set meteor
            clear_strip()
            pixels_strip1[i] = METEOR_COLOR
            if i > 0:
                pixels_strip1[i - 1] = METEOR_COLOR
            if i < NUM_PIXELS - 1:
                pixels_strip1[i + 1] = METEOR_COLOR
            pixels_strip1.show()
            time.sleep(0.05)
        # Move meteor down the strip
        pixels_strip1.fill(BACKGROUND_COLOR)

def bouncing_light_effect(duration=10):
    start_time = time.time()
    direction = 1
    position = 0
    while time.time() - start_time < duration:
        # Clear strip and set bouncing light
        clear_strip()
        pixels_strip1[position] = BOUNCE_COLOR
        pixels_strip1.show()
        time.sleep(0.05)
        
        # Update position
        if position == 0 or position == NUM_PIXELS - 1:
            direction *= -1
        position += direction

def light_show():
    clear_strip()
    
    # Run meteor effect for 15 seconds
    meteor_effect(duration=15)
    
    # Run bouncing light effect for 15 seconds
    bouncing_light_effect(duration=15)
    
    # Turn off the strip
    clear_strip()

if __name__ == "__main__":
    try:
        light_show()
    except KeyboardInterrupt:
        clear_strip()
        print("Light show interrupted.")
