#Name of the image to click on
Coke = "Sugar.png"
x_offset = -10
y_offset = -20
pos1 = (990*2, 530*2)

import sys
import pywinauto
import pyautogui
import cv2
import numpy as np
import time
from pynput.keyboard import Key, Listener, Controller
from waiting import wait
alt_down = False


def load_image(image_path):
    return cv2.imread(image_path, cv2.IMREAD_COLOR)

def find_image_on_screen(image, confidence=0.8):
    # Take a screenshot of the current screen
    screenshot = pyautogui.screenshot()
    
    # Convert the screenshot to a numpy array
    screenshot_np = np.array(screenshot)
    
    # Convert the screenshot to grayscale for template matching
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
    
    # Convert the image to grayscale for template matching
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Perform template matching
    result = cv2.matchTemplate(screenshot_gray, image_gray, cv2.TM_CCOEFF_NORMED)
    
    # Get the best match position
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    if max_val >= confidence:
        # If the confidence is high enough, return the top-left corner of the match
        return max_loc, image.shape[1::-1]  # (x, y), (width, height)
    else:
        # If no match is found, return None
        return None, None

def click_image(location, size):
    x, y = location
    width, height = size
    # Calculate the center of the matched region
    center_x = x + width // 2 + x_offset
    center_y = y + height // 2 + y_offset
    pywinauto.mouse.press(button='left', coords=(center_x, center_y))
    pywinauto.mouse.release(button='left', coords=(center_x, center_y))
    # Move the mouse to the center of the matched region and click

def open_menu():
    pywinauto.mouse.press(button='left', coords=(0, 0))
    pywinauto.mouse.release(button='left', coords=(0, 0))
    #pyautogui.click()
    #time.sleep(0.5)
    #pyautogui.click(pos1)
    #pyautogui.keyDown
    pywinauto.mouse.click(button='left', coords=(pos1)) 




def main():
    controller = Controller()
    while True:
        
        # Collect events until released
        with Listener(on_press=on_press,on_release=on_release) as listener:
            # Load the image
            image = load_image(Coke)
        
            # Search for the image on the screen 
            location, size = find_image_on_screen(image, confidence=0.8)

            if location:
                print(f"Image found at location: {location} with size: {size}")
                # Click on the image if found
                click_image(location, size)
            else:
                open_menu()
                print("Image not found on the screen.")


        time.sleep(1)

if __name__ == "__main__":
        main()
