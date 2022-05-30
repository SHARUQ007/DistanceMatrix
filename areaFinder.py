# importing requests and json
import json


# Opening JSON file
f = open('distanceMatrix.json')  
# returns JSON object as 
# a dictionary
data = json.load(f)

siteList = []
#for storing objects


# Iterating through the json
# list
matchID=792
radius=25


for site in data:
   idn=site['id']
   if(int(idn)==matchID):
    rows=site['rows']
    print(idn)
    for row in rows:
       distance=row['distance']
       idn2=row['id']
       if(distance<=radius and distance>0):
        print(idn2," ---------------> ",distance)
        eachSite ={
            "id": idn2,
            "distance" :distance 
        }
        siteList.append(eachSite)
           
output={
    "Search ID":matchID,
    "Radius (in KM)":radius,
    "Matching Sites":siteList
}
#################################################################
        
   
    
     


json_object = json.dumps(output, indent = 4)
     
# Writing to sample.json
with open("out.json", "w") as outfile:
   outfile.write(json_object)  



 
