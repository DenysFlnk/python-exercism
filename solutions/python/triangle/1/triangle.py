def equilateral(sides):
    if not is_valid_triangle(sides):
        return False

    return sides[0] == sides[1] and sides[1] == sides[2] and sides[0] == sides[2]


def isosceles(sides):
    if not is_valid_triangle(sides):
        return False

    return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]


def scalene(sides):
    if not is_valid_triangle(sides):
        return False

    return sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]


def is_valid_triangle(sides: list) -> bool:
    for side in sides:
        if side == 0:
            return False

    if (
        (sides[1] + sides[2] < sides[0])
        or (sides[0] + sides[1] < sides[2])
        or (sides[0] + sides[2] < sides[1])
    ):
        return False

    return True
