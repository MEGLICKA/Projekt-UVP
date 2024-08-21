import os
import re


def decode_unicode_escapes(s):
    """Pretvori Unicode escape znake (npr. \u0026) v njihove znake (npr. &)."""
    return s.encode('utf-8').decode('unicode_escape')

def preberi_dat_v_niz(directory, ime):
    path = os.path.join(directory, ime)
    with open(path, 'r', encoding='utf-8') as file_in:
        text = file_in.read()
    return text

def stran_v_recepte(vsebina_strani):
    return re.findall(r'{"title":.*?,"headingStyledSize".*?}]},', vsebina_strani, flags=re.DOTALL)

def recept_v_slovar(recept):
    ime = re.search(r'"title":"(.*?)"', recept)
    id = re.search(r'"id":"(.*?)"', recept)
    ocena = re.search(r'"ratingValue":(.*?)(?:,|})', recept)
    st_ocen = re.search(r'"ratingCount":(.*?)(?:,|})', recept)
    cas_priprave = re.search(r'"slug":"time","display":"(.*?)"', recept)
    level = re.search(r'"slug":"skillLevel","display":"(.*?)"', recept)
    healthy = re.search(r'"slug":"healthy","display":"Healthy"', recept)
    vegetarian = re.search(r'"slug":"vegetarian","display":"Vegetarian"', recept)
    gluten_free = re.search(r'"slug":"gluten-free","display":"Gluten-free"', recept)
    vegan = re.search(r'"slug":"vegan","display":"Vegan"', recept)

    def preveri(match):
        return decode_unicode_escapes(match.group(1)) if match else None
      
    
    return {
        'Ime': preveri(ime),
        'ID': preveri(id),
        'Ocena': preveri(ocena),
        'Število ocen': preveri(st_ocen),
        'Čas priprave': preveri(cas_priprave),
        'Level': preveri(level),
        'Healthy': True if healthy else False,
        'Vegetarian': True if vegetarian else False,
        'Gluten free': True if gluten_free else False,
        'Vegan': True if vegan else False
    }

def recepte_v_datoteko(ime, directory):
    vsebina_strani = preberi_dat_v_niz(directory, ime)
    recept = stran_v_recepte(vsebina_strani)
    recepti = [recept_v_slovar(kos) for kos in recept]
    return [rec for rec in recepti]

def odstrani_duplikate(recepti):
    videni = set()
    unikatni_recepti = []
    for recept in recepti:
        if recept['ID'] not in videni:  
            unikatni_recepti.append(recept)
            videni.add(recept['ID'])
    return unikatni_recepti

def preberi_vse_datoteke(directory):
    recepti = []
    for ime_datoteke in os.listdir(directory):
        if ime_datoteke.endswith('.html'):
            print(f"Obdelujem datoteko: {ime_datoteke}")
            vsebina_strani = preberi_dat_v_niz(directory, ime_datoteke)
            recepti_iz_datoteke = stran_v_recepte(vsebina_strani)
            recepti.extend([recept_v_slovar(kos) for kos in recepti_iz_datoteke])
    return odstrani_duplikate(recepti)



