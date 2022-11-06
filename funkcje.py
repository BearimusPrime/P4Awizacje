def licznik(liczba):
    for i in range(1,liczba+1):
        print(i)


def czytaj_plik():
    with open('xxx.txt') as f:
        tekst = f.readlines()
        f.close()


def pierwszy():
    tekst = '''</docid>
    <magazyn>'''
    return tekst


def drugi():
    tekst = '''</magazyn>
    <dostawca>Komsa</dostawca>
    <docidp4>'''
    return tekst


def trzeci():
    tekst = '''</docidp4>
  </header>
'''
    return tekst


def pozycja(kokos, plik, tresc=''):
    licznik=kokos+4
    for i in range (1,kokos+1):
        tresc += '''  <pozycja>
'''
        for j in range(1,int(plik[i+3].split()[-1])+1):
            tresc += '''    <cechy>
      <lpc>'''+str(j)+'''</lpc>
      <nrseryjny>'''+plik[licznik].rstrip()+'''</nrseryjny>
    </cechy>
'''
            licznik+=1
        cena = plik[3+i].split()[0]
        tresc += '''    <lp>'''+plik[3+i].split()[0]+'''</lp>
    <symkar>AC-'''+plik[3+i].split()[1]+'''</symkar>
    <ilosc>'''+plik[3+i].split()[-1]+'''</ilosc>
    <cena>'''+plik[-kokos-1+int(cena)].rstrip()[:-2]+'''</cena>
  </pozycja>
  '''
    return tresc


