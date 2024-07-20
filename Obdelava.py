import csv
import os
import requests
import re

def preberi_dat_v_niz(directory, ime):
    path = os.path.join(directory, ime)
    with open(path, 'r', encoding='utf-8') as file_in:
        text = file_in.read()
    return text

def stran_v_recepte(vsebina_strani):
    return re.findall(r'{"title":*?,"headingStyledSize"*?}]},', vsebina_strani, flags=re.DOTALL)

def recept_v_slovar(recept):
    ime = re.search(r'{"title":"(.*?)","headingStyledSize"', recept)
    id = re.search(r'"id":"(.*?)"', recept)
    ocena = re.search(r'{"ratingValue":(.*?),', recept)
    st_ocen = re.search(r'"ratingCount":(.*?),', recept)
    cas_priprave = re.search(r'{"slug":"time","display":"(.*?)"}', recept)
    level = re.search(r'{"slug":"skillLevel","display":"(.*?)"}', recept)
    healthy = re.search(r'{"slug":"healthy","display":"Healthy"}', recept)
    vegetarian = re.search(r'{"slug":"vegetarian","display":"Vegetarian"}', recept)
    gluten_free = re.search(r'{"slug":"gluten-free","display":"Gluten-free"}', recept)
    vegan = re.search(r'{"slug":"vegan","display":"Vegan"}', recept)

    #if ocena == None or st_ocen == None or heatlhy == None or vegetarian == None or gluten_free == None or vegan == None:
    #    return None
    sez = [healthy, vegetarian, gluten_free, vegan]
    for el in sez:
        if el == None:
            el = False
        else:
            el = True
    
    return {'ime': ime.group(1), 'id': id.group(1), 'ocena': ocena.group(1), 'st_ocen': st_ocen.group(1), 'cas_priprave': cas_priprave.group(1), 'level': level.group(1), 'healthy': healthy, 'vegetarian': vegetarian, 'gluten_free': gluten_free, 'vegan': vegan}

def recepte_v_datoteko(ime, directory):
    vsebina_strani = preberi_dat_v_niz(directory, ime)
    recept = stran_v_recepte(vsebina_strani)
    recepti = [recept_v_slovar(kos) for kos in recept]
    return [rec for rec in recepti]