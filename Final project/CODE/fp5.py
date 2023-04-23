import cv2

# Load an image
img = cv2.imread('image.jpg')

# Resize the image
resized_img = cv2.resize(img, (224, 224))

# Convert the image to grayscale
gray_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

# Normalize the image
normalized_img = gray_img / 255.0