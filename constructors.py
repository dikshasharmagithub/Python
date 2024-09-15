class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

point = Point(11,20)
print(point.x)


class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        print(f"Hi, I am {self.name} ")

john= Person("Diksha Sharma")
john.talk()   

bob = Person ("Bob Smith")
bob.talk()
