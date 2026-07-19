from turtle import Turtle,Screen
#import turtle
import anothermodule
from prettytable import PrettyTable

# print(anothermodule.another_variable)



# timmy=Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red","green")
# timmy.forward(100)


# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


table=PrettyTable()
table.add_column("pokemon",["pikachu ","squirtel","charmender"]) 
table.add_column("type",["electric","water","fire"])
table.align="l"


print(table)