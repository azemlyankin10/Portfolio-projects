import tkinter

window = tkinter.Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)
window.minsize(width=200, height=100)

input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

tkinter.Label(text='Miles').grid(column=2, row=0)
tkinter.Label(text='is equal to').grid(column=0, row=1)
label = tkinter.Label(text='0')
label.grid(column=1, row=1)
tkinter.Label(text='Km').grid(column=2, row=1)

def button_clicked():
    mi = int(input.get())
    km = mi * 1.60934
    label.config(text=round(km))

tkinter.Button(text='Calculate', command=button_clicked).grid(column=1, row=3)

window.mainloop()