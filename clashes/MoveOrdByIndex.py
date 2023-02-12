l = input()
print("".join(chr(ord(l[i]) + i) for i in range(len(l))))
