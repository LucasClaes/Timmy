import json

config_file = "offset_config.json"

def load_config():
    try:
        with open(config_file, "r") as f:
            data = f.read()
            if not data:  # Check if the file is empty
                return {
                    "menu_x_offset": -5,
                    "menu_y_offset": -10,
                    "image_x_offset": -5,
                    "image_y_offset": -10
                }
            return json.loads(data)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading config file: {e}")
        return {
            "menu_x_offset": -5,
            "menu_y_offset": -10,
            "image_x_offset": -5,
            "image_y_offset": -10
        }

def save_config(menu_x_offset, menu_y_offset, image_x_offset, image_y_offset):
    config = {
        "menu_x_offset": menu_x_offset,
        "menu_y_offset": menu_y_offset,
        "image_x_offset": image_x_offset,
        "image_y_offset": image_y_offset
    }
    try:
        with open(config_file, "w") as f:
            json.dump(config, f, indent=4)
    except IOError as e:
        print(f"Error saving config file: {e}")
