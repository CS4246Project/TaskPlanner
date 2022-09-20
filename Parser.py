import json
from Task import *
from Member import *

primitive_skills = set()
data = None

def readTestCase(filename):
    file = open(filename)
    data = json.load(file)
    members = parseMembers(data['members'])
    tasks = parseTasks(data['tasks'])
    return (members, tasks)

def parseTasks(tasks):
    tasks = []
    for task in tasks:
        name = task['name']
        prerequisites = task['prerequisite']
        skillsRequired = task['skills_required']
        for skill in skillsRequired:
            if skill not in primitive_skills:
                skillsRequired.extend(data[skill])
        tasks.append(Task(name, prerequisites, skillsRequired))
    return tasks


def parseMembers(members):
    members = []
    for member in members:
        name = member['name']
        skills = member['skills']
        for skill in skills:
            primitive_skills.add(skill)
        members.append(Member(name, skills))
    return members

    