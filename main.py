def add(numbers):
    result = 0
    for number in numbers:
        result += number
    return result


def subtract(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result -= number
    return result


def multiply(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


def divide(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        if number == 0:
            return "Dzielenie przez zero. Kalkulacja nieudana."
        result /= number
    return result


def calculator():
    operation = input("Wybierz operację (+, -, *, /): ")
    numbers = input("Podaj liczby oddzielone spacjami: ").split()
    numbers = [float(number) for number in numbers]

    if operation == "+":
        result = add(numbers)
    elif operation == "-":
        result = subtract(numbers)
    elif operation == "*":
        result = multiply(numbers)
    elif operation == "/":
        result = divide(numbers)
    else:
        return "Wybierz dostępną operację."

    return result

print(calculator())
