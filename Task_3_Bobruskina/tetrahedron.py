from shape import *


# Тетрадр
class Tetrahedron(Shape):
    def __init__(self):
        self.a = 0  # сторона
        self.density = 0.0  # плотность материала

    def ReadStrArray(self, strArray, i):
        # должно быть как минимум два непрочитанных значения в массиве
        if i >= len(strArray) - 1:
            return 0
        self.a = int(strArray[i])
        self.density = float(strArray[i + 1])
        i += 2
        return i

    def Print(self):
        print("Tetrahedron: a = ", self.a, " density = ", self.density, ", Volume = ", self.Volume())
        pass

    def Write(self, ostream):
        ostream.write(f"Tetrahedron: a = {self.a}  density = {self.density}, Volume = {self.Volume()}")
        pass

    def Volume(self):
        return 2.0 ** 0.5 / 12.0 * self.a * self.a * self.a
        pass
