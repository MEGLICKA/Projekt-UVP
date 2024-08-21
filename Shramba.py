import csv
import os

def napisi_csv(fieldnames, rows, directory, ime):
    """Ustvari CSV datoteko s podanimi stolpci ('fieldnames') in vrsticami ('rows')
    v mapi 'directory' z imenom 'ime'."""
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, ime)
    with open(path, 'w', encoding='utf-8', newline='') as csv_file: 
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return


def recepti_v_csv(recepti, directory, ime):
    """Preveri konsistentnost ključev v seznamu slovarjev 'recepti' in jih shrani v CSV datoteko."""
    assert recepti and (all(j.keys() == recepti[0].keys() for j in recepti)) # Preveri, ali vsi slovarji vsebujejo enake ključe
    field_names = list(recepti[0].keys()) # Ustvari seznam imen stolpcev na podlagi ključev prvega recepta
    napisi_csv(field_names, recepti, directory, ime)
    print(f'Podatki so shranjeni v datoteki {ime}.')
