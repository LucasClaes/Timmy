import pywinauto
import cv2
import numpy as np
from PIL import ImageGrab

def load_image(image_path):
    return cv2.imread(image_path, cv2.IMREAD_COLOR)

def find_image_on_screen(image, confidence=0.8):
    screenshot = ImageGrab.grab()
    screenshot_np = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_BGR2GRAY)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(screenshot_gray, image_gray, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    
    if max_val >= confidence:
        return max_loc, image.shape[1::-1]  # (x, y), (width, height)
    return None, None

def click_image(location, size, x_offset, y_offset):
    x, y = location
    width, height = size
    center_x = x + width // 2 + x_offset
    center_y = y + height // 2 + y_offset
    pywinauto.mouse.click(button='left', coords=(center_x, center_y))

def open_menu(x_offset, y_offset, pos1):
    pywinauto.keyboard.send_keys('{J down}')
    pywinauto.mouse.click(button='left', coords=(0, 0))
    pywinauto.mouse.click(button='left', coords=pos1)
    pywinauto.keyboard.send_keys('{J up}')
