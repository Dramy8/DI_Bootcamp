#%%
#EX1
# You are given a dictionary containing student names as keys and lists of their grades as values. 
# Your task is to create a summary report that calculates the average grade for each student, 
# assigns a letter grade, and determines the class average.
student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}
# Calculate the average grade for each student and store the results in a new dictionary called student_averages.
# Assign each student a letter grade (A, B, C, D, F) based on their average grade according to the following scale,
# and store the results in a dictionary called student_letter_grades:
# A: 90 and above
# B: 80 to 89
# C: 70 to 79
# D: 60 to 69
# F: Below 60
# Calculate the class average (the average of all students’ averages) and print it.
# Print the name of each student, their average grade, and their letter grade.

student_averages = {}
student_letter_grades = {}

for name, grades in student_grades.items():
    average = sum(grades)/len(grades)
    student_averages[name] = average
    
    if average>=90:
        letter = 'A'
    elif average>=80:
        letter = 'B'
    elif average>=70:
        letter = 'C'
    elif average>=60:
        letter = 'D'
    else:
        letter = 'F'
    student_letter_grades[name] = letter

print (f"Average grade for each student: {student_averages}")

print(f"Average letter grade for each student: {student_letter_grades}")

class_average = sum(student_averages.values())/len(student_averages.values())
print(f"Class average grade: {class_average}")

print("Summary of grades for each student: ")
for name in student_averages:
    print(f"{name}, {student_averages[name]}, {student_letter_grades[name]}")

#%%



