import tkinter as tk
import subprocess

main = tk.Tk()
var = 0  

def volume_change(x):
    global var
    if x == 1:
        var = var + 1
    else:
        var = var - 1

    print(var)

def on1():
    print("Snapshot 11")

def on2():
    print("Snapshot 12")

def on3():
    print("Snapshot 13")

def on4():
    print("Snapshot 14")

def on5():
    print("Snapshot 15")

def on6():
    print("Snapshot 16")

def on7():
    print("Snapshot 17")

def on8():
    print("Snapshot 18")

def on9():
    print("Snapshot 19")

def on10():
    print("Snapshot 20")



def sce10():
    print("Play")

def sce20():
    print("Pause")


def Home():
    exit()
    subprocess.call(["python", "guiPage1.py"])
   
def exitbtn():
    print("You have exited")
    exit()

#title = tk.Label(main, text="Snapshots", font="40")
#title.grid(row=0, column=0, columnspan=200, pady=30)

title = tk.Label(main, text="Snapshots", font="40")
title.grid(row=1, column=0, columnspan=1500, pady=30)



# ch1
on1 = tk.Button(main, text="Snapshot11", font="20", background="Orange", command=on1)


on1.grid(row=2, column=0, pady=20, padx=10)


on1.config(height=6, width=12)



# ch2
on2 = tk.Button(main, text="Snapshot12", font="20", background="Orange", command=on2)


on2.grid(row=2, column=100, pady=20, padx=10)


on2.config(height=6, width=12)

#ch3

on3 = tk.Button(main, text="Snapshot13", font="20", background="Orange", command=on3)


on3.grid(row=2, column=200, pady=20, padx=10)


on3.config(height=6, width=12)

#ch4

on4 = tk.Button(main, text="Snapshot14", font="20", background="Orange", command=on4)


on4.grid(row=2, column=300, pady=20, padx=10)


on4.config(height=6, width=12)

#ch5

on5 = tk.Button(main, text="Snapshot15", font="20", background="Orange", command=on5)


on5.grid(row=2, column=400, pady=20, padx=10)


on5.config(height=6, width=12)

#ch6

on6 = tk.Button(main, text="Snapshot16", font="20", background="Orange", command=on6)


on6.grid(row=2, column=500, pady=20, padx=10)


on6.config(height=6, width=12)

#ch7

on7 = tk.Button(main, text="Snapshot17", font="20", background="Orange", command=on7)


on7.grid(row=2, column=600, pady=20, padx=10)


on7.config(height=6, width=12)

#ch8

on8 = tk.Button(main, text="Snapshot18", font="20", background="Orange", command=on8)


on8.grid(row=2, column=700, pady=20, padx=10)


on8.config(height=6, width=12)


#ch9

on9 = tk.Button(main, text="Snapshot19", font="20", background="Orange", command=on9)


on9.grid(row=2, column=800, pady=20, padx=10)


on9.config(height=6, width=12)

#ch10

on10 = tk.Button(main, text="Snapshot20", font="20", background="Orange", command=on10)


on10.grid(row=2, column=900, pady=20, padx=10)


on10.config(height=6, width=12)





# Scenes
sc1 =  tk.Button(main , text ="Play/Pause",font = "20", command=sce10, background='orange')



sc1.grid(row =3, column = 300 ,pady=20, padx=10)


sc1.config(height = 3, width = 9)



#back

back = tk.Button(main, text="Back", pady=30, padx=20, font="20", command=Home,  background='orange')

back.grid(row=3, column= 400)

#exit

exitbtn =  tk.Button(main , text ="Exit",pady=30, padx=25, font = "20", command=exitbtn,  background='orange')

exitbtn.grid(row=3, column = 500)




main.mainloop()