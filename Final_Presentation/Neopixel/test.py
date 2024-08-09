import board
import neopixel
import time

# Define the number of NeoPixels on the strip and the GPIO pin
num_pixels = 101
pin_strip = board.D18

# Create a NeoPixel object for the strip
pixels = neopixel.NeoPixel(pin_strip, num_pixels, auto_write=False)

# Define the fixed light purple color
light_purple = (128, 0, 128)

# Function to create a shooting star effect
def shooting_star(strip, num_pixels, trail_length=30, duration=5, fade_delay=0.05):
    # Calculate the delay to match the desired duration
    delay = duration / num_pixels
    
    for start_pos in range(num_pixels + trail_length):
        # Clear the strip
        strip.fill((0, 0, 0))

        # Set the pixels for the shooting star and its trail
        for trail_pos in range(trail_length):
            pos = start_pos - trail_pos
            if 0 <= pos < num_pixels:
                brightness = max(0, (trail_length - trail_pos) / trail_length)
                r = int(light_purple[0] * brightness)
                g = int(light_purple[1] * brightness)
                b = int(light_purple[2] * brightness)
                strip[pos] = (r, g, b)

        # Update the strip
        strip.show()
        time.sleep(delay)

    # Fade out the last few pixels slowly
    for i in range(num_pixels, num_pixels + trail_length):
        if 0 <= i < num_pixels + trail_length:
            strip[i] = (0, 0, 0)  # Set to black
            strip.show()
            time.sleep(fade_delay)

try:
    for _ in range(3):
        # Run the shooting star effect
        shooting_star(pixels, num_pixels, trail_length=30, duration=5)

except KeyboardInterrupt:
    # Cleanup and turn off the NeoPixels when the script is interrupted
    pixels.fill((0, 0, 0))
    pixels.show()
