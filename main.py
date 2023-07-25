import tkinter


window=tkinter.Tk()

window.title("이소영")
window.geometry("640x400+100+100")
window.resizable(False, False)

label=tkinter.Label(window, text="안녕하세요.")
label.pack()

btn = tkinter.Button(window, text="버튼")
btn.pack()

window.mainloop()