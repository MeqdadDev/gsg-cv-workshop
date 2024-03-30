import tkinter as tk
from PIL import ImageTk, Image
from backend.yolo_human_detection import HumanDetection
from backend.imageProcessor import apply_canny_edge, apply_dog_edge, convert_to_hsv
from backend.utils import show_error_message, show_info_message, show_warning_message, find_images_path
import os

class StitchedImageApp:
    """
        Initializes the StitchedImageApp.

        Args:
            master: The master widget.
            stitched_image: The stitched image to be displayed and manipulated.

        Attributes:
            master: The master widget.
            stitched_image: The stitched image to be displayed and manipulated.
            stitch_canvas: The canvas widget for displaying the stitched image.
            stitched_photo: The Tkinter PhotoImage of the stitched image.
            operations_note_label: A label widget for displaying the available operations.
            button_frame: A frame widget for holding the buttons.
        """
    def __init__(self, master, stitched_image):
        """
        Initializes the StitchedImageApp with the given master widget and stitched image.

        Args:
            master: The master widget.
            stitched_image: The stitched image to be displayed and manipulated.

        Returns:
            None
        """
        self.master = master
        self.master.title("Stitched Image | PixCraft")
        
        self.stitched_image = stitched_image

        self.stitch_canvas = tk.Canvas(self.master)
        self.stitch_canvas.pack()

        # Convert PIL image to Tkinter PhotoImage
        self.stitched_photo = ImageTk.PhotoImage(self.stitched_image)

        # Resize canvas to fit the stitched image
        self.stitch_canvas.config(width=self.stitched_image.width, height=self.stitched_image.height)

        # Display stitched image
        self.stitch_canvas.create_image(0, 0, anchor=tk.NW, image=self.stitched_photo)
        self.stitch_canvas.image = self.stitched_photo
        
        # Display the available operations label
        self.operations_note_label = tk.Label(self.master, text="Available Operations", font=("Arial", 14, "bold"))
        self.operations_note_label.pack(pady=5)

        # Create a new frame for the buttons
        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(pady=10)

        # Add Canny Edge Detection button
        self.canny_button = tk.Button(self.button_frame, text="Canny Edge Detection", command=self.apply_canny_edge_detection)
        self.canny_button.pack(side=tk.LEFT, padx=5)

        # Add DoG Edge Detection button
        self.dog_button = tk.Button(self.button_frame, text="DoG Edge Detection", command=self.dog_kernel_slider)
        self.dog_button.pack(side=tk.LEFT, padx=5)

        # Add HSV button
        self.hsv_button = tk.Button(self.button_frame, text="HSV", command=self.apply_hsv_conversion)
        self.hsv_button.pack(side=tk.LEFT, padx=5)
        
        # Add YOLO Human Detection button
        self.detection_button = tk.Button(self.button_frame, text="Human Detection", command=self.apply_yolo_human_detection)
        self.detection_button.pack(side=tk.LEFT, padx=5)

        # Add "Save Image" button
        save_button = tk.Button(self.button_frame, text="Save Stitched Image", command=lambda: self.save_image(self.stitched_image))
        save_button.pack(pady=3)

    def apply_canny_edge_detection(self):
        """
        Applies Canny edge detection to the stitched image.

        """
        # Apply Canny edge detection to the stitched image
        edges = apply_canny_edge(self.stitched_image)
        if edges is not None:
            window_title = "Canny Edge Detection"
            self._prepare_image_view(edges, window_title)


    def dog_kernel_slider(self):
        """
        Creates a new window for selecting the kernel size for Difference of Gaussians (DoG) edge detection.

        """
        # Create a new window for DoG edge detection
        dog_window = tk.Toplevel(self.master)
        dog_window.geometry("300x255")
        dog_window.title("Slider for DoG Kernel")

        # Add a label for the slider of kernel size
        kernel_size_label = tk.Label(dog_window, text="Kernel Size:")
        kernel_size_label.pack(pady=3)

        kernel_size_note_label = tk.Label(dog_window, text="Note: Select odd numbers for kernel", fg="red")
        kernel_size_note_label.pack(pady=3)

        # Add a slider for kernel size
        kernel_size_slider = tk.Scale(dog_window, from_=1, to=33, orient=tk.HORIZONTAL)
        kernel_size_slider.set(3)  # Initial kernel size
        kernel_size_slider.pack(pady=10)

        # Create a StringVar object to associate with the radio buttons
        option_var = tk.StringVar()
        option_var.set("open")

        # Add the radio buttons
        radio_open = tk.Radiobutton(dog_window, text="Morphological Open", variable=option_var, value="open")
        radio_open.pack(pady=5)

        radio_close = tk.Radiobutton(dog_window, text="Morphological Close", variable=option_var, value="close")
        radio_close.pack(pady=5)

        # Add a button to apply DoG edge detection
        apply_button = tk.Button(dog_window, text="Apply", command=lambda: self.apply_dog_with_kernel(kernel_size_slider.get(), option_var.get()))
        apply_button.pack(pady=3)

    def apply_dog_with_kernel(self, kernel_size, morphological_type):
        """
        Applies Difference of Gaussians (DoG) edge detection with the specified kernel size and morphological type.

        Args:
            kernel_size: The size of the kernel for edge detection (must be an odd number).
            morphological_type: The type of morphological operation to apply (open/close).

        Returns:
            None
        """
        # Check if kernel_size is an odd number
        if kernel_size % 2 == 0:
            show_error_message("Please select an odd number for the kernel size.")
            return
        # Apply Difference of Gaussians (DoG) edge detection with the specified kernel size
        edges = apply_dog_edge(self.stitched_image, kernel_size, morphological_type)
        if edges is not None:
            window_title = "Difference of Gaussians (DoG) Edge Detection"
            self._prepare_image_view(edges, window_title)

    def apply_hsv_conversion(self):
        """
        Converts the stitched image to HSV color space.

        """
        hsv_image = convert_to_hsv(self.stitched_image)
        if hsv_image is not None:
            # Convert stitched image to HSV color space
            window_title = "HSV Color Model"
            # Create a new window to display the image in HSV color mode
            self._prepare_image_view(hsv_image, window_title)

    def apply_yolo_human_detection(self):
        """
        Performs human detection using YOLO on the stitched image.

        """
        human = HumanDetection()
        confidence = 0.5 # Confidence = 50%
        detection, has_person = human.detect(self.stitched_image, conf_threshold=confidence)
        if detection is not None:
            window_title = "Human Detection using YOLO"
            
            # The path of where detection results are stored
            image_paths = find_images_path(f"{(os.getcwd())}/runs/detect/")
            detection_photo = Image.open(image_paths[0])

            self._prepare_image_view(detection_photo, window_title)

            if has_person is False:
                show_warning_message(f"No person detected in the image with confidence {confidence*100}%")

    def _prepare_image_view(self, image, title):
        """
        Creates a new window to display the images with a canvas and a "Save Image" button.

        Args:
            image: The image to display.
            title: The title of the window.

        Returns:
            None
        """

        # Create a new window to display the image
        window = tk.Toplevel(self.master)
        window.title(title)

        # Convert edges to PIL format
        photo_tk = ImageTk.PhotoImage(image)

        # Create a frame to hold the canvas and button
        frame = tk.Frame(window)
        frame.pack(padx=10, pady=10)

        # Create canvas to display image
        canvas = tk.Canvas(frame, width=image.width, height=image.height)
        canvas.pack(side=tk.TOP, pady=5)

        # Display image
        canvas.create_image(0, 0, anchor=tk.NW, image=photo_tk)
        canvas.image = photo_tk

        # Add "Save Image" button
        save_button = tk.Button(frame, text="Save Image", command=lambda: self.save_image(image))
        save_button.pack(side=tk.BOTTOM, pady=7)

    def save_image(self, image_to_save):
        """
        Saves the given image to a file (.jpg format).

        Args:
            image_to_save: The image to be saved.

        """
        if file_path := tk.filedialog.asksaveasfilename(defaultextension=".jpg"):
            try:
                image_to_save.save(file_path)
                show_info_message("Image saved successfully.")
            except Exception as e:
                show_error_message(str(e))

