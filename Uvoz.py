import os
import requests



def url_v_niz(url):
    try:
        page_content = requests.get(url)
        page_content.raise_for_status()  # Preveri, ali je zahteva uspešna
    except requests.exceptions.RequestException as e:
        print(f'Spletna stran ni dosegljiva: {e}')
        return None
    return page_content.text

def niz_v_dat(tekst, directory, ime):
    os.makedirs(directory, exist_ok=True) 
    path = os.path.join(directory, ime)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(tekst)
    return None

def shrani_stran(stran, directory, ime, st_strani):
    for i in range(1, st_strani):
        # Sestavi URL za posamezno stran
        url = f"{stran}{i}"
        print(f"Prenašam stran: {url}")
        
        # Prenesi vsebino strani
        tekst = url_v_niz(url)
        
        # Če je prenos uspešen, shrani stran
        if tekst:
            ime_datoteke = f"{ime}_stran_{i}.html"
            niz_v_dat(tekst, directory, ime_datoteke)
            print(f"Stran {i} shranjena kot {ime_datoteke}")
        else:
            print(f"Neuspešen prenos za stran {i}. Preskakujem...")

#shrani_stran('https://www.bbcgoodfood.com/search?q=all&tab=recipe&page=', 'Projekt-UVP', 'Food.html', 157)
