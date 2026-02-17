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