n = 20
qs = [10, 2, 50]

robota = []
wyniki = []

# oblicz pelen zakres
p = 0
k = 3 ** n

# dodaj poczatek i koniec elementu
wyniki.append(p)
wyniki.append(k)

robota.append((p, k))

def log(m, x):
    print(m, ": ", x)

while len(robota) > 0:
    # wez element do obrobienia
    e = robota.pop()
    p = e[0]
    k = e[1]
#    log('e', e)
    
    # oblicz 1/3
    jedna3 = (k - p) // 3
#    log('jedna3', jedna3)
    
    if jedna3 > 0:
        p2 = p + jedna3
        k2 = p + jedna3 * 2
        # dodaj poczatek i koniec elementu
        wyniki.append(p2)
        wyniki.append(k2)
    
        robota.append((p, p2))
        robota.append((k2, k))
    
wyniki.sort()
#print(wyniki)

dl = len(wyniki)
print('dl:', dl)
for q in qs:
    if q > dl:
        print('NIE')
    else:
       print(q, ': ', wyniki[q - 1])
