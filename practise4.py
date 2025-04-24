import numpy as np

# Generate random student grades for 5 students and 4 subjects
# Grades between 60 and 100
student_grades = np.random.randint(60, 100, size=(5, 4))
print("Student Grades (5 students x 4 subjects):")
print(student_grades)

# 1. Get the grades of the first student
first_student_grades = student_grades[0]
print("\n1. First student's grades:", first_student_grades)

# 2. Get the grade in the second subject for the third student
third_student_second_subject = student_grades[2, 1]
print("\n2. Third student's grade in second subject:", third_student_second_subject)

# 3. Get grades of all students in the last subject
last_subject_grades = student_grades[:, -1]
print("\n3. All grades in last subject:", last_subject_grades)

# 4. Get grades of first 3 students in all subjects
first_three_students = student_grades[:3]
print("\n4. Grades of first 3 students:")
print(first_three_students)

# 5. Get grades of all students in first 2 subjects
first_two_subjects = student_grades[:, :2]
print("\n5. Grades in first 2 subjects:")
print(first_two_subjects)

# 6. Calculate the average grade for each student
student_averages = np.mean(student_grades, axis=1)
print("\n6. Average grade for each student:", student_averages)

# 7. Count students who passed (grades >= 70) in each subject
passing_counts = np.sum(student_grades >= 70, axis=0)
print("\n7. Number of passing students in each subject:", passing_counts)

# Additional analysis that might be useful:

# Get the highest grade in each subject
highest_grades = np.max(student_grades, axis=0)
print("\nHighest grade in each subject:", highest_grades)

# Get the lowest grade in each subject
lowest_grades = np.min(student_grades, axis=0)
print("\nLowest grade in each subject:", lowest_grades)

# Find which student has the highest average grade
best_student_index = np.argmax(student_averages)
print("\nStudent with highest average:", best_student_index + 1)
print("Their average grade:", student_averages[best_student_index])