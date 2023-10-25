import time
import tkinter as tk

class Clock(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label = tk.Label(self, font=("Arial", 48, "bold"))
        self.label.pack()

        self.update_time()

    def update_time(self):
        now = time.strftime("%H:%M:%S")
        self.label.config(text=now)

        self.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    clock = Clock(root)
    clock.pack()

    root.mainloop()
