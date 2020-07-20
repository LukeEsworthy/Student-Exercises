from student import Student


class Instructor:

    def __init__(self, first_name, last_name, slack_handle, specialty):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.cohort = ""
        self.specialty = specialty

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.specialty}"

    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)
