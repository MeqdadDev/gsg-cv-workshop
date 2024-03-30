import contextlib
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from datetime import datetime
import os
import shutil
from backend.imageStitcher import ImageStitcher
from gui.stitchedImage import StitchedImageApp

class ImageSelectorApp:
    """
    A class representing an image selector application.

    Args:
        master: The master widget.

    Attributes:
        selected_images: A list of selected image paths.
        program_title_label: A label widget for the program title.
        image_frame: A frame widget for displaying images.
        add_button: A button widget for adding images.
        stitch_button: A button widget for stitching images.
        note_label: A label widget for deleting images note.
        copy_right_label: A label widget for the copyright notice.

    Methods:
        select_images: Prompts the user to select images and adds them to the selected images list.
        display_image: Displays an image in the image frame.
        stitch_images: Stitches the selected images together.
        delete_image: Deletes the selected image from the list of selected images.

    """
    def __init__(self, master):
        """
        Initializes the ImageSelectorApp.

        Args:
            master: The master widget.

        """
        self.master = master
        self.selected_images = []

        self.program_title_label = tk.Label(self.master, text="PixCraft", font=("Consolas", 18, "bold"))
        self.program_title_label.pack(pady=10)

        # A frame widget for holding the selected images.
        self.image_frame = tk.Frame(self.master)
        self.image_frame.pack()

        self.add_button = tk.Button(self.master, text="Add Images", command=self.select_images)
        self.add_button.pack(pady=30)

        self.stitch_button = tk.Button(self.master, text="Stitch Images", command=self.stitch_images, state=tk.DISABLED)
        self.stitch_button.pack()

        # Add a note label for deleting images
        self.note_label = tk.Label(self.master, text="Right-click on an image to delete it.")
        self.note_label.pack(pady=10)

        # Add copyright label
        self.copy_right_label = tk.Label(self.master, text="\u00a9" + " " + str(datetime.now().year) + " Meqdad Darwish", fg="gray", font=("Helvetica", 8))
        self.copy_right_label.pack(side=tk.BOTTOM)

    def select_images(self):
        """
        Prompts the user to select images and adds them to the selected images list.

        """
        file_paths = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif")])
        for file_path in file_paths:
            self.selected_images.append(file_path)
            self.display_image(file_path)
        # Enable the "Stitch Images" button
        self.stitch_button.config(state=tk.NORMAL)

    def display_image(self, file_path):
        """
        Displays an image in the image frame.

        Args:
            file_path: The path of the image file.

        """
        image = Image.open(file_path)
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(self.image_frame, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        label.pack(side=tk.LEFT)

        # Store the image path in the label widget
        label.image_path = file_path

        # Bind a right-click event to the label
        label.bind('<Button-3>', self.delete_image)

    def stitch_images(self):
        """
        Stitches the selected images together.

        """

        self.clean_detection_outputs()
        stitched_image, _ = ImageStitcher.stitch_images(self.selected_images, self.master)
        if stitched_image is not None:
            stitch_window = tk.Toplevel(self.master)
            StitchedImageApp(stitch_window, stitched_image)
    
    def delete_image(self, event):
        """
        Deletes the selected image from the list of selected images.
        
        Args:
            event (tk.Event): The event object containing information about the event.
        """
        widget = event.widget
        image_path = widget.image_path  # Assuming you store the image path in the widget

        with contextlib.suppress(ValueError):
            self.selected_images.remove(image_path)
            widget.pack_forget()  # Hide the image label

    @staticmethod
    def clean_detection_outputs(dir_to_clean="runs"):
        current_dir = os.getcwd()
        detection_outputs = f"{current_dir}/{dir_to_clean}"
        with contextlib.suppress(Exception):
            if os.path.exists(detection_outputs):
                shutil.rmtree(detection_outputs)