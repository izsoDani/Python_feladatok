merkozesek = []
fajl = open("2007oktober.txt", "r")
for sor in fajl:
    adatok = sor.strip().split()
    merkozesek.append(adatok)
print(merkozesek)