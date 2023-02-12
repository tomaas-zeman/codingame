n = int(input())
nb = str(input())
good = False
for i in range(2, 36):
    try:
        if int(nb, i) == n:
            print(i)
            good = True
            break
    except:
        pass
if not good:
    print("error")
