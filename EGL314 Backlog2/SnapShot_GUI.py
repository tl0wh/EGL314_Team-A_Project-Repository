import tkinter as tk 
import subprocess


main = tk.Tk()
var = 0


def function1():
    subprocess.call(["python", "guiPage2.py"])
    exit()
    
def function2():
    subprocess.call(["python", "guiPage3.py"])
    exit()

def function3():
    print("You have exited")
    exit()

def function4():
    print("You have exited")
    exit()
    
def function5():
    print("You have exited")
    exit()
    
    

#page 1
title = tk.Label(main, text="L-ISA Snapshot", font="20", pady= 10)
title.grid(row=0, column=0, columnspan=6)

button1 = tk.Button(main, text="Snapshot1", font="20", command=function1,  background="orange")
button2 = tk.Button(main, text="Snapshot2", font="20", command=function2,  background="orange")
button3 = tk.Button(main, text="Exit", font="20", command=function3,  background="Green")
button4 = tk.Button(main, text="Snapshot3", font="20", command=function4,  background="orange")
button5 = tk.Button(main, text="Snapshot4", font="20", command=function5,  background="orange")

button1.grid(row=1, column=0)
button2.grid(row=1, column=2)
button3.grid(row=2, column=1)
button4.grid(row=3, column=0)
button5.grid(row=3, column=2)

button1.config(height= 5, width=10)
button2.config(height= 5, width=10)
button3.config(height= 5, width=10)
button4.config(height= 5, width=10)
button5.config(height= 5, width=10)








main.mainloop()
