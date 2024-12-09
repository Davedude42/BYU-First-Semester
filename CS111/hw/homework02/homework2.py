from byuimage import Image

if __name__ == "__main__":
	pass


def flipped(filename):
	img = Image(filename)
	newImage = Image.blank(img.width, img.height)
	for y in range(img.height):
		for x in range(img.width):
			newImage.get_pixel(x, y).color = img.get_pixel(x, img.height - y - 1).color
	return newImage


def make_borders(filename, thickness, red, green, blue):
	img = Image(filename)
	newImage = Image.blank(img.width + thickness * 2, img.height + thickness * 2)
	for y in range(newImage.height):
		for x in range(newImage.width):
			if x < thickness or x >= thickness + img.width or y < thickness or y >= thickness + img.height:
				newImage.get_pixel(x, y).color = (red, green, blue)
			else:
				newImage.get_pixel(x, y).color = img.get_pixel(x - thickness, y - thickness).color
	return newImage