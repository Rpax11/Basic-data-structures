grades=[[5, 3, 3, 5, 4],[2, 2, 2, 3],[4, 5, 5, 2],[4, 4, 3],[5, 5, 5, 4, 5]]
students={'Johnny','Bilbo','Steve','Khendrik','Aaron'}
average_grades={}
students_list=sorted(students)
for student,grades_list in zip(students_list, grades):
 average = sum(grades_list)/len(grades_list)
 average_grades[student]=average
print(average_grades)