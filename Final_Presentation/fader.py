import mido
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
    nano_kontrol2_name = "nanoKONTROL2:nanoKONTROL2 nanoKONTROL2 _ CTR 28:0"

    if nano_kontrol2_name not in mido.get_input_names():
        print(f"Device {nano_kontrol2_name} not found. Please check the device name.")
        return

    with mido.open_input(nano_kontrol2_name) as inport:
        print(f"Listening to {nano_kontrol2_name} for control changes...")
        try:
            for msg in inport:
                if msg.type == 'control_change':
                    print(f'Control: {msg.control}, Value: {msg.value}')
                    if msg.control == 16:
                        print("It works")
                        send_osc_message(msg.value)
        except KeyboardInterrupt:
            print("Stopped listening to MIDI messages.")

def send_osc_message(value):
    """Send OSC message to control L-ISA."""
    try:
        PI_A_ADDR = "192.168.254.30"  # wlan ip
        PORT = 8880

        # Map the MIDI value to the OSC value
        if value >= 64:
            # 127 to 64 maps from 0.75 to 0.25
            msg = 0.75 - (0.5 / 63) * (127 - value)
        elif value >= 32:
            # 63 to 32 maps from 0.24 to 0
            msg = 0.24 - (0.24 / 31) * (63 - value)
        else:
            # 31 to 0 maps from 1 to 0.76
            msg = 1 - (0.24 / 31) * (31 - value)
        
        # Ensure the message is within the range [0, 1]
        msg = max(0, min(1, msg))

        addr = "/ext/src/1/p"
        client = udp_client.SimpleUDPClient(PI_A_ADDR, PORT)
        client.send_message(addr, msg)
        print(f"OSC Message sent successfully with value: {msg}")

    except Exception as e:
        print("Error sending OSC message:", e)

if __name__ == "__main__":
    # Uncomment the next line if you want to list all available MIDI devices
    # list_midi_devices()

    # Open the nanoKONTROL2 and start listening for MIDI messages
    open_nano_kontrol2()
