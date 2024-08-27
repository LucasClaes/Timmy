import sys
import pywinauto
import pyautogui
import cv2
import numpy as np
import time
from pywinauto.keyboard import send_keys
from pynput.keyboard import Key, Listener
from win32api import GetSystemMetrics

# Screen dimensions and scaling
Width = GetSystemMetrics(0)
Height = GetSystemMetrics(1)
Scale = int(Height / 1080)

# Toggle state for F10
toggle_active = False
Coke = "Sugar.png"

# Offsets
x_offset = -5 * Scale
y_offset = -10 * Scale

# Define the initial position
pos1 = (990 * Scale, 530 * Scale)

def load_image(image_path):
    return cv2.imread(image_path, cv2.IMREAD_COLOR)

def find_image_on_screen(image, confidence=0.8):
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screenshot_gray, image_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    if max_val >= confidence:
        return max_loc, image.shape[1::-1]  # (x, y), (width, height)
    else:
        return None, None

def click_image(location, size):
    x, y = location
    width, height = size
    center_x = x + width // 2 + x_offset
    center_y = y + height // 2 + y_offset
    pywinauto.mouse.press(button='left', coords=(center_x, center_y))
    pywinauto.mouse.release(button='left', coords=(center_x, center_y))

def open_menu():
    send_keys('{J down}')
    pywinauto.mouse.press(button='left', coords=(0, 0))
    pywinauto.mouse.release(button='left', coords=(0, 0))
    pywinauto.mouse.click(button='left', coords=(pos1))
    send_keys('{J up}')

def on_press(key):
    global toggle_active
    if key == Key.f10:
        toggle_active = not toggle_active  # Toggle the active state
        print(f"F10 pressed. Toggle is now {'active' if toggle_active else 'inactive'}.")

def on_release(key):
    # No action needed on key release in this versionj
    pass

def main():
    global toggle_active
    
    while True:
        if toggle_active:
            # Load the image
            image = load_image(Coke)
            
            # Search for the image on the screen 
            location, size = find_image_on_screen(image, confidence=0.8)

            if location:
                print(f"Image found at location: {location} with size: {size}")
                click_image(location, size)
            else:
                open_menu()
                print("Image not found on the screen. 'J' key pressed to open the menu.")
        else:
            print("Toggle is inactive. No action taken.")
        
        time.sleep(2.5)

if __name__ == "__main__":
    # Run the listener in a separate thread
    listener = Listener(on_press=on_press, on_release=on_release)
    listener.start()
    
    # Start the main loop
    main()
