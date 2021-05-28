graduatedStudents = ['Mohannad','Samer','Samar','Ahamad','Rola','Samira','Amira']
student = input("Enter The Student name:")
StudentName = student.capitalize() # Just To Make The First Letter A Capital Letter. 
if StudentName in graduatedStudents:
   print("The student " + StudentName + " is graduated!")
else:
   print("Student " + StudentName + " is NOT graduated yet.")
