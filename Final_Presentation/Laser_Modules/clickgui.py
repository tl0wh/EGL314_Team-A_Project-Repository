import tkinter as tk
import subprocess
from pythonosc import udp_client

def send_message1(receiver_ip, receiver_port, address, message):
    try:
        client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
        client.send_message(address, message)
        print("Reaper message sent successfully.")
    except Exception as e:
        print(f"Error sending message to Reaper: {e}")

def send_message3(receiver_ip, receiver_port, address, message):
    try:
        client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
        client.send_message(address, message)
        print("Message sent successfully.")
    except Exception as e:
        print(f"Error sending message: {e}")

def send_message4(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

		# Send an OSC message to the receiver
		client.send_message(address, message)

		print("MA3 sent successfully.")
	except:
		print("MA3 not sent")

def send_color(receiver_ip, receiver_port, r, g, b):
    try:
        client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
        client.send_message("/color", [r, g, b])
        print("Color message sent successfully.")
    except Exception as e:
        print(f"Error sending color message: {e}")

def send_brightness(receiver_ip, receiver_port, brightness):
    try:
        client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
        client.send_message("/brightness", [brightness])
        print("Brightness message sent successfully.")
    except Exception as e:
        print(f"Error sending brightness message: {e}")

def send_off_message(receiver_ip, receiver_port):
    try:
        client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)
        client.send_message("/off", [])
        print("Off message sent successfully.")
    except Exception as e:
        print(f"Error sending off message: {e}")

def seq32():
    #MA3
    if __name__ == "__main__":
        LAPTOP_IP = "192.168.254.229"		# send to laptop w grandMA3
        PORTS = 8888                     # laptop w grandMA3 port number
        addrs = "/gma3/cmd"

        send_message4(LAPTOP_IP, PORTS, addrs, "Off MyRunningSequence")
        send_message4(LAPTOP_IP, PORTS, addrs, "Go Sequence 32")




    print("This is sequence 32")

def run_subprocesses():
    subprocess.Popen(["python", "./MVP/Laser_Modules/LaserShowHardCode.py"])
    subprocess.Popen(["python", "./MVP/Laser_Modules/beatdance.py"])
    print("Subprocesses started.")

def show():
    PI_A_ADDR = "192.168.254.30"    # Reaper's IP address
    PORT = 8000

    addr = "/marker/61"  # Jump to Marker
    msg = float(1)  # Trigger TRUE Value
    addr2 = "/action/1007"  # Play/Stop Function in Reaper
    msg2 = float(1)  # Trigger TRUE Value

    send_message1(PI_A_ADDR, PORT, addr, msg)
    send_message3(PI_A_ADDR, PORT, addr2, msg2)

    print("Playing Overtaken")

    run_subprocesses()
    seq32()

def on():
    subprocess.Popen(["python", "./MVP/Laser_Modules/test_AllOn.py"])

def off():
    subprocess.Popen(["python", "./MVP/Laser_Modules/test_AllOff.py"])

def seq():
    subprocess.Popen(["python", "./MVP/Laser_Modules/test.py"])

def offneo():
    subprocess.Popen(["python", "./MVP/Laser_Modules/Neooff.py"])

def Pause():
    PI_A_ADDR = "192.168.254.30"    # Reaper's IP address
    PORT = 8000

    PI_A_ADDR = "192.168.254.30"		# wlan ip
    PORT = 8000

    addr2 = "/action/40044" # Play/Stop Function in Reaper
    msg = float(1) # Trigger TRUE Value

    send_message3(PI_A_ADDR, PORT, addr2, msg)


    print("play pause")


main = tk.Tk()

on_button = tk.Button(main, text="On", font="20", command=on, background="Orange")
off_button = tk.Button(main, text="Off", font="20", command=off, background="Orange")
seq_button = tk.Button(main, text="Seq", font="20", command=seq, background="Orange")
show_button = tk.Button(main, text="Show", font="20", command=show, background="Orange")
Offneo = tk.Button(main, text="Off Neo", font="20", command=offneo, background="Orange")
Pause2 = tk.Button(main, text="Pause", font="20", command=Pause, background="Orange")

on_button.grid(row=1, column=0, columnspan=2, pady=10, padx=10)
off_button.grid(row=1, column=3, columnspan=2, pady=10, padx=10)
seq_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10)
show_button.grid(row=2, column=3, columnspan=2, pady=10, padx=10)
Offneo.grid(row=3, column=0, columnspan=2, pady=10, padx=10)
Pause2.grid(row=3, column=3, columnspan=2, pady=10, padx=10)


on_button.config(height=6, width=12)
off_button.config(height=6, width=12)
seq_button.config(height=6, width=12)
show_button.config(height=6, width=12)
Offneo.config(height=6, width=12)
Pause2.config(height=6, width=12)

main.mainloop()
