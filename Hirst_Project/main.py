import random
import turtle as turtle_module

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(213, 211, 210), (207, 215, 210), (199, 163, 119),  (210, 213, 218), (165, 187, 163), (38, 95, 116), (125, 38, 29), (51, 35, 34), (156, 77, 55), (114, 73, 82), (119, 163, 174), (196, 99, 73), (49, 130, 103), (126, 34, 42), (18, 56, 42), (215, 197, 121), (7, 65, 84), (102, 149, 73), (186, 152, 156), (78, 35, 38), (216, 158, 29), (176, 202, 180), (19, 80, 97), (218, 180, 171), (209, 182, 186), (161, 111, 116), (97, 142, 153), (171, 200, 206), (39, 76, 63)]


tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots =100
for dot_count in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)

        tim.forward(500)
        tim.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()