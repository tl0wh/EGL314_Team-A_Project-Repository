from pythonosc import udp_client

############ fixed code ####################

def send_color(receiver_ip, receiver_port, r, g, b):
    client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
    client.send_message("/color", [r, g, b])

def send_brightness(receiver_ip, receiver_port, brightness):
    client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
    client.send_message("/brightness", [brightness])

def send_pixel_color(receiver_ip, receiver_port, pixel_index, r, g, b):
    client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
    address = f"/color/{pixel_index}"
    client.send_message(address, [r, g, b])

#####################################################################################

def halfhalf(receiver_ip, receiver_port, num_pixels): 
    half_pixels = num_pixels // 2
    for i in range(half_pixels):
        send_pixel_color(receiver_ip, receiver_port, i, 0, 255, 0)  # Green
    for i in range(half_pixels, num_pixels):
        send_pixel_color(receiver_ip, receiver_port, i, 255, 0, 0)  # Red

# FOR INFO: IP address and port of the receiving Raspberry Pi 
PI_A_ADDR = "192.168.254.242"  # Change to your RPi's IP address
PORT = 2005
NUM_PIXELS = 200  # Change to match the number of NeoPixels on your strip

# Example
halfhalf(PI_A_ADDR, PORT, NUM_PIXELS)
send_brightness(PI_A_ADDR, PORT, 1.0)   # Max brightness (0-1) 1 will auto become 0.4
