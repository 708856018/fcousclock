import time
import tkinter as tk
from tkinter import messagebox

class FocusTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("专注时钟")
        self.master.geometry("300x150")

        self.minutes_entry = tk.Entry(self.master, width=5, font=("Helvetica", 16))
        self.minutes_entry.insert(0, "25")
        self.minutes_entry.grid(row=0, column=0, padx=10, pady=10)

        self.start_button = tk.Button(self.master, text="开始", command=self.start_timer, font=("Helvetica", 12))
        self.start_button.grid(row=0, column=1, padx=10, pady=10)

        self.timer_label = tk.Label(self.master, text="", font=("Helvetica", 16))
        self.timer_label.grid(row=1, column=0, columnspan=2)

        self.timer_running = False
        self.remaining_time = 0

    def start_timer(self):
        if not self.timer_running:
            try:
                minutes = int(self.minutes_entry.get())
                self.remaining_time = minutes * 60
                self.update_timer_display()
                self.timer_running = True
                self.run_timer()
            except ValueError:
                messagebox.showerror("错误", "请输入有效的分钟数")

    def run_timer(self):
        if self.remaining_time > 0 and self.timer_running:
            minutes, seconds = divmod(self.remaining_time, 60)
            timer_text = "{:02d}:{:02d}".format(minutes, seconds)
            self.timer_label.config(text=timer_text)
            self.remaining_time -= 1
            self.master.after(1000, self.run_timer)
        elif self.timer_running:
            messagebox.showinfo("完成", "专注时间结束！")
            self.timer_running = False
            self.timer_label.config(text="")
            self.minutes_entry.delete(0, tk.END)
            self.minutes_entry.insert(0, "25")

    def update_timer_display(self):
        minutes, seconds = divmod(self.remaining_time, 60)
        timer_text = "{:02d}:{:02d}".format(minutes, seconds)
        self.timer_label.config(text=timer_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = FocusTimer(root)
    root.mainloop()
