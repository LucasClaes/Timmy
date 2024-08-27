from pynput.keyboard import Key, Listener
from tkinter import StringVar

toggle_active = False

def on_press(key, status_text):
    global toggle_active
    if key == Key.f10:
        toggle_active = not toggle_active  # Toggle the active state
        status_text.set("Active" if toggle_active else "Inactive")

def on_release(key):
    # No action needed on key release in this version
    pass

def start_listener(status_text):
    listener = Listener(on_press=lambda key: on_press(key, status_text), on_release=on_release)
    listener.start()
