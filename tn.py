import xml.etree.ElementTree as ET
import urllib2 as URL
from switcher import state
import sms

def alert_pull():
	tree = ET.parse(URL.urlopen('https://alerts.weather.gov/cap/us.php?x=1'))
	root = tree.getroot()


	for x in root.findall('{http://www.w3.org/2005/Atom}entry'):
		event = x.find('{urn:oasis:names:tc:emergency:cap:1.1}event').text
		severity = x.find('{urn:oasis:names:tc:emergency:cap:1.1}severity').text
		location = x.find('{urn:oasis:names:tc:emergency:cap:1.1}areaDesc').text
		geo = x.find('{urn:oasis:names:tc:emergency:cap:1.1}geocode')
		summary = x.find('{http://www.w3.org/2005/Atom}summary').text
		stateAbr = geo[3].text[0:2]

		if severity == "Severe" and location.find('Putnam') != -1 and stateAbr == "TN":
			sms_text = "There is a "+severity+" "+event+" in Putnam County "+summary
			sms.send(sms_text)
			print sms_text
			
alert_pull()

	
