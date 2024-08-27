import tkinter as tk
from tkinter import ttk, StringVar, Frame
from config import load_config, save_config

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Program Status")
        self.geometry("450x300")

        # Load offsets
        self.config = load_config()

        # Create and configure the notebook (tabs)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill='both')

        # Create tabs
        self.menu_frame = Frame(self.notebook, padx=10, pady=10)
        self.notebook.add(self.menu_frame, text="Menu Offsets")
        self.image_frame = Frame(self.notebook, padx=10, pady=10)
        self.notebook.add(self.image_frame, text="Image Offsets")

        # Create widgets for menu offsets
        self.menu_x_offset_text = StringVar(value=f"Menu X Offset: {self.config['menu_x_offset']}")
        self.menu_y_offset_text = StringVar(value=f"Menu Y Offset: {self.config['menu_y_offset']}")
        ttk.Label(self.menu_frame, textvariable=self.menu_x_offset_text).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        ttk.Label(self.menu_frame, textvariable=self.menu_y_offset_text).grid(row=1, column=0, padx=5, pady=5, sticky="e")

        # Adjust Menu X and Y offsets
        ttk.Button(self.menu_frame, text="Menu X -", command=lambda: self.adjust_menu_x_offset(-1)).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.menu_frame, text="Menu X +", command=lambda: self.adjust_menu_x_offset(1)).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(self.menu_frame, text="Menu Y -", command=lambda: self.adjust_menu_y_offset(-1)).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(self.menu_frame, text="Menu Y +", command=lambda: self.adjust_menu_y_offset(1)).grid(row=1, column=2, padx=5, pady=5)

        # Create widgets for image offsets
        self.image_x_offset_text = StringVar(value=f"Image X Offset: {self.config['image_x_offset']}")
        self.image_y_offset_text = StringVar(value=f"Image Y Offset: {self.config['image_y_offset']}")
        ttk.Label(self.image_frame, textvariable=self.image_x_offset_text).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        ttk.Label(self.image_frame, textvariable=self.image_y_offset_text).grid(row=1, column=0, padx=5, pady=5, sticky="e")

        # Adjust Image X and Y offsets
        ttk.Button(self.image_frame, text="Image X -", command=lambda: self.adjust_image_x_offset(-1)).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(self.image_frame, text="Image X +", command=lambda: self.adjust_image_x_offset(1)).grid(row=0, column=2, padx=5, pady=5)
        ttk.Button(self.image_frame, text="Image Y -", command=lambda: self.adjust_image_y_offset(-1)).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(self.image_frame, text="Image Y +", command=lambda: self.adjust_image_y_offset(1)).grid(row=1, column=2, padx=5, pady=5)

        # Status and Click Count Labels
        self.status_text = StringVar(value="Inactive")
        self.click_count_text = StringVar(value="Clicks: 0")

        self.status_label = ttk.Label(self, textvariable=self.status_text, font=("Helvetica", 14))
        self.status_label.pack(pady=10)
        self.click_count_label = ttk.Label(self, textvariable=self.click_count_text, font=("Helvetica", 12))
        self.click_count_label.pack(pady=5)

    def adjust_menu_x_offset(self, amount):
        self.config["menu_x_offset"] += amount
        self.menu_x_offset_text.set(f"Menu X Offset: {self.config['menu_x_offset']}")
        save_config(
            self.config["menu_x_offset"],
            self.config["menu_y_offset"],
            self.config["image_x_offset"],
            self.config["image_y_offset"]
        )

    def adjust_menu_y_offset(self, amount):
        self.config["menu_y_offset"] += amount
        self.menu_y_offset_text.set(f"Menu Y Offset: {self.config['menu_y_offset']}")
        save_config(
            self.config["menu_x_offset"],
            self.config["menu_y_offset"],
            self.config["image_x_offset"],
            self.config["image_y_offset"]
        )

    def adjust_image_x_offset(self, amount):
        self.config["image_x_offset"] += amount
        self.image_x_offset_text.set(f"Image X Offset: {self.config['image_x_offset']}")
        save_config(
            self.config["menu_x_offset"],
            self.config["menu_y_offset"],
            self.config["image_x_offset"],
            self.config["image_y_offset"]
        )

    def adjust_image_y_offset(self, amount):
        self.config["image_y_offset"] += amount
        self.image_y_offset_text.set(f"Image Y Offset: {self.config['image_y_offset']}")
        save_config(
            self.config["menu_x_offset"],
            self.config["menu_y_offset"],
            self.config["image_x_offset"],
            self.config["image_y_offset"]
        )
