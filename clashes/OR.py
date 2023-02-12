n1, n2 = input().split()
result = ""
for i in range(len(n1)):
    result += str(int(n1[i]) | int(n2[i]))
print(result)
