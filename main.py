import tkinter
from tkinter import Tk, Label, font
import datetime
import time
import pygame
from pygame import mixer
import random_color

# initializing the GUI interface
screen = Tk()
screen.title("Atarist Clock") # clock name
screen.geometry("550x200") # screen size
# setting up fonts
my_font_1 = font.Font(family='Helvetica', size=100, weight='bold')
my_font_2 = font.Font(family='Helvetica', size=20, weight='bold')

# Adding sound to our clock
mixer.init()
mixer.music.load("Beep.wav")

# getting the current date and time
clock_time = datetime.datetime.now().strftime("%H:%M:%S")
date = datetime.datetime.now().strftime("%y/%m/%d")

# creating labels to put our time on on the GUI
time_label = Label(screen, text=clock_time, fg="#c8642d")
time_label.grid(row=1, column=3)
time_label["font"] = my_font_1
date_label = Label(screen, text=date, fg="black", bg="yellow")
date_label.grid(row=2, column=3)
date_label["font"] = my_font_2

# Infinity loop to continue updating the labels as time is moving.
while True:
    time.sleep(1) # 1 second delay
    screen.update() # allows us to run a while loop inside tkinter

    # checking the time every second
    time_now = datetime.datetime.now().strftime("%H:%M:%S")
    date = datetime.datetime.now().strftime("%y/%m/%d")

    # updating the labels
    time_label.config(text=time_now, fg=random_color.random_colour())
    date_label.config(text=date)
    mixer.music.play(0) # lopping the sound
