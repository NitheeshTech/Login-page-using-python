from tkinter import *

# Create GUI window
window = Tk()
window.title("User Form")

# Name
Label(window, text='USER NAME:').grid(row=1, column=1)
a = StringVar()
e = Entry(window, textvariable=a)
e.grid(row=1, column=2)

# Email ID
Label(window, text='E-MAIL ID:').grid(row=2, column=1, sticky=W)
b = StringVar()
el = Entry(window, textvariable=b)
el.grid(row=2, column=2)

# Password
Label(window, text='PASSWORD:').grid(row=3, column=1)
c = StringVar()
e2 = Entry(window, textvariable=c, show='*')
e2.grid(row=3, column=2)

# Submit button action
def act():
    x = a.get()
    y = b.get()
    z = c.get()

    print('NAME:', x)
    print('E-MAIL ID:', y)
    print('PASSWORD:', z)

# Submit button
bt = Button(window, text='SUBMIT', command=act)
bt.grid(row=4, column=2)

# Run the GUI loop
window.mainloop()