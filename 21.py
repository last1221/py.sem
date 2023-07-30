n = int(input("Введите кол-во монет: "))
heads = 0
tails = 0
for i in range(n):
    position = int(input(f"Положение монеты {i+1}: 0 или 1: "))
    if position == 0:
        heads += 1
    else:
        tails += 1
if heads > tails:
    print(f"Кол-во монет, чтобы перевернуть: {tails}")
else:
    print(f"Кол-во монет, чтобы перевернуть: {heads}")
