n = int(input())
inputs = [int(x) for x in input().split()]
inputs = sorted(inputs)
done = False
i = 0
while i < len(inputs) - 1:
    if inputs[i] != inputs[i+1]:
        print(inputs[i])
        done = True
        break
    else:
        i += 2
if not done:
    print(inputs[-1])
