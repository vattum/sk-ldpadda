import turtle as t
t.speed(3)
bredd = 250
höjd = 40

def fyll_rektangel():
    t.begin_fill()
    t.forward(bredd)
    t.right(90)
    t.forward(höjd)
    t.right(90)
    t.forward(bredd)
    t.right(90)
    t.forward(höjd)
    t.end_fill()   

# röd
t.fillcolor("red")
fyll_rektangel()

# blå
t.right(180)
t.forward(höjd)
t.left(90)

t.fillcolor("blue")
fyll_rektangel()

# orange
t.right(180)
t.forward(höjd)
t.left(90)

t.fillcolor("orange")
fyll_rektangel()


t.done()