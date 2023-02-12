s = input()
i = 0
result = ""
while i < len(s) - 1:
    result += s[i + 1] + s[i]
    i += 2
if len(s) % 2 == 1:
    result += s[len(s) - 1]
print(result)
