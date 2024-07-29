from pythonosc import udp_client

# Set the IP and port of the OSC server (the Raspberry Pi running your NeoPixel control code)
SERVER_IP = "192.168.254.242"  # Change to your RPi's IP address
SERVER_PORT = 2005

# Set the IP and port for the second Pi
SERVER_IP2 = "192.168.254.102"  # Change to your RPi's IP address
SERVER_PORT2 = 2006

# Create an OSC client
client = udp_client.SimpleUDPClient(SERVER_IP, SERVER_PORT)
client2 = udp_client.SimpleUDPClient(SERVER_IP2, SERVER_PORT2)

################################# Functions DO NOT TOUCH!!!!############################################################################

# Truss Neopixel
def send_off():
    client.send_message("/off", [])
    print("Sent off message")

# Balloon Neopixel
def send_off2():
    client2.send_message("/off", [])
    print("Sent off message")

# New function to turn off all LEDs
def send_all_off():
    send_off()
    send_off2()
    print("Sent off message to both clients")

####################################################################################################
# -------------------------Type your code here!!-------------------------------
# -----------------------There are only 170 pixels-----------------------------
# ------------ Make sure after every command there is a delay -----------------

if __name__ == "__main__":
    try:
        # Just turn off all LEDs
        send_all_off()
        
    except Exception as e:
        print(f"Error: {e}")
