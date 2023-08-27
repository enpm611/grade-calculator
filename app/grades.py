

class Grades:
    """
    Stores all individual class grades.
    """
    
    def __init__(self, quiz_1=None, quiz_2=None, midterm=None, project=None, final=None) -> None:
        """
        This constructor declares globale variables
        with the self prefix and sets them to null, 
        which is None in Python. The constructor is
        called when an object is created with Grades().
        """
        self.quiz_1 = quiz_1
        self.quiz_2 = quiz_2
        self.midterm = midterm
        self.project = project
        self.final = final
        
    def set_all(self, quiz_1=None, quiz_2=None, midterm=None, project=None, final=None):
        """
        Sets the grades all at once. 
        When calling this function, the caller can specify
        the parameters to be set like so:
        Grades().set_all(midterm=None, project=None)
        """
        self.quiz_1 = quiz_1
        self.quiz_2 = quiz_2
        self.midterm = midterm
        self.project = project
        self.final = final
        
    def __str__(self) -> str:
        """
        This method gets called whenever this object is
        printed to string (e.g., standard out).
        """
        grades = []
        if self.quiz_1 is not None:
            grades.append(f'Quiz 1: {self.quiz_1}')
        if self.quiz_2 is not None:
            grades.append(f'Quiz 2: {self.quiz_2}')
        if self.midterm is not None:
            grades.append(f'Midterm Exam: {self.midterm}')
        if self.project is not None:
            grades.append(f'Project: {self.project}')
        if self.final is not None:
            grades.append(f'Final Exam: {self.final}')
            
        if len(grades) <= 0:
            return 'No grades submitted yet.'
        else:
            # Create a string in which each element of the list
            # is separate by a comma
            return 'GRADES --- ' + ', '.join(grades)