from byuimage import Image

def iron_puzzle(filename):
    img = Image(filename)
    for pixel in img:
        pixel.red = 0
        pixel.green = 0
        pixel.blue *= 10
    return img


def west_puzzle(filename):
    img = Image(filename)
    for pixel in img:
        pixel.red = 0
        pixel.green = 0
        pixel.blue = (pixel.blue * 16) if pixel.blue < 16 else 0
    return img


def darken(filename, percent):
    img = Image(filename)
    for pixel in img:
        pixel.red   *= 1 - percent
        pixel.green *= 1 - percent
        pixel.blue  *= 1 - percent
    return img


def grayscale(filename):
    img = Image(filename)
    for pixel in img:
        pixel.red, pixel.green, pixel.blue = ((pixel.red + pixel.green + pixel.blue) / 3,) * 3
    return img


def sepia(filename):
    img = Image(filename)
    for pixel in img:
        true_red = 0.393*pixel.red + 0.769*pixel.green + 0.189*pixel.blue
        true_green = 0.349*pixel.red + 0.686*pixel.green + 0.168*pixel.blue
        true_blue = 0.272*pixel.red + 0.534*pixel.green + 0.131*pixel.blue

        pixel.red = min(true_red, 255)
        pixel.green = min(true_green, 255)
        pixel.blue = min(true_blue, 255)
    return img
    


def create_left_border(filename, weight):
    old_img = Image(filename)
    img = Image.blank(old_img.width + weight, old_img.height)

    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x, y)
            if x < weight:
                pixel.color = (0, 0, 255)
            else:
                pixel.color = old_img.get_pixel(x - weight, y).color
    
    return img


###################################################
# Code below here is for extra practice and doesn't count for or against
# your grade on this lab.
def create_stripes(filename):
    "*** YOUR CODE HERE ***"


def copper_puzzle(filename):
    img = Image(filename)
    for pixel in img:
        pixel.red = 0
        pixel.green *= 20
        pixel.blue *= 20
    return img