n = int(input())
min = None
for i in range(2, n + 1):
    if n % i == 0:
        min = i
        break
print("NONE" if min is None else min)
