import tkinter as tk
from pythonosc import udp_client

def send_message(receiver_ip, receiver_port, address, message, client_name):
    try:
        # Create an OSC client to send messages
        client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

        # Send an OSC message to the receiver
        client.send_message(address, message)

        print(f"{client_name} sent successfully.")
    except Exception as e:
        print(f"{client_name} not sent: {e}")

def start():
    print("This is the start button")
    # Hide the start button and show the other two buttons
    starts.place_forget()
    Replays.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    Startg.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
    back.place(relx=0.1, rely=0.9, anchor=tk.CENTER)

    # Example function calls
    send_message("192.168.254.30", 8000, "/action/41257", float(1), "Reaper")
    send_message("192.168.254.30", 8000, "/action/1007", float(1), "Reaper")

    # MA3 example
    send_message("192.168.254.229", 8888, "/gma3/cmd", "Off MyRunningSequence", "MA3")
    send_message("192.168.254.229", 8888, "/gma3/cmd", "Go Sequence 24", "MA3")

def Replay():
    print("Replaying instructions.....")
    # Example function calls
    send_message("192.168.254.30", 8000, "/action/41257", float(1), "Reaper")
    send_message("192.168.254.30", 8000, "/action/1007", float(1), "Reaper")

    # MA3 example
    send_message("192.168.254.229", 8888, "/gma3/cmd", "Off MyRunningSequence", "MA3")
    send_message("192.168.254.229", 8888, "/gma3/cmd", "Go Sequence 24", "MA3")

def Startgame():
    # Example function calls
    send_message("192.168.254.30", 8000, "/action/41255", float(1), "Reaper")
    send_message("192.168.254.30", 8000, "/action/1007", float(1), "Reaper")

    # MA3 example
    send_message("192.168.254.229", 8888, "/gma3/cmd", "Off MyRunningSequence", "MA3")
    send_message("192.168.254.229", 8888, "/gma3/cmd", "Go Sequence 25", "MA3")
        
    # Hide the buttons and display the message
    starts.place_forget()
    Replays.place_forget()
    Startg.place_forget()
    back.place_forget()
    label.config(text="Enjoy the game!")
    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    page2.place(relx=0.9, rely=0.9, anchor=tk.CENTER)

def Home():
    print("Going back to the home screen")
    # Reset the button and label visibility
    starts.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    Replays.place_forget()
    Startg.place_forget()
    back.place_forget()
    label.place_forget()
    page2.place_forget()

def Page2():
    print("Going back to the 2nd screen")
    # Reset the button and label visibility
    starts.place_forget()
    Replays.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    Startg.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
    back.place(relx=0.1, rely=0.9, anchor=tk.CENTER)
    label.place_forget()
    page2.place_forget()

main = tk.Tk()
main.geometry("600x400")  # size of window

# Buttons
starts = tk.Button(main, text="Start ▶", font=("Helvetica", 30), command=start, background="Orange")
Replays = tk.Button(main, text="Replay ⟳", font=("Helvetica", 30), command=Replay, background="Orange")
Startg = tk.Button(main, text="Start The Game! 🥷🏿", font=("Helvetica", 30), command=Startgame, background="Orange")
label = tk.Label(main, text="", font=("Helvetica", 40))
back = tk.Button(main, text="Home", font=("Helvetica", 30), command=Home, background="Orange")
page2 = tk.Button(main, text="Page2", font=("Helvetica", 40), command=Page2, background="Orange")

# Initial Button and Label placement
starts.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
starts.config(height=10, width=40)

Replays.place_forget()
Replays.config(height=5, width=40)

Startg.place_forget()
Startg.config(height=5, width=40)

label.place_forget()
back.place_forget()
page2.place_forget()

main.mainloop()
