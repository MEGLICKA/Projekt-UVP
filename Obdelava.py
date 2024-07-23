import os
import re
import csv

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
        return match.group(1) if match else None
    
    ime = preveri(ime)
    if ime == 'Quick lunch recipes':
        ime = 'Reuben sandwich'

    return {
        'ime': ime,
        'id': preveri(id),
        'ocena': preveri(ocena),
        'st_ocen': preveri(st_ocen),
        'cas_priprave': preveri(cas_priprave),
        'level': preveri(level),
        'healthy': True if healthy else False,
        'vegetarian': True if vegetarian else False,
        'gluten_free': True if gluten_free else False,
        'vegan': True if vegan else False
    }

def recepte_v_datoteko(ime, directory):
    vsebina_strani = preberi_dat_v_niz(directory, ime)
    recept = stran_v_recepte(vsebina_strani)
    recepti = [recept_v_slovar(kos) for kos in recept]
    return [rec for rec in recepti]

recepti = recepte_v_datoteko('kosilo.html', 'Projekt-UVP')
print(recepti[:5])


def napisi_csv(fieldnames, rows, directory, ime):
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, ime)
    with open(path, 'w', encoding='utf-8', newline='') as csv_file: 
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def recepti_v_csv(recepti, directory, ime):
    assert recepti and (all(j.keys() == recepti[0].keys() for j in recepti)) 
    field_names = list(recepti[0].keys()) 
    napisi_csv(field_names, recepti, directory, ime)

recepti_v_csv(recept_v_slovar('kosilo.html'), 'Projekt-UVP', 'test_kosilo.csv')
print(f"Datoteka test_kosilo.csv je bila uspešno ustvarjena.")