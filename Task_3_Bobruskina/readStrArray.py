from extender import *

def ReadStrArray(container, strArray):
    arrayLen = len(strArray)
    i = 0   # Индекс, задающий текущую строку в массиве
    figNum = 0
    while i < arrayLen:
        str = strArray[i]
        key = int(str)   # преобразование в целое

        if key == 1: # признак прямоугольника
            i += 1
            shape = Ball()
            i = shape.ReadStrArray(strArray, i) # чтение шара с возвратом позиции за ним
        elif key == 2: # признак треугольника
            i += 1
            shape = Parallelepiped()
            i = shape.ReadStrArray(strArray, i) # чтение параллелепипеда с возвратом позиции за ним
        elif key == 3:
            i += 1
            shape = Tetrahedron()
            i = shape.ReadStrArray(strArray, i)  # чтение тетраэдра с возвратом позиции за ним
        else:
            # что-то пошло не так. Должен быть известный признак
            # Возврат количества прочитанных фигур
            return figNum
        # Количество пробелами фигур увеличивается на 1
        if i == 0:
            return figNum
        figNum += 1
        container.store.append(shape)
    return figNum
