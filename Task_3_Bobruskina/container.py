#----------------------------------------------
import random
from extender import *

class Container:
    def __init__(self):
        self.store = []

    def InRnd(self, count):
        for i in range(count):
            key = random.randint(1, 3)
            density = random.random() * random.randint(1, 20)
            if key == 1:
                shape = Ball()
                shape.radius = random.randint(1, 20)
                shape.density = density
                self.store.append(shape)
            elif key == 2:
                shape = Parallelepiped()
                shape.a = random.randint(1, 20)
                shape.b = random.randint(1, 20)
                shape.c = random.randint(1, 20)
                shape.density = density
                self.store.append(shape)
            else:
                shape = Tetrahedron()
                shape.a = random.randint(1, 20)
                shape.density = density
                self.store.append(shape)

    def Print(self):
        print("Container is store", len(self.store), "shapes:")
        for shape in self.store:
            shape.Print()
        pass

    def Write(self, ostream):
        ostream.write(f"Container is store {len(self.store)} shapes:\n")
        for shape in self.store:
            shape.Write(ostream)
            ostream.write("\n")
        pass

    def Volume(self):
        vol = 0.0
        for shape in self.store:
            vol += shape.Volume()
        return vol

    def merge_list(self, start, mid, end):
        left = self.store[start:mid]
        right = self.store[mid:end]
        k = start
        i = 0
        j = 0
        while start + i < mid and mid + j < end:
            if left[i].Volume() > right[j].Volume():
                self.store[k] = left[i]
                i = i + 1
            else:
                self.store[k] = right[j]
                j = j + 1
            k = k + 1
        if start + i < mid:
            while k < end:
                self.store[k] = left[i]
                i = i + 1
                k = k + 1
        else:
            while k < end:
                self.store[k] = right[j]
                j = j + 1
                k = k + 1

    def merge_sort(self, start, end):
        if end - start > 1:
            mid = (start + end) // 2
            self.merge_sort(start, mid)
            self.merge_sort(mid, end)
            self.merge_list(start, mid, end)
