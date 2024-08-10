N1 = int(input("Ведите первое число: "))
N2 = int(input("Ведите второе число: "))
N3 = int(input("Ведите третье число: "))
pair = 0
if N1 == N2:
    pair += 1
if N1 == N3:
    pair += 1
if N2 == N3:
    pair += 1

if pair == 3:
    print("Одинаковых чисел: 3")
elif pair == 1:
    print("Одинаковых чисел: 2")
else:
    print("Одинаковых чисел: 0")
