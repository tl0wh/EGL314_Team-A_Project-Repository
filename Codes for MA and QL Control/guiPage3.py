import tkinter as tk 
import subprocess


main = tk.Tk()

def Home():
    subprocess.call(["python", "guipage1.py"])

def exitbtn():
    print("You have exited")
    exit()

def seq1():
    print("This is sequence 1")
    subprocess.call(["python", "./grandma3.py"])

def seq2():
    print("This is sequence 2")
    subprocess.call(["python", "./grandma2.py"])
title = tk.Label(main, text="MA3 Control", font="40")
title.grid(row=0, column=0, columnspan=200, pady=30)

def gobtn():
    subprocess.call(["python", "./grandmaGo.py"])
    
def clrbtn():
    subprocess.call(["python", "./grandmaclr.py"])
    
def pbtn():
    subprocess.call(["python", "./grandmaPause.py"])
    

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
