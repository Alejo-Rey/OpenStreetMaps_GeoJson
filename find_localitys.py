#!/usr/bin/python3
"""
Program to find the localitys of a point in Bogotá 
"""
from sympy import Polygon, Point
from sympy.abc import t
from time import time
import csv

start = time()
def open_file(file):
    """
        Returns a list of the dictionarys
        results: the list to fill
    """
    results = []
    with open(file) as File:
        reader = csv.DictReader(File)
        for row in reader:
            results.append(row)
    return results

time_poly = time()
def pass_coordinates(list_coordinates):
    """
        Returns a dictionary of polygons with the coordinates
    """

    polygons = {}
    for key, value in list_coordinates.items():
        polygons[key] = Polygon(*value)
        time_poly = time()
        print("Time of create the polygon: ", key, " : ", time_poly - start)
    return polygons

if __name__ == '__main__':
    polygons = open_file('polygons.csv')
    points = open_file('points.csv')

    localities = {}
    for coor in polygons:
        if coor.get('localidad') in localities.keys():
            localities[coor.get('localidad')].append((float(coor.get('latitud')), float(coor.get('longitud'))))
        else:
            coordinates = []
            coordinates.append((float(coor.get('latitud')), float(coor.get('longitud'))))
            localities[coor.get('localidad')] = coordinates

    polygons = pass_coordinates(localities)

    for point in points:
        for key, value in polygons.items():
            print(key)
            try:
                if value.encloses_point(Point(float(point.get('latitud')), float(point.get('longitud')))):
                    point['localidad'] = key
            except:
                print("invalid Coordinate", point.get('latitud'), point.get('longitud'))
    try:
        with open('points_locality.csv', 'w') as csvfile:
            fieldnames = ['id', 'latitud', 'longitud', 'localidad']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(points)
    except:
        print("invalid field")

    end = time()
    print("time to find the points: ", end - time_poly - start)