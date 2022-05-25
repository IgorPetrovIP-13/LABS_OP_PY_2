from abc import ABC, abstractmethod
import math

class TQuadrangle(ABC):

    def __init__(self, points: list):
        self._point1 = points[0]
        self._point2 = points[1]
        self._point3 = points[2]
        self._point4 = points[3]

    @abstractmethod
    def get_p(self):
        pass

    @abstractmethod
    def get_s(self):
        pass

class Parallelogram(TQuadrangle):

    def get_p(self):
        return (side_distance(self._point1, self._point2) + side_distance(self._point2, self._point3))*2

    def get_s(self):
        vec1 = [self._point2[0] - self._point1[0], self._point2[1] - self._point1[1]]
        vec2 = [self._point4[0] - self._point1[0], self._point4[1] - self._point1[1]]
        return abs(vec1[0] * vec2[1] - vec1[1] * vec2[0])

class Rectangle(Parallelogram):

    def get_s(self):
        return side_distance(self._point1, self._point2) * side_distance(self._point2, self._point3)

class Square(Rectangle):

    def get_p(self):
        return side_distance(self._point1, self._point2) * 4

    def get_s(self):
        return side_distance(self._point1, self._point2) ** 2


def enter_points():
    final_list = list()
    for i in range(0, 4):
        point = [int(c) for c in input(f"Point {i + 1} in format x y: ").split()]
        final_list.append(point)
    return final_list


def side_distance(first_point: list, second_point: list):
    return math.sqrt((second_point[0] - first_point[0]) ** 2 + (second_point[1] - first_point[1]) ** 2)