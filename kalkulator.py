n = float(input("podaj liczbę: "))
n2 = float(input("podaj drugą liczbę: "))
znaks = input("podaj działanie (+/-/*/:): ")
print("")

def prov(liczba):
    d = liczba*10
    cala = d//10
    b = liczba
    niecala = b-cala
    cala = int(cala)
    taknie = 10
    if niecala == 0:
        taknie = 0
    else:
        taknie = 1
    return cala, niecala, taknie

def z10na2(p):
    z = p
    ile = 0
    w = ''
    if p < 0:
        p = p - 2*p
    while p != 0:
        r = p%2
        p = p//2
        if r == 1:
            w = '1' + w
        else:
            w = '0' + w
        ile += 1
    if ile < 15:
        while ile != 15:
            w = '0' + w
            ile += 1
    elif ile > 15:
        print("liczba jest większa niż 16bit")
    if ile == 15:
        if z < 0:
            w = '1' + w
            return w
        else:
            w = '0' + w
            return w
    return w

def z10na2dziel(k):
    w = ''
    if k < 0:
        k = k - 2*k
    while k != 0:
        reszta = k%2
        k = k//2
        if reszta == 1:
            w = '1' + w
        else:
            w = '0' + w
    return w

def z10na2niecala(d):
    w = ''
    ile = 0
    while d != 1 or ile < 4:
        if ile < 4:
            d = d*2
            if d > 1:
                w += '1'
                ile += 1
                d -= 1
            elif d < 1:
                w += '0'
                ile += 1
            else:
                w += '1'
                break
        else:
            break
    return w

def z2na10(L):
    ile = 0
    a = L
    w = 0
    l = []
    for i in a:
        l.append(i)
    l.reverse()
    for d in l:
        if d == '1':
            w += 2**ile
            ile += 1
        else:
            ile += 1
    return w
        
def u2(o):
    ile = 0
    l = []
    q = 1
    w = ''
    for i in o:
        if i == "1":
            l.append(0)
            ile += 1
        elif i == "0":
            l.append(1)
            ile += 1
    while q != 0:
        if l[ile - q] == 0:
            l[ile - q] = 1
            q = 0
        else:
            l[ile - q] = 0
            q += 1
    for g in l:
        g = str(g)
        w = w + g
    return w

def plus(q, dod):
    if q > 1:
        if (q+dod)%2 == 0:
            w = 0
        else:
            w = 1
        wd = (q+dod)//2
    elif q == 1:
        if (q+dod)%2 == 0:
            w = 0
            wd = 1
        else:
            w = 1
            wd = 0
    else:
        if dod == 1:
            w = 1
            wd = 0
        else:
            w = 0
            wd = 0
    return w, wd

def dodanie(q1, q2):
    ile = len(q1)
    l1 = []
    l2 = []
    for i1 in q1:
        l1.append(i1)
    for i2 in q2:
        l2.append(i2)
    l1.reverse()
    l2.reverse()
    if len(l1) > len(l2):
        while len(l1) != len(l2):
            l2.append('0')
    elif len(l1) < len(l2):
        while len(l1) != len(l2):
            l1.append('0')
    il = 0
    w = ''
    dod = 0
    while il < ile:
        if il < ile:
            if l1[il] == '1' and l2[il] == '0' and dod == 0:
                w = '1' + w
                il += 1
                dod = 0
            elif l1[il] == '0' and l2[il] == '0' and dod == 0:
                w = '0' + w
                il += 1
                dod = 0
            elif l1[il] == '1' and l2[il] == '1' and dod == 0:
                w = '0' + w
                il += 1
                dod = 1
            elif l1[il] == '1' and l2[il] == '0' and dod == 1:
                w = '0' + w
                il += 1
                dod = 1
            elif l1[il] == '0' and l2[il] == '0' and dod == 1:
                w = '1' + w
                il += 1
                dod = 0
            elif l1[il] == '1' and l2[il] == '1' and dod == 1:
                w = '1' + w
                il += 1
                dod = 1
            elif l1[il] == '0' and l2[il] == '1' and dod == 0:
                w = '1' + w
                il += 1
                dod = 0
            elif l1[il] == '0' and l2[il] == '1' and dod == 1:
                w = '0' + w
                il += 1
                dod = 1
        elif il >= ile:
            break
    return w

def minus(q1, q2):
    ile = len(q1)
    l1 = []
    l2 = []
    for i1 in q1:
        l1.append(i1)
    for i2 in q2:
        l2.append(i2)
    l1.reverse()
    l2.reverse()
    if len(l1) > len(l2):
        l2.append('1')
    if len(l1) < len(l2):
        l1.append('0')
    il = 0
    w = ''
    dod = 0
    while il < ile:
        if il < ile:
            if l1[il] == '1' and l2[il] == '0' and dod == 0:
                w = '1' + w
                il += 1
                dod = 0
            elif l1[il] == '0' and l2[il] == '0' and dod == 0:
                w = '0' + w
                il += 1
                dod = 0
            elif l1[il] == '1' and l2[il] == '1' and dod == 0:
                w = '0' + w
                il += 1
                dod = 1
            elif l1[il] == '1' and l2[il] == '0' and dod == 1:
                w = '0' + w
                il += 1
                dod = 1
            elif l1[il] == '0' and l2[il] == '0' and dod == 1:
                w = '1' + w
                il += 1
                dod = 0
            elif l1[il] == '1' and l2[il] == '1' and dod == 1:
                w = '1' + w
                il += 1
                dod = 1
            elif l1[il] == '0' and l2[il] == '1' and dod == 0:
                w = '1' + w
                il += 1
                dod = 0
            elif l1[il] == '0' and l2[il] == '1' and dod == 1:
                w = '0' + w
                il += 1
                dod = 1
        elif il >= ile:
            break
    j = 19
    lista = []
    wyn = ''
    for k in w:
        lista.append(k)
    while lista and lista[0] == '0':
        if lista[0] == '0':
            del lista[0]
    for d in lista:
        wyn += d
    return wyn

def mnoz(x1, x2):
    ile1 = 0
    ile2 = 0
    ile3 = 0
    ile4 = 0
    ile5 = 0
    ile6 = 0
    ile7 = 0
    ile8 = 0
    ile9 = 0
    ile10 = 0
    ile11 = 0
    ile12 = 0
    ile13 = 0
    ile14 = 0
    ile15 = 0
    ile16 = 0
    w = '0'
    l1 = []
    l2 = []
    for i1 in x1:
        l1.append(i1)
    for i2 in x2:
        l2.append(i2)
    l = l2.copy()
    l11 = l1.copy()
    l.reverse()
    x = ''
    for i in l11:
        x = x + i
    print("-----------------")
    ile = 0
    ilezer = 16
    while len(l11) > 0:
        ilezer2 = ilezer
        x = ''
        lk = []
        if l[ile] == '0':
            for i in l11:
                x = x + i
            zero = ''
            while ilezer2 != 0:
                zero += '0'
                ilezer2 -= 1
            print(zero)
            ile += 1
            del l11[0]
        else:
            for i in l11:
                x = x + i
            print(x)
            ile += 1
            pom = 16 - len(l11)
            if pom != 0:
                while pom != 0:
                    lk.append('0')
                    pom -= 1
            xx = l11.copy()
            xx.reverse()
            for k in xx:
                lk.append(k)
            if len(lk) >= 1:
                if lk[0] == '1':
                    ile1 += 1
            if len(lk) >= 2:
                if lk[1] == '1':
                    ile2 += 1
            if len(lk) >= 3:
                if lk[2] == '1':
                    ile3 += 1
            if len(lk) >= 4:
                if lk[3] == '1':
                    ile4 += 1
            if len(lk) >= 5:
                if lk[4] == '1':
                    ile5 += 1
            if len(lk) >= 6:
                if lk[5] == '1':
                    ile6 += 1
            if len(lk) >= 7:
                if lk[6] == '1':
                    ile7 += 1
            if len(lk) >= 8:
                if lk[7] == '1':
                    ile8 += 1
            if len(lk) >= 9:
                if lk[8] == '1':
                    ile9 += 1
            if len(lk) >= 10:
                if lk[9] == '1':
                    ile10 += 1
            if len(lk) >= 11:
                if lk[10] == '1':
                    ile11 += 1
            if len(lk) >= 12:
                if lk[11] == '1':
                    ile12 += 1
            if len(lk) >= 13:
                if lk[12] == '1':
                    ile13 += 1
            if len(lk) >= 14:
                if lk[13] == '1':
                    ile14 += 1
            if len(lk) >= 15:
                if lk[14] == '1':
                    ile15 += 1
            if len(lk) == 16:
                if lk[15] == '1':
                    ile16 += 1
            del l11[0]
        ilezer -= 1
    print("----------------------")
    wd = 0
    lw = []
    pam1, wd = plus(ile1, 0)
    lw.append(pam1)
    pam2, wd = plus(ile2, wd)
    lw.append(pam2)
    pam3, wd = plus(ile3, wd)
    lw.append(pam3)
    pam4, wd = plus(ile4, wd)
    lw.append(pam4)
    pam5, wd = plus(ile5, wd)
    lw.append(pam5)
    pam6, wd = plus(ile6, wd)
    lw.append(pam6)
    pam7, wd = plus(ile7, wd)
    lw.append(pam7)
    pam8, wd = plus(ile8, wd)
    lw.append(pam8)
    pam9, wd = plus(ile9, wd)
    lw.append(pam9)
    pam10, wd = plus(ile10, wd)
    lw.append(pam10)
    pam11, wd = plus(ile11, wd)
    lw.append(pam11)
    pam12, wd = plus(ile12, wd)
    lw.append(pam12)
    pam13, wd = plus(ile13, wd)
    lw.append(pam13)
    pam14, wd = plus(ile14, wd)
    lw.append(pam14)
    pam15, wd = plus(ile15, wd)
    lw.append(pam15)
    pam16, wd = plus(ile16, wd)
    lw.append(pam16)
    lw.reverse()
    wynik = ''
    for dy in lw:
        wynik += str(dy)
    return wynik

def dzielenie(y1, y2, taknie):
    l1 = []
    l2 = []
    w = ''
    for i1 in y1:
        l1.append(i1)
    for i2 in y2:
        l2.append(i2)
    ile = len(l1)
    ilep = len(l2)
    X = []
    Y = u2(y2)
    ileelem = ilep
    for elem in l1:
        if ileelem != 0:
            X.append(elem)
            ileelem -= 1
    while ile != 0:
        liczba = ''
        for g in X:
            if g == '0':
                liczba += '0'
            elif g == '1':
                liczba += '1'
        if z2na10(liczba) >= z2na10(y2):
            ost = minus(liczba, Y)
            w += '1'
            X = []
            for b in ost:
                X.append(b)
            ile -= 1
        else:
            w += '0'
            ile -= 1
        if len(l1) > ilep:
            dodatek = l1[ilep]
            X.append(dodatek)
            ilep += 1
        else:
            break
    liczba = ''
    for g in X:
        if g == '0':
            liczba += '0'
        elif g == '1':
            liczba += '1'
    ku = z2na10(liczba)
    liczba = str(liczba)
    if taknie == 0:
        if liczba == '' or ku == 0:
            ww = w
        else:
            ww = w + '.'
            ww = ww + liczba
    else:
        ww = w
    return ww, liczba

def dzielost(ost, b):
    ile = 0
    d = u2(b)
    w = ''
    while ile < 4:
        ost += '0'
        if z2na10(ost) < z2na10(b):
            w += '0'
            ile += 1
        elif z2na10(ost) > z2na10(b):
            w += '1'
            ile += 1
            ost = minus(ost, d)
        else:
            w += '1'
            break
    return w
        
def wyprintowaniewyniku(nnn1, nnn2, znak):
    cala1, niecala1, taknie1 = prov(nnn1)
    cala2, niecala2, taknie2 = prov(nnn2)

    if znak != ':':
        x = z10na2(cala1)
        y = z10na2(cala2)
    else:
        x = z10na2dziel(cala1)
        y = z10na2dziel(cala2)

    listadl1 = []
    listadl2 = []

    if taknie1 == 1:
        xniecala = z10na2niecala(niecala1)
        for element1 in xniecala:
            listadl1.append(element1)
        ileniecalax = len(xniecala)
    if taknie2 == 1:
        yniecala = z10na2niecala(niecala2)
        for element2 in yniecala:
            listadl2.append(element2)
        ileniecalay = len(yniecala)

    if taknie1 == taknie2:
        taknie = taknie1
        if taknie == 1:
            if ileniecalay > ileniecalax:
                iile = ileniecalay - ileniecalax
                if iile != 0:
                    while iile != 0:
                        listadl1.append('0')
                        ileniecalax += 1
                        iile -= 1
            elif ileniecalax > ileniecalay:
                iile = ileniecalax - ileniecalay
                if iile != 0:
                    while iile != 0:
                        del listadl1[-1]
                        ileniecalax -= 1
                        iile -= 1
            xniecala = ''
            for s1 in listadl1:
                xniecala += s1
            yniecala = ''
            for s2 in listadl2:
                yniecala += s2
            j1 = x + '.'
            j1 = j1 + xniecala
            j2 = y + '.'
            j2 = j2 + yniecala
            x = x + xniecala
            y = y + yniecala
            ileniecalafull = ileniecalax + ileniecalay

    if len(x) > 16:
        ll = []
        for k in x:
            ll.append(k)
        while len(ll) > 16:
            if ll[0] == '0':
                del ll[0]
            else:
                print("błąd")
                break
        x = ''
        for punkt in ll:
            x += punkt
    
    if len(y) > 16:
        ll2 = []
        for k2 in y:
            ll2.append(k2)
        while len(ll2) > 16:
            if ll2[0] == '0':
                del ll2[0]
            else:
                print("błąd")
                break
        y = ''
        for punkt2 in ll2:
            y += punkt2

    if nnn1 < 0:
        x1 = u2(x)
    else:
        x1 = x
    if nnn2 < 0:
        y1 = u2(y)
    else:
        y1 = y
    if taknie == 1:
        print(nnn1, "(10) =", j1, "(u2)")
        print(nnn2, "(10) =", j2, "(u2)")
    else:
        print(nnn1, "(10) =", x1, "(u2)")
        print(nnn2, "(10) =", y1, "(u2)")

    print("")
    print(x1)
    if znak != ":":
        print(znak)
    else:
        print("/")
    print(y1)

    if znak == "*":
        wyniks = mnoz(x1, y1)
        print(wyniks)
        listawynik = []
        for pupupu in wyniks:
            listawynik.append(pupupu)
        if taknie == 1:
            listawynik2 = []
            while ileniecalafull != 0:
                am = listawynik[-1]
                listawynik2.append(am)
                del listawynik[-1]
                ileniecalafull -= 1
            listawynik2.reverse()
            if len(listawynik2) > 4:
                while len(listawynik2) > 4:
                    del listawynik2[-1]
            wynik = ''
            for elems in listawynik:
                wynik += elems
            wynik += '.'
            for elements in listawynik2:
                wynik += elements
        else:
            wynik = wyniks

    elif znak == "+":
        wynik = dodanie(x1, y1)

    elif znak == "-":
        if nnn1 >= nnn2:
            y1 = u2(y1)
            wynik = minus(x1, y1)
        else:
            b = x1
            x1 = y1
            y1 = b
            y1 = u2(y1)
            wynik = minus(x1, y1)
            wynik = u2(wynik)

    else:
        wynik, ostatek = dzielenie(x1, y1, taknie1)
        if taknie1 == 1:
            if z2na10(ostatek) != 0:
                wyn = dzielost(ostatek, y1)
                wynik += '.'
                wynik += wyn

    print("----------------")
    if nnn2 >= nnn1:
        print("wynik =", wynik, "(u2)")
    else:
        print("wynik =", wynik, "(2)")
    print("")

wyprintowaniewyniku(n, n2, znaks)

    
print("wynik jest zaokrąglony do 4 znaków po przecinku")
print("jeśli przecinku nie ma, to wynik jest *coś*.0000")

# INSTRUKCJA
# Najpierw trzeba wpisać jedną liczbę 
# Następnie wpisać drugą liczbę
# Trzecim krokiem działanie, które Pan chce wypełnić
# Np. dla 1 + 2 trzeba najpierw wpisać 1, potem wpisać 2, a następnie +
# Dla 10*3 trzeba najpierw wpisać 10, dalej 3, trzecim krokiem *
# Dla liczb nie całych trzeba wpisywać ich przez kropkę np. 24.125
# Jeśli wpisywać przez przecinek, program to nie odczyta