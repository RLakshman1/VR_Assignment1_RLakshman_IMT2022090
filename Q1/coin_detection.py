import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = "coins.jpg"  # Update path if needed
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (15, 15), 0)

# Apply adaptive thresholding for better detection
adaptive_thresh = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
)

# Find contours
contours, _ = cv2.findContours(adaptive_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours based on area to remove noise
min_area = 1000  # Adjusted based on expected coin size
filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

# Draw detected contours
output_contours = image.copy()
for cnt in filtered_contours:
    cv2.drawContours(output_contours, [cnt], -1, (0, 255, 0), 2)

# Display the result
plt.figure(figsize=(6, 6))
plt.imshow(cv2.cvtColor(output_contours, cv2.COLOR_BGR2RGB))
plt.title(f"Detected Coins: {len(filtered_contours)}")
plt.axis("off")
plt.show()

# Print total number of coins detected
print(f"Total Coins Detected: {len(filtered_contours)}")
