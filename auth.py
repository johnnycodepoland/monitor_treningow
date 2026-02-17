from utils import load_users
password_tries = 3
login_tries = 3

def logowanie():
    password_tries = 3
    login_tries = 3
    users = load_users()

    while login_tries > 0 and password_tries > 0:
        login = input("Podaj swój login: ")
        if login in users:
            while password_tries > 0:
                password = input("Podaj swoje hasło: ")
                if password == users[login]:
                    print("Zalogowano ✅")
                    return login
                else:
                    print("Błędne hasło ❌")
                    password_tries -= 1
                    try:
                        with open("data/logi.txt", "a") as file:
                            file.write(f"Nieudane logowanie. Login: {login} Hasło: {password}\n")
                    except OSError: # to nam zabezpiecza plik przed np. tym że go nie ma
                        print("Błąd podczas zapisywania do pliku logów ❌")
        else:
            print("Podano niepoprawny login")
            login_tries -= 1

        if password_tries == 0:
            print("Zablokowano dostęp do konta!")
            exit()
        if login_tries == 0:
            print("Zablokowano dostęp do konta!")
            exit()

def rejestracja():
    users = load_users()

    while True:
        login = input("Podaj login który chcesz przypisać do swojego konta: ")
        if len(login) >= 8:
            if login not in users:
                while True:
                    password = input("Podaj nowe hasło: ")
                    if len(password) >= 8:
                        while True:
                            password_second = input("Powtórz nowe hasło: ")
                            if password_second == password:
                                with open ("data/users.txt", "a") as file:
                                    file.write(f"{login}:{password}\n")
                                print("Użytkownik został dodany ✅")
                                return
                            else:
                                print("Podane hasła nie są takie same ❌")
                    else:
                        print("Podane hasło jest za krótkie ❌")
            else:
                print("Podany login jest zajęty ❌")
        else:
            print("Podany login jest za krótki ❌")