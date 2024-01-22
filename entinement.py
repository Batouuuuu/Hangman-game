a = ["J","o","h","n"]
b = ["*","o","*","*"]
c = []

for lettre, lettre_b in zip(a,b):
    if lettre == lettre_b:
        c.append("V")
    else:
        c.append("*")
print(c)

