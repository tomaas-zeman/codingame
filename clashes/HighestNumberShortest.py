n=int(input())
i=input().split()
print("".join(reversed(sorted(i)))if i.count("0")!=n else "0")