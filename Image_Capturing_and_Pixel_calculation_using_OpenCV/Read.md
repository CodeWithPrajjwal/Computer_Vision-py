# **How It Works:**
Open the Webcam: Uses ```python
cv2.VideoCapture(0)
``` to access the default webcam.
Display Webcam Feed: Displays the video feed in a window.
Capture Image: Waits for the user to press the *'s'* key to capture an image.
Calculate Pixels: Computes the total number of pixels as the product of the image width and height.
Save Image: Saves the captured image in both JPG and PNG formats using cv2.imwrite().
Exit: Pressing *'q'* allows the user to exit the program without saving.

# **Theoritical understanding**
1. Digital Images - Raster Images:
The captured image from the webcam is a raster image (a grid of pixels), and operations like capturing, saving, and printing pixel counts directly involve raster image processing.
2. Color and Pixel-Level Operations:
The experiment involves pixel-level operations such as reading and analyzing the image's width, height, and color channels.
The image is saved in formats like JPG and PNG, showcasing how color and pixel-level data are encoded for storage.
3. Introduction to OpenCV:
The program uses OpenCV, which is a computer vision library introduced in your syllabus. OpenCV is essential for performing real-time image processing tasks such as capturing images from a webcam.
4. Camera Model and Image Acquisition:
While the experiment does not explicitly use the Pinhole Camera Model, the act of capturing an image through a webcam inherently relates to understanding how cameras capture and digitize real-world images.
5. Histogram and Image Dimensions:
The total number of pixels (calculated as height × width) is a fundamental property of an image, which is indirectly related to histograms and analyzing image data distributions.

