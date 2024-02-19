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


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(first_name, last_name, age, gender)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()}record_book: {self.record_book}\n'


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()
        self.counter = 0

    def add_student(self, student):
        self.group.add(student)
        self.counter += 1
        if self.counter > 10:
            raise Exception('There cannot be more than 10 students in a group')

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)
        else:
            print("Student not found.")

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
            else:
                return f"There is no such student in the {self.number} group"

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f'Number:{self.number}\n {all_students} '


student1 = Student("male", 20, "John", "Smith", "A123")
student2 = Student("female", 19, "Katherine", "Taylor", "A124")
group1 = Group(12)
group1.add_student(student1)
group1.add_student(student2)
#print(group1)
# print(group1.find_student("Taylor"))
# print(group1.find_student("Johnson"))
#group1.delete_student("Taylor")

student3 = Student("female", 19, "Katherine", "Taylor", "A124")
group1.add_student(student3)
student4 = Student("female", 19, "Katherine", "Taylor", "A124")
group1.add_student(student4)
student5 = Student("female", 19, "Katherine", "Taylor", "A124")
group1.add_student(student5)
student6 = Student("female", 19, "Katherine", "Taylor", "A124")
group1.add_student(student6)
student7 = Student("female", 19, "Katherine", "Taylor", "A124")
group1.add_student(student7)
student8 = Student("female", 19, "Katherine", "Taylor", "A124")
group1.add_student(student8)
student9 = Student("female", 19, "Katherine", "Taylor", "A124")
group1.add_student(student9)
student10 = Student("female", 19, "Katherine", "Taylor", "A124")
group1.add_student(student10)

student11 = Student("female", 19, "Katherine", "Taylor", "A124")
group1.add_student(student11)
print(group1)