import ShapeClass as shape

a = shape.Point(3, 4)

print(a)
print(repr(a))
print(str(a))
print(a.distance_from_origin())

c = shape.Circle(3, 2, 1)
print(c)
print(repr(c))
print(str(c))

print(c.circumference())
print(c.edge_distance_from_origin())