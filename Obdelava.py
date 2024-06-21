import csv
import os
import requests
import re

def preberi_dat_v_niz(directory, ime):
    path = os.path.join(directory, ime)
    with open(path, 'r', encoding='utf-8') as file_in:
        text = file_in.read()
    return text

def stran_v_oglase(vsebina_strani):
    pass