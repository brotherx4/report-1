# Import
import numpy as np
import numpy.fft as fourier
import sys
from scipy import misc
import matplotlib.pyplot as plt

# Displays the image from array of pixel brightness
def displayImage(im):
    # Display with grayscale colour map
    plt.imshow(im,cmap=plt.cm.gray)
    # Show the image
    plt.show()

# Creates the array from given image
def createArray(image):
    return(misc.imread(image))

# Performs FFT and conjugations to return peak shift value
def fftOperations(im):
    a = fourier.fft(im[i])
    b = fourier.fft(im[i+1])
    bConj = np.conj(b)
    c = a * bConj
    return(np.argmax(fourier.ifft(c)))

# Shifts the line with np.roll
def shift(im, peak):
    return(np.roll(im[i+1], peak))


# Reads in image from terminal
image = open(sys.argv[1], "r")

# Creates and displays the raw image
imageArray = createArray(image)
newImage = []
#displayImage(imageArray)

# Loops over entire array, checks, and shifts each line as necessary
for i in range(imageArray.shape[0]):
    # Try/Except included for last line in array
    try:
        # Finds peak and shifts if not at zero
        peak = fftOperations(imageArray)
        if peak == 0:
            newImage.append(imageArray[i+1])
        else:
            newImage.append(shift(imageArray, peak))

        peak1 = fftOperations(imageArray)
    except:
        pass


# Displays shifted image
displayImage(newImage)
