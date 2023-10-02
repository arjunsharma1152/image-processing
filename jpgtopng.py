import sys
import os
from PIL import Image

imgFolder = sys.argv[1]
outputFolder = sys.argv[2]

if not (os.path.exists(outputFolder)):
	os.makedirs(outputFolder)

for fileName in os.listdir(imgFolder):

	img = Image.open(f'{imgFolder}{fileName}')

	cleanName = os.path.splitext(fileName)[0]

	img.save(f'{outputFolder}{cleanName}.png',"png")

print("Done")