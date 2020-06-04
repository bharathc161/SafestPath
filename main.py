from urllib2 import urlopen
import json
import numpy as np#kind of array for fast manipulation

def crimeWeight(lati, longi, hr):#latitude longitude hour
    #basically this function will return crime weight at the given latitude in 200 meter radius.
    url = "https://data.phila.gov/resource/sspu-uyfa.json?$$app_token=bF12rIkELtbJ8PXnuzuZTWmVF"
    radius = "200"
    locationUrl = url + ("&$where=within_circle(shape,%s,%s,%s)" % (lati, longi, radius))
    #To select points from a database within a certain distance from a given latitude/longitude point, within a selection circle, 

    response = urlopen(locationUrl)#opens url , The return value from urlopen() gives access to the headers from the HTTP server through the info() method,
    #and the data for the remote resource via methods like read() and readlines().
    data = json.loads(response.read().decode('utf-8'))#UTF-8 most commonly used encodings,  UTF stands for “Unicode Transformation Format”, and the '8' means that 8-bit 
    Crime_type_100 = 0
    Crime_type_200 = 0
    Crime_type_300 = 0
    Crime_type_400 = 0
    Crime_type_500 = 0
    Crime_type_600 = 0  
    Crime_type_other = 0

    rdata = []#will store hours(time) 
    labels = []#kind of crime 

    for d in data: 
        u = d.get("ucr_general")#int in the form of string ,representing crime rate  
        if u != "":
            u = int(u)
            u = u - (u % 100)
            if not (u == 700 or u == 1000 or u == 1100 or u == 1200 or u == 1300 or u ==1500 or (u > 1500 and u <= 2400) or u == 2600):
				if(hr==int(d.get('hour_')))
				
					if u == 100:
						Crime_type_100 += 1
					elif u == 200:
						Crime_type_200 += 1
					elif u == 300:
						Crime_type_300 += 1
					elif u == 400:
						Crime_type_400 += 1
					elif u == 500:
						Crime_type_500 += 1
					elif u == 600:
						Crime_type_600 += 1
					else:
						Crime_type_other += 1
				 

    #print "CrimeType-homicides = " + str(Crime_type_100)
    #print "CrimeType-rapes = " + str(Crime_type_200)
    #print "CrimeType-robberies = " + str(Crime_type_300)
    #print "CrimeType-assaults = " + str(Crime_type_400)
    #print "CrimeType-burglaries = " + str(Crime_type_500)
    #print "CrimeType-thefts = " + str(Crime_type_600)
    #print "CrimeType-crimes = " + str(Crime_type_other)
   
	crimeWt = (Crime_type_100*7 + Crime_type_200*6 + Crime_type_300*5 + Crime_type_400*4 + Crime_type_500*3 + Crime_type_600*2 + Crime_type_other*1)
     

    return crimeWt;







 
