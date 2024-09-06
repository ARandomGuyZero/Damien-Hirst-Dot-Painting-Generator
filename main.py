"""
Damien Hirst Dot Painting Generator

Author: Alan
Date: September 5th 2024

This script generates the dot painting from the British artist Damien Hirst.
It takes color from an image and uses it to generate the dots from the famous picture.
NOTE: This code uses the Python library "colorgram"
"""

from drawing import draw_row, extract_colors
from turtle_position import TurtlePosition
from turtle import Turtle, Screen

# CONSTANTS
IMAGE = "rainbow.jpg" # String with the image path file, which we will use it to extract the colors from
NUMBER_COLORS = 10 # Integer with the number of colors
DOT_SIZE = 20 # Integer with the size of the dot
DOTS_PER_ROW = 10 # Integer with the number of dots per row
DOT_SPACE = 50 # Integer containing how much space each dot takes

# Turtle object called tim c:
tim = Turtle()
tim.hideturtle()
tim.speed("fastest") # Making him draw faster

screen = Screen()
screen.colormode(255) # Color range (RGB) for the colors

# Turtle object called turtle_position, which has the logic for turtle's position
turtle_position = TurtlePosition(turtle=tim, dots_per_row=DOTS_PER_ROW, dot_space= DOT_SPACE)

def create_painting():
    # Getting a list of colors
    colors = extract_colors(IMAGE, NUMBER_COLORS) # List with integer tuples (RGB colors data)
    turtle_position.start_position()  # Start the position of the turtle
    # Basic loops
    for _ in range(DOTS_PER_ROW):
        # Draws a row of dots and then moves the turtle to the beginning of the next row
        draw_row(tim, DOTS_PER_ROW, DOT_SPACE, DOT_SIZE, colors)
        turtle_position.start_new_row()

create_painting()
screen.exitonclick()
