from auth import logowanie, rejestracja, password_tries, login_tries
from personal_bests import dodaj_rekord_zyciowy, wyswietl_rekord_zyciowy, edytuj_rekord_zyciowy
from trainings import dodaj_trening, wyswietl_treningi
from utils import load_users


def panel_uzytkownika(login):
    zalogowany = True
    choose = ""
    users = load_users()

    while zalogowany:
        print("================================")
        print("  WITAJ W PANELU UŻYTKOWNIKA  ")
        print("================================")
        print("Wybierz jedną z poniższych opcji:")
        print("1. Zmień hasło")
        print("2. Dodaj trening")
        print("3. Wyświetl dodane treningi")
        print("4. Dodaj rekord życiowy")
        print("5. Wyświetl rekord życiowy")
        print("6. Edytuj rekord życiowy")
        print("7. Wyloguj się")

        choose = input("Wybierz akcję do wykonania: ")

        if choose == "7":
            print("Za chwile nastąpi wylogowanie ❌")
            zalogowany = False
            break
        elif choose == "1":
            password = input("Podaj stare hasło: ")
            if password == users[login]:
                while True:
                    new_password = input("Podaj nowe hasło: ")
                    if len(new_password) >= 8:
                        while True:
                            second_password = input("Powtórz nowe hasło: ")
                            if second_password == new_password:
                                users[login] = new_password
                                with open("data/users.txt", "w") as file:
                                    for user, password in users.items():
                                        file.write(f"{user}:{password}\n")
                                print("Hasło zostało zmienione ✅")
                                return
                            else:
                                print("Podane hasła się nie zgadzają ❌")
                    else:
                        print("Podane hasło jest za krótkie ❌")
            else:
                print("Podano niepoprawne stare hasło ❌")
        elif choose == "2":
            dodaj_trening(login)
        elif choose == "3":
            wyswietl_treningi(login)
        elif choose == "4":
            dodaj_rekord_zyciowy(login)
        elif choose == "5":
            wyswietl_rekord_zyciowy(login)
        elif choose == "6":
            edytuj_rekord_zyciowy(login)
        else:
            print("Nieznana opcja! Wybierz ponownie.")

logged_user = None

while password_tries > 0 and login_tries > 0:
    print("================================")
    print("  WITAJ W SYSTEMIE LOGOWANIA  ")
    print("================================")
    print("Wybierz jedną z poniższych opcji:")
    print("1. Zaloguj się")
    print("2. Zarejestruj się")
    print("3. Zamknij program")

    choose = input("Wybierz akcję do wykonania: ")
    if choose == "1":
        logged_user = logowanie()
    elif choose == "2":
        rejestracja()
    elif choose == "3":
        print("Zamykam program ❌")
        break
    else:
        print("Nieznana opcja! Wybierz ponownie.")
    if logged_user:
        panel_uzytkownika(logged_user)