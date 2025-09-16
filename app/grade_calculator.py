import copy
from grades import Grades
from grade_weights import GradeWeights

class GradeCalculator:
    """
    Calculates the overall course grade for ENPM611.
    """

    @staticmethod
    def calculate_course_percentage(grades: Grades, weights: GradeWeights) -> float:
        """
        Calculates the percentage of the overall course grade.
        Returns None if not all required grades are present.
        """
        # Convert tasks into a dict for easy access
        grade_dict = {a["Task"]: a["grade"]/100 for a in grades.assignments}

        # Check if all required tasks are present
        required = ["Quiz 1", "Quiz 2", "Midterm", "Project", "Final Exam"]
        if not all(task in grade_dict for task in required):
            print("Can't calculate final grade without all assignments graded")
            return None

        # Compute weighted grade
        quizzes_part = ((grade_dict["Quiz 1"] + grade_dict["Quiz 2"]) / 2) * weights.quizzes
        midterm_part = grade_dict["Midterm"] * weights.midterm
        project_part = grade_dict["Project"] * weights.project
        final_part = grade_dict["Final Exam"] * weights.final
        return quizzes_part + midterm_part + project_part + final_part

    @staticmethod
    def calculate_optimistic_course_percentage(grades: Grades, weights: GradeWeights) -> float:
        """
        Calculates the course grade assuming all missing tasks are 100%.
        """
        grade_dict = {a["Task"]: a["grade"]/100 for a in grades.assignments}

        # Fill in missing required tasks with 100%
        required = ["Quiz 1", "Quiz 2", "Midterm", "Project", "Final Exam"]
        for task in required:
            if task not in grade_dict:
                grade_dict[task] = 1.0

        # Compute weighted grade
        quizzes_part = ((grade_dict["Quiz 1"] + grade_dict["Quiz 2"]) / 2) * weights.quizzes
        midterm_part = grade_dict["Midterm"] * weights.midterm
        project_part = grade_dict["Project"] * weights.project
        final_part = grade_dict["Final Exam"] * weights.final
        return quizzes_part + midterm_part + project_part + final_part

    @staticmethod
    def calculate_letter_grade(percentage_grade: float) -> str:
        """Convert percentage grade into a letter grade."""
        if percentage_grade is None:
            return None
        if percentage_grade >= 0.91:
            return 'A'
        elif percentage_grade >= 0.8:
            return 'B'
        elif percentage_grade >= 0.74:
            return 'C'
        elif percentage_grade >= 0.6:
            return 'D'
        else:
            return 'F'
