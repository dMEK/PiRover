# This program formats a gps  file for use in Google Earth
# KML is a type of XML used by Google Earth to delineate landmarks, objects and paths
# Rather than saving locations as a CSV, this program needs the lat and long seperated by spaces
# The file should be locations.log

import string

#open files for reading and writing
gps = open('locations.log', 'r')
#f = gps.readlines()
kml = open('locations.kms', 'w')

kml.write('<?xml version="1.0" encoding="UTF-8" ?>'\n)
kml.write('<kml xmlns="http://www.opengis.net/kml/2.2">'\n)
kml.write('<Document>'\n)
kml.write('<name>Rover Path</name>'\n)
kml.write('<description>Path taken by Rover</description>'\n)
kml.write('<Style id-"yellowLineGreenPoly">'\n)
kml.write('<LineStyle><color>7f00ffff</color><width>4</width></LineStyle>'\n)
kml.write('<PolyStyle><color>7f00ff00</color></PolyStyle>'\n)
kml.write('</Style>'\n)
kml.write('<Placemark<name>Rover Path</name>'\n)
kml.write('<styleUrl>#yellowLineGreenPoly</styleUrl>'\n)
kml.write('<Linestring>'\n)
kml.write('<extrude>1</extrude><tesselate>1</tesselate>'\n)
kml.write('<>'\n)
kml.write('<coordinates>'\n)
for line in gps:
  coordinate = string.split(line)
  print coordinate
  longitude=coordinate[0]
  latitude==coordinate[1]
  kml.write(longitude + "," + latitude + "\n")
kml.write('</coordinates>'\n)
kml.write('</Linestring>'\n)
kml.write('</Placemark>'\n)
kml.write('</Document>'\n)
kml.write('</kml>'\n)
gps.close()
kml.close()
