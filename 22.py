s = int(input('сумма двух чисел \n'))
p = int(input('произведение чисел \n'))
for x in range(s):
    for y in range(p):
        if s == x + y and p == x * y:
            print(f"{x} {y}")


