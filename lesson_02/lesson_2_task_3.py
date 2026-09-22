import math


def square(side):
    if side <= 0:
        raise ValueError("Сторона квадрата должна быть положительной.")

    area = side * side

    if side != int(side):
        return math.ceil(area)

    return int(area)


print(square(5))
print(square(2.3))
