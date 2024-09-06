class TurtlePosition:
    """
    Logic for the position of the turtle
    """
    def __init__(self, turtle, dots_per_row, dot_space):
        self.turtle = turtle # Turtle to be use
        self.dots_per_row = dots_per_row # Integer with number of dots per row
        self.dot_space = dot_space # Integer of space between each dot

    def start_position(self):
        """
        Returns the draw to the original position
        """
        beginning_position = (self.dots_per_row * self.dot_space) / 2

        self.turtle.penup()
        self.turtle.right(90)
        self.turtle.forward(beginning_position)
        self.turtle.right(90)
        self.turtle.forward(beginning_position)
        self.turtle.right(180)
        self.turtle.pendown()

    def start_new_row(self):
        """
        Returns the turtle to the drawing position
        """
        row_position = (self.dots_per_row * self.dot_space)

        self.turtle.penup()
        self.turtle.left(90)
        self.turtle.forward(self.dot_space)
        self.turtle.left(90)
        self.turtle.forward(row_position)
        self.turtle.left(180)
