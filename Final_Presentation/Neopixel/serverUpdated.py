import board
import neopixel
from pythonosc import dispatcher, osc_server

# Define the number of NeoPixels on the strip and the GPIO pin
NUM_PIXELS = 170
PIN_STRIP1 = board.D18
MAX_BRIGHTNESS = 0.5  # Increased max brightness

# Create a NeoPixel object for the strip
pixels_strip1 = neopixel.NeoPixel(PIN_STRIP1, NUM_PIXELS, auto_write=False)

# Function to set the color of a specific pixel
def set_pixel_color(strip, pixel, color, brightness):
    r = int(color[0] * brightness)
    g = int(color[1] * brightness)
    b = int(color[2] * brightness)
    strip[pixel] = (r, g, b)

# Function to set colors for all pixels using an array
def set_pixels_color_array(strip, colors, brightness):
    for i in range(min(NUM_PIXELS, len(colors))):
        set_pixel_color(strip, i, colors[i], brightness)
    strip.show()

# Function to set brightness for all pixels
def set_brightness(strip, brightness):
    brightness = min(brightness, MAX_BRIGHTNESS)
    strip.brightness = brightness
    strip.show()

# OSC message handler
def handle_osc_message(addr, *args):
    print(f"Received OSC message: {addr} {args}")
    try:
        if addr == "/color_array":
            handle_color_array_message(args)
        elif addr == "/brightness":
            handle_brightness_message(args)
        elif addr == "/off":
            handle_off_message()
        else:
            print(f"Unknown OSC message: {addr} {args}")
    except Exception as e:
        print(f"Error handling OSC message {addr}: {e}")

def handle_color_array_message(args):
    if len(args) % 3 == 0:
        colors = [(int(args[i]), int(args[i+1]), int(args[i+2])) for i in range(0, len(args), 3)]
        brightness = MAX_BRIGHTNESS  # Default brightness if not provided
        set_pixels_color_array(pixels_strip1, colors, brightness)
    else:
        print(f"Invalid arguments for /color_array: {args}")

def handle_brightness_message(args):
    if len(args) == 1:
        brightness = float(args[0])
        brightness = min(brightness, MAX_BRIGHTNESS)  # Clamp brightness to MAX_BRIGHTNESS
        set_brightness(pixels_strip1, brightness)
    else:
        print(f"Invalid arguments for /brightness: {args}")

def handle_off_message():
    set_pixels_color_array(pixels_strip1, [(0, 0, 0)] * NUM_PIXELS, 0)

# OSC server setup
RECEIVER_IP = "192.168.254.242"  # Change to your RPi's IP address
RECEIVER_PORT = 2005

dispatcher = dispatcher.Dispatcher()
dispatcher.map("/color_array", handle_osc_message)
dispatcher.map("/brightness", handle_osc_message)
dispatcher.map("/off", handle_osc_message)

server = osc_server.ThreadingOSCUDPServer((RECEIVER_IP, RECEIVER_PORT), dispatcher)
print("Serving on {}".format(server.server_address))

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("Server stopped")
except Exception as e:
    print(f"Error: {e}")
finally:
    pixels_strip1.fill((0, 0, 0))
    pixels_strip1.show()
