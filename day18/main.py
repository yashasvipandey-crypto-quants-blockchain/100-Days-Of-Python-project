from turtle import *
import random
import colorgram


tim = Turtle()
tim.shape("turtle")
tim.color("red")

# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# def draw_shape(num_sides):
#     angle=360/num_sides
#     for i in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3,11):
#    draw_shape(shape_side_n)


# ways=[tim.right,tim.left]
# for walk in range(50):
#     choice= random.choice(ways)
#     choice(90)
#     tim.forward(10)


# tim.speed("fastest")
# for i in range (100):
#     tim.circle(100)
#     current_heading=(tim.heading())
#     tim.setheading(current_heading + 10)
#     tim.circle(100)


# rgb_colors=[]
# colors=colorgram.extract('hello.jpg',30)
# for color in colors:
#     rgb_colors.append(color.rgb)

# print(rgb_colors)


screen = Screen()
screen.exitonclick()