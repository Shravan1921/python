student_ID = input("enter student ID")
student_name = input("enter student name")
student_attendance = int(input("enter student attendance"))

subjects = 0
total_score = 0

while input("Add another sub score?(yes to continue): ").lower() == "yes":
     total_score = float(input("Enter Subject Score :"))
     subjects +=1
     
     cont = input("Do you want to enter another score?(yes/Yes to continue):")
     if cont.lower() != "yes":
          break
     
     average_score = total_score / subjects

     if average_score >= 85:
          performance = "Excellent"
     elif average_score >=70 :
          performance = "Good"
     elif average_score >=50 :
          performance = "Average"
     else:
          performance = "Needs to be improved"
     
     
     if student_attendance >=75:
          attendance_status = "WARNING! Low attendance"
     else:
          attendance_status = "OK: Attendance satisfied"

print("\n----Final Results----")
print(f"Student_ID:         {student_ID}")
print(f"Student_Name:       {student_name}")
print(f"Student_Attendance: {student_attendance}")
print(f"Total_Score:        {total_score}")
print(f"Average Score:      {average_score}")
print(f"Performance Level:  {performance}")









