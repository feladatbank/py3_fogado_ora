"""
                       Fogadóóra          (18 pont)
{{{{ Az osztály használata nem KÖTELEZŐ DE több pontot kaphat érte!!! }}}}
ÜGYELJEN arra hogy az fogado.txt fálj beolvasásánál van fejléc!!!
fejléc:
a tanár vezetékneve; utóneve; a lefoglalt időpont; a foglalás rögzítésének dátuma és időpontja

1. A feladat megoldásához hozzon létre programot fogado_ora azonosítóval(néven)!

2.  Olvassa be a fogado.txt állományban található adatokat és tárolja el adatokat egy listába,ügyeljen arra, hogy az állomány fejlécet tartalmaz! Amely használatával a további feladatok megoldhatók! A kimenet a mintának megfelelő adatot adja vissza! Lehetőség szerint CLASS HASZNÁLATÁVAL! Ha nem CLASS-sal oldod meg, akkor is érvényes, de nem kaphatsz a feladatra maximális pontot.

3. Írja a képernyőre, hogy hány foglalás adatait tartalmazza a fájl!

4. Kérje be a felhasználótól egy tanár nevét, majd jelenítse meg a mintának megfelelően
a képernyőn, hogy a megadott tanárnak hány időpontfoglalása van! Ha a megadott tanárhoz
– ilyen például Farkas Attila – még nem történt foglalás, akkor „A megadott néven nincs
időpontfoglalás.” üzenetet jelenítse meg!

5. Kérjen be a felhasználótól egy érvényes időpontot a forrásfájlban található formátumban
(pl. 17:40)! A program írja a képernyőre a megadott időpontban foglalt tanárok névsorát!
Egy sorban egy név szerepeljen!

Output / kimenet__________________________________________________

3.feladat
Foglalások száma: 161

4.feladat
Adjon meg egy nevet: Nagy Ferenc
Nagy Ferenc néven 6 időpontfoglalás van.

5.feladat
Adjon meg egy érvényes időpontot (pl. 17:10): 17:40
Hantos Hedvig
Csorba Ede
Keller Katalin
Papp Lili
Magos Magdolna
Fodor Zsuzsanna
Nagy Marcell
Olasz Ferenc
Veres Gergely
Beke Bianka
Szalai Levente

__________________________________________________

"""


#1-2


class Fogado_ora:
  def __init__(self,sor):
    vezetek,uto,lefoglalt_ido,foglalas_ido = sor.strip().split(" ")
    self.vezetek = vezetek
    self.uto = uto
    self.lefoglalt_ido = lefoglalt_ido
    self.foglalas_ido = foglalas_ido

with open("fogado.txt","r",encoding="utf-8") as f:
  f.readline()
  lista = [Fogado_ora(sor) for sor in f]

#3

print(f"3.feladat\nFoglalások száma: {len(lista)}")
print()

#4

bekeres = input("4.feladat\nAdjon meg egy nevet: ")
szeletelo = bekeres.split(" ")

#Nagy Ferenc 17:00 2017.10.28-21:30

kereso = len([sor for sor in lista if sor.vezetek == szeletelo[0] and sor.uto ==  szeletelo[1]])

if kereso:
  print(f"{bekeres} néven {kereso} időpontfoglalás van.")
else:
  print("A megadott néven nincs időpontfoglalás.")
print()

#5

bekeres2 = input("5.feladat\nAdjon meg egy érvényes időpontot (pl. 17:10): ")

kereso2 = [(sor.vezetek,sor.uto) for sor in lista if sor.lefoglalt_ido == bekeres2]
#kereso2.sort()

[print(f"{sor[0]} {sor[1]}") for sor in kereso2]
