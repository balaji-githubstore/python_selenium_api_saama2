import math


def volume_of_sphere(radius)->float:
    return (4 * math.pi * radius * radius * radius) / 3


def volume_of_cuboid(length, width, height):
    return length * width * height


def get_author_name()->str:
    return 'Balaji Dinakaran'


def quit():
    value = 'close browser'


def volume_of_hemisphere(radius)->float:
    return (2/3)*math.pi*math.pow(radius,3)