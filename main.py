from PIL import Image , ImageDraw , ImageFont
import os 

import math

chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
# chars = "#Wo- " [::-1]

charArray = list(chars)
charlength = len(charArray)
interval = charlength / 256

scaleFactor = 0.2

onecharwidth = 8
onecharheight = 16

def getchar(inputInt):
    return charArray[math.floor(inputInt*interval)]

text_file = open("output.txt", "w")

im = Image.open("img.jpg")

brightness = 1.4

fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

width, height = im.size
im = im.resize((int(scaleFactor * width), int(scaleFactor*height*(onecharwidth / onecharheight))), Image.BICUBIC)
width, height = im.size
pix = im.load()

outputImage = Image.new('RGB', (onecharwidth * width, onecharheight * height), color = (0, 0, 0))
d = ImageDraw.Draw(outputImage)

for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        h = int((r + g + b) / 3)
        pix[j, i] = (h, h, h)

        text_file.write(getchar(h))
        r = int(r * brightness)
        g = int(g * brightness)
        b = int(b * brightness)

        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))
        d.text((j*onecharwidth,  i*onecharheight), getchar(h), font = fnt, fill = (r, g, b))

    text_file.write("\n")

outputImage.save('output3.png')

os.startfile("output3.png")