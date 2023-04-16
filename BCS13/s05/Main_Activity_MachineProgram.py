# Initialize lists to store student names and grades
student_names = []
class_participation_grades = []
summative_assessment_grades = []
final_examination_grades = []

# Input grades for five students
for i in range(5):
    name = input("Enter name of student {}: ".format(i+1))
    class_participation_total = 0
    for j in range(5):
        class_participation = float(input("Enter class participation grade {} for {}: ".format(j+1, name)))
        class_participation_total += class_participation
    summative_assessment_total = 0
    for k in range(3):
        summative_assessment = float(input("Enter summative assessment grade {} for {}: ".format(k+1, name)))
        summative_assessment_total += summative_assessment
    final_examination = float(input("Enter final examination grade for {}: ".format(name)))

    student_names.append(name)
    class_participation_grades.append(class_participation_total / 5)  # Average of class participation grades
    summative_assessment_grades.append(summative_assessment_total / 3)  # Average of summative assessment grades
    final_examination_grades.append(final_examination)
# Calculate grades and letter grades for each student

print("--------------------------------------------")
print("|Student Name | Average Grade | Letter Grade|")
print("--------------------------------------------")

# Loop through the students
for i in range(5):
    # Calculate the average grade and letter grade
    grade = (class_participation_grades[i] * 0.3) + (summative_assessment_grades[i] * 0.3) + (
                final_examination_grades[i] * 0.4)
    letter_grade = ''
    if grade >= 90:
        letter_grade = 'A'
    elif grade >= 80:
        letter_grade = 'B'
    elif grade >= 70:
        letter_grade = 'C'
    elif grade >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    # Format the row as a table

    print("|{:<12}| {:<14.2f}| {:<12}|".format(student_names[i], grade, letter_grade))
    print("--------------------------------------------")
