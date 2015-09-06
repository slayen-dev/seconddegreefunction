from math import *
print("Enter a, b et c : ")
a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))
delta = b * b - (4 * a * c)
if delta < 0.0:
    print("No solutions")
elif delta == 0.0:
    x0 = (-b / 2 * a)
    print("A single solution : X0 =", x0)
else:
    x1 = (-b - sqrt(delta)) / 2 * a
    x2 = (-b + sqrt(delta)) / 2 * a
    print("Two solutions : X1 =", x1, "et X2 =", x2)
