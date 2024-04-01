class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def get_new_fractions_with_common_denominator(first_fraction, second_fraction):
        if first_fraction.b == second_fraction.b:
            return first_fraction.a, second_fraction.a, first_fraction.b

        else:
            first_fraction_new_a = first_fraction.a * second_fraction.b
            common_denominator = first_fraction.b * second_fraction.b

            second_fraction_new_a = second_fraction.a * first_fraction.b
            # second_fraction_new_b = second_fraction.b * first_fraction.b

            # new_first_fraction = Fraction(first_fraction_new_a, first_fraction_new_b)
            # new_second_fraction = Fraction(second_fraction_new_a, second_fraction_new_b)
            return first_fraction_new_a, second_fraction_new_a, common_denominator

    def __add__(self, other):
        first_a, second_a, denominator = self.get_new_fractions_with_common_denominator(self, other)
        new_a = first_a + second_a
        new_fraction = Fraction(new_a, denominator)
        return new_fraction

    def __mul__(self, other):
        new_a = self.a * other.a
        new_b = self.b * other.b
        result = Fraction(new_a, new_b)
        return result

    def __sub__(self, other):
        first_a, second_a, denominator = self.get_new_fractions_with_common_denominator(self, other)
        new_a = first_a - second_a
        new_fraction = Fraction(new_a, denominator)
        return new_fraction

    def __eq__(self, other):
        first_a, second_a, denominator = self.get_new_fractions_with_common_denominator(self, other)
        return first_a == second_a

    def __gt__(self, other):
        first_a, second_a, denominator = self.get_new_fractions_with_common_denominator(self, other)
        return first_a > second_a

    def __lt__(self, other):
        first_a, second_a, denominator = self.get_new_fractions_with_common_denominator(self, other)
        return first_a < second_a

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
print(f_c)
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
print(f_d)
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
print(f_e)
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
