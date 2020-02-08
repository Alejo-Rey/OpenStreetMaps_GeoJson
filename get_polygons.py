#!/usr/bin/python3
"""
Program to get the vectors and export to csv the localitys of Bogotá 
"""
from time import time
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
start = time()
print(start)
for local in localitys:
    try:
        req = requests.get("{}{}{}".format(url, local, fields))
        for x in req.json():
            if x.get('geojson').get('type') == 'Polygon' and x.get('type') == 'administrative':
                for coor in x.get('geojson').get('coordinates')[0]:
                    vectors.append({'localidad': local, 'latitud': coor[1], 'longitud': coor[0]})

        with open('polygons.csv', 'w') as csvfile:
            fieldnames = ['localidad', 'latitud', 'longitud']
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
end = time()
print(end - start)