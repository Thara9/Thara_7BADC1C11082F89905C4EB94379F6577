class Student:

  def __init__(self, name ,roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa
def sort_students(students_list):
  sorted_students = sorted(students_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students
Student = [
  Student("rakhi", "A123", 9.8),
  Student("rishi", "A124", 8.9),
  Student("dev", "A125", 8.1),
  Student("vishnu", "126", 7.9),
]
sorted_students = sort_students(Student)
for student in sorted_students:
   print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,student.roll_number, student.cgpa))
