import threading
from tkinter import *

from modules.Calendar import Datepicker

from modules.PraamidScraper import PraamidScraper

is_running = False


def start():
    global is_running
    if not is_running:
        is_running = True
        get_tickets()


def get_tickets():
    # trips = PraamidScraper().get_data(date.get(), direction.get(), W1.get(), W2.get())

    trips = ["test", "test2", "test3"]
    trips = []

    if len(trips) == 0:
        print("No trips")
        render_text(["No trips found: Polling every " + str(W3.get()) + " minute(s)"])
        threading.Timer(W3.get() * 60, get_tickets).start()
    else:
        render_text(trips)
        global is_running
        is_running = False
        return


def get_times():
    times = []
    for x in range(0, 24):
        times.append(x)
    return times


def exit_app():
    top.destroy()


def render_text(trips):
    for trip in trips:
        T.insert(INSERT, trip + "\n")


# Tkinter starts
top = Tk()
top.title("Praamid Notifier")

frame = Frame(top)
frame.pack()

left_frame = Frame(top)
left_frame.pack(side=LEFT)

# Text of available trips
# T = Text(state=DISABLED)
T = Text()
T.pack(anchor=W)

# Radiobuttons
L1 = Label(left_frame, text="Select your trip")
L1.pack(anchor=W)

direction = StringVar()
R1 = Radiobutton(left_frame, text="Virtsu - Kuivastu", variable=direction, value="VK")
R1.select()
R1.pack(anchor=W)

R2 = Radiobutton(left_frame, text="Kuivastu - Virtsu", variable=direction, value="KV")
R2.pack(anchor=W)

R3 = Radiobutton(left_frame, text="Rohuküla - Heltermaa", variable=direction, value="RH")
R3.pack(anchor=W)

R4 = Radiobutton(left_frame, text="Heltermaa - Rohuküla", variable=direction, value="HR")
R4.pack(anchor=W)

# Datepicker
L2 = Label(left_frame, text="Select date of trip")
L2.pack(anchor=W)

E = Entry(left_frame)
E.setvar("a")
E.pack(anchor="w")

date = Datepicker(left_frame)
date.pack(anchor="w")

# Times Slider
L3 = Label(left_frame, text="Trips starting from")
L3.pack(anchor=W)

W1 = Scale(left_frame, from_=0, to=24, orient=HORIZONTAL)
W1.pack(anchor=W)

L4 = Label(left_frame, text="Trips until to")
L4.pack(anchor=W)

W2 = Scale(left_frame, from_=0, to=24, orient=HORIZONTAL)
W2.set(24)
W2.pack(anchor=W)

# Ping interval
L5 = Label(left_frame, text="Set ping interval if no tickets (minutes)")
L5.pack(anchor=W)

W3 = Scale(left_frame, from_=1, to=30, orient=HORIZONTAL)
W3.set(1)
W3.pack(anchor=W)

# Twilio SMS notifications
L6 = Label(left_frame, text="Check if you want to be notified via SMS")

L6.pack(anchor=W)
check_var = IntVar()
C = Checkbutton(left_frame, text="SMS notification (via Twilio)", variable=check_var, onvalue=1, offvalue=0)
C.pack(anchor=W)

# Bottom buttons
B1 = Button(left_frame, text="Check for tickets", command=start)
B1.pack(anchor=W)

B2 = Button(left_frame, text="Exit", command=exit_app)
B2.pack(anchor=W)

top.mainloop()
