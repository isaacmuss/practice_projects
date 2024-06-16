n = 1357913579135798

n_str = str(n)

for i in range(len(n_str)):
    digit = int(n_str[i])
    if digit % 2 == 0:
        verif = False
        break
    else:
        verif = True

print(verif)

