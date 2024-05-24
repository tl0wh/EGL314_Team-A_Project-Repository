import tkinter as tk 
import subprocess


main = tk.Tk()
var = 0


def function1():
    subprocess.call(["python", "guiPage2.py"])
  
    
def function2():
    subprocess.call(["python", "guiPage3.py"])
    

def function3():
    print("You have exited")
    exit()
    

#page 1
title = tk.Label(main, text="Home", font="20", pady= 10)
title.grid(row=0, column=0, columnspan=6)

button1 = tk.Button(main, text="Reaper", font="20", command=function1)
button2 = tk.Button(main, text="MA3", font="20", command=function2)
button3 = tk.Button(main, text="Exit", font="20", command=function3)

button1.grid(row=1, column=0)
button2.grid(row=1, column=2)
button3.grid(row=2, column=1)

button1.config(height= 5, width=10)
button2.config(height= 5, width=10)
button3.config(height= 5, width=10)








main.mainloop()