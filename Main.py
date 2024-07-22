import os

import Uvoz as uv
import Obdelava as ob
import Shramba as sh


recepti_kosila_url = 'https://www.bbcgoodfood.com/recipes/collection/quick-lunch-recipes'
recepti_directory = 'Projekt-UVP'
ime_html = 'kosilo.html'
ime_csv = 'kosilo.csv'

def main(redownload=True, reparse=True):
    path = os.path.join(recepti_directory, ime_html)
    if redownload or not os.path.exists(path):
        uv.shrani_stran(recepti_kosila_url, recepti_directory, ime_html)
    else: 
        print('Datoteka html že obstaja')
    
    path = os.path.join(recepti_directory, ime_csv)
    if reparse or not os.path.exists(path): 
        recepti = ob.recepte_v_datoteko(ime_html, recepti_directory)

        sh.recepti_v_csv(recepti, recepti_directory, ime_csv)
    else:
        print('Datoteka csv že obstaja')
        
