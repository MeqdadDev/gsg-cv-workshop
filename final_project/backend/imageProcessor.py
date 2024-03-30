import cv2 as cv
import numpy as np
from PIL import Image

def apply_canny_edge(image):
    """
    Applies the Canny edge detection algorithm to the given image.

    Args:
        image (PIL.Image): The input image.

    Returns:
        Image (PIL.Image): The image with Canny edges.
    """
    # Convert image to numpy array
    image_np = np.array(image)

    # Convert image to grayscale
    gray_image = cv.cvtColor(image_np, cv.COLOR_RGB2GRAY)

    # Finding median and generating two values based on Gaussian natural distribution.
    median = np.median(gray_image)
    lower_edge = int(median * 0.68)
    upper_edge = int(median * 1.32)

    # Apply Canny edge detection
    edges = cv.Canny(gray_image, lower_edge, upper_edge)

    return Image.fromarray(edges)

def apply_dog_edge(image, kernel_size, morphological_type):
    """
    Applies the Difference of Gaussians (DoG) edge detection algorithm to the given image.

    Args:
        image (PIL.Image.Image): The input image.
        kernel_size (int): The size of the Gaussian kernel.

    Returns:
        PIL.Image.Image: The image with DoG edges.
    """
    # Convert image to numpy array
    image_np = np.array(image)

    # Convert image to grayscale
    gray_image = cv.cvtColor(image_np, cv.COLOR_RGB2GRAY)
    
    sigma1 = 3
    gaussian_kernel1 = (19, 19)
    
    sigma2 = 5
    gaussian_kernel2 = (31, 31)
    
    # Apply Difference of Gaussians (DoG) edge detection
    blurred1 = cv.GaussianBlur(gray_image, gaussian_kernel1, sigma1)
    blurred2 = cv.GaussianBlur(gray_image, gaussian_kernel2, sigma2)
    dog_img = blurred1 - blurred2

    # Apply morphological operation to clean edges
    structural_element = np.ones((kernel_size, kernel_size), np.uint8)
    if morphological_type == "close":
        cleaned_edges = cv.morphologyEx(dog_img, cv.MORPH_CLOSE, structural_element)
    elif morphological_type == "open":
        cleaned_edges = cv.morphologyEx(dog_img, cv.MORPH_OPEN, structural_element)

    return Image.fromarray(cleaned_edges)

def convert_to_hsv(image):
    """
    Converts the given image to the HSV color space.

    Args:
        image (PIL.Image.Image): The input image.

    Returns:
        PIL.Image.Image: The image in the HSV color space.
    """
    # Convert image to numpy array
    image_np = np.array(image)

    # Convert image to HSV color space
    hsv_image = cv.cvtColor(image_np, cv.COLOR_RGB2HSV)

    return Image.fromarray(hsv_image)