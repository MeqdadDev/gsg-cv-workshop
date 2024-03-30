import cv2
from PIL import Image
from backend.utils import show_error_message

class ImageStitcher:
    """
    A class for stitching multiple images together.

    Methods:
        stitch_images: Stitches the given image paths together.
        _resize_stitched_image: Resizes the stitched image to fit the screen.
    """

    @staticmethod
    def stitch_images(image_paths, master):
        """
        Stitches the given image paths together.

        Args:
            image_paths (list): A list of image paths to be stitched.
            master: The main window instance.

        Returns:
            tuple: A tuple containing the stitched image (PIL format) and the list of input images.
                   Returns (None, None) if there is an error.
        """
        # Check if at least two images are provided
        if len(image_paths) < 2:
            show_error_message("Please select at least two images for stitching.")
            return None, None

        try:
            # Load all selected images
            images = [cv2.imread(image_path) for image_path in image_paths]

            # Stitch images
            stitcher = cv2.Stitcher_create()
            status, stitched_image = stitcher.stitch(images)

            if status == cv2.Stitcher_OK:
                # Convert stitched image to RGB and PIL format
                stitched_image = cv2.cvtColor(stitched_image, cv2.COLOR_BGR2RGB)
                stitched_image_pil = ImageStitcher._resize_stitched_image(stitched_image, master)

                return stitched_image_pil, images
            else:
                show_error_message("Image stitching failed. No feature matching!")
                return None, None
        except Exception as e:
            show_error_message(f"An error occurred: {str(e)}")
            return None, None

    @staticmethod
    def _resize_stitched_image(stitched_image, master):
        """
        Resizes the stitched image to fit the screen.

        Args:
            stitched_image (numpy.ndarray): The stitched image in OpenCV format.
            master: The main window instance.

        Returns:
            PIL.Image: The resized stitched image in PIL format.
        """
        image_height, image_width, _ = stitched_image.shape
        aspect_ratio = image_width / image_height

        # Resize the stitched image to fit the screen
        window_width = master.winfo_screenwidth()
        window_height = master.winfo_screenheight()
        if window_width / aspect_ratio > window_height:
            window_width = int(window_height * aspect_ratio)
        else:
            window_height = int(window_width / aspect_ratio)
        resized_image = cv2.resize(stitched_image, (window_width, window_height), interpolation=cv2.INTER_AREA)
        return Image.fromarray(resized_image)