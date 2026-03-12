a = float(input("Первое число: "))
op = input("Операция (+ или -): ")
b = float(input("Второе число: "))

if op == "+":
    print("Результат:", a + b)
elif op == "-":
    print("Результат:", a - b)
else:
    print("Неизвестная операция")