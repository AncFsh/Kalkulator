import logging
logging.basicConfig(level=logging.INFO)

def Dodawanie(x, y):
    return x + y
def Odejmowanie(x, y):
    return x - y
def Mnożenie(x, y):
    return x * y
def Dzielenie(x, y):
    return x / y

'Korzystając z biblioteki logging, informujemy użytkownika, jakie działanie wykonamy i jakie będą jego argumenty (np. Dodaję 1 i 3).'
while True:
    liczba = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))

    if liczba in (1, 2, 3, 4):
        x = float(input(f'Podaj pierwszą liczbę: '))
        y = float(input(f'Podaj drugą liczbę: '))
        logging.info(f"Podane liczby to: {x} i {y}")

        if liczba == 1:
            print(Dodawanie(x, y))
        elif liczba == 2:
            print(Odejmowanie(x, y))
        elif liczba == 3:
            print(Mnożenie(x, y))
        elif liczba == 4:
            print(Dzielenie(x, y))
    else:
        print("Nieprawidłowa liczba, podaj liczbę odpowiadającą działaniu.")
'co do dodania możliwości dodawania i mnożenia większej ilości elementów muszę się Ciebie poradzić - myślałem' \
' o dodawaniu do listy kolejnych wpisanych elementów'
    break
