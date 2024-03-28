"""
Author: #Smart_Coder
--> #Smart_Coder Third Umpire Decision Review System
Version: 1.0
"""

# Importing Modules
import tkinter as tk
from PIL import Image, ImageTk
from cv2 import VideoCapture, CAP_PROP_POS_FRAMES, resize,  cvtColor, COLOR_BGR2RGB, imread
import threading
import time
import tkinter.messagebox as tmsg

width = 650
height = 370

stream = VideoCapture("clip.mp4")

def play(speed):
    frame1 = stream.get(CAP_PROP_POS_FRAMES)
    stream.set(CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    try:
        frame = resize(frame, (width, height))
        frame = cvtColor(frame, COLOR_BGR2RGB)
        frame = ImageTk.PhotoImage(image=Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, 0, image=frame, anchor=tk.NW)
    except:
        tmsg.showinfo("#Smart_Coder Third Umpire Decision Review System", "The video has ended.")

def pending(decision):
    # 1. Display Decision Pending Image
    frame = cvtColor(imread("asset/pending.png"), COLOR_BGR2RGB)
    frame = ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tk.NW)
    canvas.grid(row=0, column=0, columnspan=2)

    # Wait 2 Second..
    time.sleep(2)

    # Show Sponsorship...
    frame = cvtColor(imread("asset/sponser.png"), COLOR_BGR2RGB)
    frame = ImageTk.PhotoImage(image=Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tk.NW)
    canvas.grid(row=0, column=0, columnspan=2)

    # Wait 2 Second..
    time.sleep(2)

    # Show Decision
    if decision:
        frame = cvtColor(imread("asset/out.png"), COLOR_BGR2RGB)
        frame = ImageTk.PhotoImage(image=Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, 0, image=frame, anchor=tk.NW)
        canvas.grid(row=0, column=0, columnspan=2)

    else:
        frame = cvtColor(imread("asset/not_out.png"), COLOR_BGR2RGB)
        frame = ImageTk.PhotoImage(image=Image.fromarray(frame))
        canvas.image = frame
        canvas.create_image(0, 0, image=frame, anchor=tk.NW)
        canvas.grid(row=0, column=0, columnspan=2)


def out():
    answer = tmsg.askyesno("#Smart_Coder Third Umpire Decision Review System", "Are you Sure to Give Out ?")

    if answer:
        thread = threading.Thread(target=pending, args=(True,))
        thread.daemon = True  # Correct assignment of daemon property
        thread.start()


def not_out():
    answer = tmsg.askyesno("#Smart_Coder Third Umpire Decision Review System", "Are you Sure Not to Give Out ?")

    if answer:
        thread = threading.Thread(target=pending, args=(False,))
        thread.daemon = True  # Correct assignment of daemon property
        thread.start()


# Tkinter GUI
window = tk.Tk()
window.title("#Smart_Coder Third Umpire Decision Review System")
window.wm_iconbitmap("asset/icon.ico")
window.resizable(False, False)

cv_img = cvtColor(imread("asset/welcome.png"), COLOR_BGR2RGB)
canvas = tk.Canvas(window, width=width, height=height)
photo = ImageTk.PhotoImage(image=Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, anchor=tk.NW, image=photo)
canvas.grid(row=0, column=0, columnspan=3)

# Configure column weights to resize proportionally
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)

# Buttons to control playback
btn = tk.Button(window, text="Previous (Slow)", command=lambda: play(-2))
btn.grid(row=1, column=0, sticky="ew", padx=20, pady=5)

btn = tk.Button(window, text="Previous (Fast)", command=lambda: play(-25))
btn.grid(row=1, column=1, sticky="ew", padx=20, pady=5)

btn = tk.Button(window, text="Next (Slow)", command=lambda: play(2))
btn.grid(row=2, column=0, sticky="ew", padx=20, pady=5)

btn = tk.Button(window, text="Next (Fast)", command=lambda: play(25))
btn.grid(row=2, column=1, sticky="ew", padx=20, pady=5)

btn = tk.Button(window, text="Give Out !!", command=out)
btn.grid(row=3, column=0, sticky="ew", columnspan=2, padx=20, pady=5)

btn = tk.Button(window, text="Give Not Out !!", command=not_out)
btn.grid(row=4, column=0, sticky="ew", columnspan=2, padx=20, pady=5)

window.mainloop()