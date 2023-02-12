r=""
for c in input():
 if c.isalpha()and (r and r[-1].isalpha()):r+=" "
 r+=c
print(r)
