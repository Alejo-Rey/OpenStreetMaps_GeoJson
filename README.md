# OpenStreetMap GeoJson

## Description
What you should find in this project:

* How to consume the API of OpenStreetMap
* How to write and read in a CSV file
* How to manage Error of request methods and others
* How to create a polygon with Sympy library
* How to find a point in a polygon with Sympy

---

### [get_polygons.py](./get_polygons.py)
* This program create a csv file with all the localities od Bogotá. Use some librearys like: \
  - time
  - requests
  - json
  - csv
  - sys\
  Do a request for the API of OpenStreetMap with some params to get a JSON and then get the polygon\
  of this request. Then is storage in a csv file.\
  to run it:\
  `./get_polygons.py`


### [find_localitys.py](./find_localitys.py)
* This program read some csv files and create the polygons of sympy and find the points in this, use:\
  - sympy
  - time
  - csv\
  Sympy is necesary to install.\
    `sudo pip3 install sympy`
  Read the polygons and the points file, whit polygons create a the polygons with Sympy,\
  then you can find with a method the points in the polygons, and then write it in a csv file.\
  to run it:\
  `./find_localitys.py`

## Author
* **Alejo-Rey** - [Alejo-Rey](https://github.com/Alejo-Rey)
