import tkinter as tk 
import subprocess
from pythonosc import udp_client, osc_message_builder
import time



def send_message(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

		# Send an OSC message to the receiver
		client.send_message(address, message)

		print("Message sent successfully.")
	except:
		print("Message not sent")



LAPTOP_IP = "192.168.0.100"	# send to laptop w grandMA3
PORT =8888                  # laptop w grandMA3 port number
addr = "/gma3/cmd"







main = tk.Tk()
def off():
    send_message(LAPTOP_IP, PORT, addr, "Off MyRunningSequence")
    send_message(LAPTOP_IP, PORT, addr, "Off MyRunningSequence")
    
def go():
    send_message(LAPTOP_IP, PORT, addr, "Go+")


def pause():
    send_message(LAPTOP_IP, PORT, addr, "Pause")


def clear():
    send_message(LAPTOP_IP, PORT, addr, "Clear")

def Home():
    subprocess.call(["python", "guiPage1.py"])

def exitbtn():
    print("You have exited")
    exit()

def seq23():
    print("This is sequence 23")
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 23")



def seq24():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 23")

    print("This is sequence 24")

def seq25():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 23")

    print("This is sequence 25")

def seq26():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 23")

    print("This is sequence 26")

def seq27():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 23")

    print("This is sequence 27")

def seq28():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 23")

    print("This is sequence 28")

def seq29():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 23")

    print("This is sequence 29")

def seq30():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 23")

    print("This is sequence 30")

def seq31():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 23")

    print("This is sequence 31")

def seq32():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 23")

    print("This is sequence 32")

def seq33():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 23")

    print("This is sequence 33")

def seq34():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 23")

    print("This is sequence 34")

def seq35():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 23")

    print("This is sequence 35")

def seq36():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 23")

    print("This is sequence 36")

def seq37():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 23")

    print("This is sequence 37")

def seq38():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 23")

    print("This is sequence 38")

def seq39():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 23")

    print("This is sequence 39")

def seq40():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 23")

    print("This is sequence 40")

def seq41():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 23")

    print("This is sequence 41")

def seq42():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 23")

    print("This is sequence 42")

def seq43():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 23")

    print("This is sequence 43")

def seq44():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 23")

    print("This is sequence 44")

def seq45():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 23")

    print("This is sequence 45")

title = tk.Label(main, text="MA3 Control", font="40")
title.grid(row=0, column=0, columnspan=200, pady=30)


#sequence
seq23 = tk.Button(main, text="Sequence 23", font="20", command=seq23 , background="Orange")
seq24 = tk.Button(main, text="Sequence 24", font="20", command=seq24, background= "Orange")
seq25 = tk.Button(main, text="Sequence 25", font="20", command=seq25, background= "Orange")
seq26 = tk.Button(main, text="Sequence 26", font="20", command=seq26, background= "Orange")
seq27 = tk.Button(main, text="Sequence 27", font="20", command=seq27, background= "Orange")
seq28 = tk.Button(main, text="Sequence 28", font="20", command=seq28, background= "Orange")
seq29 = tk.Button(main, text="Sequence 29", font="20", command=seq29, background= "Orange")
seq30 = tk.Button(main, text="Sequence 30", font="20", command=seq30, background= "Orange")
seq31 = tk.Button(main, text="Sequence 31", font="20", command=seq31, background= "Orange")
seq32 = tk.Button(main, text="Sequence 32", font="20", command=seq32, background= "Orange")
seq33 = tk.Button(main, text="Sequence 33", font="20", command=seq33, background= "Orange")
seq34 = tk.Button(main, text="Sequence 34", font="20", command=seq34, background= "Orange")
seq35 = tk.Button(main, text="Sequence 35", font="20", command=seq35, background= "Orange")
seq36 = tk.Button(main, text="Sequence 36", font="20", command=seq36, background= "Orange")
seq37 = tk.Button(main, text="Sequence 37", font="20", command=seq37, background= "Orange")
seq38 = tk.Button(main, text="Sequence 38", font="20", command=seq38, background= "Orange")
seq39 = tk.Button(main, text="Sequence 39", font="20", command=seq39, background= "Orange")
seq40 = tk.Button(main, text="Sequence 40", font="20", command=seq40, background= "Orange")
seq41 = tk.Button(main, text="Sequence 41", font="20", command=seq41, background= "Orange")
seq42 = tk.Button(main, text="Sequence 42", font="20", command=seq42, background= "Orange")
seq43 = tk.Button(main, text="Sequence 43", font="20", command=seq43, background= "Orange")
seq44 = tk.Button(main, text="Sequence 44", font="20", command=seq44, background= "Orange")
seq45 = tk.Button(main, text="Sequence 45", font="20", command=seq45, background= "Orange")

seq23.grid(row=2, column=0, columnspan=2, pady=10, padx=100)
seq24.grid(row=3, column=0, columnspan=2, pady=10, padx=100)
seq25.grid(row=4, column=0, columnspan=2, pady=10, padx=100)
seq26.grid(row=5, column=0, columnspan=2, pady=10, padx=100)
seq27.grid(row=6, column=0, columnspan=2, pady=10, padx=100)
seq28.grid(row=7, column=0, columnspan=2, pady=10, padx=100)
seq29.grid(row=8, column=0, columnspan=2, pady=10, padx=100)
seq30.grid(row=9, column=0, columnspan=2, pady=10, padx=100)
seq31.grid(row=2, column=5, columnspan=2, pady=10, padx=100)
seq32.grid(row=3, column=5, columnspan=2, pady=10, padx=100)
seq33.grid(row=4, column=5, columnspan=2, pady=10, padx=100)
seq34.grid(row=5, column=5, columnspan=2, pady=10, padx=100)
seq35.grid(row=6, column=5, columnspan=2, pady=10, padx=100)
seq36.grid(row=7, column=5, columnspan=2, pady=10, padx=100)
seq37.grid(row=8, column=5, columnspan=2, pady=10, padx=100)
seq38.grid(row=9, column=5, columnspan=2, pady=10, padx=100)
seq39.grid(row=2, column=10, columnspan=2, pady=10, padx=100)
seq40.grid(row=3, column=10, columnspan=2, pady=10, padx=100)
seq41.grid(row=4, column=10, columnspan=2, pady=10, padx=100)
seq42.grid(row=5, column=10, columnspan=2, pady=10, padx=100)
seq43.grid(row=6, column=10, columnspan=2, pady=10, padx=100)
seq44.grid(row=7, column=10, columnspan=2, pady=10, padx=100)
seq45.grid(row=8, column=10, columnspan=2, pady=10, padx=100)






seq23.config(height=4, width=12)
seq24.config(height=4, width=12)
seq25.config(height=4, width=12)
seq26.config(height=4, width=12)
seq27.config(height=4, width=12)
seq28.config(height=4, width=12)
seq29.config(height=4, width=12)
seq30.config(height=4, width=12)
seq31.config(height=4, width=12)
seq32.config(height=4, width=12)
seq33.config(height=4, width=12)
seq34.config(height=4, width=12)
seq35.config(height=4, width=12)
seq36.config(height=4, width=12)
seq37.config(height=4, width=12)
seq38.config(height=4, width=12)
seq39.config(height=4, width=12)
seq40.config(height=4, width=12)
seq41.config(height=4, width=12)
seq42.config(height=4, width=12)
seq43.config(height=4, width=12)
seq44.config(height=4, width=12)
seq45.config(height=4, width=12)

#Go

Go = tk.Button(main, text ="Go", font="20", background='orange', command =go)

Go.grid(row=2, column=15, columnspan=2, pady=10, padx=100)

Go.config(height=3, width=6)


#Pause

pause = tk.Button(main, text ="Pause", font="20",background='orange' ,command =pause)

pause.grid(row=3, column=15, columnspan=2, pady=10, padx=100)

pause.config(height=3, width=6)

#clear

clear = tk.Button(main, text ="Clear", font="20",background='orange', command =clear)

clear.grid(row=4, column=15, columnspan=2, pady=10, padx=10)

clear.config(height=3, width=6)

#back

back = tk.Button(main, text ="Back", font="20", command=Home, background='orange')

back.grid(row=5, column=15, columnspan=2, pady=50, padx=50)

back.config(height=3, width=8)

#exit

exitbtn = tk.Button(main, text ="Exit", font="20", command=exitbtn, background='orange')

exitbtn.grid(row=5, column=15, columnspan=2, pady=50, padx=50)

exitbtn.config(height=3, width=8)


offbtn = tk.Button(main, text ="Exit", font="20", command=off, background='orange' )

offbtn.grid(row=6, column=15, columnspan=2, pady=50, padx=50)

offbtn.config(height=3, width=8)

main.mainloop()