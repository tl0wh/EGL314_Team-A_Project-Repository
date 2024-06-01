from pythonosc import udp_client, osc_message_builder
import time
import tkinter as tk 
import subprocess

def send_message(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

		# Send an OSC message to the receiver
		client.send_message(address, message)

		print("Message sent successfully.")
	except:
		print("Message not sent")


#change the below values
if __name__ == "__main__":
    LAPTOP_IP = "192.168.0.100"		# send to laptop w grandMA3
    PORT = 8888                  # laptop w grandMA3 port number
    addr = "/gma3/cmd"

main = tk.Tk()
title = tk.Label(main, text="MA3 Control", font="40")
title.grid(row=0, column=0, columnspan=200, pady=30)

def Home():
    subprocess.call(["python", "guipage1.py"])

def exitbtn():
    print("You have exited")
    exit()

def seq1():
    print("This is sequence 1")
    send_message(LAPTOP_IP, PORT, addr, "FaderMaster Page 1.201 At 100")

def seq2():
    print("This is sequence 2")
    send_message(LAPTOP_IP, PORT, addr, "FaderMaster Page 1.202 At 100")

def gobtn():
     print("This is the Go+ Button")
     send_message(LAPTOP_IP, PORT, addr, "Go+ Executor")
    
def clrbtn():
    print("This is the Clear Button")
    send_message(LAPTOP_IP, PORT, addr, "Clear")

def pbtn():
     print("This is the Pause Button")
     send_message(LAPTOP_IP, PORT, addr, "Pause Executor")

    

#sequence
seq1 = tk.Button(main, text="Sequence 1", font="20", command=seq1)
seq2 = tk.Button(main, text="Sequence 2", font="20", command=seq2)

seq1.grid(row=2, column=0, columnspan=2, pady=10, padx=100)
seq2.grid(row=3, column=0, columnspan=2, pady=10, padx=100)

seq1.config(height=4, width=12)
seq2.config(height=4, width=12)


#Go

Go = tk.Button(main, text ="Go", font="20", command = gobtn)

Go.grid(row=2, column=3, columnspan=2, pady=10, padx=100)

Go.config(height=3, width=6)

#Pause

pause = tk.Button(main, text ="Pause", font="20", command = pbtn)

pause.grid(row=3, column=3, columnspan=2, pady=10, padx=100)

pause.config(height=3, width=6)

#clear

clear = tk.Button(main, text ="Clear", font="20" , command= clrbtn)

clear.grid(row=4, column=3, columnspan=2, pady=10, padx=100)

clear.config(height=3, width=6)

#back

back = tk.Button(main, text ="Back", font="20", command=Home)

back.grid(row=5, column=1, columnspan=2, pady=50, padx=100)

back.config(height=3, width=8)

#exit

exitbtn = tk.Button(main, text ="Exit", font="20", command=exitbtn)

exitbtn.grid(row=5, column=2, columnspan=2, pady=50, padx=10)

exitbtn.config(height=3, width=8)

main.mainloop()
