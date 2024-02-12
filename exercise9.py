# task 1 - is_even without /, //, % and divmod
def is_even(number):
    even_list = [0, 2, 4, 6, 8]
    last_digit = int(str(number)[-1])
    print(last_digit)
    if last_digit in even_list:
        return True
    else:
        return False


print(is_even(2494563894038 ** 2))
print(is_even(1056897 ** 2))
print(is_even(24945638940387 ** 3))
