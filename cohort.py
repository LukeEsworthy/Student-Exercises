class Cohort:

    def __init__(self, name):
        self.name = name
        self.student = []
        self.instructor = []

    def __str__(self):
        return f"{self.name}"
