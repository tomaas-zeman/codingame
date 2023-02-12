n_1, n_2 = input().split()
result = ""
for i in range(len(n_1)):
    result += str(int(n_1[i] != n_2[i]))
print(result)


