import requests

bahnhof = raw_input("Bitte geben Sie den Startbahnhof ein: ")
bahnhof2 = raw_input("Bitte geben Sie den Zielbahnhof ein: ")

url0 = 'http://open-api.bahn.de/bin/rest.exe/location.name?authKey=DBhackFrankfurt0316&lang=de&input=' + bahnhof +'&format=json'

data0 = requests.get(url0).json()
try:
	ort = data0['LocationList']['StopLocation'][0]['id']
except KeyError:
	ort = data0['LocationList']['StopLocation']['id']  
	
url3 = 'http://open-api.bahn.de/bin/rest.exe/location.name?authKey=DBhackFrankfurt0316&lang=de&input=' + bahnhof2 +'&format=json'

data3 = requests.get(url3).json()
try:
	ort2 = data3['LocationList']['StopLocation'][0]['id'][2:]
except KeyError:
	ort2 = data3['LocationList']['StopLocation']['id'][2:]
#print ort2

url = 'http://open-api.bahn.de/bin/rest.exe/departureBoard?authKey=DBhackFrankfurt0316&lang=de&id=' + ort + '&date=2016-02-22&time=18:00&format=json'

response = requests.get(url)

data = response.json()

print "\n"+ "Verbindungen von " + bahnhof +" nach " + bahnhof2 +"\n"


for l in data['DepartureBoard']['Departure']:
	#print l
	url2 = l['JourneyDetailRef']['ref']
	response2 = requests.get(url2)
	data2 = response2.json()
	#print data2
	#try:
	zug = data2['JourneyDetail']['Names']['Name']['name']
	for j in data2['JourneyDetail']['Stops']['Stop']:##damit findet er alle Zuege, die am Zielbahnhof vorbeifahren. Das ist nicht so ganz, was ich will :(
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
		try: 
			text8 = j['id']
		except KeyError:
			text8 = ""
		if (text8 == ort2):
			print text4 + " um " + text5 +" am " + text6 + " auf Gleis " + text7 + " mit Zug " + zug

