from byuimage import Image
import sys

def main():
	args = sys.argv[1:]

	if not validate_commands(args):
		print("Wrong arguments!!!!!!!")
		return

	flag = args[0]
	restArgs = args[1:]

	if flag == '-d':
		display(restArgs[0])
	elif flag == '-k':
		darken(restArgs[0], restArgs[1], float(restArgs[2]))
	elif flag == '-s':
		sepia(restArgs[0], restArgs[1])
	elif flag == '-g':
		grayscale(restArgs[0], restArgs[1])
	elif flag == '-b':
		make_borders(restArgs[0], restArgs[1], int(restArgs[2]), int(restArgs[3]), int(restArgs[4]), int(restArgs[5]))
	elif flag == '-f':
		flipped(restArgs[0], restArgs[1])
	elif flag == '-m':
		mirror(restArgs[0], restArgs[1])
	elif flag == '-c':
		collage(restArgs[0], restArgs[1], restArgs[2], restArgs[3], restArgs[4], int(restArgs[5]))
	elif flag == '-y':
		greenscreen(restArgs[0], restArgs[1], restArgs[2], float(restArgs[3]), float(restArgs[4]))

def validate_commands(args):
	if len(args) == 0:
		return False
	flag = args[0]
	restArgs = args[1:]

	if flag == '-d' and len(restArgs) == 1:
		return True
	if flag == '-k' and len(restArgs) == 3:
		return True
	if flag == '-s' and len(restArgs) == 2:
		return True
	if flag == '-g' and len(restArgs) == 2:
		return True
	if flag == '-b' and len(restArgs) == 6:
		return True
	if flag == '-f' and len(restArgs) == 2:
		return True
	if flag == '-m' and len(restArgs) == 2:
		return True
	if flag == '-c' and len(restArgs) == 6:
		return True
	if flag == '-y' and len(restArgs) == 5:
		return True

	return False

def display(filename):
	Image(filename).show()

def darken(filename, outputFilename, percent):
	img = Image(filename)
	s = 1 - percent
	for p in img:
		p.red *= s
		p.green *= s
		p.blue *= s
	img.save(outputFilename)

def sepia(filename, outputFilename):
	img = Image(filename)
	for pixel in img:
		true_red = 0.393*pixel.red + 0.769*pixel.green + 0.189*pixel.blue
		true_green = 0.349*pixel.red + 0.686*pixel.green + 0.168*pixel.blue
		true_blue = 0.272*pixel.red + 0.534*pixel.green + 0.131*pixel.blue

		pixel.red = min(true_red, 255)
		pixel.green = min(true_green, 255)
		pixel.blue = min(true_blue, 255)
	img.save(outputFilename)

def grayscale(filename, outputFilename):
	img = Image(filename)
	for pixel in img:
		pixel.red, pixel.green, pixel.blue = ((pixel.red + pixel.green + pixel.blue) / 3,) * 3
	img.save(outputFilename)

def make_borders(filename, outputFilename, thickness, red, green, blue):
	img = Image(filename)
	newImage = Image.blank(img.width + thickness * 2, img.height + thickness * 2)
	for y in range(newImage.height):
		for x in range(newImage.width):
			if x < thickness or x >= thickness + img.width or y < thickness or y >= thickness + img.height:
				newImage.get_pixel(x, y).color = (red, green, blue)
			else:
				newImage.get_pixel(x, y).color = img.get_pixel(x - thickness, y - thickness).color
	newImage.save(outputFilename)

def flipped(filename, outputFilename):
	img = Image(filename)
	newImage = Image.blank(img.width, img.height)
	for y in range(img.height):
		for x in range(img.width):
			newImage.get_pixel(x, y).color = img.get_pixel(x, img.height - y - 1).color
	newImage.save(outputFilename)

def mirror(filename, outputFilename):
	img = Image(filename)
	newImage = Image.blank(img.width, img.height)
	for y in range(img.height):
		for x in range(img.width):
			newImage.get_pixel(x, y).color = img.get_pixel(img.width - x - 1, y).color
	newImage.save(outputFilename)

def collage(file1, file2, file3, file4, outputFilename, thickness):
	img1 = Image(file1)
	img2 = Image(file2)
	img3 = Image(file3)
	img4 = Image(file4)

	ni = Image.blank(thickness * 3 + img1.width + img2.width, thickness * 3 + img1.height + img3.height)

	for y in range(ni.height):
		for x in range(ni.width):
			if x >= thickness and y >= thickness:
				if x < thickness + img1.width:
					if y < thickness + img1.height:
						ni.get_pixel(x, y).color = img1.get_pixel(x - thickness, y - thickness).color
					elif y >= thickness * 2 + img1.height and y < thickness * 2 + img1.height * 2:
						ni.get_pixel(x, y).color = img3.get_pixel(x - thickness, y - thickness * 2 - img1.height).color
					else:
						ni.get_pixel(x, y).color = (0, 0, 0)
				elif x >= thickness * 2 + img1.width and x < thickness * 2 + img1.width * 2:
					if y < thickness + img1.height:
						ni.get_pixel(x, y).color = img2.get_pixel(x - thickness * 2 - img1.width, y - thickness).color
					elif y >= thickness * 2 + img1.height and y < thickness * 2 + img1.height * 2:
						ni.get_pixel(x, y).color = img4.get_pixel(x - thickness * 2 - img1.width, y - thickness * 2 - img1.height).color
					else:
						ni.get_pixel(x, y).color = (0, 0, 0)
				else:
					ni.get_pixel(x, y).color = (0, 0, 0)
			else:
				ni.get_pixel(x, y).color = (0, 0, 0)
	
	ni.save(outputFilename)

def detect_green(pixel, threshold, factor):
	average = (pixel.red + pixel.green + pixel.blue) / 3
	if pixel.green >= factor * average and pixel.green > threshold:
		return True
	else:
		return False
		
def greenscreen(forfile, backfile, outimg, threshold, factor):
	forimg = Image(forfile)
	backimg = Image(backfile)
	newImage = Image.blank(forimg.width, forimg.height)

	for y in range(newImage.height):
		for x in range(newImage.width):
			if detect_green(forimg.get_pixel(x, y), threshold, factor):
				newImage.get_pixel(x, y).color = backimg.get_pixel(x, y).color
			else:
				newImage.get_pixel(x, y).color = forimg.get_pixel(x, y).color
	newImage.save(outimg)

if __name__ == "__main__":
	main()