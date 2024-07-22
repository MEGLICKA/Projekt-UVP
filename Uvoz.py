import os
import requests



def url_v_niz(url):
    try:
        page_content = requests.get(url)
    except requests.exception.RequestException:
        print('Spletna stran ni dosegljiva.')
        return None
    return page_content.text

def niz_v_dat(tekst, directory, ime):
    os.makedirs(directory, exist_ok=True) 
    path = os.path.join(directory, ime)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(tekst)
    return None

def shrani_stran(stran, directory, ime):
    tekst = url_v_niz(stran)
    niz_v_dat(tekst, directory, ime)

shrani_stran(https://www.bbcgoodfood.com/recipes/collection/quick-lunch-recipes, 'Projekt-UVP', 'kosilo.html')
