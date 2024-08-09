from pythonosc import udp_client
import time
import random

# Set the IP and port of the OSC server (the Raspberry Pi running your NeoPixel control code)
SERVER_IP = "192.168.254.242"  # Change to your RPi's IP address
SERVER_PORT = 2005

# Define the number of NeoPixels
NUM_PIXELS = 180  # Increased by 10 pixels

# BPM settings
BPM = 53
BEAT_DURATION = 60 / BPM  # Duration of each beat in seconds

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
    if brightness > 0.5:
        brightness = 0.5
    client.send_message("/brightness", brightness)
    print(f"Sent brightness {brightness}")

# Function to turn off the lights
def send_off():
    client.send_message("/off", [])
    print("Sent off message")

# Create a meteor effect color array with trailing particles
def create_meteor_effect_array(num_pixels, duration, color, background_color, speed=0.05, trail_length=5):
    frames = []
    position = 0
    steps = int(duration / speed)
    
    for _ in range(steps):
        frame = [background_color] * num_pixels
        
        # Create the meteor trail
        for i in range(trail_length):
            if position - i >= 0:
                # Trail fades out over time
                fade_factor = max(0, (trail_length - i) / trail_length)
                frame[position - i] = (
                    int(color[0] * fade_factor),
                    int(color[1] * fade_factor),
                    int(color[2] * fade_factor)
                )
        
        # Move the meteor with maximum brightness
        frame[position] = color  # Set meteor to full brightness
        frames.append(frame)
        
        position += 1
        if position >= num_pixels:
            position = 0
    
    return frames

# Create a smooth gradient color palette
def create_gradient_palette(start_color, end_color, steps):
    palette = []
    for i in range(steps):
        r = int(start_color[0] + (end_color[0] - start_color[0]) * i / (steps - 1))
        g = int(start_color[1] + (end_color[1] - start_color[1]) * i / (steps - 1))
        b = int(start_color[2] + (end_color[2] - start_color[2]) * i / (steps - 1))
        palette.append((r, g, b))
    return palette

# Generate a rainbow color based on position
def get_rainbow_color(position, num_pixels):
    hue = position / num_pixels
    r = int(255 * (1 - hue) if hue < 0.5 else 255 * hue)
    g = int(255 * (1 - abs(hue - 0.5) * 2))
    b = int(255 * hue if hue < 0.5 else 255 * (1 - hue))
    return (r, g, b)

# Create a smooth volume meter effect with moving pixels
def create_moving_volume_meter_array(num_pixels, current_volume, previous_volume, bpm, transition_speed=0.5):
    frame = [(0, 0, 0)] * num_pixels
    min_pixels = 50  # Minimum number of pixels to light up
    max_pixels = 180  # Maximum number of pixels to light up
    max_volume = 255

    # Calculate the target number of lit pixels based on volume
    target_lit_pixels = min(max_pixels, max(min_pixels, int((current_volume / max_volume) * max_pixels)))
    previous_lit_pixels = min(max_pixels, max(min_pixels, int((previous_volume / max_volume) * max_pixels)))
    
    # Compute the number of pixels to light up in this frame
    lit_pixels = min(num_pixels, int(previous_lit_pixels + (target_lit_pixels - previous_lit_pixels) * transition_speed))
    
    # Adjust the transition speed to sync with BPM
    beat_duration = 60 / bpm  # Duration of each beat
    speed_factor = beat_duration / transition_speed

    # Generate the color array with smooth transitions
    for i in range(num_pixels):
        if i < lit_pixels:
            frame[i] = get_rainbow_color(i, num_pixels)
        else:
            frame[i] = (0, 0, 0)  # Turn off pixels not lit

    return frame

# Real-time volume amplitude effect for a specified duration
def run_volume_amplitude_effect(duration=10):  # Extended to 10 seconds
    end_time = time.time() + duration

    previous_volume = 0
    while time.time() < end_time:
        # Generate dummy volume amplitude data (for demonstration purposes)
        volume_data = [random.randint(0, 255) for _ in range(15)]  # Example with 15 frequency bands
        
        # Compute average volume for demonstration purposes
        avg_volume = sum(volume_data) / len(volume_data)
        
        # Create and send the color array for the current volume data
        frame = create_moving_volume_meter_array(NUM_PIXELS, avg_volume, previous_volume, BPM)
        send_color_array(frame)
        
        # Update previous volume
        previous_volume = avg_volume
        
        # Update every 0.1 seconds
        time.sleep(0.1)

    # Turn off the lights after the effect
    send_off()

# Send a sequence of color arrays
def send_color_array_sequence(frames, speed=0.05):
    for frame in frames:
        send_color_array(frame)
        time.sleep(speed)

# Create a light show that follows a given BPM
def create_bpm_light_show(num_pixels, bpm, duration, colors):
    beat_duration = 60 / bpm  # Duration of each beat in seconds
    steps = int(duration / beat_duration)
    
    frames = []
    for i in range(steps):
        frame = [colors[i % len(colors)]] * num_pixels
        frames.append(frame)
    
    return frames

# Example usage
if __name__ == "__main__":
    try:
        # Set initial brightness for the background
        send_brightness(0.5)
        time.sleep(1)

        # Create and send meteor effect with trailing particles
        meteor_frames = create_meteor_effect_array(NUM_PIXELS, 10, (75, 0, 130), (0, 0, 0), trail_length=10)
        send_color_array_sequence(meteor_frames, speed=0.05)

        # Run the volume amplitude effect for 10 seconds
        run_volume_amplitude_effect()

        # Create and send BPM light show
        bpm_colors = [(190, 123, 120), (0, 80, 190), (120, 160, 0), (27, 0, 255)]  # Example colors: red, green, blue, yellow
        bpm_frames = create_bpm_light_show(NUM_PIXELS, BPM, 10, bpm_colors)
        send_color_array_sequence(bpm_frames, speed=BEAT_DURATION)

        # Turn off the lights
        send_off()

    except Exception as e:
        print(f"Error: {e}")
