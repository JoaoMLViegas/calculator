from tkinter import*

root = Tk()
root.title("Calculator")
root.iconphoto(False, PhotoImage(file="calculator.png"))
root.resizable(False, False)

e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Button Functions

def button_number(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_add():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + "+")


def button_subtract():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + "-")


def button_multiply():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + "*")


def button_divide():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + "/")


def button_equal():
    current = e.get()
    e.delete(0, END)
    total = eval(current)
    e.insert(0, total)


def button_decimal():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + ".")


def button_backspace():
    e.delete(e.index("end") - 1)


def button_clear():
    e.delete(0, END)


def button_math_root():
    def calculate_root():
        root1 = float(entry1.get())
        root2 = float(entry2.get())
        global root
        root = root2 ** (1/root1)
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(root))
        top.destroy()


    top = Toplevel()
    top.title("Nth Root Window")
    Label(top, text="Which root do you want?").pack()
    entry1 = Entry(top, width=30)
    entry1.pack()
    Label(top, text="Which number do you want on the root?").pack()
    entry2 = Entry(top, width=30)
    entry2.pack()
    Button(top, text="Insert", command=calculate_root).pack()
    Button(top, text="Cancel", command=top.destroy).pack()


def button_math_power():
    def calculate_power():
        power1 = float(entry1.get())
        power2 = float(entry2.get())
        global power
        power = power1 ** power2
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(power))
        top.destroy()

    top = Toplevel()
    top.title("Power Window")
    Label(top, text="Insert base").pack()
    entry1 = Entry(top, width=30)
    entry1.pack()
    Label(top, text="Insert exponent").pack()
    entry2 = Entry(top, width=30)
    entry2.pack()
    Button(top, text="Insert", command=calculate_power).pack()
    Button(top, text="Cancel", command=top.destroy).pack()


# Define Buttons

button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_number(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_number(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_number(9))

button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_number(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_number(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_number(6))

button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_number(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_number(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_number(3))

button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_number(0))
button_power = Button(root, text="a^b ", padx=31, pady=20, command=button_math_power)
button_root = Button(root, text="√", padx=39, pady=20, command=button_math_root)

button_decimal = Button(root, text=". ", padx=40, pady=20, command=button_decimal)
button_backspace = Button(root, text="←", padx=38, pady=20, command=button_backspace)
button_clear = Button(root, text="C", padx=39, pady=20, command=button_clear)

button_add = Button(root, text="+", padx=40, pady=20, command=button_add)
button_subtract = Button(root, text="- ", padx=40, pady=20, command=button_subtract)
button_multiply = Button(root, text="×", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="÷", padx=40, pady=20, command=button_divide)
button_equal = Button(root, text="=", padx=40, pady=20, command=button_equal)


# Put buttons on the screen
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button0.grid(row=4, column=0)
button_power.grid(row=4, column=1)
button_root.grid(row=4, column=2)

button_decimal.grid(row=5, column=0)
button_backspace.grid(row=5, column=1)
button_clear.grid(row=5, column=2)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row=5, column=3)


root.mainloop()
