
## JSON represnts data as nested lists and dictionaries

import json

"""
data ='''{               ## starts with curly brace so its a dict
  "name" : "Chuck",
  "phone" : {             ## first dict within a dict
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {            ## second dict within a dict
     "hide" : "yes"
   }
}'''


info = json.loads(data) ## loads stands for load string    ## info is a dict because data as seen above is in curly braces if it was in [] it would be a list
print('Name:',info["name"])
print('Hide:',info["email"]["hide"])

"""


"""

input = '''[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]'''

info = json.loads(input)
print('User count:', len(info))
for item in info:           ## item here is the 2 dicts inside the list
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])


"""


"""
http://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%2C+MI   ## This is where we get the data in json below

###########   data start

{
    "status": "OK",
     "results": [
        {
            "geometry": {
                "location_type": "APPROXIMATE",
                 "location": {
                    "lat": 42.2808256,
                     "lng": -83.7430378
                }
            },
            "address_components": [
                {
                    "long_name": "Ann Arbor",
                     "types": [
                        "locality",
                         "political"
                    ],
                    "short_name": "Ann Arbor"
                }
             ],
             "formatted_address": "Ann Arbor, MI, USA",
             "types": [
                "locality",
                "political"
            ]
        }
    ]
}


############### data end 


import urllib.request, urllib.parse, urllib.error    ## libraries to porcess the URL
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})   ## concatenate to the end of the serviceurl to get the detail from the entererd place in address

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()    ## check these functions and what they do from documentation but over here its the UTF and unicode conversion 
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':        relates to data pulled and above code
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)





"""