import tkinter as tk
from tkinter import messagebox
import time

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Time Tracker")

        self.time_label = tk.Label(root, text="00:00", font=("Helvetica", 24))
        self.time_label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start Timer", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop Timer", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

        self.seconds = 0
        self.timer_running = False

    def start_timer(self):
        self.timer_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.update_timer()

    def stop_timer(self):
        self.timer_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def update_timer(self):
        if self.timer_running:
            self.seconds += 1
            minutes, seconds = divmod(self.seconds, 60)
            time_str = f"{minutes:02d}:{seconds:02d}"
            self.time_label.config(text=time_str)

            if self.seconds == 1800:  # Alert when the timer reaches 2 minutes
                self.show_alert()

            self.root.after(1000, self.update_timer)  # Update every 1000 milliseconds (1 second)

    def show_alert(self):
        messagebox.showinfo("Screen Time Alert", "You've reached 30 minutes of screen time!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
