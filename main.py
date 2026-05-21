from PIL import Image , ImageDraw , ImageFont

import math

import os

from typer import getchar
# chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]

# map pixel brightness (0..255) to a character (chars ordered darkest->lightest)
# def pixel_to_char(bright):
#     bright: 0 = black, 255 = white
#     idx = int((1 - bright / 255) * (len(chars) - 1))  # 0 => darkest char
#     return chars[idx]

# Example usage inside your loops:
# h = int((r + g + b) / 3)
# ch = pixel_to_char(h)
# ...store/print ch instead of writing grayscale image...

chars = "#Wo- " [::-1]

charArray = list(chars)
charlength = len(charArray)
interval = charlength / 256

scaleFactor = 0.3

onecharwidth = 8
onecharheight = 18

def getchar(input_int):
    return charArray[math.floor(input_int * interval)]

text_file = open("output.txt", "w")

im = Image.open("img.jpg")

width, height = im.size
im = im.resize((int(scaleFactor * width), int(scaleFactor * height * (onecharwidth / onecharheight))), Image.NEAREST)
width, height = im.size
pix = im.load()

outputImage = Image.new('RGB', (onecharwidth * width, onecharheight * height), color = (255, 255, 255))
width, height = outputImage.size

print(width, height)

# iterate over the resized input image (im), not the outputImage dimensions
im_width, im_height = im.size
for i in range(im_height):
    for j in range(im_width):
        r, g, b = pix[j, i]
        h = int((r + g + b) / 3)
        pix[j, i] = (h, h, h)
        text_file.write(getchar(h))

    text_file.write("\n")


im.save("output.png")

os.startfile("output.txt")