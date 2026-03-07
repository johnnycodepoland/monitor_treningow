from utils import load_personal_bests
styles = {
    "1": {
        "name": "Motylkowy",
        "50": "50_butterfly",
        "100": "100_butterfly",
        "200": "200_butterfly"
    },
    "2": {
        "name": "Grzbietowy",
        "50": "50_backstroke",
        "100": "100_backstroke",
        "200": "200_backstroke"
    },
    "3": {
        "name": "Klasyczny",
        "50": "50_breaststroke",
        "100": "100_breaststroke",
        "200": "200_breaststroke"
    },
    "4": {
        "name": "Dowolny",
        "50": "50_freestyle",
        "100": "100_freestyle",
        "200": "200_freestyle",
        "400": "400_freestyle",
        "800": "800_freestyle",
        "1500": "1500_freestyle"
    },
    "5": {
        "name": "Zmienny",
        "100": "100_medley",
        "200": "200_medley",
        "400": "400_medley"
    }
}

def save_personal_best(login, time, description):
    try:
        with open("data/personal_bests.csv", "a") as file:
            file.write(f"{login.strip()},{time.strip()},{description.strip()}\n")
        print("Rekord życiowy został dodany ✅")
    except FileNotFoundError:
        return

def add_personal_best(login):
    while True:
        for key, val in styles.items():
            print(f"{key}. {val['name']}") # key to numer sekcji np. 1,2 ; val zawiera wszystkie dane zawarte w np. "1", a val['name'] zawiera tylko nazwę którą potrzebujemy
        while True:
            choose = input("Twój wybór: ")
            if choose in styles:
                current_style = styles[choose]
                for i, key in enumerate(current_style):
                    if key == "name":
                        continue
                    else:
                        print(f"{i}. {key}")
                while True:
                    choose_2 = input("Twój wybór (długość): ")
                    if choose_2 in styles[choose]:
                        choosed_style = styles[choose][choose_2]
                        if check_personal_bests(login, choosed_style):
                            print("Masz już czas na tym dystansie ❌")
                            return
                        else:
                            while True:
                                try:
                                    time = input("Podaj swój czas (MM:SS:ss): ")
                                    minutes, seconds, milliseconds = time.split(":")
                                    if minutes.isdigit() and seconds.isdigit() and milliseconds.isdigit() and int(seconds) < 60 and int(milliseconds) < 100:
                                        save_personal_best(login, time, styles[choose][choose_2])
                                        return
                                    else:
                                        print("Podano niepoprawny format czasu ❌")
                                except ValueError:
                                    print("Podano niepoprawny format czasu ❌")
                    else:
                        print("Podano niepoprawny dystans ❌")
            else:
                print("Taki styl nie istnieje ❌")

def check_personal_bests(login, choosed_style):
    time_found = False
    try:
        with open ("data/personal_bests.csv", "r") as file:
            for line in file:
                line = line.strip() # usuwa nam "białe znaki" z kodu np. \n
                if not line:
                    continue
                user, time, style = line.split(",")
                if user.strip() == login and style.strip() == choosed_style:
                    print(f"🏊 Styl: {style}")
                    print(f"⏱️ Czas: {time}")
                    print("-------------------------")
                    time_found = True # Dajemy jako True jest uda nam się znaleźć szukany czas
                    return True
    except FileNotFoundError:
        return
    if not time_found:
        return False

def show_personal_best(login):
    while True:
        for key, val in styles.items():
            print(f"{key}. {val['name']}") # key to numer sekcji np. 1,2 ; val zawiera wszystkie dane zawarte w np. "1", a val['name'] zawiera tylko nazwę którą potrzebujemy
        while True:
            choose = input("Twój wybór: ")
            if choose in styles:
                current_style = styles[choose]
                for i, key in enumerate(current_style):
                    if key == "name":
                        continue
                    else:
                        print(f"{i}. {key}")
                while True:
                    choose_2 = input("Twój wybór (długość): ")
                    if choose_2 in styles[choose]:
                        choosed_style = styles[choose][choose_2]
                        check_personal_bests(login, choosed_style)
                        if check_personal_bests(login, choosed_style) is not False:
                            return
                        else:
                            print("Nie masz czasu na tym dystansie ❌")
                            return
                    else:
                        print("Podano niepoprawny dystans ❌")
            else:
                print("Taki styl nie istnieje ❌")

def edit_personal_best(login):
    personal_bests = load_personal_bests()

    while True:
        for key, val in styles.items():
            print(f"{key}. {val['name']}") # key to numer sekcji np. 1,2 ; val zawiera wszystkie dane zawarte w np. "1", a val['name'] zawiera tylko nazwę którą potrzebujemy
        while True:
            choose = input("Twój wybór: ")
            if choose in styles:
                current_style = styles[choose]
                for i, key in enumerate(current_style):
                    if key == "name":
                        continue
                    else:
                        print(f"{i}. {key}")
                while True:
                    choose_2 = input("Twój wybór (długość): ")
                    if choose_2 in styles[choose]:
                        choosed_style = styles[choose][choose_2]
                        if check_personal_bests(login, choosed_style):
                            while True:
                                try:
                                    new_time = input("Podaj swój nowy czas (MM:SS:ss): ")
                                    minutes, seconds, milliseconds = new_time.split(":")
                                    if minutes.isdigit() and seconds.isdigit() and milliseconds.isdigit() and int(seconds) < 60 and int(milliseconds) < 100:
                                        personal_bests[login][choosed_style] = new_time
                                        try:
                                            with open("data/personal_bests.csv", "w") as file:
                                                for user, records in personal_bests.items():
                                                    for style, time in records.items():
                                                        file.write(f"{user.strip()},{time.strip()},{style.strip()}\n")
                                            print("Nowy czas został zapisany ✅")
                                            return
                                        except FileNotFoundError:
                                            return
                                    else:
                                        print("Podano niepoprawny format czasu ❌")
                                except ValueError:
                                    print("Podano niepoprawny format czasu ❌")
                        else:
                            print("Nie masz czasu na tym dystansie ❌")
                            return
                    else:
                        print("Podano niepoprawny dystans ❌")
            else:
                print("Taki styl nie istnieje ❌")

def delete_personal_best(login):
    personal_bests = load_personal_bests()

    while True:
        for key, val in styles.items():
            print(f"{key}. {val['name']}") # key to numer sekcji np. 1,2 ; val zawiera wszystkie dane zawarte w np. "1", a val['name'] zawiera tylko nazwę którą potrzebujemy
        while True:
            choose = input("Twój wybór: ")
            if choose in styles:
                current_style = styles[choose]
                for i, key in enumerate(current_style):
                    if key == "name":
                        continue
                    else:
                        print(f"{i}. {key}")
                while True:
                    choose_2 = input("Twój wybór (długość): ")
                    if choose_2 in styles[choose]:
                        choosed_style = styles[choose][choose_2]
                        if check_personal_bests(login, choosed_style):
                            while True:
                                confirm = input("Czy na pewno chcesz usunąć rekord? (t/n): ")
                                if confirm.lower() == "t":
                                    try:
                                        del personal_bests[login][choosed_style]
                                        try:
                                            with open("data/personal_bests.csv", "w") as file:
                                                for user, records in personal_bests.items():
                                                    for style, time in records.items():
                                                        file.write(f"{user.strip()},{time.strip()},{style.strip()}\n")
                                            print("Rekord życiowy został usunięty ✅")
                                            return
                                        except FileNotFoundError:
                                            return
                                    except KeyError:
                                        print("Wystąpił błąd podczas usuwania ❌")
                                elif confirm.lower() == "n":
                                    print("Anuluje usuwanie ❌")
                                    return
                                else:
                                    print("Wybrano niepoprawną opcję ❌")
                        else:
                            print("Nie masz czasu na tym dystansie ❌")
                            return
                    else:
                        print("Podano niepoprawny dystans ❌")
            else:
                print("Taki styl nie istnieje ❌")