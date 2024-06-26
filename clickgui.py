import tkinter as tk 

#from pythonosc import udp_client, osc_message_builder

from pythonosc import udp_client, osc_message_builder
import time 
import subprocess



main = tk.Tk()

var = 0  

def on():
    subprocess 



on = tk.Button(main, text="Murugan Light", font="20", command=on , background="Orange")

off = tk.Button(main, text="Intro+SS 11", font="20", command=off, background= "Orange")

seq = tk.Button(main, text="Map+SS 15", font="20", command=seq, background= "Orange")

on.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

off.grid(row=1, column=3, columnspan=2, pady=10, padx=10)

seq.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

on.config(height=6, width=12)

off.config(height=6, width=12)

seq.config(height=6, width=12)

main.mainloop()