import turtle

def draw_triangle(points, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()


def get_mid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, degree, my_turtle):
    colors = ['white']

    draw_triangle(points, colors[degree % len(colors)], my_turtle)

    # Recursive case: degree > 0
    if degree > 0:
        mid1 = get_mid(points[0], points[1])
        mid2 = get_mid(points[1], points[2])
        mid3 = get_mid(points[2], points[0])

        sierpinski([points[0], mid1, mid3], degree - 1, my_turtle)
        sierpinski([mid1, points[1], mid2], degree - 1, my_turtle)
        sierpinski([mid3, mid2, points[2]], degree - 1, my_turtle)


def main():
    my_turtle = turtle.Turtle()
    my_turtle.speed('fastest')  
    screen = turtle.Screen()
    screen.title("Sierpinski Triangle - 6 Levels")
    screen.setup(width=700, height=700)
    screen.tracer(2)

    size = 300
    top_point = (0, size)
    left_point = (-size, -size/2)
    right_point = (size, -size/2)

    points = [top_point, left_point, right_point]

    # Degree=6 for draw 6 levels
    sierpinski(points, 6, my_turtle)

    screen.update()
    my_turtle.hideturtle()

    screen.exitonclick()

if __name__ == "__main__":
    main()