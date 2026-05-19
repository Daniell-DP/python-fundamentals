figure = input()
from math import pi

the_face_of_figure = 0

if figure == "square":
    number_side = float(input())
    the_face_of_figure = number_side * number_side
elif figure == "rectangle":
    side_length_1 = float(input())
    side_length_2 = float(input())
    the_face_of_figure = side_length_1 * side_length_2
elif figure == "circle":
    radius = float(input())
    the_face_of_figure = pi * radius * radius
elif figure == "triangle":
    side_length = float(input())
    length_of_height = float(input())
    the_face_of_figure = (side_length * length_of_height) / 2

print(f'{the_face_of_figure:.3f}')