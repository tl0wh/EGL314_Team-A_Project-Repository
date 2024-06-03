import tkinter as tk 
#from pythonosc import udp_client, osc_message_builder
import time

main = tk.Tk()
var = 0  


def send_message(receiver_ip, receiver_port, address, message):
	try:
		# Create an OSC client to send messages
		client = udp_client.SimpleUDPClient(receiver_ip, receiver_port)

		# Send an OSC message to the receiver
		client.send_message(address, message)

		print("Message sent successfully.")
	except:
		print("Message not sent")


if __name__ == "__main__":
    LAPTOP_IP = "192.168.0.100"	# send to laptop w grandMA3
    PORT =8888                  # laptop w grandMA3 port number
    addr = "/gma3/cmd"



#def volume_change(x):
 #   global var
  #  if x == 1:
 #       var = var + 1
 #   else:
   #     var = var - 1

   # print(var)

# Marker 1 defined as First Marker for the team. In reality , Markler Num = Allocated Snapshot11

def on1():
    print("Snapshot 11")
    PI_A_ADDR = "192.168.254.30"  # wlan ip
    PORT = 8000

    addr = "/action/41251" # Jump to Marker One
    msg = float(1) # Trigger TRUE Value

    send_message(PI_A_ADDR, PORT, addr, msg)

def on2():
    print("Snapshot 12")
    PI_A_ADDR = "192.168.254.30"  # wlan ip
    PORT = 8000

    addr = "/action/41252" # Jump to Marker One
    msg = float(1) # Trigger TRUE Value

    send_message(PI_A_ADDR, PORT, addr, msg)


def on3():
    print("Snapshot 13")
    PI_A_ADDR = "192.168.254.30"  # wlan ip
    PORT = 8000

    addr = "/action/41253" # Jump to Marker One
    msg = float(1) # Trigger TRUE Value

    send_message(PI_A_ADDR, PORT, addr, msg)


def on4():
    print("Snapshot 14")
    PI_A_ADDR = "192.168.254.30"  # wlan ip
    PORT = 8000

    addr = "/action/41254" # Jump to Marker One
    msg = float(1) # Trigger TRUE Value

    send_message(PI_A_ADDR, PORT, addr, msg)


def on5():
    print("Snapshot 15")
    PI_A_ADDR = "192.168.254.30"  # wlan ip
    PORT = 8000

    addr = "/action/41255" # Jump to Marker One
    msg = float(1) # Trigger TRUE Value

    send_message(PI_A_ADDR, PORT, addr, msg)

def on6():
    print("Snapshot 16")
    PI_A_ADDR = "192.168.254.30"  # wlan ip
    PORT = 8000

    addr = "/action/41256" # Jump to Marker One
    msg = float(1) # Trigger TRUE Value

    send_message(PI_A_ADDR, PORT, addr, msg)

def on7():
    print("Snapshot 17")
    PI_A_ADDR = "192.168.254.30"  # wlan ip
    PORT = 8000

    addr = "/action/41257" # Jump to Marker One
    msg = float(1) # Trigger TRUE Value

    send_message(PI_A_ADDR, PORT, addr, msg)

def on8():
    print("Snapshot 18")
    PI_A_ADDR = "192.168.254.30"  # wlan ip
    PORT = 8000

    addr = "/action/41258" # Jump to Marker One
    msg = float(1) # Trigger TRUE Value

    send_message(PI_A_ADDR, PORT, addr, msg)

def on9():
    print("Snapshot 19")
    PI_A_ADDR = "192.168.254.30"  # wlan ip
    PORT = 8000

    addr = "/action/41259" # Jump to Marker One
    msg = float(1) # Trigger TRUE Value

    send_message(PI_A_ADDR, PORT, addr, msg)

def on10():
    print("Snapshot 20")
    PI_A_ADDR = "192.168.254.30"  # wlan ip
    PORT = 8000

    addr = "/action/41260" # Jump to Marker One
    msg = float(1) # Trigger TRUE Value

    send_message(PI_A_ADDR, PORT, addr, msg)







def off():
    send_message(LAPTOP_IP, PORT, addr, "Off MyRunningSequence")
    send_message(LAPTOP_IP, PORT, addr, "Off MyRunningSequence")
    
def go():
    send_message(LAPTOP_IP, PORT, addr, "Go+")


def pause():
    send_message(LAPTOP_IP, PORT, addr, "Pause")


def clear():
    send_message(LAPTOP_IP, PORT, addr, "Clear")



def exitbtn():
    print("You have exited")
    exit()

def seq23():
    print("This is sequence 23")
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 23")



def seq24():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 24")

    print("This is sequence 24")

def seq25():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 25")

    print("This is sequence 25")

def seq26():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 26")

    print("This is sequence 26")

def seq27():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 27")

    print("This is sequence 27")

def seq28():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 28")

    print("This is sequence 28")

def seq29():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 29")

    print("This is sequence 29")

def seq30():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 30")

    print("This is sequence 30")

def seq31():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 31")

    print("This is sequence 31")

def seq32():
    send_message(LAPTOP_IP, PORT, addr, "Go+ Sequence 32")

    print("This is sequence 32")






#sequence
seq23 = tk.Button(main, text="Murugan Light", font="20", command=seq23 , background="Orange")
seq24 = tk.Button(main, text="Intro+SS 11", font="20", command=seq24, background= "Orange")
seq25 = tk.Button(main, text="Map+SS 15", font="20", command=seq25, background= "Orange")
seq26 = tk.Button(main, text="Lvl2+SS 16", font="20", command=seq26, background= "Orange")
seq27 = tk.Button(main, text="Lose+SS 14", font="20", command=seq27, background= "Orange")
seq28 = tk.Button(main, text="Clear#2+SS 13", font="20", command=seq28, background= "Orange")
seq29 = tk.Button(main, text="Outro+SS 12", font="20", command=seq29, background= "Orange")
seq30 = tk.Button(main, text="smoke#2", font="20", command=seq30, background= "Orange")
seq31 = tk.Button(main, text="Sequence 31", font="20", command=seq31, background= "Orange")
seq32 = tk.Button(main, text="Sequence 32", font="20", command=seq32, background= "Orange")


seq23.grid(row=2, column=0, columnspan=2, pady=10, padx=10)
seq24.grid(row=2, column=3, columnspan=2, pady=10, padx=10)
seq25.grid(row=3, column=0, columnspan=2, pady=10, padx=10)
seq26.grid(row=3, column=3, columnspan=2, pady=10, padx=10)
seq27.grid(row=4, column=0, columnspan=2, pady=10, padx=10)
seq28.grid(row=4, column=3, columnspan=2, pady=10, padx=10)
seq29.grid(row=5, column=0, columnspan=2, pady=10, padx=10)
seq30.grid(row=5, column=3, columnspan=2, pady=10, padx=10)
seq31.grid(row=6, column=0, columnspan=2, pady=10, padx=10)
seq32.grid(row=6, column=3, columnspan=2, pady=10, padx=10)


seq23.config(height=6, width=12)
seq24.config(height=6, width=12)
seq25.config(height=6, width=12)
seq26.config(height=6, width=12)
seq27.config(height=6, width=12)
seq28.config(height=6, width=12)
seq29.config(height=6, width=12)
seq30.config(height=6, width=12)
seq31.config(height=6, width=12)
seq32.config(height=6, width=12)


#Go

Go = tk.Button(main, text ="Go", font="20", background='orange', command =go)

Go.grid(row=7, column=0, columnspan=2, pady=10, padx=10)

Go.config(height=3, width=6)


#Pause

pause = tk.Button(main, text ="Pause", font="20",background='orange' ,command =pause)

pause.grid(row=7, column=3, columnspan=2, pady=10, padx=100)

pause.config(height=3, width=6)

#clear

clear = tk.Button(main, text ="Clear", font="20",background='orange', command =clear)

clear.grid(row=7, column=4, columnspan=6, pady=10, padx=10)

clear.config(height=3, width=6)






offbtn = tk.Button(main, text ="Off Sequence", font="20", command=off, background='orange' )

offbtn.grid(row=7, column=1, columnspan=3, pady=10, padx=50)

offbtn.config(height=3, width=10)



# ch1
on1 = tk.Button(main, text="Snapshot11", font="20", background="Orange", command=on1)


on1.grid(row=2, column=10, pady=20, padx=10)


on1.config(height=6, width=12)



# ch2
on2 = tk.Button(main, text="Snapshot12", font="20", background="Orange", command=on2)


on2.grid(row=2, column=15, pady=20, padx=10)


on2.config(height=6, width=12)

#ch3

on3 = tk.Button(main, text="Snapshot13", font="20", background="Orange", command=on3)


on3.grid(row=3, column=10, pady=20, padx=10)


on3.config(height=6, width=12)

#ch4

on4 = tk.Button(main, text="Snapshot14", font="20", background="Orange", command=on4)


on4.grid(row=3, column=15, pady=20, padx=10)


on4.config(height=6, width=12)

#ch5

on5 = tk.Button(main, text="Snapshot15", font="20", background="Orange", command=on5)


on5.grid(row=4, column=10, pady=20, padx=10)


on5.config(height=6, width=12)

#ch6

on6 = tk.Button(main, text="Snapshot16", font="20", background="Orange", command=on6)


on6.grid(row=4, column=15, pady=20, padx=10)


on6.config(height=6, width=12)

#ch7

on7 = tk.Button(main, text="Snapshot17", font="20", background="Orange", command=on7)


on7.grid(row=5, column=10, pady=20, padx=10)


on7.config(height=6, width=12)

#ch8

on8 = tk.Button(main, text="Snapshot18", font="20", background="Orange", command=on8)


on8.grid(row=5, column=15, pady=20, padx=10)


on8.config(height=6, width=12)


#ch9

on9 = tk.Button(main, text="Snapshot19", font="20", background="Orange", command=on9)


on9.grid(row=6, column=10, pady=20, padx=10)


on9.config(height=6, width=12)

#ch10

on10 = tk.Button(main, text="Snapshot20", font="20", background="Orange", command=on10)


on10.grid(row=6, column=15, pady=20, padx=10)


on10.config(height=6, width=12)

# Scenes
sc1 =  tk.Button(main , text ="Play/Pause",font = "20",  background='orange')



sc1.grid(row =7, column = 10 ,pady=20, padx=10)


sc1.config(height = 3, width = 9)



#exit

exitbtn = tk.Button(main, text ="Exit", font="20", command=exitbtn, background='orange')

exitbtn.grid(row=7, column=15, columnspan=2, pady=50, padx=50)

exitbtn.config(height=3, width=8)









main.mainloop()
