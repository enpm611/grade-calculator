import json
import os

class Grades:
    """
    Stores grades from assignments and allows loading them from JSON.
    """

    def __init__(self):
        self.assignments = []

    def load_from_json(self, filename):
        """Load assignments from a JSON file."""
        if not os.path.isabs(filename):
            filename = os.path.join(os.path.dirname(__file__), filename)

        with open(filename, "r") as f:
            data = json.load(f)

        if "assignments" not in data:
            raise ValueError("JSON must contain an 'assignments' list")

        self.assignments = data["assignments"]

    def as_dict(self):
        """
        Return assignments as a dictionary:
        {"Quiz 1": 0.98, "Midterm": 1.0, ...}
        Converts grades to fractions (out of 1.0).
        """
        return {a["Task"]: a["grade"] / 100 for a in self.assignments}

    def __str__(self) -> str:
        """Pretty print assignments with percentages."""
        if not self.assignments:
            return "No grades submitted yet."

        grades = [f"{a['Task']}: {a['grade']}%" for a in self.assignments]
        return "GRADES --- " + ", ".join(grades)

    def average(self):
        """Compute average grade as a percentage (0–100)."""
        if not self.assignments:
            return 0.0
        total = sum(a["grade"] for a in self.assignments)
        return total / len(self.assignments)
