# ASCII - art project
# Print an image in the terminal where contours are drawn with ascii characters
# full description of the project is here:
# https://robertheaton.com/2018/06/12/programming-projects-for-advanced-beginners-ascii-art/
#
# October, 2020

import PIL
import numpy as np

from PIL import Image
# read the dimensions of the images
im = Image.open('ascii-pineapple.jpg')
#im = Image.open('IMG-20191231-WA0003.jpg')
print('Loaded image')
print('Image Size: ', im.size)
print('Resizing to quarter')
im = im.resize((round(im.size[0]/4), round(im.size[1]/4)))
print('Image Size: ', im.size)
# load image
pixel = np.array(im)
# convert from rgb to single value
#pixel_mean=pixel.mean(2)
pixel_mean=0.5*(pixel.max(2)+pixel.min(2))
#pixel_mean=0.21 * pixel[:,:,0] + 0.72 * pixel[:,:,1] + 0.07 * pixel[:,:,2]

#convert brightness numbers to ascii characters
# on dark background: darkest to bright
ascii_char="`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ncol = 255 #number of colors
nchr = len(ascii_char) #number of ascii characters
im_ascii = (pixel_mean * (nchr / ncol)).round().astype(int) - 1

print('Successfully constructed brightness matrix')
print('Brightness matrix Size: ', im_ascii.shape)

#print ascii-image
def print_ascii_image(im_ascii,ascii_char):
    I,J=im_ascii.shape
    for i in range(I):
        for j in range(J):
            #print each character in each row of your ASCII matrix three times
#            print(ascii_char[im_ascii[i][j]],end = '')
            print(ascii_char[im_ascii[i][j]]*3,end = '')
        print('')
print_ascii_image(im_ascii,ascii_char)

