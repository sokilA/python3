#! /usr/bin/python3

import math


class Dot:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance(self, dot_second):
        return math.sqrt((dot_second.x - self.x) ** 2 + (dot_second.y - self.y) ** 2)


class Triangle:
    def __init__(self, first_dot, second_dot, third_dot):
        self.first_dot = first_dot
        self.second_dot = second_dot
        self.third_dot = third_dot

        self.first_side = self.first_dot.distance(self.second_dot)
        self.second_side = self.second_dot.distance(self.third_dot)
        self.third_side = self.third_dot.distance(self.first_dot)

    def is_exist(self) -> bool:
        if self.first_side > 0 and self.second_side > 0 and self.third_side > 0:
            hypotenuse = max(self.first_side, self.second_side, self.third_side)
            catets = self.first_side + self.second_side + self.third_side - hypotenuse
            if (catets > hypotenuse):
                return True
            else:
                return False
        else:
            return False

    def get_perimeter(self):
        if not (self.is_exist()):
            return "Triangle not exists"
        return self.first_side + self.second_side + self.third_side

    def get_square(self):
        if not (self.is_exist()):
            return "Triangle not exists"
        p = self.get_perimeter() / 2
        return (p * (p - self.first_side) * (p - self.second_side) * (p - self.third_side)) ** 0.5


def input_data() -> Triangle:
    first_dot = Dot(float(input("Enter first dot - A_x: ")), float(input("Enter A_y:  ")))
    second_dot = Dot(float(input("Enter second dot B_x: ")), float(input("Enter B_y: ")))
    third_dot = Dot(float(input("Enter third dot C_x: ")), float(input("Enter C_y: ")))
    return Triangle(first_dot, second_dot, third_dot)


def output(triangle) -> None:
        print("Triangle exists:", triangle.is_exist())
        print("Perimeter of triangle:", triangle.get_perimeter())
        print("Squere of triangle:", triangle.get_square())


output(input_data())
