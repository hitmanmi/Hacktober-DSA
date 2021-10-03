# Mid-Point Ellipse Algorithm C019322

def midptellipse(rx, ry, xc, yc):

    x = 0
    y = ry

    # Initial decision parameter of region 1
    d1 = ((ry * ry) - (rx * rx * ry) + (0.25 * rx * rx))
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y

    # For region 1
    while (dx < dy):

        # Using 4-way symmetry
        print("(", x + xc, ",", y + yc, ")")
        print("(", -x + xc, ",", y + yc, ")")
        print("(", x + xc, ",", -y + yc, ")")
        print("(", -x + xc, ",", -y + yc, ")")

        # Checking and updating value of decision parameter based on algorithm
        if (d1 < 0):
            x += 1
            dx = dx + (2 * ry * ry)
            d1 = d1 + dx + (ry * ry)
        else:
            x += 1
            y -= 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d1 = d1 + dx - dy + (ry * ry)

    # Decision parameter : - region 2
    d2 = (((ry * ry) * ((x + 0.5) * (x + 0.5))) + ((rx * rx) * ((y - 1) * (y - 1))) - (rx * rx * ry * ry))

    # Plotting points : - region 2
    while (y >= 0):

        # using 4-way symmetry
        print("(", x + xc, ",", y + yc, ")")
        print("(", -x + xc, ",", y + yc, ")")
        print("(", x + xc, ",", -y + yc, ")")
        print("(", -x + xc, ",", -y + yc, ")")

        # Checking and updating parameter value based on algorithm
        if (d2 > 0):
            y -= 1
            dy = dy - (2 * rx * rx)
            d2 = d2 + (rx * rx) - dy
        else:
            y -= 1
            x += 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d2 = d2 + dx - dy + (rx * rx)


if __name__ == '__main__':
    x1 = int(input("Enter x1 "))
    y1 = int(input("Enter y1 "))
    x2 = int(input("Enter x2 "))
    y2 = int(input("Enter y2 "))
    midptellipse(x1, y1, x2, y2)
