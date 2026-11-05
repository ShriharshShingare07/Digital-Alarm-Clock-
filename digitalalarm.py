
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time
import threading

alarm_active = False

# Function to update digital clock
def update_clock():
    current_time = time.strftime("%I:%M:%S %p")
    clock_label.config(text=current_time)
    date_label.config(text=time.strftime("%A, %d %B %Y"))
    root.after(1000, update_clock)

# Function to set alarm
def set_alarm():
    global alarm_active

    alarm_time = alarm_entry.get()

    try:
        datetime.strptime(alarm_time, "%H:%M:%S")
        alarm_active = True
        status_label.config(
            text="Alarm Set Successfully!",
            fg="green"
        )
        threading.Thread(
            target=check_alarm,
            args=(alarm_time,),
            daemon=True
        ).start()

    except ValueError:
        messagebox.showerror(
            "Invalid Time",
            "Enter time in HH:MM:SS format"
        )

# Function to check alarm
def check_alarm(alarm_time):
    global alarm_active

    while alarm_active:
        current_time = datetime.now().strftime("%H:%M:%S")

        if current_time == alarm_time:
            alarm_active = False
            root.after(0, ring_alarm)
            break

        time.sleep(1)

# Function to ring alarm
def ring_alarm():
    messagebox.showinfo(
        "ALARM",
        "Wake Up! It's Time!"
    )
    status_label.config(text="Alarm Finished", fg="red")

# Function to stop alarm
def stop_alarm():
    global alarm_active
    alarm_active = False
    status_label.config(text="Alarm Stopped", fg="red")

# Main window
root = tk.Tk()
root.title("Digital Alarm Clock")
root.geometry("500x400")
root.config(bg="#17202A")
root.resizable(False, False)

# Heading
heading = tk.Label(
    root,
    text="DIGITAL ALARM CLOCK",
    font=("Arial", 22, "bold"),
    bg="#17202A",
    fg="white"
)
heading.pack(pady=20)

# Clock display
clock_label = tk.Label(
    root,
    font=("Arial", 45, "bold"),
    bg="#17202A",
    fg="#00FFCC"
)
clock_label.pack(pady=10)

# Date display
date_label = tk.Label(
    root,
    font=("Arial", 14),
    bg="#17202A",
    fg="white"
)
date_label.pack(pady=5)

# Alarm input
alarm_entry = tk.Entry(
    root,
    font=("Arial", 18),
    justify="center"
)
alarm_entry.pack(pady=15)

alarm_entry.insert(0, "HH:MM:SS")

# Set alarm button
set_button = tk.Button(
    root,
    text="SET ALARM",
    font=("Arial", 12, "bold"),
    bg="#27AE60",
    fg="white",
    command=set_alarm
)
set_button.pack(pady=8)

# Stop alarm button
stop_button = tk.Button(
    root,
    text="STOP ALARM",
    font=("Arial", 12, "bold"),
    bg="#E74C3C",
    fg="white",
    command=stop_alarm
)
stop_button.pack(pady=8)

# Status
status_label = tk.Label(
    root,
    text="No Alarm Set",
    font=("Arial", 12),
    bg="#17202A",
    fg="white"
)
status_label.pack(pady=10)

# Start clock
update_clock()

# Run application
root.mainloop()
