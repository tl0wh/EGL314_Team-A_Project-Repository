import tkinter as tk 

#from pythonosc import udp_client, osc_message_builder

from pythonosc import udp_client, osc_message_builder
import time 
import subprocess





main = tk.Tk()

var = 0  

def red():
    subprocess.call(["python", "./Neopixel/testneo.py"])

def off():
    subprocess.call(["python", "./Neopixel/off.py"])

def green():
    subprocess.call(["python", "./Neopixel/green.py"])

def blue():
    subprocess.call(["python", "./Neopixel/blue.py"])

def nice():
    subprocess.call(["python", "./Neopixel/Neopixeltest.py"])

def sequence():
    subprocess.call(["python", "./Neopixel/design.py"])



      
    



green = tk.Button(main, text="Green", font="20", command=green , background="Orange")

off = tk.Button(main, text="Off", font="20", command=off, background= "Orange")

red = tk.Button(main, text="red", font="20", command=red, background= "Orange")

blue = tk.Button(main, text="blue", font="20", command=blue, background= "Orange")

nice = tk.Button(main, text="nice", font="20", command=nice, background= "Orange")

sequence = tk.Button(main, text="sequence", font="20", command=sequence, background= "Orange")



green.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

off.grid(row=1, column=3, columnspan=2, pady=10, padx=10)

red.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

blue.grid(row=2, column=3, columnspan=2, pady=10, padx=10)

nice.grid(row=3, column=0, columnspan=2, pady=10, padx=10)

sequence.grid(row=3, column=3, columnspan=2, pady=10, padx=10)

green.config(height=6, width=12)

off.config(height=6, width=12)

red.config(height=6, width=12)

blue.config(height=6, width=12)

nice.config(height=6, width=12)

sequence.config(height=6, width=12)

main.mainloop()