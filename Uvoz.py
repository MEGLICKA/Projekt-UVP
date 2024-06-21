import csv
import os
import requests
import re

sicilija_julija_url = 'https://www.airbnb.com/s/Sicily--Italy/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2024-07-01&monthly_length=3&monthly_end_date=2024-10-01&price_filter_input_type=0&channel=EXPLORE&query=Sicily%2C%20Italy&place_id=ChIJs1lT0GhiEBMRUH22ZykECwE&location_bb=Qhs%2FnkF6cmxCDfiuQT7PvA%3D%3D&date_picker_type=calendar&checkin=2024-07-01&checkout=2024-07-08&source=structured_search_input_header&search_type=autocomplete_click'
sicilija_directory = 'Projekt-UVP'
ime_html = 'sicilija.html'
ime_csv = 'sicilija.csv'

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


