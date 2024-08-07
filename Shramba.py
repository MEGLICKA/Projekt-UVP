import csv
import os


def napisi_csv(fieldnames, rows, directory, ime):
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, ime)
    with open(path, 'w', encoding='utf-8', newline='') as csv_file: 
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return


def recepti_v_csv(recepti, directory, ime):
    assert recepti and (all(j.keys() == recepti[0].keys() for j in recepti)) 
    field_names = list(recepti[0].keys()) 
    napisi_csv(field_names, recepti, directory, ime)