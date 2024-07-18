from pythonosc import udp_client

# IP address and port of your OSC server (RPi)
server_ip = "192.168.254.242"  # Replace with your RPi's IP address
server_port = 2005

# Create UDP client
client = udp_client.SimpleUDPClient(server_ip, server_port)

# Function to turn off the NeoPixel strip
def turn_off():
    client.send_message("/off", [])
    print("Sent 'off' command to NeoPixel strip.")

# Example usage:

if __name__ == "__main__":
    try:
        turn_off()  # Turn off the NeoPixel strip
    except Exception as e:
        print(f"Error: {e}")
