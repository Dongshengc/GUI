from tkinter import *

window = Tk()
window.geometry('800x600')
window.title('First GUI application')
label = Label(window, text = 'Hello User', font =('Times NewRoman', 50))
label.grid(row = 0, column = 0)

txt = Entry(window, width = 10, state = 'disabled')
txt.grid(row = 0, column = 2)
txt.focus()

def hit():
	res = 'Welcome to ' + txt.get()
	label.configure(text = res)


btn = Button(window, text = 'Hit me!', bg = 'orange', fg = 'black', command = hit)
btn.grid(row = 0, column = 1)


window.mainloop()
