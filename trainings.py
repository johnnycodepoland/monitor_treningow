from utils import load_trainings

def dodaj_trening(login):
    from datetime import datetime

    while True:
        try:
            training_date = str(input("Podaje datę treningu (YYYY-MM-DD): "))
            datetime.strptime(training_date, "%Y-%m-%d") # ta funkcja pozwala nam
            break
        except:
            print("Podano niepoprawny format daty ❌")
    while True:
        try:
            training_distance = int(input("Podaj dystans treningu (m): "))
            break
        except ValueError:
            print("Podaj liczbę!")
    while True:
        try:
            training_time = int(input("Podaj długość treningu (min): "))
            break
        except ValueError:
            print("Podaj liczbę!")

    with open ("data/trainings.csv", "a") as file:
        file.write(f"{login}, {training_date}, {training_distance}, {training_time}\n")
    print("Trening został dodany ✅")

def wyswietl_treningi(login):
    trainings = load_trainings()

    if login in trainings:
        for date, distance, time in trainings[login]:
            print(f"📅 Data: {date}")
            print(f"🏊 Dystans: {distance}m")
            print(f"⏱️ Czas: {time} min")
            print("-------------------------")
    else:
        print("Nie masz jeszcze żadnych treningów ❌")
