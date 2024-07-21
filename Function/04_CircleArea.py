import math

def circle(r):
    # Area of circle = pi*r**2
    Area = round(math.pi,2) *( r ** 2)
    Circumference = 2 * round(math.pi,2) * r
    return Area, Circumference

a, c = circle(2)

print("Area :", a, "circumference :", c)

