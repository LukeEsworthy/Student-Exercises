from nssperson import NSSPerson
from student import Student


class Instructor(NSSPerson):

    def __init__(self, first_name, last_name, slack_handle, specialty):
        super().__init__(first_name, last_name, slack_handle)
        self.specialty = specialty

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.specialty}"

    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)
