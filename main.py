import subprocess
import numpy
from datetime import date, timedelta
from PIL import Image

pixels = []

im = Image.open('image.png')
pix = im.convert("RGB")

for x in range(pix.width):
    for y in range(pix.height):
        pixels.append(pix.getpixel((x,y)))

start = date(2021, 1, 3)

dates = []

count = 0
for i in pixels:
    if i == (0,0,0):
        dates.append(start + timedelta(count))
    count += 1


for day in dates:
    subprocess.call("git add .")
    subprocess.call("git commit --date \"" + str(day) + "\" -m \"bananana\"")
    subprocess.call("git push GitArt master")
    
    file = open("./dummy.txt", "a")
    file.write("1\n")
    file.close()
