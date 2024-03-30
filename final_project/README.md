# Final Project
# Project Document: AI-Enhanced Image Stitching and Edge Detection

## Goal
The goal of this project is to develop an application that allows users to select a group of images, which the application will then stitch together into a single panoramic image. This stitched image will undergo multiple edge detection processes using different techniques: Canny Edge Detection, Difference of Gaussians (DoG) with an adjustable morphological operation, and an AI-based edge
detector specifically tuned to recognize human figures with a confidence level of more than 50%.

The application will provide an interactive interface for users to adjust parameters and visually compare the results of different edge detection techniques.

## Requirements
### Functional Requirements:

**Image Selection and Stitching:**

* The application must include a user interface (UI) component to allow users to select a group of images from their computer.

* Stitch the selected images into a single panoramic image.

* Display both the individual images and the stitched panoramic image within the application on a first window.

**Edge Detection Implementation:**

* Apply Canny Edge Detection to the stitched image and display the result.

* Implement Difference of Gaussians (DoG) edge detection followed by a morphological operation to clean the results.

* Provide a user interface component (e.g., a slider) to adjust the kernel size of the morphological operation. The kernel shape can be any form selected by the developer.

* Display both results and the slider on a second window.

**AI-based Human Edge Detection:**

* Implement an AI-based object detection model capable of identifying human figures within the stitched image.

* The model should filter and display only those detections with a confidence level above 50%.

* The results should be visually represented on the stitched image, clearly marking detected human figures on a third window.

**User Interface:**

* Develop a simple, intuitive user interface that allows users to upload images, view processed results, and adjust Morphological Operations’ parameters dynamically.

## Non-functional Requirements:

**Performance**: The application should process images and perform edge detection efficiently, ensuring a responsive user experience.

**Usability**: The interface should be user-friendly, with clear instructions and feedback for users to easily navigate and use the application's features.

**Scalability**: The design should accommodate future enhancements, such as the addition of new edge detection algorithms or support for larger image sets.

----
## Screenshots for the Project (PixCraft)

### Welcome Screen

<p align="center">
<picture>
  <img alt="PixCraft Screenshot" src="screenshots/1.png" width="80%" hight="80%" >
</picture>
</p>

### Selecting Images from PC

<p align="center">
<picture>
  <img alt="PixCraft Screenshot" src="screenshots/2.png" width="80%" hight="80%" >
</picture>
</p>

### Generate Stitched Image with Available Operations

<p align="center">
<picture>
  <img alt="PixCraft Screenshot" src="screenshots/3.png" width="80%" hight="80%" >
</picture>
</p>

### Canny Edge Detection

<p align="center">
<picture>
  <img alt="PixCraft Screenshot" src="screenshots/4.png" width="80%" hight="80%" >
</picture>
</p>

### DoG with Morphological Operation and Kernel Slider

<p align="center">
<picture>
  <img alt="PixCraft Screenshot" src="screenshots/5.png" width="40%" hight="40%" >
</picture>
</p>

### DoG Edge Detection

<p align="center">
<picture>
  <img alt="PixCraft Screenshot" src="screenshots/6.png" width="80%" hight="80%" >
</picture>
</p>

### HSV Color Model

<p align="center">
<picture>
  <img alt="PixCraft Screenshot" src="screenshots/7.png" width="80%" hight="80%" >
</picture>
</p>

### Human Detection using YOLO v8.1

<p align="center">
<picture>
  <img alt="PixCraft Screenshot" src="screenshots/8.png" width="80%" hight="80%" >
</picture>
</p>

### Warning, Error and Informational Messages

<p align="center">
<picture>
  <img alt="PixCraft Screenshot" src="screenshots/9.png" width="40%" hight="40%" >
</picture>
</p>

<p align="center">
<picture>
  <img alt="PixCraft Screenshot" src="screenshots/10.png" width="40%" hight="40%" >
</picture>
</p>

<p align="center">
<picture>
  <img alt="PixCraft Screenshot" src="screenshots/11.png" width="40%" hight="40%" >
</picture>
</p>
