import sqlite3
from PIL import Image
import io

def import_images_from_database(database_path):EE
    # Connect to the database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    # Query the database for images
    cursor.execute("SELECT image_data FROM images")
    images = cursor.fetchall()

    # Convert the image data into PIL Image objects
    pil_images = []
    for image in images:
        image_data = image[0]
  pil_image = Image.open(io.BytesIO(image_data))
        pil_images.append(pil_image)

    # Close the database connection
    connection.close()

    return pil_images

# Example usage
images = import_images_from_database('images.db')
for i, image in enumerate(images):
    image.save(f'image_{i}.png')
# Define the number of times to loop
num_loops = 5

# Loop using a for loop
for i in range(num_loops):
    # Code to execute on each iteration
    print(f'Loop {i + 1} of {num_loops}')

# Loop using a while loop
i = 0
while i < num_loops:
    # Code to execute on each iteration
    print(f'Loop {i + 1} of {num_loops}')
    i += 1
from PIL import Image

def convert_to_black_and_white(image_path):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to black and white
    black_and_white_image = image.convert('L')

    # Save the black and white image
    black_and_white_image.save('black_and_white.png')

# Example usage
convert_to_black_and_white('image.png')
from PIL import Image
import numpy as np

def compare_images(image1_path, image2_path):
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Convert images to numpy arrays
    image1_array = np.asarray(image1)
    image2_array = np.asarray(image2)

    # Compare the two images
     if image1_array.shape == image2_array.shape:
        difference = np.sum(image1_array - image2_array)
        if difference == 0:
            print("The images are the same")
        else:
            print("The images are different")
    else:
        print("The images have different dimensions and cannot be compared")

# Example usage
compare_images('image1.png', 'image2.png')
from PIL import Image
from PIL import ImageStat

def measure_contrast(image_path):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to grayscale
    grayscale_image = image.convert('L')

    # Calculate the contrast level
    stat = ImageStat.Stat(grayscale_image)
    contrast = stat.stddev[0]

    return contrast
# Example usage
contrast = measure_contrast('image.png')
print(f'Contrast: {contrast}')