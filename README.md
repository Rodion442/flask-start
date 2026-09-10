# flask-start

Projekt aplikacji webowej Flask — dynamiczne ścieżki.

## Lista tras

- `/czesc/<imie>` — Powitanie (np. `/czesc/Jan`)
- `/czesc/<imie>/<int:wiek>` — Powitanie z wiekiem (np. `/czesc/Jan/20`)
- `/dodaj/<int:a>/<int:b>` — Dodawanie (np. `/dodaj/5/3`)
- `/odejmij/<int:a>/<int:b>` — Odejmowanie (np. `/odejmij/10/4`)
- `/pomnoz/<int:a>/<int:b>` — Mnożenie (np. `/pomnoz/4/5`)
- `/podziel/<int:a>/<int:b>` — Dzielenie z obsługą 400 (np. `/podziel/10/2`)
- `/potega/<int:a>/<int:b>` — Potęgowanie (np. `/potega/2/3`)
- `/tabliczka/<int:n>` — Tabliczka mnożenia 1-20 (np. `/tabliczka/5`)
- `/produkty?kat=...&sort=...` — Query string (np. `/produkty?kat=laptopy&sort=cena`)
- `/element/<int:id>` — Pobieranie elementu po ID (np. `/element/1`)
- `/elementy` — Lista wszystkich elementów
- `/start` — Przekierowanie 302 na `/`

## Odpowiedź na pytanie z Zadania 1
Gdy w wieku podamy tekst (np. `/czesc/Jan/abc`), Flask zwróci błąd **404 Not Found**, ponieważ konwerter `<int:wiek>` oczekuje wyłącznie liczby całkowitej.