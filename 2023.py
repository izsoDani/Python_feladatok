

kep = []
def kepp():
    kepsor = []
    keppont = []
    with open('kep.txt', 'r',) as fajl:
        for sor in fajl:
            adatok = sor.strip().split(' ')

            for ertek in adatok:
                keppont.append(int(ertek))
                if len(keppont) == 3:
                    kepsor.append(keppont)
                    keppont = []
            kep.append(kepsor)
            kepsor = []
    print("Hello")

def szinek():
    sor = int(input("Sor:"))
    oszlop = int(input("Oszlop:"))

    kepp()
    print(f"A képpont színe RGB {kep[sor - 1][oszlop - 1]}")


def vilagos():
    db = 0
    kepp()
    for sor in kep:
        for elem in sor:
            rgb = sum(elem)
            if rgb > 600:
                db += 1
    print(db)

def sotet():

    keves = 1000
    for sor in kep:
        for elem in sor:
            osszeg = sum(elem)
            if osszeg < keves:
                keves = osszeg

#            keves.append(osszeg)
#    legkevesebb = min(keves)
#    print(legkevesebb)
    print(keves)
    for sor in kep:
        for elem in sor:
            if sum(elem) == keves:
                print(elem)


def hatar(sorszam, elteres):
    kepp()
    van_elteres = False
    korabbi_ertek = -1
    for elem in kep[sorszam]:
        osszeg = sum(elem)
        if korabbi_ertek == -1:
            korabbi_ertek = osszeg
            continue
        if abs(osszeg - korabbi_ertek) >= elteres:
            van_elteres = True
            break
        else:
            korabbi_ertek = osszeg
    return van_elteres

legfelso_sor = -1
legalso_sor = -1
elteres = 10


for sorszam in range(len(kep)):
    if van_elteres:
        if legfelso_sor == -1:
            legfelso_sor = sorszam
        legalso_sor = sorszam

print(legfelso_sor)
print(legalso_sor)
