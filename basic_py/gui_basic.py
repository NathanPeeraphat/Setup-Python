import tkinter as tk

def set_message():
    text = text_input.get()
    title_label.configure(text=text)

window = tk.Tk()
window.title('Basic Python')
window.minsize(width=400, height=400)

title_label = tk.Label(master=window, text='รักน้องแฟนเค้ก')
title_label.pack()

text_input = tk.Entry(master=window)
text_input.pack()

ok_button = tk.Button(master=window, text='ok', command=set_message)
ok_button.pack()

window.mainloop()