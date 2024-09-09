

import copy


from grades import Grades
from grade_weights import GradeWeights

class GradeCalculator:
    """
    Calculates the overall course grade for ENPM611.
    """
    
    @staticmethod
    def calculate_course_percentage(grades:Grades, weights:GradeWeights) -> float:
        """"
        Calculates the percentace of the overall course
        grade. If not all grades have been set yet, this
        function returns None.
        """
        if grades.quiz_1 is None or grades.quiz_2 is None or grades.midterm is None or grades.project is None or grades.final is None:
            print("Can't calculate final grade without all assignments graded")
            return None
        else:
            quizzes_part = ((grades.quiz_1 + grades.quiz_2) / 2) * weights.quizzes
            midterm_part = grades.midterm * weights.midterm
            project_part = grades.project * weights.project
            final_part = grades.final * weights.final
            course_grade = quizzes_part + midterm_part + project_part + final_part
            return course_grade
        
        
    @staticmethod
    def calculate_optimistic_course_percentage(grades:Grades, weights:GradeWeights) -> float:
        """
        Calculates the course percentage grade assuming that
        all assignments that have not been completed receive 100%. 
        """
        


        optimistic_grades:Grades = copy.copy(grades)
        


        if optimistic_grades.quiz_1 is None:
            optimistic_grades.quiz_1 = 1
        if optimistic_grades.quiz_2 is None:
            optimistic_grades.quiz_2 = 1
        if optimistic_grades.midterm is None:
            optimistic_grades.midterm = 1
        if optimistic_grades.project is None:
            optimistic_grades.project = 1
        if optimistic_grades.final is None:
            optimistic_grades.final = 1
        


        return GradeCalculator.calculate_course_percentage(optimistic_grades, weights)
        
    @staticmethod
    def calculate_letter_grade(percentage_grade:float) -> str:
        """
        Calculate the letter grade giving a percentage grade.
        The cutoffs for letter grades can be found in the introductory slides
        and in the syllabus.
        """
        

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