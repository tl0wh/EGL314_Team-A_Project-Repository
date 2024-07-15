import tkinter as tk
from pythonosc import udp_client

def send_message2(receiver_ip, receiver_port, address, message):
    try:
        # Create an OSC client to send messages
        client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

        # Send an OSC message to the receiver
        client.send_message(address, message)

        print("MA3 sent successfully.")
    except:
        print("MA3 not sent")

def send_message1(receiver_ip, receiver_port, address, message):
    try:
        # Create an OSC client to send messages
        client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

        # Send an OSC message to the receiver
        client.send_message(address, message)

        print("Reaper sent successfully.")
    except:
        print("Reaper not sent")

def send_message3(receiver_ip, receiver_port, address, message):
    try:
        # Create an OSC client to send messages
        client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

        # Send an OSC message to the receiver
        client.send_message(address, message)

        print("Message sent successfully.")
    except:
        print("Message not sent")

# GUI
def start():
    print("This is the start button")
    # Hide the start button and show the other two buttons
    starts.place_forget()
    Replays.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    Startg.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
    # Example function calls
    send_message1("192.168.254.30", 8000, "/action/41257", float(1))
    send_message3("192.168.254.30", 8000, "/action/1007", float(1))

    # MA3 example
    if __name__ == "__main__":
        send_message2("192.168.254.229", 8888, "/gma3/cmd", "Off MyRunningSequence")
        send_message2("192.168.254.229", 8888, "/gma3/cmd", "Go Sequence 24")

def Replay():
    print("Replaying instructions.....")
    # Example function calls
    send_message1("192.168.254.30", 8000, "/action/41257", float(1))
    send_message3("192.168.254.30", 8000, "/action/1007", float(1))

    # MA3 example
    if __name__ == "__main__":
        send_message2("192.168.254.229", 8888, "/gma3/cmd", "Off MyRunningSequence")
        send_message2("192.168.254.229", 8888, "/gma3/cmd", "Go Sequence 24")

def Startgame():
    # Example function calls
    send_message1("192.168.254.30", 8000, "/action/41255", float(1))
    send_message3("192.168.254.30", 8000, "/action/1007", float(1))

    # MA3 example
    if __name__ == "__main__":
        send_message2("192.168.254.229", 8888, "/gma3/cmd", "Off MyRunningSequence")
        send_message2("192.168.254.229", 8888, "/gma3/cmd", "Go Sequence 25")
        
    # Hide the buttons and display the message
    starts.place_forget()
    Replays.place_forget()
    Startg.place_forget()
    label.config(text="Enjoy the game!")
    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

main = tk.Tk()
main.geometry("600x400") # size of window

# Buttons
starts = tk.Button(main, text="Start ▶", font=("Helvetica", 30), command=start, background="Orange")
Replays = tk.Button(main, text="Replay ⟳", font=("Helvetica", 30), command=Replay, background="Orange")
Startg = tk.Button(main, text="Start The Demo! 🥷🏿", font=("Helvetica", 30), command=Startgame, background="Orange")
label = tk.Label(main, text="", font=("Helvetica", 40))

# Initial Button and Label placement
starts.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
starts.config(height=10, width=40)

Replays.place_forget()
Replays.config(height=5, width=40)

Startg.place_forget()
Startg.config(height=5, width=40)

label.place_forget()

main.mainloop()
