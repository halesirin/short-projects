#Resizes and adds a "mask" over a picture to change the shirt the figure wears
from PIL import ImageOps
from PIL import Image
import sys
import os

#get the file as command-line arg
ext = os.path.splitext(sys.argv[1])
ext2 = os.path.splitext(sys.argv[2])

if (len(sys.argv)) > 3:
    sys.exit("too many command-line arguments")
elif (len(sys.argv)) < 3:
    sys.exit("too few command-line arguments")
elif ext[1].lower() not in [".png",".jpg",".jpeg"]:
    print(ext[1])
    sys.exit("Invalid input")
elif ext[1].lower() != ext2[1].lower():
    sys.exit("Input and output have different extensions")

#open shirt and input file
try:
    shirt = Image.open("shirt.png")
    before1 = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File does not exist")
#resize file
shirt_size = shirt.size
before1 = ImageOps.fit(before1, (600,600), method = Image.Resampling.BICUBIC, centering=(0.5, 0.5))
before1_size = before1.size
#overlay shirt over file
before1.paste(shirt, mask = shirt)
#save file
before1.save(f"{sys.argv[2]}")