import board
import neopixel
import time
from pythonosc import dispatcher, osc_server

# Define the number of NeoPixels on each strip and the GPIO pins
num_pixels = 200
pin_strip1 = board.D18
pin_strip2 = board.D21

# Create NeoPixel objects for each strip
pixels_strip1 = neopixel.NeoPixel(pin_strip1, num_pixels, auto_write=False)
pixels_strip2 = neopixel.NeoPixel(pin_strip2, num_pixels, auto_write=False)

# Function to set the color of a strip
def set_color(strip, color, brightness):
    for i in range(num_pixels):
        r = int(color[0] * brightness)
        g = int(color[1] * brightness)
        b = int(color[2] * brightness)
        strip[i] = (r, g, b)
    strip.show()

# OSC message handler
def handle_osc_message(addr, *args):
    if addr == "/color":
        if len(args) == 3:
            r, g, b = args
            color = (r, g, b)
            # Default brightness if not provided
            brightness = 1.0
            set_color(pixels_strip1, color, brightness)
            set_color(pixels_strip2, color, brightness)
    elif addr == "/brightness":
        if len(args) == 1:
            brightness = args[0]
            pixels_strip1.brightness = brightness
            pixels_strip2.brightness = brightness
            pixels_strip1.show()
            pixels_strip2.show()
    else:
        print(f"Unknown OSC message: {addr} {args}")

# OSC server setup
receiver_ip = "192.168.254.242"  # Change to your RPi's IP address
receiver_port = 2005

dispatcher = dispatcher.Dispatcher()
dispatcher.map("/color", handle_osc_message)
dispatcher.map("/brightness", handle_osc_message)

server = osc_server.ThreadingOSCUDPServer((receiver_ip, receiver_port), dispatcher)
print("Serving on {}".format(server.server_address))
server.serve_forever()