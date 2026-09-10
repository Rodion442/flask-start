from flask import Flask, request, url_for, redirect, abort

app = Flask(__name__)

# --- Zadanie 1: Powitanie ---
@app.route("/czesc/<imie>")
def czesc(imie):
    return f"Cześć, {imie}!"

@app.route("/czesc/<imie>/<int:wiek>")
def czesc_wiek(imie, wiek):
    return f"Cześć, {imie}, masz {wiek} lat."

# --- Zadanie 2: Kalkulator ---
@app.route("/dodaj/<int:a>/<int:b>")
def dodaj(a, b):
    return f"{a} + {b} = {a + b}"

@app.route("/odejmij/<int:a>/<int:b>")
def odejmij(a, b):
    return f"{a} - {b} = {a - b}"

@app.route("/pomnoz/<int:a>/<int:b>")
def pomnoz(a, b):
    return f"{a} * {b} = {a * b}"

@app.route("/podziel/<int:a>/<int:b>")
def podziel(a, b):
    if b == 0:
        return "Nie dzielimy przez zero", 400
    return f"{a} / {b} = {a / b}"

@app.route("/potega/<int:a>/<int:b>")
def potega(a, b):
    return f"{a} ^ {b} = {a ** b}"

# --- Zadanie 3: Tabliczka mnożenia ---
@app.route("/tabliczka/<int:n>")
def tabliczka(n):
    if n < 1 or n > 20:
        return "Liczba n musi być w przedziale 1-20", 400
    
    wynik = []
    for i in range(1, 11):
        wynik.append(f"{n} x {i} = {n * i}")
    return "<br>".join(wynik)

# --- Zadanie 4: Query string ---
@app.route("/produkty")
def produkty():
    kat = request.args.get("kat", "wszystkie")
    sort = request.args.get("sort", "domyślne")
    return f"Kategoria: {kat}, sortowanie: {sort}"

# --- Zadanie 5: Mini-baza w słowniku (Korty tenisowe / Rezerwacje) ---
KORTY = {
    1: "Kort Centralny (Nawierzchnia ceglana)",
    2: "Kort 2 (Trawa)",
    3: "Kort 3 (Hard court)",
    4: "Kort Kryty A (Hala)",
    5: "Kort Kryty B (Hala)"
}

@app.route("/element/<int:id>")
def element(id):
    if id not in KORTY:
        abort(404)
    return f"Kort: {KORTY[id]}"

@app.route("/elementy")
def elementy():
    lista = [f"{k:id}: {nazwa}" for id, nazwa in KORTY.items()]
    return "<br>".join(lista)

# --- Zadanie 6: Przekierowanie ---
@app.route("/")
def index():
    return "Strona główna serwisu"

@app.route("/start")
def start():
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)