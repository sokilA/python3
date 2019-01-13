#!/usr/bin/env python3

import abc
import random


class Employee:
    @abc.abstractmethod
    def calc_salary(self):
        return

    @abc.abstractmethod
    def calc_tax(self):
        return


class HourlyEmployee(Employee):
    def __init__(self, name: str, hourly_rate: int):
        self.name = name
        self.hourly_rate = hourly_rate

    def calc_salary(self) -> float:
        return 20.8 * 8 * self.hourly_rate

    def calc_tax(self) -> float:
        return self.calc_salary() * 0.18 + self.calc_salary() * 0.015


class MonthlyEmployee(Employee):
    def __init__(self, name: str, monthly_rate: int):
        self.name = name
        self.monthly_rate = monthly_rate

    def calc_salary(self) -> int:
        return self.monthly_rate

    def calc_tax(self) -> float:
        return self.calc_salary() * 0.18 + self.calc_salary() * 0.015


class Entrepreneur(Employee):
    def __init__(self, name: str, hourly_rate: int):
        self.name = name
        self.hourly_rate = hourly_rate

    def calc_salary(self) -> float:
        return 20.8 * 8 * self.hourly_rate * 1.1

    def calc_tax(self) -> float:
        return self.calc_salary() * 0.05 + 704


class Freelancer(Employee):
    def __init__(self, name: str, line_rate: int, number_lines: int):
        self.name = name
        self.line_rate = line_rate
        self.number_lines = number_lines

    def calc_salary(self) -> float:
        return self.line_rate * self.number_lines

    def calc_tax(self) -> float:
        return self.calc_salary() * 0.18 + self.calc_salary() * 0.015 + 704


def employees_creating() -> list:
    names = ('Tom', 'Jon', 'Ana', 'Kate', 'Andrii')
    employees = []
    for each in range(4):
        name = random.choice(names)
        employees.append(random.choice([
            HourlyEmployee(name, random.randint(50, 250)),
            MonthlyEmployee(name, random.randint(5000, 25000)),
            Entrepreneur(name, random.randint(200, 700)),
            Freelancer(name, random.randint(5, 10), random.randint(2000, 10000))
        ]))
    return sorted(employees, key=lambda x: x.calc_salary(), reverse=True)


def output(employees: list):
    for employee in employees:
        print('Employee:', employee.name, ' Salary:', employee.calc_salary(), ' Tax:',
              employee.calc_tax(), '\n')


output(employees_creating())
