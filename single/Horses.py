import sys
n = int(input())
strengths = []
for i in range(n):
    strengths.append(int(input()))
strengths = sorted(strengths)
min = sys.maxsize
for i in range(len(strengths) - 1):
    diff = abs(strengths[i]-strengths[i+1])
    if diff < min:
        min = diff
print(min)
