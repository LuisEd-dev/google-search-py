import requests
import random

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

consulta = raw_input("Pesquisa >>> ")
num = input("Numero de resultados: ")
pagina = 0

while True:
	useragent = y[random]
	try:
		print (">_ Usando proxy %s " % proxy),
		headers = {'User-Agent': useragent}
		parametros = {'q' : consulta, 'start':pagina, 'num':num }
		resposta = requests.get('http://www.google.com/search', params=parametros, timeout = 20, headers=headers, proxies={"http" : proxy}) #
		msg = "Our systems have detected unusual traffic from your computer network"
		msg2 = "support.google.com/websearch/answer"
		if msg in resposta.text or msg2 in resposta.text:
			print "O Google detectou o bot..."
			try:
				proxy = proxies[proxies.index(proxy)+1]
				continue
			except IndexError:
				print ">_ Todos os Proxies testados"			
				break
			else:
				continue
		divs = resposta.text
		divs = divs.split('<div><a class="')
		if len(divs) == 0:
			print "!! Erro no Proxy"
			
			try:
				proxy = proxies[proxies.index(proxy)+1]
				continue
			except IndexError:
				print ">_ Todos os Proxies testados"			
				break
			else:
				continue
		print
		for div in divs:
			
			div = div.split('href="')[1];
			div = div.strip('/url?q=');
			div = div.split('&amp;')[0] 
			div = div.strip('num=%s' % num)
			#div = div.strip('aclk?sa=l')
			if 'http' in div: 
				print div
			else: 
				print "!! Erro no Proxy"
			#	continue
			#break
		#else:
			#proxy = proxies[proxies.index(proxy)+1]
			#continue		
		break
		
	except requests.exceptions.ConnectTimeout:
		try:
			print 'Timed Out...'
			proxy = proxies[proxies.index(proxy)+1]
			continue
		except IndexError:
			print ">_ Todos os Proxies testados"			
			break
		else:
			continue
	except requests.exceptions.ProxyError:
		try:
			proxy = proxies[proxies.index(proxy)+1]
			continue
		except IndexError:
			print ">_ Todos os Proxies testados"			
			break
		else:
			continue
	except requests.exceptions.ConnectionError:
		try:
			proxy = proxies[proxies.index(proxy)+1]
			continue
		except IndexError:
			print ">_ Todos os Proxies testados"			
			break
		else:
			continue
	except requests.exceptions.ReadTimeout:
		try:
			print 'Timed Out...'
			proxy = proxies[proxies.index(proxy)+1]
			continue
		except IndexError:
			print ">_ Todos os Proxies testados"			
			break
		else:
			continue
	except requests.exceptions.TooManyRedirects:
		try:
			proxy = proxies[proxies.index(proxy)+1]
			continue
		except IndexError:
			print ">_ Todos os Proxies testados"			
			break
		else:
			continue
	except AttributeError:
		break
	except IndexError:
		proxy = proxies[proxies.index(proxy)+1]
		continue
	except Exception as e:
		print type(e)
		proxy = proxies[proxies.index(proxy)+1]
		continue
