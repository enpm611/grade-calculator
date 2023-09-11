

class GradeWeights:
    """
    Specifies the weights assigned to each grade
    catefory for ENPM611. The weights can be found
    in the introductory slides and in the syllabus.
    """
    
    def __init__(self) -> None:
        self.quizzes = 0.1
        self.quiz1 = 0.05
        self.quiz2 = 0.05
        self.midterm = 0.2
        self.project = 0.4
        self.final = 0.3