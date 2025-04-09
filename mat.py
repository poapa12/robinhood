trzby = [
  [1200, 1350, 1100, 1600, 1800, 1750, 1900],
  [1000, 950, 1200, 1100, 1050, 1300, 1400],
  [1500, 1450, 1600, 1700, 1750, 1650, 1800],
  [900, 850, 800, 950, 1000, 1050, 1100],
  [1300, 1250, 1350, 1400, 1450, 1500, 1550]
]
 
def soucet():
  suma_radku = [sum(trzby[i]) for i in range(0,5)]
  celkova_suma = sum(suma_radku)
  maximum = max(suma_radku)
  print(suma_radku, "\n", celkova_suma, "\n", maximum)
soucet()
 
def prumerna_trzba_na_den():
    dny = len(trzby[0])
    obchodnici = len(trzby)
    prumery = []
    for den in range(dny):
        soucet_dne = sum(trzby[obchodnik][den] for obchodnik in range(obchodnici))
        prumery.append(soucet_dne / obchodnici)
    return prumery

print(prumerna_trzba_na_den())


def den_s_max_obratem(trzby):
    dny = len(trzby[0])
    obraty_za_dny = [sum(trzby[obchodnik][den] for obchodnik in range(len(trzby))) for den in range(dny)]
    max_den_index = obraty_za_dny.index(max(obraty_za_dny))
    return max_den_index, obraty_za_dny

def oznaceni_trzeb(trzby):
    nova_tabulka = []
    for obchodnik in trzby:
        prumer = sum(obchodnik) / len(obchodnik)
        nova_rada = ['P' if trzba >= prumer else 'N' for trzba in obchodnik]
        nova_tabulka.append(nova_rada)
    return nova_tabulka

max_den_index, obraty = den_s_max_obratem(trzby)
oznacena_tabulka = oznaceni_trzeb(trzby)

print("Index dne s nejvyšším obratem:", max_den_index)
print("Denní obraty:", obraty)
print("Tabulka s označením 'N' a 'P':")
for rada in oznacena_tabulka:
    print(rada)
