# create class item
class Item:
    def __init__(self, name, description, price, country):
        self.name = name
        self.description = description
        self.price = price
        self.country = country

    def __str__(self):
        return (f"name = {self.name}\n"
                f"description = {self.description}\n"
                f"price = {self.price}\n"
                f"country = {self.country}\n ")


# class buyer
class Buyer:

    def __init__(self, name, surname, age, phone_number):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        return (f"name = {self.name} {self.surname}\n"
                f"phone = +{self.phone_number}\n")


# class Purchase
class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, count):
        self.products[item] = count

    def get_total(self):
        self.total = 0
        for item, count in self.products.items():
            self.total += count * item.price
        return self.total

    def __str__(self):
        products_string = ""
        for item, count in self.products.items():
            products_string += f"{item.name}: {count}\n"

        return (f"User: {self.user.name} {self.user.surname}\n"
                f"Phone: +{self.user.phone_number}\n"
                f"Products:\n{products_string}"
                f"Total value = {self.get_total()}\n")


iphone = Item("iphone", "model - 15", 100500, "USA")
lemon = Item("lemon", "yellow", 20, "Spain")
apple = Item("apple", "green", 10, "Poland")
#print(lemon)
first_buyer = Buyer("John", "Johnson", 33, "420807602748")
#print(first_buyer)

cart = Purchase(first_buyer)
cart.add_item(lemon, 6)
cart.add_item(apple, 4)
cart.get_total()
print(cart)
