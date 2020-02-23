# coding: utf-8

import requests
import random
import sys

banner = '''\033[01m
 _____             _         _____                 _   
|   __|___ ___ ___| |___ ___|   __|___ ___ ___ ___| |_ 
|  |  | . | . | . | | -_|___|__   | -_| .'|  _|  _|   |
|_____|___|___|_  |_|___|   |_____|___|__,|_| |___|_|_|
              |___|                       by LuisEd-dev
\033[0m'''

#define user-agent
with open("user-agents.txt", "r") as usera:
	x = usera.read()
	y = x.split('\n')
	z = len(y)
random = random.randint(1, z)

#proxies
proxies = []
plist = requests.get('https://free-proxy-list.net/')
for num in range(1, 200):
	text = plist.text
	text = text.split('<tbody><tr><td>')
	text = str(text).split('</td></tr><tr><td>')
	ip = text[num].split('</td><td>')
	port = text[num].split('</td><td>')
	proxie = "%s:%s" %(ip[0], port[1])
	proxies.append(proxie)

proxy = proxies[0]

print banner

consulta = raw_input("\033[01mPesquisa -> \033[0m")
try:
	num = int(input("\033[01mNumero de resultados -> \033[0m"))
except NameError:
	sys.exit('\033[01;31mSomente numeros são aceitos\033[0m')
pagina = 0

while True:
	useragent = y[random]
	try:
		print (" >_ Usando Proxy: \033[4m%s\033[0m" % proxy),
		headers = {'User-Agent': useragent}
		parametros = {'q' : consulta, 'start':pagina, 'num':num }
		resposta = requests.get('http://www.google.com/search', params=parametros, timeout = 30, headers=headers, proxies={"http" : proxy}) #, proxies={"http" : proxy}
		msg = "Our systems have detected unusual traffic from your computer network"
		msg2 = "support.google.com/websearch/answer"
		if msg in resposta.text or msg2 in resposta.text:
			print "-> \033[31mProxy Detectado Pelo Google\033[0m"
			try:
				proxy = proxies[proxies.index(proxy)+1]
				continue
			except IndexError:
				print "-> Todos os Proxies testados"			
				break
			else:
				continue
		divs = resposta.text
		divs = divs.split('<div><a class="')
		if len(divs) == 0:
			print "-> \033[31mErro no Proxy\033[0m"
			
			try:
				proxy = proxies[proxies.index(proxy)+1]
				continue
			except IndexError:
				print "-> Todos os Proxies testados"			
				break
			else:
				continue
		print
		for div in divs:
			try:
				div = div.split('href="/url?q=')[1]
				div = div.split('&amp;')[0]
				print '\033[32m'+ div + '\033[0m'
			except:
				continue
		break
	
	except AttributeError:
		break
	except IndexError:
		proxy = proxies[proxies.index(proxy)+1]
		continue
	except Exception as erro:
		error = str(type(erro))
		print "-> \033[31m" + error.split("<class 'requests.exceptions.")[1].split("'>")[0] + "\033[0m"
		proxy = proxies[proxies.index(proxy)+1]
		continue
