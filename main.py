import sys
import pywinauto
import pyautogui
import cv2
import numpy as np
import time
from pynput.keyboard import Key, Listener, Controller
from win32api import GetSystemMetrics


Width = GetSystemMetrics(0)
Height = GetSystemMetrics(1)
print(Height)
Scale = int(Height / 1080)

alt_down = False
Coke = "Sugar.png"

#offsets
x_offset = -5 * Scale
y_offset = -10 * Scale

# Define the initial position
pos1 = (990*Scale, 530*Scale)

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
    pywinauto.mouse.press(button='left', coords=(0, 0))
    pywinauto.mouse.release(button='left', coords=(0, 0))
    pywinauto.mouse.click(button='left', coords=(pos1)) 

def on_press(key):
    global alt_down
    if key == Key.alt_l or key == Key.alt_r:  # Check both left and right Alt keys
        alt_down = True

def on_release(key):
    global alt_down
    if key == Key.alt_l or key == Key.alt_r:  # Check both left and right Alt keys
        alt_down = False
        print("Alt key released")

def main():
    global alt_down
    controller = Controller()
    
    while True:
        # Load the image
        image = load_image(Coke)
        
        # Search for the image on the screen 
        location, size = find_image_on_screen(image, confidence=0.8)

        if location and alt_down:
            print(f"Image found at location: {location} with size: {size}")
            click_image(location, size)
        elif not location and alt_down:
            open_menu()
            print("Image not found on the screen.")
        else:
            print("Alt key is not pressed. No action taken.")

        time.sleep(2.5)

if __name__ == "__main__":
    # Run the listener in a separate thread
    listener = Listener(on_press=on_press, on_release=on_release)
    listener.start()
    
    # Start the main loop
    main()