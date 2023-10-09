smsek = []

fajl = open("2008majus.txt", "r")
for sor in fajl:
    adatok = sor.strip()
    smsek.append(adatok)
smsek.remove(smsek[0])
print(smsek)

ujsms = []
for egyuzenet in smsek:
    uzenet = {}
