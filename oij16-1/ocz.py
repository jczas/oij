dane = ["AK", "2222222222", "K92"]
wyniki = []
maks = 0
ile = 0

for osoba in dane:
    suma = 0
    asy = False
    for karta in osoba:
        if karta ==  "2": suma += 2
        if karta ==  "3": suma += 3
        if karta ==  "4": suma += 4
        if karta ==  "5": suma += 5
        if karta ==  "6": suma += 6
        if karta ==  "7": suma += 7
        if karta ==  "8": suma += 8
        if karta ==  "9": suma += 9
        if karta ==  "T": suma += 10
        if karta ==  "J": suma += 10
        if karta ==  "Q": suma += 10
        if karta ==  "K": suma += 10
        if karta ==  "A": 
            suma += 1
            asy = True
        if suma <= 11 and asy: suma += 10
        if suma <= 21 and suma >= maks:
            if suma > maks: 
                maks = suma
                ile = 1
            else:
                ile += 1
        
    wyniki.append(suma)
    
print(ile)
wygrani = []
for i in range(len(wyniki)):
    if wyniki[i] == maks:
        wygrani.append(str(i+1))

print(" ".join(wygrani))

