import json
from auth import signin, signup, password_tries, login_tries
from personal_bests import add_personal_best, show_personal_best, edit_personal_best, delete_personal_best
from trainings import add_training, show_trainings
from utils import load_users

def user_panel(login):
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
        print("7. Usuń rekord życiowy")
        print("8. Wyloguj się")

        choose = input("Wybierz akcję do wykonania: ")

        if choose == "8":
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
                                try:
                                    with open ("data/users.json", "w") as file:
                                        json.dump(users, file)
                                except FileNotFoundError:
                                    return
                                print("Hasło zostało zmienione ✅")
                                return
                            else:
                                print("Podane hasła się nie zgadzają ❌")
                    else:
                        print("Podane hasło jest za krótkie ❌")
            else:
                print("Podano niepoprawne stare hasło ❌")
        elif choose == "2":
            add_training(login)
        elif choose == "3":
            show_trainings(login)
        elif choose == "4":
            add_personal_best(login)
        elif choose == "5":
            show_personal_best(login)
        elif choose == "6":
            edit_personal_best(login)
        elif choose == "7":
            delete_personal_best(login)
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
        logged_user = signin()
    elif choose == "2":
        signup()
    elif choose == "3":
        print("Zamykam program ❌")
        break
    else:
        print("Nieznana opcja! Wybierz ponownie.")
    if logged_user:
        user_panel(logged_user)