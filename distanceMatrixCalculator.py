from math import sin, cos, sqrt, atan2, radians

def distance_from_latlong(la1,lo1,la2,lo2):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(la1)
    lon1 = radians(lo1)

    lat2 = radians(la2)
    lon2 = radians(lo2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    # print("Result:",round(distance),"km")
    return round(distance)
    


# importing requests and json
import json


# Opening JSON file
f = open('data.json')  
# returns JSON object as 
# a dictionary
data = json.load(f)

distanceMatrix = []
#for storing objects


# Iterating through the json
# list
for site1 in data['sites']:
   lat1=str(site1['lat'])
   lon1=str(site1['lang'])
   idn1= str(site1['id'])
##################################################################

#    print("id 1             : "+idn1)
#    print("latitute 1       : "+lat1)
#    print("longitude 1      : "+lon1)
   siteList = []
   for site2 in data['sites']:
        lat2=str(site2['lat'])
        lon2=str(site2['lang'])
        idn2= str(site2['id'])
        distance=distance_from_latlong(site1['lat'],site1['lang'],site2['lat'],site2['lang'])
        # print("id 2             : "+idn2)
        # print("latitute 2       : "+lat2)
        # print("longitude 2      : "+lon2)
    
        eachSite ={
            "id": idn2,  
            "distance":distance        
        }
        siteList.append(eachSite) 
   obj={"id": idn1,
         "rows":siteList  
            }
   distanceMatrix.append(obj)


json_object = json.dumps(distanceMatrix, indent = 4)
     
# Writing to sample.json
with open("distanceMatrix.json", "w") as outfile:
   outfile.write(json_object)  



 
