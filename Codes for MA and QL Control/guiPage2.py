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

def channel_on_1():
    if on_button_1.config('text')[-1] == 'ON':
        on_button_1.config(text='OFF', background="Orange")
        print("Channel 1 ON")
        subprocess.call(["python", "Ql1/yamaha.py"])
    else:
        on_button_1.config(text='ON', background="Grey")
        print("Channel 1 Off")
        subprocess.call(["python", "Ql1/yamaha5.py"])
        

def channel_on_2():
    if on_button_2.config('text')[-1] == 'ON':
        on_button_2.config(text='OFF', background="Orange")
        print("Channel 2 Off")
        subprocess.call(["python", "Ql1/yamaha2.py"])
    else:
        on_button_2.config(text='ON', background="Grey")
        print("Channel 2 On")
        subprocess.call(["python", "Ql1/yamaha6.py"])

def channels1_cue():
    print("Scene 1 is on")
    subprocess.call(["python", "Ql1/yamaha3.py"])
    
def channels2_cue():
    print("Scene 2 is on")
    subprocess.call(["python", "Ql1/yamaha4.py"])
    
def sce1():
    print("This is Scene 1")

def sce2():
    print("This is Scene 2")

def home():
    exit()
    subprocess.call(["python", "guiPage1.py"])
   
def exit_btn():
    print("You have exited")
    exit()

title = tk.Label(main, text="QL1", font="40")
title.grid(row=0, column=0, columnspan=200, pady=30)

title = tk.Label(main, text="Ch1", font="40")
title.grid(row=1, column=0, columnspan=100, pady=30)

title = tk.Label(main, text="Ch2", font="40")
title.grid(row=1, column=2, columnspan=100, pady=30)

# ch1
on_button_1 = tk.Button(main, text="ON", font="20", background="Grey", command=channel_on_1)
cue1 = tk.Button(main, text="Cue", font="20")
volume_up_1 = tk.Button(main, text="Vol+", font="20", command=lambda m=1: volume_change(m))
volume_down_1 = tk.Button(main, text="Vol-", font="20", command=lambda m=0: volume_change(m))

volume_up_1.grid(row=5, column=0, columnspan=2, pady=20, padx=10)
volume_down_1.grid(row=6, column=0, pady=20, padx=10)
on_button_1.grid(row=2, column=0, pady=20, padx=10)
cue1.grid(row=3, column=0, pady=20, padx=10)

on_button_1.config(height=6, width=12)
cue1.config(height=6, width=12)
volume_up_1.config(height=6, width=12)
volume_down_1.config(height=6, width=12)

# ch2

on_button_2 = tk.Button(main, text="ON", font="20", background="Grey", command=channel_on_2)
cue2 = tk.Button(main, text="Cue", font="20")
volume_up_2 = tk.Button(main, text="Vol+", font="20", command=lambda m=1: volume_change(m))
volume_down_2 = tk.Button(main, text="Vol-", font="20", command=lambda m=0: volume_change(m))


volume_up_2.grid(row=5, column=100, pady=20, padx=10)
volume_down_2.grid(row=6, column=100, pady=20, padx=10)
on_button_2.grid(row=2, column=100, pady=20, padx=10)
cue2.grid(row=3, column=100, pady=20, padx=10)

on_button_2.config(height=6, width=12)
cue2.config(height=6, width=12)
volume_up_2.config(height=6, width=12)
volume_down_2.config(height=6, width=12)

# Scenes
scene_1 = tk.Button(main, text="Scene1", font="20", command=channels2_cue)
scene_2 = tk.Button(main, text="Scene2", font="20", command=channels1_cue)


scene_1.grid(row=2, column=400, pady=20, padx=10)
scene_2.grid(row=3, column=400, pady=20, padx=10)

scene_1.config(height=3, width=12)
scene_2.config(height=3, width=12)

# back

back_button = tk.Button(main, text="Back", pady=30, padx=20, font="20", command=home)

back_button.grid(row=5, column=400)

# exit

exit_button = tk.Button(main, text="Exit", pady=30, padx=25, font="20", command=exit_btn)

exit_button.grid(row=6, column=400)

main.mainloop()


