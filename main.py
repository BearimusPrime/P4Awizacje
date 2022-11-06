from funkcje import *
import base64

if __name__ == '__main__':
    tekst = '''<ns0:mt_order xmlns:ns0="http://p4.org/xi/softlab">
  <header>
    <docid>'''
    with open('xxx.txt', 'r',encoding='UTF8') as f:
        plik = f.readlines()
    tekst += plik[0].rstrip()
    tekst += pierwszy()
    tekst += plik[1].rstrip()
    tekst += drugi()
    tekst += plik[2].rstrip()
    tekst += trzeci()
    tekst += pozycja(int(plik[3]),plik)
    tekst += '''</ns0:mt_order>'''
    encoded = base64.b64encode(bytes(tekst, "utf-8"))
    print(tekst)
    print(encoded)
