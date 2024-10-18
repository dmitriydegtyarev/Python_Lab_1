while True:
    try:
        a = float(input("Введіть а -> "))
        b = float(input("Введіть b -> "))
    except ValueError:
        print("Будь ласка, введіть коректне числове значення")
        continue

    if a <= 0 or b <= 0:
        print("Введені значення повинні бути більше 0")
        continue

    if a > b:
        r = a * b + 1

    elif a == b:
        r = 25

    else:
        r = (a - 5) / b

    print("Результат обчислення виразу: ", r)
    break