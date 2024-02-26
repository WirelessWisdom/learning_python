import student_group
from student_group import student
from student_group import group
from student_group import human


student1 = student_group.student.Student("male", 20, "John", "Smith", "A123")
student2 = student_group.student.Student("female", 19, "Katherine", "Taylor", "A124")
group1 = student_group.group.Group(12)
group1.add_student(student1)
group1.add_student(student2)
print(group1)
# print(group1.find_student("Taylor"))
# print(group1.find_student("Johnson"))
#group1.delete_student("Taylor")

student3 = student_group.student.Student("female", 19, "Katherine", "Taylor", "A124")
group1.add_student(student3)
student4 = student_group.student.Student("female", 19, "Katherine", "Taylor", "A124")
group1.add_student(student4)
student5 = student_group.student.Student("female", 19, "Katherine", "Taylor", "A124")
group1.add_student(student5)
student6 = student_group.student.Student("female", 19, "Katherine", "Taylor", "A124")
group1.add_student(student6)
student7 = student_group.student.Student("female", 19, "Katherine", "Taylor", "A124")
group1.add_student(student7)
student8 = student_group.student.Student("female", 19, "Katherine", "Taylor", "A124")
group1.add_student(student8)
student9 = student_group.student.Student("female", 19, "Katherine", "Taylor", "A124")
group1.add_student(student9)
student10 = student_group.student.Student("female", 19, "Katherine", "Taylor", "A124")
group1.add_student(student10)

student11 = student_group.student.Student("female", 19, "Katherine", "Taylor", "A124")
group1.add_student(student11)
print(group1)