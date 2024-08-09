from pythonosc import udp_client
import time

# Set the IP and port of the OSC server (the Raspberry Pi running your NeoPixel control code)
SERVER_IP = "192.168.254.242"  # Change to your RPi's IP address
SERVER_PORT = 2005

# Create an OSC client
client = udp_client.SimpleUDPClient(SERVER_IP, SERVER_PORT)

# Function to send an array of colors
def send_color_array(colors):
    address = "/color_array"
    flattened_colors = [color for rgb in colors for color in rgb]
    client.send_message(address, flattened_colors)
    print(f"Sent color array: {flattened_colors}")

# Function to set the brightness
def send_brightness(brightness):
    client.send_message("/brightness", brightness)
    print(f"Sent brightness {brightness}")

# Function to turn off the lights
def send_off():
    client.send_message("/off", [])
    print("Sent off message")

# Example usage
if __name__ == "__main__":
    try:
        # Create an array of colors (example with 170 pixels)
        colors = [(255, 0, 0)] * 57 + [(0, 255, 0)] * 56 + [(0, 0, 255)] * 57  # Red, Green, Blue sections
        send_color_array(colors)
        time.sleep(1)
        send_brightness(0.05)
        time.sleep(1)
        send_brightness(0.6)  # This should be clamped to 0.5
        time.sleep(1)
        colors = [(0, 0, 0)] * 57 + [(0, 255, 0)] * 56 + [(0, 0, 0)] * 57  # Red, Green, Blue sections
        send_color_array(colors)
        # Turn off the lights
        send_off()

    except Exception as e:
        print(f"Error: {e}")
