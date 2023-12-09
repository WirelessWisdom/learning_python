# task 1
import this  # appeared to be some philosophy by some dinosaur developer

# task 2
from math import sqrt
a = 1
b = 5
c = 4

x = (-b + sqrt(b**2 - 4*a*c))/2*a
print(x)

y = (-b - sqrt(b**2 - 4*a*c))/2*a
print(y)

# task 3
name = input("Please enter your name: ")
#print("Hello " + name)
print("Hello {}".format(name))
print(f"Hello {name}")


# task 4
exchange_rate = 36.5
amount = int(input("Please enter the amount of UAH you want to exchange: "))
#uah = int(amount)
usd = round(amount / exchange_rate, 2)
#usd_to_print = str(usd)
print(f"You will receive {usd} USD")

# task 5 aka Zavdannya 2
snake_case = input("Please enter 3 words in format a_b_c: ")
splited = snake_case.split("_")

capitalized_words = []
for word in splited:
    cap_word = str(word.capitalize())
    capitalized_words.append(cap_word)
print("".join(capitalized_words))

#for word in splited:
#    cap_word = str(word.capitalize())
#    print(cap_word)


# task 6 aka Zavdannya 3
person = input("Please enter name and dates of birth and death, use * as separator: ")
l = person.split("*")
name = l[0]
date_of_birth = int(l[1].split("-")[0])
date_of_death = int(l[2].split("-")[0])

age = date_of_death - date_of_birth
print(f"{name}\nDied in age of {age}")

