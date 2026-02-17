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

def zapisz_rekord_zyciowy(login, time, description):
    with open("data/personal_bests.csv", "a") as file:
        file.write(f"{login}, {time}, {description}\n")
    print("Rekord życiowy został dodany ✅")

def dodaj_rekord_zyciowy(login):
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
                        while True:
                            try:
                                time = input("Podaj swój czas (MM:SS:ss): ")
                                minutes, seconds, milliseconds = time.split(":")
                                if minutes.isdigit() and seconds.isdigit() and milliseconds.isdigit() and int(seconds) < 60 and int(milliseconds) < 100:
                                    zapisz_rekord_zyciowy(login, time, styles[choose][choose_2])
                                    return
                                else:
                                    print("Podano niepoprawny format czasu ❌")
                            except ValueError:
                                print("Podano niepoprawny format czasu ❌")
                    else:
                        print("Podano niepoprawny dystans ❌")
            else:
                print("Taki styl nie istnieje ❌")

def sprawdz_rekordy_zyciowe(login, choosed_style):
    time_found = False

    with open ("data/personal_bests.csv", "r") as file:
        for line in file:
            line = line.strip() # usuwa nam "białe znaki" z kodu np. \n
            user, time, style = line.split(",")
            if user.strip() == login and style.strip() == choosed_style:
                print(f"🏊 Styl: {style}")
                print(f"⏱️ Czas: {time}")
                print("-------------------------")
                time_found = True # Dajemy jako True jest uda nam się znaleźć szukany czas

    if not time_found:
        print("Nie masz czasu na tym dystansie ❌")

def wyswietl_rekord_zyciowy(login):
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
                        sprawdz_rekordy_zyciowe(login, choosed_style)
                        return
                    else:
                        print("Podano niepoprawny dystans ❌")
            else:
                print("Taki styl nie istnieje ❌")