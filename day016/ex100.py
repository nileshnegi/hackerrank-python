"""
Class 2 - Find the Torsional Angle

Given four points `A`, `B`, `C` and `D` in a 3D Cartesian coordinate system,
print the angle between the plane made by the points `A`, `B`, `C` and
`B`, `C`, `D` in degrees (not radians). Let this angle be `phi`.
So `cos(phi) = (X.Y)/(|X||Y|)` where `X = ABxBC` and `Y = BCxCD`, and
`X.Y` is the dot product of `X` and `Y`, and `ABxBC` is the cross product of
`AB` and `BC`. Also `AB = B-A`.
"""
import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __sub__(self, no):
        return Points(no.x-self.x, no.y-self.y, no.z-self.z)
    
    def dot(self, no):
        return self.x*no.x + self.y*no.y + self.z*no.z
    
    def cross(self, no):
        return Points(self.y*no.z - self.z*no.y, self.z*no.x - self.x*no.z, self.x*no.y - self.y*no.x)
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
