import board
import neopixel
import time
from pythonosc import dispatcher, osc_server

# Define the number of NeoPixels on the strip and the GPIO pin
num_pixels = 200
pin_strip1 = board.D18

# Create a NeoPixel object for the strip
pixels_strip1 = neopixel.NeoPixel(pin_strip1, num_pixels, auto_write=False)

# Function to set the color of the strip
def set_color(strip, color, brightness):
    for i in range(num_pixels):
        r = int(color[0] * brightness)
        g = int(color[1] * brightness)
        b = int(color[2] * brightness)
        strip[i] = (r, g, b)
    strip.show()

# OSC message handler
def handle_osc_message(addr, *args):
    print(f"Received OSC message: {addr} {args}")
    if addr == "/color":
        if len(args) == 3:
            r, g, b = args
            color = (r, g, b)
            # Default brightness if not provided
            brightness = 1.0
            set_color(pixels_strip1, color, brightness)
    elif addr == "/brightness":
        if len(args) == 1:
            brightness = args[0]
            pixels_strip1.brightness = brightness
            pixels_strip1.show()
    elif addr == "/off":
        set_color(pixels_strip1, (0, 0, 0), 0)
    else:
        print(f"Unknown OSC message: {addr} {args}")

# OSC server setup
receiver_ip = "192.168.254.242"  # Change to your RPi's IP address
receiver_port = 2005

dispatcher = dispatcher.Dispatcher()
dispatcher.map("/color", handle_osc_message)
dispatcher.map("/brightness", handle_osc_message)
dispatcher.map("/off", handle_osc_message)

server = osc_server.ThreadingOSCUDPServer((receiver_ip, receiver_port), dispatcher)
print("Serving on {}".format(server.server_address))
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("Server stopped")
except Exception as e:
    print(f"Error: {e}")
