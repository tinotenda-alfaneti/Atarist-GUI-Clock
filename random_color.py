import random


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return rgb_color((r, g, b))


def rgb_color(rgb):
    return '#%02x%02x%02x' % rgb
