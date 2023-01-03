import logging
logging.basicConfig(level=logging.INFO)

def add(x, y):
    return x + y
def substract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

while True:
    liczba = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))

    if liczba in (1, 2, 3, 4):
        x = float(input(f'Podaj pierwszą liczbę: '))
        y = float(input(f'Podaj drugą liczbę: '))
        logging.info(f"Podane liczby to: {x} i {y}")

        if liczba == 1:
            print(add(x, y))
        elif liczba == 2:
            print(substract(x, y))
        elif liczba == 3:
            print(multiply(x, y))
        elif liczba == 4:
            print(divide(x, y))
    else:
        print("Nieprawidłowa liczba, podaj liczbę odpowiadającą działaniu.")
    break

'co do dodania możliwości dodawania i mnożenia większej ilości elementów muszę się Ciebie poradzić - myślałem'
' o dodawaniu do listy kolejnych wpisanych elementów'