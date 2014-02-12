import requests
import json

print """
	1 - Almeria
	2 - Cadiz
	3 - Cordoba
	4 - Granada
	5 - Huelva
	6 - Jaen
	7 - Malaga
	8 - Sevilla
	"""



dicc1={1:"Almeria", 2:"Cadiz", 3:"Cordoba", 4:"Granada", 5:"Huelva", 6:"Jaen", 7:"Malaga", 8:"Sevilla"}



Ciudad = int(raw_input("¿Desea saber la temperatura de alguna provincia?"))

Respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather', params = {'q': "%s, spain" % dicc1[Ciudad]})

dicc = json.loads(Respuesta.tex)

print "La temperatura actual de la provincia de" ,dicc1[Ciudad], "es" , dicc["main"]["temp"] - 273, "Grados Centigrados"


