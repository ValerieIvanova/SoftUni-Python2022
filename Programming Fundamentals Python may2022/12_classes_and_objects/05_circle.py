class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        d = self.diameter * Circle.__pi
        return d

    def calculate_area(self):
        a = Circle.__pi * self.radius ** 2
        return a

    def calculate_area_of_sector(self, angle):
        a_s = (angle/360) * Circle.calculate_area(self)
        return a_s


circle = Circle(10)
angle = 5
print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")