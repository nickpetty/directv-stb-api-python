import urllib
import json

class DirecTV: 
	#http://stackoverflow.com/questions/6924519/error-when-parsing-json-data
	#Get JSON data from DTV STB
	def contact(self, url):
		return json.load(urllib.urlopen(url))

	#Example of parsing
	def get_info(self, ip):
		res = self.contact('http://' + ip + ':8080/tv/getTuned')
		return(str(res['callsign']), str(res['major']), str(res['title']))

	def chng_chnl(ip, n):
		url = 'http://' + ip + ':8080/tv/tune?major=' + n
		res = DirecTV.contact(url)
		return res['status']['msg']

	def keyInput(ip, n):
		url = 'http://' + ip + ":8080/remote/processKey?key=" + n
		res = DirecTV.contact(url)


#print DirecTV().get_info('10.0.0.100')[2]