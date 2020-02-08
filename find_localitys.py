#!/usr/bin/python3
"""
Program to get the vectors and export to csv the localitys of Bogotá 
"""
import requests
import json
import csv
import sys

"""
def vectors():
        cd get and export the vectors
"""

url = "https://nominatim.openstreetmap.org/search.php?q="
localitys = ["Usaquén", "Santa Fe", "San Cristobal", "Usme",
                "Tunjuelito", "Bosa", "Kennedy", "Fontibón", 
                "Engativá", "Suba", "Chapinero", "Barrios Unidos",
                "Teusaquillo","Los Mártires", "Antonio Nariño",
                "Puente Aranda", "La Candelaria", "Rafael Uribe Uribe",
                "Ciudad Bolívar", "Sumapaz"]
fields = "+bogota+colombia&polygon_geojson=1& format=json"
vectors = []
"for local in localitys: 'localidad',    'localidad': localitys[0], "
try:
    req = requests.get("{}{}{}".format(url, localitys[0],fields))
    for x in req.json():
        if x.get('geojson').get('type') == 'Polygon' and x.get('type') == 'administrative':
            for coor in x.get('geojson').get('coordinates')[0]:
                vectors.append({'latitud': coor[1], 'longitud': coor[0]})

    with open('1.csv', 'w') as csvfile:
        fieldnames = ['latitud', 'longitud']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(vectors)


except requests.exceptions.Timeout:
    print("Timeout")
except requests.exceptions.TooManyRedirects:
    print("URL is bad, try a different one")
except requests.exceptions.RequestException as e:
    print("Requests Error: ")
    print(e)
    sys.exit(1)



print(vectors)
print(type(vectors))
"        for x in req.json(): vectors.append(x.get('geojson').get('coordinates')) if x.get('geojson').get('type') == 'Polygon' else ''"
