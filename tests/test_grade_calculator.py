import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

import pytest
from grade_calculator import GradeCalculator
from grades import Grades
from grade_weights import GradeWeights


# FUNCTIONAL (BLACK-BOX) TESTS: Boundary Value Analysis (BVA)


def test_tc_01():
    """TC-01: Verification of 'A' grade boundary"""
    #Input values: 0.95
	#Expected output: A

    assert GradeCalculator.calculate_letter_grade(0.95) == 'A'
    
def test_tc_02():
    """TC-02: Verification of upper 'B' grade boundary"""
    #Input values: 0.899
	#Expected output: B

    assert GradeCalculator.calculate_letter_grade(0.899) == 'B'
    
def test_tc_03():
    """TC-03: Verification of 'B' grade boundary """
    #Input values: 0.8
	#Expected output: B
    assert GradeCalculator.calculate_letter_grade(0.8) == 'B'
    
def test_tc_04():
    """TC-04: Verification of upper 'C' grade boundary"""
    #Input values: 0.799
	#Expected output: C

    assert GradeCalculator.calculate_letter_grade(0.799) == 'C'
    
def test_tc_05():
    """TC-05: Verification of 'C' grade boundary"""
    #Input values: 0.74
	#Expected output: C

    assert GradeCalculator.calculate_letter_grade(0.74) == 'C'
    
def test_tc_06():
    """TC-06: Verification of upper 'D' grade boundary"""
    #Input values: 0.739
	#Expected output: D

    assert GradeCalculator.calculate_letter_grade(0.739) == 'D'
    
def test_tc_07():
    """TC-07: Verification of 'D' grade boundary"""
    #Input values: 0.6
	#Expected output: D

    assert GradeCalculator.calculate_letter_grade(0.6) == 'D'
    
def test_tc_08():
    """TC-08: Verification of 'F' grade boundary"""
    #Input values: 0.599
	#Expected output: F

    assert GradeCalculator.calculate_letter_grade(0.599) == 'F'
    

    
# STRUCTURAL (WHITE-BOX) TESTS: Path Testing

def test_tc_09():
    """TC-09: Verification of th when a grade component is missing"""
    #Input values: quiz_1 = None, quiz_2 = 0.8, midterm = 0.7, project = 0.85, final = 0.9
	#Expected output: None, because at least one grade is missing
    grades = Grades(quiz_1=None, quiz_2=0.8, midterm=0.7, project=0.85, final=0.9)
    weights = GradeWeights()
    result = GradeCalculator.calculate_course_percentage(grades, weights)
    assert result is None
    
def test_tc_10():
    """TC-10: Verification of th when all grade components are valid"""
    #Input values: quiz_1 = 0.7 , quiz_2 = 0.8, midterm = 0.7, project = 0.85, final = 0.9
	#Expected output: valid course percentage = 0.825
    grades = Grades(quiz_1=0.7, quiz_2=0.8, midterm=0.7, project=0.85, final=0.9)
    weights = GradeWeights()
    result = GradeCalculator.calculate_course_percentage(grades, weights)
    assert result == 0.825
