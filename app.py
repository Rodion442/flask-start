from flask import Flask

# Inicjalizacja aplikacji Flask
app = Flask(__name__)


# Zadanie 2 & 3: Strona główna
@app.route("/")
def index():
    # Zmień "Twoje Imię" na swoje rzeczywiste imię
    return "Cześć, tu Twoje Imię! Witamy w serwisie rezerwacyjnym."


# Zadanie 3: Dodatkowe trasy tekstowe
@app.route("/o-nas")
def o_nas():
    return "Jesteśmy nowatorskim systemem do rezerwacji kortów tenisowych."


@app.route("/kontakt")
def kontakt():
    return "Napisz do nas: kontakt@rezerwacje-sportowe.pl"


@app.route("/regulamin")
def regulamin():
    return "1. Rezerwacji należy dokonywać z wyprzedzeniem. 2. Odwołanie rezerwacji do 24h przed."


# Zadanie 4: Trasa z kodem statusu HTTP 403 Forbidden
@app.route("/admin")
def admin():
    return "Brak dostępu", 403


# Zadanie 5: Trasa zwracająca słownik (Flask automatycznie konwertuje na JSON)
@app.route("/api/info")
def api_info():
    return {
        "nazwa": "System Rezerwacji Kortów",
        "autor": "Twoje Imię i Nazwisko",
        "wersja": "0.1",
    }


# Uruchomienie serwera deweloperskiego z aktywnym debuggerem
if __name__ == "__main__":
    app.run(debug=True)