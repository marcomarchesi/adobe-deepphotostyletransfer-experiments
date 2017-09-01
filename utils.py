from PIL import Image
import scipy
from scipy import ndimage, misc
import numpy as np

def sobel(img_array):
    '''
    image: image to convert with Sobel filter
    '''
    dx = ndimage.sobel(img_array, 0)  # horizontal derivative
    dy = ndimage.sobel(img_array, 1)  # vertical derivative
    mag = np.hypot(dx, dy)  # magnitude, equivalent to sqrt(dx**2 + dy**2)
    mag *= 255.0 / np.max(mag)  # normalize (Q&D)
    return mag

def grayscale_sobel(img_array):
    '''
    image: image to process with Sobel filter and grayscale
    '''
    sobel_image = sobel(img_array)
    grayscale_image = Image.fromarray(np.uint8(sobel_image))
    gray_out = ndimage.imread(grayscale_image, mode="L")
    return gray_out

content_image = np.array(Image.open(""))