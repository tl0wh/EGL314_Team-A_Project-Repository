from pythonosc import udp_client
import time

# Fixed code for sending color and brightness
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

# Function to create a bouncing ball effect (slower version)
def bouncing_ball(receiver_ip, receiver_port, num_pixels, duration=30):
    num_frames = int(duration / 0.2)  # Adjusting for 0.2 seconds per frame
    ball_position = 0
    ball_speed = 1  # Adjust speed as needed
    
    for frame in range(num_frames):
        # Calculate ball position based on frame and speed
        ball_position += ball_speed
        
        # Reverse direction if ball reaches end of strip
        if ball_position >= num_pixels or ball_position < 0:
            ball_speed *= -1
        
        # Calculate colors based on ball position
        r = int(255 * abs(ball_position / num_pixels))
        g = int(255 * (1 - abs(ball_position / num_pixels)))
        b = 0
        
        # Clear previous frame
        for pos in range(num_pixels):
            send_pixel_color(receiver_ip, receiver_port, pos, 0, 0, 0)
        
        # Draw ball at current position
        send_pixel_color(receiver_ip, receiver_port, int(ball_position), r, g, b)
        
        time.sleep(0.2)  # Adjusted delay to fit within slower processing speed

# Constants
PI_A_ADDR = "192.168.254.242"  # Replace with your RPi's IP address
PORT = 2005
NUM_PIXELS = 200  # Adjust based on your NeoPixels

# Example usage
try:
    # Play the bouncing ball effect (slower version)
    bouncing_ball(PI_A_ADDR, PORT, NUM_PIXELS, duration=30)  # Adjusted for 30 seconds duration

    # Set brightness to maximum at the end
    send_brightness(PI_A_ADDR, PORT, 1.0)   # Max brightness (0-1), adjusted for your setup

except KeyboardInterrupt:
    print("Interrupted")
finally:
    # Clean up or final actions if needed
    pass
