import json
from Task import *
from Member import *

def readTestCase(filename):
    file = open(filename)
    data = json.load(file)
    parseMembers(data['members'])
    parseTasks(data['tasks'])

def parseTasks(tasks):
    for task in tasks:
        name = task['name']
        prerequisites = task['prerequisite']
        skillsRequired = task['skills_required']
        newTask = Task(name, prerequisites, skillsRequired)


def parseMembers(members):
    for member in members:
        name = member['name']
        skills = member['skills']
        newMember = Member(name, skills)
    