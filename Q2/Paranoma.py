import cv2
import numpy as np

def stitch_images(images):
    """
    Stitches multiple images from left to right into a single panorama.
    
    Parameters:
        images (list): List of images (numpy arrays) to be stitched.
    
    Returns:
        Saves the final panorama as an image and displays it.
    """
    
    # Create OpenCV's Stitcher instance
    stitcher = cv2.Stitcher_create()

    # Perform stitching
    status, panorama = stitcher.stitch(images)

    if status == cv2.STITCHER_OK:
        # Display the final stitched panorama
        cv2.imshow("Curtain Panorama", panorama)
        
        # Save the resulting panorama image
        cv2.imwrite("curtain_panorama.jpg", panorama)

        # Wait for a key press and then close the display window
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error: Stitching failed. Try adjusting image overlap, alignment, or lighting.")

# Define the list of images in the correct order (left to right)
image_files = ["p1.jpg", "p2.jpg", "p3.jpg"]  
images = []

# Load images and check if all images are loaded correctly
for img_file in image_files:
    img = cv2.imread(img_file)
    if img is None:
        print(f"Error: Could not load {img_file}. Check file path and format.")
    else:
        images.append(img)

# Proceed with stitching only if all images were successfully loaded
if len(images) == len(image_files):
    stitch_images(images)
else:
    print("Error: Some images could not be loaded. Please fix file paths and try again.")
