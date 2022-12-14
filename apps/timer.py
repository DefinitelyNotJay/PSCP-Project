import tkinter as tk
import datetime
import winsound as ws
from tkinter import PhotoImage, messagebox
def timer():
    # Creating class
    class Countdown(tk.Toplevel):
        def __init__(self):
            """ Declare all functions and variables """
            super().__init__() #escape defining infinite times
            self.title('Timer')
            self.geometry("300x500+500+70")
            self.icon = PhotoImage(file="images/icon/alarm-clock.png")
            self.iconphoto(False, self.icon)
            self.resizable(False, False)
            self.create_widgets()
            self.show_widgets()
            self.seconds_left = 0
            self._timer_on = False

        def create_widgets(self):
            """ create & design all widgets """
            self.canvas = tk.Canvas(self, bg = "#191845", height = 500, width = 300, bd = 0, highlightthickness = 0, relief = "ridge")
            self.image_image_1 = PhotoImage(file=("images/timer_img/image_1.png"))
            _ = self.canvas.create_image(162.0, 255.0, image=self.image_image_1)
            self.canvas.create_text(182.0, 151.0, anchor="nw", text="sec", fill="#FFFFFF", font=("Roboto Mono", 15 * -1))
            self.canvas.create_text(140.0, 151.0, anchor="nw", text="min", fill="#FFFFFF", font=("Roboto Mono", 15 * -1))
            self.canvas.create_text(107.0, 151.0, anchor="nw", text="hr", fill="#FFFFFF", font=("Roboto Mono", 15 * -1))
            self.canvas.create_text(94.5, 245.0, anchor="nw", text="enter the time", fill="#FFFFFF", font=("Roboto Mono", 14 * -1))
            self.text_label = tk.Label(self, text="0:00:00", font=("Roboto Mono", 22), bg="#645CAA", fg="#FFFFFF")

            # ---------- hour entry ----------

            self.entry_hour_image = PhotoImage(file=("images/timer_img/entry_1.png"))
            self.entry_hr = tk.Entry(self, bd=0, bg="#747395", fg="#fff", highlightthickness=0, justify = "ce")

            # ---------- min  entry ----------

            self.entry_min_image = PhotoImage(file=("images/timer_img/entry_2.png"))
            self.entry_min = tk.Entry(self, bd=0, bg="#797ba0", fg="#fff", highlightthickness=0, justify = "ce")

            # ---------- sec entry ----------

            self.entry_sec_image = PhotoImage(file=("images/timer_img/entry_3.png"))
            self.entry_sec = tk.Entry(self, bd=0, bg="#666da3", fg="#fff", highlightthickness=0, justify = "ce")
            self.entry_sec.focus_set() #focus second entry when open window

            # ---------- button ----------
            self.image_image_2 = tk.PhotoImage(file="images/timer_img/button_reset.png")
            self.image_image_3 = tk.PhotoImage(file="images/timer_img/button_stop.png")
            self.image_image_4 = tk.PhotoImage(file="images/timer_img/button_start.png")
            self.reset = tk.Button(self, bg="#2a327d", command=self.reset_button, image=self.image_image_2, relief=tk.SUNKEN, cursor='hand2', border=0, borderwidth = 0, activebackground='#2a327d')
            self.stop = tk.Button(self, bg="#2a327d", command=self.stop_button, image=self.image_image_3, relief=tk.SUNKEN, cursor='hand2', border=0, borderwidth = 0, activebackground='#2a327d')
            self.start = tk.Button(self, bg="#2a327d", command=self.start_button, image=self.image_image_4, relief=tk.SUNKEN, cursor='hand2', border=0, borderwidth = 0, activebackground='#2a327d')

        def show_widgets(self):
            """ pack all widgets """
            self.canvas.place(x = 0, y = 0)
            self.text_label.place(x = 90, y = 106)
            self.entry_min.place(x=137.5, y=220, width=35.0, height=15.0)
            self.entry_sec.place(x=192.5, y=220.0, width=35.0, height=15.0)
            self.entry_hr.place(x=82.5, y=220.0, width=35.0, height=15.0)
            self.start.place(x=103, y=277)
            self.stop.place(x=103, y=331)
            self.reset.place(x=103, y=385)

        def get_time(self):
            """ Get time values from all 3 entries """
            hr = int(self.entry_hr.get())*3600 if self.entry_hr.get() != "" else 0
            minutes = int(self.entry_min.get())*60 if self.entry_min.get() != "" else 0
            sec = int(self.entry_sec.get()) if self.entry_sec.get() != "" else 0
            return hr + minutes + sec

        def after_button(self):
            """ get all buttons back from pressing reset or start """
            self.start.forget()
            self.stop.forget()
            self.reset.forget()
            self.start.place(x=103, y=277)
            self.stop.place(x=103, y=331)
            self.reset.place(x=103, y=385)

        def countdown(self):
            """ time countdown function """
            self.text_label["text"] = self.convert_seconds_left_to_time()
            if self.seconds_left:
                #if time remaining > 0
                self.seconds_left -= 1
                self._timer_on = self.after(1000, self.countdown)
            else:
                # When timeout
                self._timer_on = False
                messagebox.showwarning(title="Time Out", message="Time OUT!!!!!!!!!")

        def reset_button(self):
            """ reset to 0:00:00 again """
            self.seconds_left = 0
            self.stop_timer()
            self._timer_on = False
            self.text_label["text"] = "0:00:00"
            self.text_label.place(x = 90, y = 106) #get Label back in position
            self.after_button()

        def stop_button(self):
            """ stop the present time """
            self.seconds_left = self.get_time()
            self.stop_timer()

        def start_button(self):
            """ start countdown """
            # get time from label
            self.seconds_left = self.get_time()
            self.stop_timer()
            self.countdown()
            self.after_button()
            self.text_label.place(x = 90, y = 106)

        def stop_timer(self):
            """ time stop """
            if self._timer_on:
                self.after_cancel(self._timer_on)
                self._timer_on = False

        def convert_seconds_left_to_time(self):
            return datetime.timedelta(seconds=self.seconds_left)

    countdown = Countdown()
    countdown.mainloop() #loop