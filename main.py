import tkinter as tk

class MyCalculator:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x300")
        self.root.title("My Calculator")

        self.label = tk.Label(self.root, text="Hello Kitty", font=('Arial', 18))
        self.label.pack()

        self.button = tk.Button(self.root, text="AC", height=1, width=4 ,font=('Arial', 18))
        self.button.place(x=10, y=50)

        self.button = tk.Button(self.root, text="+/-", height=1, width=4 ,font=('Arial', 18))
        self.button.place(x=85, y=50)

        self.button = tk.Button(self.root, text="%", height=1, width=4 ,font=('Arial', 18))
        self.button.place(x=160, y=50)

        self.button = tk.Button(self.root, text="÷", height=1, width=4 ,font=('Arial', 18))
        self.button.place(x=235, y=50)

        self.button = tk.Button(self.root, text="x", height=1, width=4 ,font=('Arial', 18))
        self.button.place(x=235, y=50)

        self.button = tk.Button(self.root, text="-", height=1, width=4 ,font=('Arial', 18))
        self.button.place(x=235, y=50)

        self.button = tk.Button(self.root, text="+", height=1, width=4 ,font=('Arial', 18))
        self.button.place(x=235, y=50)

        self.button = tk.Button(self.root, text="=", height=1, width=4 ,font=('Arial', 18))
        self.button.place(x=235, y=50)

        self.button = tk.Button(self.root, text="7", height=1, width=4 ,font=('Arial', 18))
        self.button.place(x=10, y=100)

        self.button = tk.Button(self.root, text="8", height=1, width=4 ,font=('Arial', 18))
        self.button.place(x=85, y=100)

        self.button = tk.Button(self.root, text="9", height=1, width=4 ,font=('Arial', 18))
        self.button.place(x=160, y=100)

        self.button = tk.Button(self.root, text="4", height=1, width=4 ,font=('Arial', 18))
        self.button.place(x=10, y=150)

        self.button = tk.Button(self.root, text="5", height=1, width=4 ,font=('Arial', 18))
        self.button.place(x=85, y=150)

        self.button = tk.Button(self.root, text="6", height=1, width=4 ,font=('Arial', 18))
        self.button.place(x=160, y=150)

        self.button = tk.Button(self.root, text="1", height=1, width=4 ,font=('Arial', 18))
        self.button.place(x=10, y=200)

        self.button = tk.Button(self.root, text="2", height=1, width=4 ,font=('Arial', 18))
        self.button.place(x=85, y=200)

        self.button = tk.Button(self.root, text="3", height=1, width=4 ,font=('Arial', 18))
        self.button.place(x=160, y=200)

        self.button = tk.Button(self.root, text="0", height=1, width=9 ,font=('Arial', 18))
        self.button.place(x=10, y=250)

        self.button = tk.Button(self.root, text=".", height=1, width=4 ,font=('Arial', 18))
        self.button.place(x=160, y=250)

        self.root.mainloop()

MyCalculator()