def load_users():
    users = {}

    try:
        with open("data/users.txt", "r") as file:
            for line in file:
                login, password = line.strip().split(":")
                users[login] = password
    except FileNotFoundError:
        return {}
    return users

def load_trainings():
    trainings = {}

    try:
        with open ("data/trainings.csv", "r") as file:
            for line in file:
                line = line.strip() # usuwa nam "białe znaki" z kodu np. \n
                user, date, distance, time = line.split(",")
                if user not in trainings:
                    trainings[user] = []
                trainings[user].append((date, int(distance), int(time)))
    except FileNotFoundError:
        return {}
    return trainings

def load_personal_bests():
    personal_bests = {}

    try:
        with open ("data/personal_bests.csv", "r") as file:
            for line in file:
                line = line.strip() # usuwa nam "białe znaki" z kodu np. \n
                user, time, style = line.strip().split(",")
                if user not in personal_bests:
                    personal_bests[user] = {}
                personal_bests[user][style] = time
    except FileNotFoundError:
        return {}
    return personal_bests
