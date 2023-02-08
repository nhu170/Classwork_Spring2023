
def line_driver():
    point_one = point_one_input()
    point_two = point_two_input()
    x_value = x_input()
    y_value = point_on_line(point_one, point_two, x_value)
    print(y_value)


def point_one_input():
    x = input("Enter the x-value for point 1:")
    x = float(x)
    y = input("Enter the y-value for point 1:")
    y = float(y)
    point = (x, y)
    return point


def point_two_input():
    x = input("Enter the x-value for point 2:")
    x = float(x)
    y = input("Enter the y-value for point 2:")
    y = float(y)
    point = (x, y)
    return point


def x_input():
    x = input("Enter desired x value:")
    x = float(x)
    return x


def point_on_line(point1, point2, x):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    slope = (y1-y2)/(x1-x2)
    y_intercept = (x1*y2 - x2*y1)/(x1-x2)
    print("Line solution is y = {}x + {}".format(slope, y_intercept))
    y = slope*x + y_intercept
    return y


if __name__ == "__main__":
    line_driver()
