# overloading defalt python methods and why is exteremely useful

class Point():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def  __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)
    
    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)
    
    def __gt__(self, other):
        return self.length() > other.length()
    
    def  __ge__(self, other):
        return self.length() >= other.length()
    
    def __lt__(self, other):
        return self.length() < other.length()
    
    def __le__(self, other):
        return self.length() <= other.length()
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    

    def __str__(self): # this method is used to return a string representation of the object when it is printed. It is called when you use the print() function on an instance of the class. By defining this method, you can customize how the object is displayed as a string.
        return f"Point({self.x}, {self.y})"
        

p1 = Point(3,4)
p2 = Point(3,2)
p3 = Point(1,3)
p4 = Point(0,1)
print(p1) # this will call the __str__ method and print "Point(3, 4)"
print(p1 + p2) # this will call the __add__ method and return a new Point with coordinates (6, 6)
print(p1 - p2) # this will call the __sub__ method and return a new Point with coordinates (0, 2)
print(p1 * p2) # this will call the __mul__ method and return a new Point with coordinates (9, 8)
print(p1 > p2) # this will call the __gt__ method and return True because the length of p1 is greater than the length of p2
print(p1 >= p2) # this will call the __ge__ method and return True because the length of p1 is greater than or equal to the length of p2
print(p1 < p2) # this will call the __lt__ method and return False because the length of p1 is not less than the length of p2
print(p1 <= p2) # this will call the __le__ method and return False because the length of p1 is not less than or equal to the length of p2
print(p1 == p2) # this will call the __eq__ method and return False because the coordinates of p1 and p2 are not the same
print(p1 == Point(3,4)) # this will call the __eq__ method and return True because the coordinates of p1 and the new Point(3,4) are the same


