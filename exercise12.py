import random


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    @classmethod
    def add(cls, first_rectangle, second_rectangle):
        first_square = first_rectangle.get_square()
        second_square = second_rectangle.get_square()
        sum_of_squares = first_square + second_square
        # new_width, new_height = Rectangle.get_sides_of_rectangle(sum_of_squares)
        result = Rectangle.get_sides_of_rectangle(sum_of_squares)
        (new_width, new_height) = result
        return Rectangle(new_width, new_height)

    @staticmethod
    def get_sides_of_rectangle(square):
        # width = random.randint(1, 5)
        width = 1
        height = int(square / width)
        return width, height

    @classmethod
    def eq(cls, first_rectangle, second_rectangle):
        first_square = first_rectangle.get_square()
        second_square = second_rectangle.get_square()
        if first_square > second_square:
            return f"First rectangle is bigger than second\n"
        elif first_square < second_square:
            return f"Second rectangle is bigger than first\n"
        elif first_square == second_square:
            return f"Rectangles are equal!\n"

    @classmethod
    def mul(cls, rectangle, multiplication_number):
        square = rectangle.get_square()
        new_square = square * multiplication_number
        result = Rectangle.get_sides_of_rectangle(new_square)
        (new_width, new_height) = result
        return Rectangle(new_width, new_height)

    @classmethod
    def deduction(cls, first_rectangle, second_rectangle):
        first_square = first_rectangle.get_square()
        second_square = second_rectangle.get_square()
        if first_square > second_square:
            deduction_of_squares = first_square - second_square
            result = Rectangle.get_sides_of_rectangle(deduction_of_squares)
            (new_width, new_height) = result
            return Rectangle(new_width, new_height)
        else:
            raise Exception(f"The square of first rectangle can't be smaller than of a second one\n")

    @classmethod
    def division(cls, rectangle, division_number):
        square = rectangle.get_square()
        new_square = square / division_number
        result = Rectangle.get_sides_of_rectangle(new_square)
        (new_width, new_height) = result
        return Rectangle(new_width, new_height)

    def __str__(self):
        return f'width: {self.width}, height: {self.height}\n'


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8
assert r2.get_square() == 18

# r3 = r1 + r2
r3 = Rectangle.add(r1, r2)
print(r3)
assert r3.get_square() == 26

equality = Rectangle.eq(r1, r2)
print(equality)

r4 = Rectangle.mul(r1, 4)
print(r4)
assert r4.get_square() == 32

r5 = Rectangle.deduction(r2, r1)
print(r5)
assert r5.get_square() == 10

r6 = Rectangle.division(r2, 3)
print(r6)
assert r6.get_square() == 6