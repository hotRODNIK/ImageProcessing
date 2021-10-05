# Program Name: GrayScaleBlur.py
# Programmer Name: Nick E.
# Date: 03-03-2021
# Program Description: Part One of this lab converts an image to grayscale,
# the second part blurs an image and the third part detects a line


import matplotlib.pyplot
import numpy

# This function converts the image to a grayscale
def ToGrayScale():
    # Read in the image
    myImage = matplotlib.pyplot.imread('flower.png')

    # Get the dimensions
    height=myImage.shape[0]
    width=myImage.shape[1]

    # Iterate over the image
    for x in range(0, height-1):
      for y in range(0,width-1):
        # Compute the required value for each colour channel (Source: https://en.wikipedia.org/wiki/Luma_(video))
        avg = myImage[x][y][0] * 0.2126 + myImage[x][y][1] * 0.7152 + myImage[x][y][2] * 0.0722
        myImage[x][y] = [avg, avg, avg, 1.0] # Preserve alpha value and assign proper colours

    # Plot the Image
    imgplot = matplotlib.pyplot.imshow(myImage)
    matplotlib.pyplot.show()

# This function blurs the image, it is subtle, but there is indeed a blur
def ToBlur():
    # Read in the image
    myImage = matplotlib.pyplot.imread('flower.png')

    # Get the dimensions
    height=myImage.shape[0]
    width=myImage.shape[1]

    # Iterate over the image, bounds had to be adjusted
    for x in range(1, height-2):
      for y in range(1,width-2):
        # Compute the required value for each colour channel
        # This works by computing the average of the colours of the pixel immediately above and below
        # and left and right of the current pixel
        # Gaussian blur works by considering a "rectangle" of pixels close to the current pixel
        # More weight is placed on the pixels closest to the one being examined, when the average is computed
        # One can think about this as a Bivariate Normal distribution to understand what's going on with the weights
        # Source: (https://datacarpentry.org/image-processing/06-blurring/)
        avgR = (myImage[x][y - 1][0] + myImage[x][y + 1][0] + myImage[x + 1][y][0] + myImage[x - 1][y][0]) / 4
        avgG = (myImage[x][y - 1][1] + myImage[x][y + 1][1] + myImage[x + 1][y][1] + myImage[x - 1][y][1]) / 4
        avgB = (myImage[x][y - 1][2] + myImage[x][y + 1][2] + myImage[x + 1][y][2] + myImage[x - 1][y][2]) / 4
        myImage[x][y] = [avgR, avgG, avgB, 1.0] # Preserve alpha value and assign proper colours

    # Plot the Image
    imgplot = matplotlib.pyplot.imshow(myImage)
    matplotlib.pyplot.show()
    #matplotlib.pyplot.imsave('flowerblur.png', myImage)
    # This commented out line was for testing the blur effect

# Welcome message to prompt the user and get input
print("Welcome to Nick's Image Processor \nPlease Make a Selection to Continue")
userIn = input("'G'rayscale an Image \n'B'lur an Image \n=> ")

# Decide what to do
userIn = userIn.upper()

if userIn == "G":
    ToGrayScale()
    print("Done!")
elif userIn == "B":
    ToBlur()
    print("Done!")
else:
    print("Invalid Input")
