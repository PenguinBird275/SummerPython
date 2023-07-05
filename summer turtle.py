# 1.import the turtle library
import turtle
# 2. write turtle.speed and place it at 0 inside open & closed parentheses
turtle.speed(0)
# 3. write turtle.bgcolor and place "skyblue" inside open & closed parentheses
turtle.bgcolor("skyblue")
#######Grass######
# 4. write turtle.penup and have open & closed parentheses
turtle.penup()
# 5. write turtle.goto inside the open & closed parentheses write -400, -100
turtle.goto(-400, -100)
# 6. write turtle.pendown and have open & closed parentheses
turtle.pendown()
# 7. write turtle.color and place "limegreen" have open & closed parentheses
turtle.color("limegreen")
# 8. write turtle.begin_fill and have open & closed parentheses
turtle.begin_fill()
# 9. create a for loop where the range is (2):
for i in range(2):
    # 10. write turtle.forward and inside the open & closed parentheses have 800
    turtle.forward(800)
    # 11.write turtle.right and inside the open & closed parentheses have 90
    turtle.right(90)
    # 12. write turtle.forward and inside the open & closed parentheses have 400
    turtle.forward(400)
    # 13. write turtle.right and inside the open & closed parentheses have 90
    turtle.right(90)
# 14. write turtle.end_fill and have open & closed parentheses
turtle.end_fill()
# Left Mountain

turtle.penup()

turtle.goto(-400, -100)

turtle.pendown()

turtle.color("dimgray")

turtle.begin_fill()

for i in range(3):

    turtle.forward(300)

    turtle.left(120)

turtle.end_fill()

# Right Mountain
turtle.penup()
# 15. write turtle.goto inside the open & closed parentheses write 100, -100
turtle.goto(100, -100)
turtle.pendown()
turtle.begin_fill()
for i in range(3):
    turtle.forward(300)
    turtle.left(120)
turtle.end_fill()
# Middle Mountain
turtle.penup()
# 16. write turtle.goto inside the open & closed parentheses write -160, -100
turtle.goto(-160, -100)
turtle.pendown()
turtle.color("gray")
turtle.begin_fill()
for i in range(3):
    turtle.forward(400)
    turtle.left(120)
turtle.end_fill()
# Middle Mountain Ice Cap
turtle.penup()
# 17. write turtle.goto inside the open & closed parentheses write -35, 120
turtle.goto(-35, 120)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
turtle.left(35)
turtle.forward(60)
turtle.right(90)
turtle.forward(30)
turtle.left(100)
#18. write turtle.forward and inside the open & closed parentheses have 45
turtle.forward(45)
turtle.right(85)
#19. write turtle.forward and inside the open & closed parentheses have 65
turtle.forward(65)
turtle.left(160)
turtle.forward(150)
turtle.end_fill()
# Left Mountain Ice Cap
turtle.penup()
turtle.goto(-215, 100)
turtle.pendown()
turtle.color("snow")
turtle.begin_fill()
turtle.forward(70)
turtle.left(120)
turtle.forward(75)
turtle.left(150)
turtle.forward(45)
turtle.right(90)
turtle.forward(45)
turtle.left(120)
turtle.end_fill()
# Right Mountain Ice Cap
turtle.penup()
turtle.goto(203, 80)
turtle.pendown()
turtle.begin_fill()
turtle.forward(95)
# 20. write turtle.right and inside the open & closed parentheses have 120
turtle.right(120)
turtle.forward(80)
turtle.right(150)
turtle.forward(50)
turtle.left(70)
turtle.end_fill()
turtle.left(50)
# Sun
turtle.penup()
turtle.goto(-500, 350)
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill()
turtle.circle(125)
turtle.end_fill()
# Tree
def tree():
# Tree trunk
    turtle.color("saddlebrown")
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
    turtle.end_fill()
# Turn the turtle around
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(5)
# Leaves on tree
    turtle.color("forestgreen")
    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()
    turtle.right(90)
# Plant the first tree
turtle.penup()
turtle.goto(-25,-200)
turtle.pendown()
tree()
# Plant the second tree
turtle.penup()
turtle.goto(200,-150)
turtle.pendown()
tree()
# Plant the third tree
turtle.penup()
turtle.goto(300,-250)
turtle.pendown()
tree()
# Plant the fourth tree
turtle.penup()
turtle.goto(-300,-250)
turtle.pendown()
tree()
# Plant the fifth tree
turtle.penup()
turtle.goto(-200,-100)
turtle.pendown()
tree()
turtle.hideturtle()
turtle.done()
