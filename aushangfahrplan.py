import requests

bahnhof = raw_input("Bitte geben Sie den Startbahnhof ein: ")
#bahnhof2 = raw_input("Bitte geben Sie den Zielbahnhof ein: ")

url0 = 'http://open-api.bahn.de/bin/rest.exe/location.name?authKey=DBhackFrankfurt0316&lang=de&input=' + bahnhof +'&format=json'

data0 = requests.get(url0).json()
try:
	ort = data0['LocationList']['StopLocation'][0]['id']
except KeyError:
	ort = data0['LocationList']['StopLocation']['id']  
	 

url = 'http://open-api.bahn.de/bin/rest.exe/departureBoard?authKey=DBhackFrankfurt0316&lang=de&id=' + ort + '&date=2016-02-22&time=18:00&format=json'

response = requests.get(url)

data = response.json()

#data['DepartureBoard']['Departure'][1]['name']
k =0 
for i in data['DepartureBoard']['Departure']:
	text0 = i['direction']
	text1 = i['name']
	text2 = i['time']
	text3 = i['date']	
	print "Verbindung: " +str(k) +" Zielbahnhof: " + text0 + " Abfahrt: " + text2  + " am " + text3 + " Zug: " + text1 
	k+=1

verbindung = int(raw_input("Bitte geben Sie die gewuenschte Verbindung ein: "))

#print data

url2 = data['DepartureBoard']['Departure'][verbindung]['JourneyDetailRef']['ref']

#print url2

response2 = requests.get(url2)

data2 = response2.json()

#print data2

#print "Zuglauf: " + data2['JourneyDetail']['Names']['Name']['name']

#print data2['JourneyDetail']['Stops']['Stop'][0]['name']



for j in data2['JourneyDetail']['Stops']['Stop']:
	text4 = j['name']
	try: 
		text7 = j['track']
	except KeyError: 
		text7 = "unbekannt"
	try: 
		text5 = j['depTime']
	except KeyError:
		text5 = j['arrTime']
	try: 
		text6 = j['depDate']
	except KeyError:
		text6 = j['arrDate']
	print text4 + " um " + text5 +" am " + text6 + " auf Gleis " + text7 

#print j
