number = int(input())
result = []
divisor = 2
while number > 1:
    if number % divisor == 0:
        result.append(str(divisor))
        number = number / divisor
    else:
        divisor += 1
print(" ".join(result))
