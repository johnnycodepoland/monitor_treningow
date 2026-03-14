import json

def load_users():
    users = {}

    try:
        with open("data/users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        return {}
    return users

def load_trainings():
    trainings = {}

    try:
        with open ("data/trainings.json", "r") as file:
            trainings = json.load(file)
    except FileNotFoundError:
        return {}
    return trainings

def load_personal_bests():
    personal_bests = {}

    try:
        with open ("data/personal_bests.json", "r") as file:
            personal_bests = json.load(file)
    except FileNotFoundError:
        return {}
    return personal_bests
