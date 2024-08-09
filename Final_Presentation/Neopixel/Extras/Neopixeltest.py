from pythonosc import udp_client
import time

# Set the IP and port of the OSC server (the Raspberry Pi running your NeoPixel control code)
SERVER_IP = "192.168.254.242"  # Change to your RPi's IP address
SERVER_PORT = 2005

# Create an OSC client
client = udp_client.SimpleUDPClient(SERVER_IP, SERVER_PORT)

################################# Functions DO NOT TOUCH!!!!############################################################################

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

####################################################################################################
# -------------------------Type your code here!!-------------------------------
# -----------------------There are only 170 pixels-----------------------------
# ------------ Make sure after every command there is a delay -----------------
# Example code explanation
# Pixels 1-57 will turn red, Pixels 58 to 113 will be turn green and Pixels 114 to 170 will turn blue
# After waiting 1 second, light will turn to 0.05
# After waiting 1 second, Light will brighten to 0.6
# After waiting 1 second, only pixel 58 to 113 will be turned on shining green
# After waiting 0.5. seconds it turns off.


if __name__ == "__main__":
    try: #type your code here
        colors = [(255, 0, 0)] * 57 + [(0, 255, 0)] * 56 + [(0, 0, 255)] * 57  # Red, Green, Blue sections
        send_color_array(colors)
        time.sleep(1)

        send_brightness(0.05)
        time.sleep(1)
        send_brightness(0.6)
        time.sleep(1)

        colors = [(0, 0, 0)] * 57 + [(0, 255, 0)] * 56 + [(0, 0, 0)] * 57 
        send_color_array(colors)
        time.sleep(0.5)
        send_off()

    except Exception as e:
        print(f"Error: {e}")
