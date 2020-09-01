import math

radius = float(input('Radius: '))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print("Radius: " + str(radius))
print("Area: " + str(area))
print("Circumference: " + str(circumference))


print("Radius: " + str(radius))
print("Radius: ", radius)
print("Radius: %.3f" % radius)
print("Radius: {:.3f}".format(radius))
print(f"Radius: {radius:.3f}")
