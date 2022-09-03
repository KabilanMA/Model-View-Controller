import tkinter as tk
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Simple Expense Manager")
        
if __name__ == "__main__":
    app = App()
    app.mainloop()