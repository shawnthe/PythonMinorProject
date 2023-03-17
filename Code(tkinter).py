import tkinter as tk

from tkinter import messagebox

from datetime import timedelta

class Timer:

    def __init__(self, master):

        self.master = master

        master.title("Countdown Timer")

        self.timer_running = False

        self.time_left = timedelta(minutes=30)

        self.paused = False

        # Create labels for displaying the timer

        self.label = tk.Label(master, font=("Helvetica", 24))

        self.label.pack(pady=10)

        # Create entry for custom time input

        self.time_entry = tk.Entry(master, width=10)

        self.time_entry.pack(pady=5)

        # Create buttons for controlling the timer

        self.start_button = tk.Button(master, text="Start", command=self.start_timer)

        self.start_button.pack(pady=5)

        self.pause_button = tk.Button(master, text="Pause", command=self.pause_timer, state="disabled")

        self.pause_button.pack(pady=5)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_timer, state="disabled")

        self.reset_button.pack(pady=5)

    def start_timer(self):

        if not self.timer_running:

            # Get custom time input from entry, if available

            custom_time = self.time_entry.get()

            if custom_time:

                try:

                    minutes, seconds = map(int, custom_time.split(':'))

                    self.time_left = timedelta(minutes=minutes, seconds=seconds)

                except:

                    messagebox.showerror("Error", "Invalid time format. Please enter in MM:SS format.")

                    return

            self.timer_running = True

            self.start_button.config(state="disabled")

            self.pause_button.config(state="normal")

            self.reset_button.config(state="normal")

            self.countdown()

    def countdown(self):

        if self.timer_running:

            if not self.paused:

                if self.time_left.total_seconds() <= 0:

                    messagebox.showinfo("Time's up!", "The timer has finished!")

                    self.timer_running = False

                    self.start_button.config(state="normal")

                    self.pause_button.config(state="disabled")

                    self.reset_button.config(state="disabled")

                else:

                    self.label.config(text=str(self.time_left))

                    self.time_left -= timedelta(seconds=1)

                    self.master.after(1000, self.countdown)

    def pause_timer(self):

        if self.timer_running:

            if not self.paused:

                self.paused = True

                self.pause_button.config(text="Resume")

            else:

                self.paused = False

                self.pause_button.config(text="Pause")

                self.countdown()

    def reset_timer(self):

        self.timer_running = False

        self.paused = False

        self.time_left = timedelta(minutes=30)

        self.label.config(text="30:00")

        self.time_entry.delete(0, tk.END)

        self.start_button.config(state="normal")

        self.pause_button.config(text="Pause", state="disabled")

        self.reset_button.config(state="disabled")

root = tk.Tk()

my_timer = Timer(root)

root.mainloop()

