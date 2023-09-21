class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa
def sort_students(student_list):
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students
students = [
Student ("Sujitha","22UCS29",9.3),
Student ("Janci","22UCS07",9.4),
Student ("Sindhuja","22UCS27",9.2),
Student ("Priya","22UCS21",9.1),
Student ("Lakshmipriya","22UCS10",8.9)
]
sorted_students = sort_students(students)
for student in sorted_students:
  print("name:{},roll Number:{},CGPA:{}".format(student.name,
student.roll_number,
             student.cgpa))
