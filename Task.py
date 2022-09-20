class Task:
    def __init__(self, name, prerequisites, skills):
        self.name = name
        self.skills = skills                   #List of strings
        self.prerequisites = prerequisites     #List of strings
        