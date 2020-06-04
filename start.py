import json #java script object notation 
import datetime
from urllib2 import urlopen
from main import crimeWeight

def routeFinder(orgVal,destiVal):
#originValue & destinationValue (dataType-string )	
  
    orgVal = orgVal.replace(" ","+")
	#replaces space with + , to get in desired format.   
    destiVal = destiVal.replace(" ","+")
    mapsUrl = "https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%st&key=AIzaSyAkKc-oigF24jNtgQio6erz128zRqCO_U4&mode=walking&alternatives=true" % (originVal,destinationVal)
     
	response = urlopen(mapsUrl) 
    data = json.loads(response.read().decode('utf-8')) 
    co_list = []
	#coordinate list
    numberOfRoutes = len(data.get('routes'))
	#no of paths len returns number of items in an  object 
    x = 0
    for route in data.get('routes'):#  iterate on every route
        co_list.append([])
        for step in (route.get('legs')[0].get('steps')):#The DirectionsLeg is an object literal with the following fields:
                            #steps[] contains an array of DirectionsStep objects denoting information about each separate step of the leg of the journey.
            lati = step.get('start_location').get('lat')
            longi = step.get('start_location').get('lng')
            co_list[x].append((lati,longi))#appending latitude & longitude on that particular path
        x+=1

     
    now = datetime.datetime.now()#present time 

    wtValue = []
    #weighted values list
    x1 = 0
    for route in co_list: 
        wtValue.append([])
        y1 = 0
        for step in route:
            wtValue[x1].append(crimeWeight(str(co_list[x1][y1][0]), str(co_list[x1][y1][1]), now.hour))#taking wt of each step 
            y1+=1
        x1+=1

    x1 = 0
    minimum = float(10000000)
    min_route = 0
    for route in wtValue:
        if minimum > (float(sum(route))/len(route)):
            minimum = sum(route)/len(route)
            min_route = x1
        x1+=1

    return co_list[min_route]



