class Human:

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def __str__(self):
        return (f'name: {self.first_name} {self.last_name}\n'
                f'age: {self.age}\n'
                f'gender: {self.gender}\n')