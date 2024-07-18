from pythonosc import udp_client

def send_message(receiver_ip, receiver_port, address, message):
    try:
        # Create an OSC client to send messages
        client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

        # Send an OSC message to the receiver
        client.send_message(address, message)

        print("Message sent successfully.")
    except Exception as e:
        print(f"Message not sent: {e}")

# FOR INFO: IP address and port of the receiving Raspberry Pi
PI_A_ADDR = "192.168.254.242"  # wlan ip
PORT = 2005

# Send a regular message
addr = "/print"
msg = "salutations from pi_B"
send_message(PI_A_ADDR, PORT, addr, msg)

# Send a script to be executed
script = """
print("Hello from the Raspberry Pi!")
# Add more Python code here
"""
send_message(PI_A_ADDR, PORT, "/execute_script", script)
