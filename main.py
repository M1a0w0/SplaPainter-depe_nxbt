import numpy as np
from PIL import Image

img = Image.open("./input.png")
img = img.convert('1')
img = img.crop((0, 0, 320, 120))
img.save("./result.png", "PNG")

width, height = img.size
result = "10s\nA 0.1s\n5s\n"

for i in range(height):
	line = False
	for j in range(width):
		color = img.getpixel((j, i))
		if color<128:
			line = True
			break
	if line:
		for j in range(width):
			color = img.getpixel((j, i))
			if color<128:
				result += "A 0.1s\n0.1s\n"
			result +="DPAD_RIGHT 0.1s\n0.1s\n"
		result += "DPAD_DOWN 0.1s\n0.1s\nL_STICK@-100+000 3.2s\n"
	else:
		result +="DPAND_DOWN 0.1s\n0.1s\n"

file = open("./result.txt", "w")
file.write(result)
file.close()