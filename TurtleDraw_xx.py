import turtle
import math

# calculate distance between two points
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def main():

    # setup screen
    screen = turtle.Screen()
    screen.setup(450, 450)

    t = turtle.Turtle()
    t.speed(0)

    filename = input("Enter file name: ")

    try:
        file = open(filename, "r")
    except:
        print("Could not open file.")
        return

    total_distance = 0
    previous_point = None
    first_point = True

    # read file line by line
    for line in file:
        line = line.strip()

        if line == "":
            continue

        # start a new shape
        if line.lower() == "stop":
            t.penup()
            previous_point = None
            first_point = True
            continue

        # split into color + coordinates
        parts = line.split()
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        t.color(color)

        # first point of each segment
        if first_point:
            t.penup()
            t.goto(x, y)
            t.pendown()
            first_point = False
        else:
            # add distance between connected points
            total_distance += distance(previous_point, (x, y))
            t.goto(x, y)

        previous_point = (x, y)

    file.close()

    # display total distance
    t.penup()
    t.goto(120, -200)
    t.write(f"Total Distance: {round(total_distance, 2)}", font=("Arial", 10, "normal"))

    # wait before closing
    input("Press Enter to close...")
    turtle.bye()

main()