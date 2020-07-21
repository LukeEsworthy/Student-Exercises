from nssperson import NSSPerson


class Student(NSSPerson):

    def __init__(self, first_name, last_name, slack_handle):
        super().__init__(first_name, last_name, slack_handle)
        self.exercises = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}\'s Slack handle is {self.slack_handle}, and I am working on {self.exercises}"
