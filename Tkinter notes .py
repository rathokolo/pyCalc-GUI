#Garaphical user interface (GUI) Allows the suer to interact with the operating system and other programs using graphical elements such as icons, buttons, and dialog boxes.
""" A Computer's user interface is part of the computer with which the user interacts.
    - One part of the user interface is that hardware devices such as keyboard and the video display are required.
    - Another part of the user interface has to do with how the computer's operating system accepts commands from the user.
    - The Graphical user interface allows users to interact with the opearting system and other programs through graphical elements on the screen.
"""
""" GUI program's are event-driven """
"""def main():
    user_interface = input('13.1 What is user interface?')
    command_line = input('13.2 How does command line interface work?')
    user_run = input('When the user runs a program in a text-based environment, such as the command line, wht determines the order in which things happen?')
    event_driven = input('What is an event driven program?')

main()
"""
from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title('Calculator')
        master.geometry('357x420+0+0')
        master.config(bg='red')
        master.resizable(False, False)

        self.equation = StringVar()  
        self.entry_value = ''

        Entry(master, width=17, bg='#fff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        buttons = [
            ('(', 0, 50), (')', 90, 50), ('%', 180, 50), ('/', 270, 50),
            ('7', 0, 125), ('8', 90, 125), ('9', 180, 125), ('x', 270, 125),
            ('4', 0, 200), ('5', 90, 200), ('6', 180, 200), ('-', 270, 200),
            ('1', 0, 275), ('2', 90, 275), ('3', 180, 275), ('+', 270, 275),
            ('C', 0, 350), ('0', 90, 350), ('.', 180, 350), ('=', 270, 350),
        ]

        for (text, x, y) in buttons:
            action = (
                self.solve if text == '=' else
                self.clear if text == 'C' else
                lambda value=text: self.show(value)
            )
            Button(master, width=11, height=4, text=text, relief='flat', bg='white', command=action).place(x=x, y=y)

    def show(self, value):
        self.entry_value += str(value if value != 'x' else '*')
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)  # Allow chaining of operations
        except Exception as e:
            self.equation.set('Error')
            self.entry_value = ''

root = Tk()
calculator = Calculator(root)
root.mainloop()

