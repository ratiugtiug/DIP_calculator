import tkinter as tk

class MyCalculator:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x300")
        self.root.title("My Calculator")

        self.label = tk.Label(self.root, text="Hello DIP01", font=('Arial', 18))
        self.label.pack()

        self.button = tk.Button(self.root, text="7", height=1, width=3 ,font=('Arial', 18))
        self.button.place(x=20, y=50)

        self.button = tk.Button(self.root, text="8", height=1, width=3 ,font=('Arial', 18))
        self.button.place(x=120, y=50)

        self.button = tk.Button(self.root, text="9", height=1, width=3 ,font=('Arial', 18))
        self.button.place(x=220, y=50)

        self.button = tk.Button(self.root, text="4", height=1, width=3 ,font=('Arial', 18))
        self.button.place(x=20, y=100)

        self.button = tk.Button(self.root, text="5", height=1, width=3 ,font=('Arial', 18))
        self.button.place(x=120, y=100)

        self.button = tk.Button(self.root, text="6", height=1, width=3 ,font=('Arial', 18))
        self.button.place(x=220, y=100)

        self.button = tk.Button(self.root, text="1", height=1, width=3 ,font=('Arial', 18))
        self.button.place(x=20, y=150)

        self.button = tk.Button(self.root, text="2", height=1, width=3 ,font=('Arial', 18))
        self.button.place(x=120, y=150)

        self.button = tk.Button(self.root, text="3", height=1, width=3 ,font=('Arial', 18))
        self.button.place(x=220, y=150)

        self.root.mainloop()

MyCalculator()