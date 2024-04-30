import tkinter as tk

def times():
    number = int(number_input.get())
    
    if number == 0:
        output_label.configure(text='ควย')
        return
    
    output = ''
    for i in range(1, 13):
        output += str(number) + ' x ' + str(i)
        output += ' = ' + str(number * i) + '\n'

    output_label.configure(text=output)

window = tk.Tk()
window.title('สูตรคูณ')
window.minsize(width=400, height=400)

title_label = tk.Label(master=window, text='ใส่สูตรคูณแม่ที่อยากรู้')
title_label.pack(pady=25)

number_input = tk.Entry(master=window, width=15)
number_input.pack(pady=2)

go_button = tk.Button(
    master=window, text='ได้แก่',
    command=times, width=15, height=2
)
go_button.pack(pady=10)

output_label = tk.Label(master=window)
output_label.pack(pady=25)

window.mainloop()