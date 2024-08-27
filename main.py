import threading
import time
from tkinter import StringVar
from gui import Application
from input_handling import start_listener
from image_processing import load_image, find_image_on_screen, click_image, open_menu
from config import load_config

def main_loop(app):
    config = load_config()
    toggle_active = False
    click_count = 0
    
    while True:
        if toggle_active:
            image = load_image("Sugar.png")
            location, size = find_image_on_screen(image, confidence=0.8)
            
            if location:
                click_image(location, size, config["image_x_offset"], config["image_y_offset"])
                click_count += 1
                app.click_count_text.set(f"Clicks: {click_count}")
            else:
                open_menu(config["menu_x_offset"], config["menu_y_offset"], (990 * Scale, 530 * Scale))
                app.status_text.set("Image not found. Menu opened.")
        else:
            app.status_text.set("Inactive")
        
        time.sleep(2.5)

if __name__ == "__main__":
    app = Application()
    
    # Start the keyboard listener
    start_listener(app.status_text)
    
    # Start the main processing loop in a separate thread
    processing_thread = threading.Thread(target=main_loop, args=(app,), daemon=True)
    processing_thread.start()
    
    # Start the GUI event loop
    app.mainloop()
