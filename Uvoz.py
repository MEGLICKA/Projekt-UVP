import os
import requests

def url_v_niz(url):
    """Prenese vsebino spletne strani iz podanega URL-ja in jo vrne kot niz.
    Če pride do napake pri povezavi, se izpiše obvestilo in vrne None."""
    try:
        page_content = requests.get(url)
        page_content.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f'Spletna stran ni dosegljiva: {e}')
        return None
    return page_content.text

def niz_v_dat(tekst, directory, ime):
    """Shrani podan niz v datoteko, ki se nahaja v mapi 'directory' 
    z imenom 'ime'. Če mapa ne obstaja, se samodejno ustvari."""
    os.makedirs(directory, exist_ok=True) 
    path = os.path.join(directory, ime)
    with open(path, 'w', encoding='utf-8') as file_out:
        file_out.write(tekst)
    return None

def shrani_stran(stran, directory, ime, st_strani):
    """Postopoma prenese in shrani več strani s podanega URL-ja.
    'st_strani' določa število strani, ki jih želimo prenesti."""
    for i in range(1, st_strani):
        url = f'{stran}{i}'
        print(f'Prenašam stran: {url}')
        
        tekst = url_v_niz(url)
        
        if tekst:
            ime_datoteke = f'{ime}_stran_{i}.html'
            niz_v_dat(tekst, directory, ime_datoteke)
            print(f'Stran {i} shranjena kot {ime_datoteke}')
        else:
            print(f'Neuspešen prenos za stran {i}. Preskakujem...')

