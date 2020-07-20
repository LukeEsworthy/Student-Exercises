class Student:

    def __init__(self, first_name, last_name, slack_handle):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.cohort = ""
        self.exercises = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}\'s Slack handle is {self.slack_handle}, and I am working on {self.exercises}"
