from colorgram import extract
from random import choice

def extract_colors(image_to_extract, number_of_colors):
    """
    Extracts an image and gets the color
    :param image_to_extract: String with the image path
    :param number_of_colors: Integer with the number of colors
    :return: List of tuples with integers of R, G, B of an extracted color's RGB
    """
    colors = []
    extracted_colors = extract(image_to_extract, number_of_colors)

    # Simple loop to extract each color and add it to a tuple which is appended to a list
    for extracted_color in extracted_colors:
        rgb_color = extracted_color.rgb
        red = rgb_color.r
        green = rgb_color.g
        blue = rgb_color.b
        new_color = (red, green, blue)
        colors.append(new_color)

    return colors

def draw_row(turtle, dots_per_row, dot_space, dot_size, colors):
    """
    Draws a dot
    :param turtle: Turtle to be use
    :param dots_per_row: Integer with number of dots per row
    :param dot_space: Integer of space between each dot
    :param dot_size: Integer of size of dots
    :param colors: List of tuples with integers of R, G, B of an extracted color's RGB
    """
    for _ in range(dots_per_row):
        turtle.color(choice(colors))
        turtle.dot(dot_size)
        turtle.penup()
        turtle.forward(dot_space)
        turtle.pendown()