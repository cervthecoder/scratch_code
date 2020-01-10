class Student:

    def __init__(self, name, major, gpa, isonprobation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = isonprobation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False


