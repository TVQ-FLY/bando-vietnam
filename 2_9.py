import turtle

win = turtle.Screen()
win.title("Bản đồ Việt Nam")
win.register_shape("pen2.gif")
pen = turtle.Pen()
pen.speed(2)
pen.shape("pen2.gif")
pen.penup()

pen.pensize(3)

file = open("vietnam.txt", 'r')
vietnams = file.readlines()
pen.color("red", "red")
count = 0
for vietnam in vietnams:
    viet = vietnam.strip().split()
    pen.goto(float(viet[0]), float(viet[1]))
    if count == 0:
        pen.pendown()
        pen.begin_fill()
    count += 1
pen.end_fill()
pen.penup()

file = open('saovang.txt', 'r')
saovangs = file.readlines()
pen.color("yellow", "yellow")
count = 0
for sao in saovangs:
    s = sao.strip().split()
    pen.goto(float(s[0]), float(s[1]))
    if count == 0:
        pen.pendown()
        pen.begin_fill()
    count += 1
pen.end_fill()
pen.penup()

pen.color("red", "red")
pen.pensize(3)
file = open('cacdao.txt', 'r')
cacdao = file.readlines()
file.close()
count = 0
for dao in cacdao:
    count += 1
    d = dao.strip().split(" ")
    pen.goto(float(d[0]), float(d[1]))
    if count % 7 == 1:
        pen.pendown()
        pen.begin_fill()
    if count % 7 == 0:
        pen.end_fill()
        pen.penup()

pen.hideturtle()

pen.penup()
pen.color("red")
pen.goto(120, 20)
pen.write("Quần đảo Hoàng Sa", align="left", font=("Arial", 12, "bold"))
pen.penup()
pen.color("red")
pen.goto(140, -180)
pen.write("Quần đảo Trường Sa", align="left", font=("Arial", 12, "bold"))
pen.penup()
pen.goto(-10, -350)
pen.color("red")
pen.write("I love Viet Nam - Clip by Tran Van Quyen",
          align="left", font=("Arial", 16, "bold"))

turtle.done()
# Clip by Tran Van Quyen