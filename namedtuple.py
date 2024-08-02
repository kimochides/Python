from collections import namedtuple
import math

#define a named tuple for the coordinates
Point=namedtuple('Point',['x','y'])

#create two points
p1=Point(5,25)
p2=Point(10,20)

#calculate distance between the two points
distance=math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
print("Distance between point 1 and point 2:",distance)