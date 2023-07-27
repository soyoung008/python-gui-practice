import tkinter
import datetime 

window=tkinter.Tk()

window.title("What time?")
window.geometry("640x400+100+100")
window.resizable(False, False)

count = 0

def countUP():
    global count
    coutn+=1
    label.config(text=str(count))
    
label = tkinter.Label(window, text="0")
label.pack()

button = tkinter.Button(window, overrelife="solid", width=15, command=countUP, repeatdelay=1000, repeatinterval=100)
button.pack()

window.mainloop()