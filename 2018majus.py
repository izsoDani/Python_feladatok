jarasok = []

fajl = open("2018majus.txt", "r")
for sor in fajl:
    bekijarasok = {}
    adatok = sor.strip().split()
    bekijarasok['ora'] = adatok[0]
    bekijarasok['perc'] = adatok[1]
    bekijarasok['szemelyaz'] = adatok[2]
    bekijarasok['be_ki'] = adatok[3]
    jarasok.append(bekijarasok)
fajl.close()
print(jarasok)