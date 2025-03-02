# VR_Assignment1_RLakshman_IMT2022090 

README: Coin Detection & Paranoma
1. Coin Detection
Description
This program detects and counts coins in an image using OpenCV. The image is processed using grayscale conversion, Gaussian blur, and adaptive thresholding. Contours are extracted to identify coins based on their area.

Requirements
Python 3.x
OpenCV (cv2)
NumPy
Matplotlib
Installation
Install dependencies using pip:

pip install opencv-python numpy matplotlib
Usage
Place the image of coins (coins.jpg) in the same directory as the script.
Run the script:
python coin_detection.py
The output will display the detected coins and print the total count.
Output
A displayed image with detected coin contours.
Printed total number of detected coins.
2. Image Stitching (Curtain Panorama)
Description
This program stitches multiple overlapping images (left to right) into a single panorama using OpenCV’s built-in stitching function.

Requirements
Python 3.x
OpenCV (cv2)
NumPy
Installation
Install dependencies using pip:

pip install opencv-python numpy
Usage
Place the images (p1.jpg, p2.jpg, p3.jpg) in the same directory as the script.
Run the script:
python panorama_stitching.py
The final stitched image (curtain_panorama.jpg) will be displayed and saved.
Output
A displayed panoramic image of the stitched curtain.
The output image is saved as curtain_panorama.jpg.
Troubleshooting
Ensure images have sufficient overlap for better stitching.
Keep consistent lighting and alignment while capturing images.
If stitching fails, try different image sequences or increase overlap.
