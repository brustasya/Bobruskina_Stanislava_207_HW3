from shape import *


# Шар
class Ball(Shape):
    def __init__(self):
        self.radius = 0  # радиус
        self.density = 0.0  # плотность материала

    def ReadStrArray(self, strArray, i):
        # должно быть как минимум два непрочитанных значения в массиве
        if i >= len(strArray) - 1:
            return 0
        self.radius = int(strArray[i])
        self.density = float(strArray[i + 1])
        i += 2
        return i

    def Print(self):
        print("Ball: radius = ", self.radius, " density = ", self.density, ", Volume = ", self.Volume())
        pass

    def Write(self, ostream):
        ostream.write(f"Ball: radius = {self.radius}  density = {self.density}, Volume = {self.Volume()}")
        pass

    def Volume(self):
        return 4.0 / 3.0 * 3.1415926 * self.radius * self.radius * self.radius
        pass
