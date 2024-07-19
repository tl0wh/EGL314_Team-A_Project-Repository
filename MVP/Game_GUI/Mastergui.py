import tkinter as tk 

#from pythonosc import udp_client, osc_message_builder

from pythonosc import udp_client, osc_message_builder
import time



main = tk.Tk()

var = 0  

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



def off(): #off sequence MA3
    #MA3
    if __name__ == "__main__":
        LAPTOP_IP = "192.168.254.229"		# send to laptop w grandMA3
        PORTS = 8888                     # laptop w grandMA3 port number
        addrs = "/gma3/cmd"

        send_message2(LAPTOP_IP, PORTS, addrs, "Off MyRunningSequence")

    print("off")
    

def go(): #Go MA3
    #MA3
    if __name__ == "__main__":
        LAPTOP_IP = "192.168.254.229"		# send to laptop w grandMA3
        PORTS = 8888                     # laptop w grandMA3 port number
        addrs = "/gma3/cmd"

        send_message2(LAPTOP_IP, PORTS, addrs, "Go+")


    print("go")



def pause(): #Pause MA3
    #MA3
    
    PI_A_ADDR = "192.168.254.30"		# wlan ip
    PORT = 8000

    addr2 = "/action/40044" # Play/Stop Function in Reaper
    msg = float(1) # Trigger TRUE Value

    send_message3(PI_A_ADDR, PORT, addr2, msg)


    print("pause")

    if __name__ == "__main__":
        LAPTOP_IP = "192.168.254.229"		# send to laptop w grandMA3
        PORTS = 8888                     # laptop w grandMA3 port number
        addrs = "/gma3/cmd"

        send_message2(LAPTOP_IP, PORTS, addrs, "Off MyRunningSequence")




def clear(): #clear MA3
    #MA3
    if __name__ == "__main__":
        LAPTOP_IP = "192.168.254.229"		# send to laptop w grandMA3
        PORTS = 8888                     # laptop w grandMA3 port number
        addrs = "/gma3/cmd"

        send_message2(LAPTOP_IP, PORTS, addrs, "Clear")


    print("clear")


def pp(): #Play Pause Reaper
    # REAPER
    PI_A_ADDR = "192.168.254.30"		# wlan ip
    PORT = 8000

    addr2 = "/action/40044" # Play/Stop Function in Reaper
    msg = float(1) # Trigger TRUE Value

    send_message3(PI_A_ADDR, PORT, addr2, msg)


    print("play pause")




def exitbtn():

    print("You have exited")

    exit()



def seq23():
    #MA3
    if __name__ == "__main__":
        LAPTOP_IP = "192.168.254.229"		# send to laptop w grandMA3
        PORTS = 8888                     # laptop w grandMA3 port number
        addrs = "/gma3/cmd"


        PI_A_ADDR = "192.168.254.30"		# wlan ip
        PORT = 8000
        addr = "/action/41251" # Jump to Marker
        msg = float(1)

        send_message2(LAPTOP_IP, PORTS, addrs, "Off MyRunningSequence")
        send_message1(PI_A_ADDR, PORT, addr, msg)
        send_message2(LAPTOP_IP, PORTS, addrs, "Go Sequence 23")

    print("This is sequence 23")








def seq24(): #intro
    # REAPER
    PI_A_ADDR = "192.168.254.30"		# wlan ip
    PORT = 8000

    addr = "/action/41257" # Jump to Marker
    msg = float(1) # Trigger TRUE Value
    addr2 = "/action/1007" # Play/Stop Function in Reaper
    msg = float(1) # Trigger TRUE Value

    send_message1(PI_A_ADDR, PORT, addr, msg)
    send_message3(PI_A_ADDR, PORT, addr2, msg)

    #MA3
    if __name__ == "__main__":
        LAPTOP_IP = "192.168.254.229"		# send to laptop w grandMA3
        PORTS = 8888                     # laptop w grandMA3 port number
        addrs = "/gma3/cmd"

        send_message2(LAPTOP_IP, PORTS, addrs, "Off MyRunningSequence")
        send_message2(LAPTOP_IP, PORTS, addrs, "Go Sequence 24")




    print("This is sequence 24")



def seq25():

    # REAPER
    PI_A_ADDR = "192.168.254.30"		# wlan ip
    PORT = 8000

    addr = "/action/41255" # Jump to Marker
    msg = float(1) # Trigger TRUE Value
    addr2 = "/action/1007" # Play/Stop Function in Reaper
    msg = float(1) # Trigger TRUE Value

    send_message1(PI_A_ADDR, PORT, addr, msg)
    send_message3(PI_A_ADDR, PORT, addr2, msg)

    #MA3
    if __name__ == "__main__":
        LAPTOP_IP = "192.168.254.229"		# send to laptop w grandMA3
        PORTS = 8888                     # laptop w grandMA3 port number
        addrs = "/gma3/cmd"

        send_message2(LAPTOP_IP, PORTS, addrs, "Off MyRunningSequence")
        send_message2(LAPTOP_IP, PORTS, addrs, "Go Sequence 25")



    print("This is sequence 25")



def seq26():

     # REAPER
    PI_A_ADDR = "192.168.254.30"		# wlan ip
    PORT = 8000

    addr = "/action/41256" # Jump to Marker
    msg = float(1) # Trigger TRUE Value
    addr2 = "/action/1007" # Play/Stop Function in Reaper
    msg = float(1) # Trigger TRUE Value

    send_message1(PI_A_ADDR, PORT, addr, msg)
    send_message3(PI_A_ADDR, PORT, addr2, msg)

    #MA3
    if __name__ == "__main__":
        LAPTOP_IP = "192.168.254.229"		# send to laptop w grandMA3
        PORTS = 8888                     # laptop w grandMA3 port number
        addrs = "/gma3/cmd"

        send_message2(LAPTOP_IP, PORTS, addrs, "Off MyRunningSequence")
        send_message2(LAPTOP_IP, PORTS, addrs, "Go Sequence 26")

    print("This is sequence 26")



def seq27():  #lose
    # REAPER
    PI_A_ADDR = "192.168.254.30"		# wlan ip
    PORT = 8000

    addr = "/action/41254" # Jump to Marker
    msg = float(1) # Trigger TRUE Value
    addr2 = "/action/1007" # Play/Stop Function in Reaper
    msg = float(1) # Trigger TRUE Value

    send_message1(PI_A_ADDR, PORT, addr, msg)
    send_message3(PI_A_ADDR, PORT, addr2, msg)

    #MA3
    if __name__ == "__main__":
        LAPTOP_IP = "192.168.254.229"		# send to laptop w grandMA3
        PORTS = 8888                     # laptop w grandMA3 port number
        addrs = "/gma3/cmd"

        send_message2(LAPTOP_IP, PORTS, addrs, "Off MyRunningSequence")
        send_message2(LAPTOP_IP, PORTS, addrs, "Go Sequence 27")



    print("This is sequence 27")



def seq28():

    # REAPER
    PI_A_ADDR = "192.168.254.30"		# wlan ip
    PORT = 8000

    addr = "/action/41253" # Jump to Marker
    msg = float(1) # Trigger TRUE Value
    addr2 = "/action/1007" # Play/Stop Function in Reaper
    msg = float(1) # Trigger TRUE Value

    send_message1(PI_A_ADDR, PORT, addr, msg)
    send_message3(PI_A_ADDR, PORT, addr2, msg)

    #MA3
    if __name__ == "__main__":
        LAPTOP_IP = "192.168.254.229"		# send to laptop w grandMA3
        PORTS = 8888                     # laptop w grandMA3 port number
        addrs = "/gma3/cmd"

        send_message2(LAPTOP_IP, PORTS, addrs, "Off MyRunningSequence")
        send_message2(LAPTOP_IP, PORTS, addrs, "Go Sequence 28")



    print("This is sequence 28")



def seq29():

    # REAPER
    PI_A_ADDR = "192.168.254.30"		# wlan ip
    PORT = 8000

    addr = "/action/41253" # Jump to Marker
    msg = float(1) # Trigger TRUE Value
    addr2 = "/action/1007" # Play/Stop Function in Reaper
    msg = float(1) # Trigger TRUE Value

    send_message1(PI_A_ADDR, PORT, addr, msg)
    send_message3(PI_A_ADDR, PORT, addr2, msg)

    #MA3
    if __name__ == "__main__":
        LAPTOP_IP = "192.168.254.229"		# send to laptop w grandMA3
        PORTS = 8888                     # laptop w grandMA3 port number
        addrs = "/gma3/cmd"

        send_message2(LAPTOP_IP, PORTS, addrs, "Off MyRunningSequence")
        send_message2(LAPTOP_IP, PORTS, addrs, "Go Sequence 29")



    print("This is sequence 29")



def seq30():
    #MA3
    if __name__ == "__main__":
        LAPTOP_IP = "192.168.254.229"		# send to laptop w grandMA3
        PORTS = 8888                     # laptop w grandMA3 port number
        addrs = "/gma3/cmd"

        send_message2(LAPTOP_IP, PORTS, addrs, "Off MyRunningSequence")
        send_message2(LAPTOP_IP, PORTS, addrs, "Go Sequence 30")



    print("This is sequence 30")



def seq31():
    # REAPER
    PI_A_ADDR = "192.168.254.30"		# wlan ip
    PORT = 8000

    addr = "/action/41255" # Jump to Marker
    msg = float(1) # Trigger TRUE Value
    addr2 = "/action/1007" # Play/Stop Function in Reaper
    msg = float(1) # Trigger TRUE Value

    send_message1(PI_A_ADDR, PORT, addr, msg)
    send_message3(PI_A_ADDR, PORT, addr2, msg)


    #MA3
    if __name__ == "__main__":
        LAPTOP_IP = "192.168.254.229"		# send to laptop w grandMA3
        PORTS = 8888                     # laptop w grandMA3 port number
        addrs = "/gma3/cmd"

        send_message2(LAPTOP_IP, PORTS, addrs, "Off MyRunningSequence")
        send_message2(LAPTOP_IP, PORTS, addrs, "Go Sequence 31")




    print("This is sequence 31")



def seq32():
    #MA3
    if __name__ == "__main__":
        LAPTOP_IP = "192.168.254.229"		# send to laptop w grandMA3
        PORTS = 8888                     # laptop w grandMA3 port number
        addrs = "/gma3/cmd"

        send_message2(LAPTOP_IP, PORTS, addrs, "Off MyRunningSequence")
        send_message2(LAPTOP_IP, PORTS, addrs, "Go Sequence 32")




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

seq31 = tk.Button(main, text="Demo Stage", font="20", command=seq31, background= "Orange")

seq32 = tk.Button(main, text="Sequence 32", font="20", command=seq32, background= "Orange")





seq23.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

seq24.grid(row=1, column=3, columnspan=2, pady=10, padx=10)

seq25.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

seq26.grid(row=2, column=3, columnspan=2, pady=10, padx=10)

seq27.grid(row=3, column=0, columnspan=2, pady=10, padx=10)

seq28.grid(row=3, column=3, columnspan=2, pady=10, padx=10)

seq29.grid(row=1, column=6, columnspan=2, pady=10, padx=10)

seq30.grid(row=1, column=9, columnspan=2, pady=10, padx=10)

seq31.grid(row=2, column=6, columnspan=2, pady=10, padx=10)

seq32.grid(row=3, column=6, columnspan=2, pady=10, padx=10)





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



Go.grid(row=5, column=0, columnspan=2, pady=10, padx=10)



Go.config(height=3, width=6)





#Pause



pause = tk.Button(main, text ="Off Everyt", font="20",background='orange' ,command =pause)



pause.grid(row=5, column=3, columnspan=2, pady=10, padx=100)



pause.config(height=3, width=6)



#clear



clear = tk.Button(main, text ="Clear", font="20",background='orange', command =clear)



clear.grid(row=5, column=4, columnspan=6, pady=10, padx=10)



clear.config(height=3, width=6)













offbtn = tk.Button(main, text ="Off Sequence", font="20", command=off, background='orange' )



offbtn.grid(row=5, column=1, columnspan=3, pady=10, padx=50)



offbtn.config(height=3, width=10)





sc1 =  tk.Button(main , text ="Play/Pause",font = "20", command=pp,  background='orange')







sc1.grid(row =5, column = 10 ,pady=20, padx=10)





sc1.config(height = 3, width = 9)







#exit



exitbtn = tk.Button(main, text ="Exit", font="20", command=exitbtn, background='orange')



exitbtn.grid(row=5, column=15, columnspan=2, pady=50, padx=50)



exitbtn.config(height=3, width=8)



















main.mainloop()