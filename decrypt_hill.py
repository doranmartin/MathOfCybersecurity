e_co = 20
f_co = 1
f_co_a = 10
f_co_b = -3
c = 5

e_co += f_co * f_co_b
f_co *= f_co_a
    

for e in range(100):
    if (e_co * e + f_co) % 26 == c:
        print(e)
        break
