from grades import Grades
from grade_weights import GradeWeights
from grade_calculator import GradeCalculator

# Instantiate Grade and Weights objects
my_grades = Grades()
weights = GradeWeights()

# Load grades from JSON
my_grades.load_from_json("grades.json")

# Print out the grades to console
print(my_grades)

# Calculate course grade based on the grades set above
percentage_grade = GradeCalculator.calculate_course_percentage(my_grades, weights)
if percentage_grade is None:
    print("Can't calculate overall course grade without all individual grades.")
else:
    letter_grade = GradeCalculator.calculate_letter_grade(percentage_grade)
    print(f'The letter grade with an overall {percentage_grade*100:.2f}% is {letter_grade}')

# Calculate the grade assuming that all assignments not turned in yet, will be 100%
optimistic_percentage_grade = GradeCalculator.calculate_optimistic_course_percentage(my_grades, weights)
optimistic_letter_grade = GradeCalculator.calculate_letter_grade(optimistic_percentage_grade)
print(f'If all other assignments are 100%, the overall course would be {optimistic_percentage_grade*100:.2f}%, which is a {optimistic_letter_grade}')
