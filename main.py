import tkinter
import datetime 

window=tkinter.Tk()

window.title("What time?")
window.geometry("640x400+100+100")
window.resizable(False, False)

label=tkinter.Label(window, text="Python", width=10, height=5, fg="red", relief="solid")
label.pack()

def what_time():
    print(datetime.datetime.now())

what_time()
btn=tkinter.Button(window)
btn.config(width=10)
btn.config(text = "현재 시각")
btn.config(command = what_time)

btn.pack()

window.mainloop()