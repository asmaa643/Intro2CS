#################################################################
# FILE : hello_turtle.py
# WRITER : Asmaa Ghrayeb , asmaa.ghrayeb , 212017719
# EXERCISE : intro2cse ex1 2021
# DESCRIPTION: A simple program that draw a flower bed that contains 3 flowers
# STUDENTS I DISCUSSED THE EXERCISE WITH: None
# WEB PAGES I USED: None
# NOTES: (nothing)
#################################################################


import turtle


def draw_petal():
    """These next lines draw a petal"""
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(135)


def draw_flower():
    """These next lines draw a flower"""
    turtle.left(45)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(90)
    draw_petal()
    turtle.left(135)
    turtle.forward(150)


def draw_flower_and_advance():
    """These next lines draw a flower and move the pen to paint more flowers"""
    draw_flower()
    turtle.right(90)
    turtle.up()
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()


def draw_flower_bed():
    """These next lines draw a flower bed"""
    turtle.up()
    turtle.forward(200)
    turtle.left(180)
    turtle.down()
    draw_flower_and_advance()
    draw_flower_and_advance()
    draw_flower_and_advance()


if __name__ == "__main__":
    draw_flower_bed()
    turtle.done()
