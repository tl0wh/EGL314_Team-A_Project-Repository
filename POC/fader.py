import mido
import subprocess
from pythonosc import udp_client

def list_midi_devices():
    """Lists all available MIDI input and output devices."""
    print("Input MIDI Devices:")
    for input_name in mido.get_input_names():
        print(input_name)
    print("\nOutput MIDI Devices:")
    for output_name in mido.get_output_names():
        print(output_name)

def open_nano_kontrol2():
    """Opens the nanoKONTROL2 device and listens for control change messages."""
    # Replace this with the exact name of your nanoKONTROL2 input port
    # if it's different from what's listed below.
    nano_kontrol2_name = "nanoKONTROL2:nanoKONTROL2 nanoKONTROL2 _ CTR 28:0"

    # Check if the nanoKONTROL2 is in the list of input names
    if nano_kontrol2_name not in mido.get_input_names():
        print(f"Device {nano_kontrol2_name} not found. Please check the device name.")
        return

    # Open the input port for the nanoKONTROL2
    with mido.open_input(nano_kontrol2_name) as inport:
        print(f"Listening to {nano_kontrol2_name} for control changes...")
        try:
            for msg in inport:
                if msg.type == 'control_change':
                    # Print out the control number and its value (fader/knob position)
                    print(f'Control: {msg.control}, Value: {msg.value}')
                    if msg.control == 16:
                        print("It works")
                        send_osc_message(msg.value)
        except KeyboardInterrupt:
            print("Stopped listening to MIDI messages.")

def send_osc_message(value):
    """Send OSC message to control L-ISA."""
    try:
        # IP address and port of the receiving Raspberry Pi
        PI_A_ADDR = "192.168.254.30"  # wlan ip
        PORT = 8880

        addr = "/ext/src/1/p"
        msg = float(value) / 127  
        client = udp_client.SimpleUDPClient(PI_A_ADDR, PORT)
        client.send_message(addr, msg)
        print("OSC Message sent successfully.")
    except Exception as e:
        print("Error sending OSC message:", e)

if __name__ == "__main__":
    # Uncomment the next line if you want to list all available MIDI devices
    # list_midi_devices()

    # Open the nanoKONTROL2 and start listening for MIDI messages
    open_nano_kontrol2()