import os

import Uvoz as uv
import Obdelava as ob
import Shramba as sh


recepti_kosila_url = 'https://www.bbcgoodfood.com/search?q=all&tab=recipe&page='
recepti_directory = 'Projekt-UVP'
ime_html = 'Good_Food'
ime_csv = 'Recepti.csv'
st_strani = 157

def main(redownload=True, reparse=True):
    path = os.path.join(recepti_directory, ime_html)
    if redownload or not os.path.exists(path):
        uv.shrani_stran(recepti_kosila_url, recepti_directory, ime_html, st_strani)
    else: 
        print('Datoteka html že obstaja')
    
    path = os.path.join(recepti_directory, ime_csv)
    if reparse or not os.path.exists(path): 
        recepti = ob.preberi_vse_datoteke(recepti_directory)

        sh.recepti_v_csv(recepti, recepti_directory, ime_csv)
    else:
        print('Datoteka csv že obstaja')
        
if __name__ == '__main__':
    main()