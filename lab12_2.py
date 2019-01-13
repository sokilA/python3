#! /usr/bin/python3
import math


class Star:
    def __init__(self, name: str, x: float, y: float):
        self.name = name
        self.x = x
        self.y = y

    def rotate(self, angle: int) -> None:
        rad = angle * (math.pi / 180)
        self.x = self.x * math.cos(rad) - self.y * math.sin(rad)
        self.y = self.x * math.sin(rad) + self.y * math.cos(rad)


def input_data() -> list:
    with open("input.txt", 'rt') as file:
        yield file.readline()
        for line in file:
            data = line.split()
            yield Star(data[0], float(data[1]), float(data[2]))


def rotate_all(stars: list) -> list:
    angle = int(stars.__next__().split()[1])
    for star in stars:
        star.rotate(angle)
        yield star


def output(stars: list) -> None:
    with open("output.txt", 'wt') as file:
        stars = list(stars)
        stars.sort(key=lambda star: (star.y, star.x))
        for star in stars:
            file.write(star.name + ' ')


output(rotate_all(input_data()))
