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