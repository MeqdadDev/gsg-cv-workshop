import tkinter.messagebox as messagebox
import os

def show_error_message(message):
    """
    Displays an error message using a Tkinter messagebox.

    Args:
        message (str): The error message to display.
    """
    messagebox.showerror("Error", message)

def show_info_message(message):
    """
    Displays an information message using a Tkinter messagebox.

    Args:
        message (str): The information message to display.
    """
    messagebox.showinfo("Information", message)

def show_warning_message(message):
    """
    Displays a warning message using a Tkinter messagebox.

    Args:
        message (str): The warning message to display.
    """
    messagebox.showwarning("Warning", message)

def find_images_path(path):
    """
    Finds and returns a list of image paths in the given directory.

    Args:
        path: The directory path to search for images.

    Returns:
        list: A list of image paths found in the directory.

    """
    image_paths = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            # Check for common image extensions
            if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
                image_paths.append(os.path.join(dirpath, filename))
    return image_paths
