import json,urllib,ast

lat = -33.7370074
long = 150.9511264
range_area = 10
max = 20

def getData(lat,long,range_area,max):

    url = 'http://contact.woolworths.com.au/storelocator/service/proximity/SUPERMARKETS/latitude/'+str(lat)+'/longitude/'+str(long)+'/range/'+str(range_area)+'/max/'+str(max)+'/json'

    response = urllib.urlopen(url)

    data = json.loads(response.read())

    jdata = ast.literal_eval(json.dumps(data))

    return jdata['locatorList']['storeList']['storeRank']

valApi = getData(lat,long,range_area,max)

print valApi

