from pet import Pet
import time
import tkinter as tk
from tkinter import ttk
import datetime
#from timer import timer

# creates a window instance


# adds a title


class Countdown(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.show_widgets()
        self.seconds_left = 0
        self._timer_on = False

    def show_widgets(self):

        self.label.pack()
        self.entry.pack()
        self.start.pack()

    def create_widgets(self):

        self.label = tk.Label(self, text="00:00:00")
        self.entry = tk.Entry(self, justify='center')
        self.entry.focus_set()
        self.start = tk.Button(self, text="Start", command=self.start_button)

    def countdown(self):
        '''Update label based on the time left.'''
        self.label['text'] = self.convert_seconds_left_to_time() 

        if self.seconds_left:
            self.seconds_left -= 1
            self._timer_on = self.after(1000, self.countdown)
        else:
            self._timer_on = False

    def start_button(self):
        '''Start counting down.'''
        #remove the '* 60' if you want to test faster
        self.seconds_left = int(self.entry.get()) * 60 # 1. to fetch the seconds
        self.stop_timer()                           # 2. to prevent having multiple
        self.countdown()                            #    timers at once

    def stop_timer(self):
        '''Stops after schedule from executing.'''
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on = False

    def convert_seconds_left_to_time(self):
        return datetime.timedelta(seconds=self.seconds_left)




if __name__ == '__main__':
    root = tk.Tk()
    root.title("Study Mates!")
    root.minsize(500,500)
    #root.resizable(False, False)

    introMessage = tk.Label(root, text="Please enter how long you want each session to be, in minutes")
    introMessage.pack()
    countdown = Countdown(root)
    countdown.pack()

    for x in range(4):
        

    #breakCountdown = BreakCountdown(root)
    #breakCountdown.pack()

        root.mainloop()


class CountdownLabel(tk.Label):
    """ A Label in the format of HH:MM:SS, that displays counting down from given 
    seconds.
    """

    def __init__(self, master, seconds_left):
        super().__init__(master)
        self._seconds_left = seconds_left
        self._timer_on = False
        self._countdown()                   # Start counting down immediately

    def _start_countdown(self):
        self._stop_countdown()
        self._countdown()

    def _stop_countdown(self):
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on = False

    def _countdown(self):
        self['text'] = self._get_timedelta_from_seconds(self._seconds_left)
        if self._seconds_left:
            self._seconds_left -= 1 
            self._timer_on = self.after(1000, self._countdown)

    @staticmethod
    def _get_timedelta_from_seconds(seconds):
        return dt.timedelta(seconds=seconds)


if __name__ == '__main__':
    root = tk.Tk()

    for x in range(4):
        countdown = CountdownLabel(root, 3)
        countdown.pack()
        breakMessage = tk.Label(text = "Time for a break!")
        breakMessage.pack()

    root.mainloop()

