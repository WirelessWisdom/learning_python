# task 1
import datetime
import this  # appeared to be some pseudo philosophy by some dinosaur developer

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
print("Hello " + name)

# task 4
exchange_rate = 36.5
amount = input("Please enter the amount of UAH you want to exchange: ")
uah = int(amount)
usd = round(uah / exchange_rate, 2)
usd_to_print = str(usd)
print("You will receive " + usd_to_print + " USD")

# task 5 aka Zavdannya 2
snake_case = input("Please enter 3 words in format a_b_c: ")
splited = snake_case.split("_")

for word in splited:
    cap_word = str(word.capitalize())
    print(cap_word)

# task 6 aka Zavdannya 3
person = input("Please enter name and dates of birth and death, use * as separator: ")
l = person.split("*")
name = l[0]
date_of_birth = l[1].split("-")
date_of_death = l[2].split("-")

year_of_birth = int(date_of_birth[0])
year_of_death = int(date_of_death[0])

age = str(year_of_death - year_of_birth)
print(name)
print("Died in age of " + age)

