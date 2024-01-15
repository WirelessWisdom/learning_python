# task 1 - prime_generator

def prime_generator(border, *args):
    for number in range(1, border):
        if prime_check(number):
            yield number


def prime_check(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


print(list(prime_generator(20)))


# task 2 - generate_cube_numbers
def generate_cube_numbers(cube_number):
    for number in range(2, cube_number):
        cubed_number = number**3
        if cubed_number <= cube_number:
            yield cubed_number
        else:
            return


print(list(generate_cube_numbers(200)))
