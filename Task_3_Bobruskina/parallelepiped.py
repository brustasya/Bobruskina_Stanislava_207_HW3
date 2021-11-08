from shape import *


# Параллелепипед
class Parallelepiped(Shape):
    def __init__(self):
        # Стороны
        self.a = 0
        self.b = 0
        self.c = 0
        self.density = 0.0  # плотность материала

    def ReadStrArray(self, strArray, i):
        # должно быть как минимум два непрочитанных значения в массиве
        if i >= len(strArray) - 1:
            return 0
        self.a = int(strArray[i])
        self.b = int(strArray[i + 1])
        self.c = int(strArray[i + 2])
        self.density = float(strArray[i + 3])
        i += 4
        return i

    def Print(self):
        print("Parallelepiped: a = ", self.a, " b = ", self.b, " c = ", self.c,
              " density = ", self.density, ", Volume = ", self.Volume())
        pass

    def Write(self, ostream):
        ostream.write(f"Parallelepiped: a = {self.a}  b = {self.b} c = {self.c}"
                      f" density = {self.density}, Volume = {self.Volume()}")
        pass

    def Volume(self):
        return self.a * self.b * self.c
        pass
