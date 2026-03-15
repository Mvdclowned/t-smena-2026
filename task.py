n, k = map(int, input().split())
x, y = 0, 1
res = []

while x <= k:
    if x >= n:
        res.append(str(x))
    x, y = y, x + y

if res:
    print(" ".join(res))
else:
    print("В заданном диапазоне нет чисел Фибоначчи")
