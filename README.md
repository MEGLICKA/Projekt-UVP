# Projekt UVP: Analiza receptov

Projekt se osredotoča na analizo zbirke receptov, kjer se raziskujejo različni vidiki, kot so ocene, čas priprave, zahtevnost, in druge značilnosti receptov. Uporabljena so orodja za obdelavo podatkov, vizualizacijo in izračun statistik, kar omogoča vpogled v najbolj priljubljene in kakovostne recepte.

## Delovanje funkcij
V datoteki `Uvoz.py` se prične uvoz podatkov v obliki .html, ki se shranijo v mapo `Projekt-UVP`. `Obdelava.py` skrbi, da se uvoženi podatki obdelajo po naših željah, s pomočjo `Shramba.py` pa se le-ti shranijo v obliki .csv datoteke.

Vse te funkcije so združene v datoteki `Main.py`, s pomočjo katere zaženemo cel postopek pridobivanja, obdelovanja in shranjevanja podatkov.
Vpogled v izluščene podatke in njihovo kratko analizo je na voljo v datoteki `Recepti.ipynb`.

## Navodila za uporabo
Predpogoj za pravilno delovanje projekta je naložen program Python verzije 3. Vsebino projekta si naložite na svojo napravo s kloniranjem repozitorija.

### Knjižnice
Za optimalno delovanje funkcij je zaželjena namestitev naslednjih knjižnic, v kolikor jih še nimate. Namestite jih lahko s sledečim ukazom v terminalu:
```
pip install __knjižnica__
```
* knjižnice za pridobivanje, obdelovanje in shranjevanje podatkov: **os requests re csv html**

* knjižnice za analizo podatkov: **pandas mathplotlib numpy seaborn**

### Zagon programa
Po pravilni vzpostavitvi delovnega okolja in kloniranju repozitorija, program zaženete s klicom datoteke `Main.py` v terminalu:
```
python Main.py
```
Program se zaključi z izpisom: _Podatki so shranjeni v datoteki Recepti.csv._ 
Po tem lahko zaženete datoteko `Recepti.ipynb` in si ogledate analizo podatkov.

## Avtor
Julija Meglič - [moj GitHub profil](https://github.com/MEGLICKA)
