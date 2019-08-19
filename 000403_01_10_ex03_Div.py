a = int(input())
b = int(input())
if b != 0:
    print(a/b)
else:
    print("Деление невозможно, b = ", b)
# дополняем условие: просим еще раз ввести "b" (если произошел случай "else", просим еще раз ввести "b")
if b != 0:
    print(a/b)
else:
    print("Деление невозможно, b = ", b)
    b = int(input("Введите число, отличное от нуля: "))
    if b == 0:
        print("Неверно")
    else:
        print(a/b)




