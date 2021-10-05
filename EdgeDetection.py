# Program Name: NickEekhofLabSix.py
# Programmer Name: Nick E.
# Date: 03-03-2021
# Program Description: This program detects the edges of an image, plots that image and then writes
# the new image to disk

import matplotlib.pyplot
import numpy

# Read in the image
myImage = matplotlib.pyplot.imread('abstract.png')

# Get the dimensions
height=myImage.shape[0]
width=myImage.shape[1]

# Iterate over the image to convert to grayscale
for x in range(0, height-1):
  for y in range(0,width-1):
    # Compute the required value for each colour channel (Source: https://en.wikipedia.org/wiki/Luma_(video))
    avg = myImage[x][y][0] * 0.2126 + myImage[x][y][1] * 0.7152 + myImage[x][y][2] * 0.0722
    myImage[x][y] = [avg, avg, avg, 1.0] # Preserve alpha value and assign proper colours

# Alert to progress
print("Converted to Grayscale, Detecting Edges...")

# Define a threshold
threshold = 0.1

# Find the edges, but make sure values are adjusted accordingly
for x in range(0, height - 2):
    for y in range(0, width - 2):
        # Get the value of the pixel to the right and below and compute the difference
        right = numpy.sum(myImage[x + 1][y])
        below = numpy.sum(myImage[x][y + 1])
        difference = abs(right - below)

        # Compare to threshold and detect edges
        if difference >= threshold:
            myImage[x][y] = [0.0, 0.0, 0.0, 1.0] # preserve alpha value
        else:
            myImage[x][y] = [1.0, 1.0, 1.0, 1.0]

# Plot the Image
print("Edges Detected, Plotting...")
imgplot = matplotlib.pyplot.imshow(myImage)
print("Done!")
print("Writing Image to Disk....")
matplotlib.pyplot.imsave("edges.png", myImage)
print("Done!")
matplotlib.pyplot.show()
