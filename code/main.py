# -*- coding: latin-1 -*-
#IA monstrona pra percorrer um grafo
import math
import os

os.system('clear')

#retorna uma letra do alfabeto no índice dado por parâmetro
def alfabeto(n):
	a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
	return a[n]

#printa uma par de barra
def barra():
	print '-------------------------------------------------------'


#gera a matriz de adjacências nula baseada no tamanho do grafo
def matrizAdj(x):
	#declara uma sublista (linha) e uma superlista (matriz) (entenda sublista como a lista que irá entrar dentro de uma outra lista)
	m=[]
	M=[]
	#itera pela variavel de controle (i) de 0 até o número de vértices passado por parâmetro (x)
	for i in range(0, x):
		#itera pela segunda variavel de controle (i2) de 0 até i e empurra 0 no final da lista pelo número de vezes
		#igual a coluna que está sendo iterada (i), de modo que se gere a matriz de adjacências reduzida
		for i2 in range(0, i+1):
			m.append(0)
		#empurra a sublista na superlista de forma que se faça uma lista de linhas e colunas (ou matriz, se preferir)
		M.append(m)
		#zera a sublista para que possa se fazer a proxima linha
		m =[]
	#retorna a matriz
	return M

#pausa a execução e prompta o usuário á apertar enter (á ser testado)
def pause():
	print ''
	raw_input('Pressione Enter para continuar...')

#gera o grafico de 2 linhas e n colunas (1 >= n >= 10)
#também chama o método que cria a matriz de adjacências e o retorna (teste de retorno múltiplo, opcional)
def geraGrafo(x):
	#declara as linhas (sublistas l1, l2) e a matriz que irá formar o grafo com as duas linhas (superlista g)
	g = []
	l1 = []
	l2 = []
	#chama a função que gera a matriz de adjs e joga na variavel abaixo
	m = matrizAdj(x)
	#itera pelo número de vértices passado por parâmetro
	for i in range(0, x):
	#termina uma linha e começa a outra caso a contagem supere a metade do número de vértices
		if i >= x/2:
			l1.append(alfabeto(i))
		else:
			l2.append(alfabeto(i))

	#empurra as linhas na matriz do grafo
	g.append(l2)
	g.append(l1)
	#retorna o grafo e a matriz de adjs
	return g, m

#printa o grafo ou matriz formatada e bonitonha
def printaGrafo(grafo):
	for g in grafo:
		for i, l in enumerate(g):
			print l,
			if i == len(g) - 1:
				print ''


def printaAdj(adj):
	fim = len(adj[len(adj) -1])
	print '  ',
	for b in range(0, fim):
		print alfabeto(b)+' ',
	print ''
	for i1, a in enumerate(adj):
		for i2, l in enumerate(a):
			if i2 == 0:
				print alfabeto(i1)+' ',
			if l == math.sqrt(2):
				print '√2',
			else:
				print l,
				print '',
			if i2 == len(a) - 1:
				print ''

#itera sobre as linhas do grafo e procura pelo vértice passado por parâmetro
def procuraVertice(grafo, elem, v=False):
	c = 0
	for g in grafo:
		for l in g:
			#caso existente retorna True, caso contrario retorna False
			if elem == l:
				#caso você confirme a opção v a função também retorna o contador incrementado continuamente a cada iteração em um elemento de qualquer linha (necessario para preencher a matriz de adjs)
				if v:
					return c, True
				else: 
					return True
			c +=1
	return False

def getCoord(grafo, elem):
	c = 0
	for g in grafo:
		for l in g:
			if elem == l:
				return c
			c +=1

#itera sobre o grafo checa se os dois vértices passados por parâmetro são vizinhos (necessário para estabelecer uma aresta)
def checaVizinho(grafo, v1, v2):
	for g in grafo:
		for i, l in enumerate(g):
			if l == v1:
				i1 = i
			if l == v2:
				i2 = i

	#subtrai os índices e caso a diferença deles bata com os testes abaixo significa que são vizinhos
	#vizinhos horizontais ou diagonais podem retornar -1 e 1
	#vizinhos verticais retornam 0
	#retorna verdadeiro se passarem no teste
	if i1 - i2 == 0 or i1 - i2 == 1 or i1 - i2 == -1:
		return True
	else:
		return False


def checaDiag(grafo, v1, v2):
	#itera sobre o grafo e testa para diagonalidade (vizinhos horizontais e diagonais retornam o mesmo valor)
	i1 = -1
	i2 = -1
	d1 = 0
	d2 = 0
	e1 = 0
	e = 0
	for e1, g in enumerate(grafo):
		for e, l in enumerate(g):
			if l == v1:
				i1 = e
				d1 = e1
			if l == v2:
				i2 = e
				d2 = e1
	
	if d1 != d2:
		return i1, i2, True
	else:
		return i1, i2, False

#preenche matriz de adjs de acordo com a aresta passada por parâmetro
def preencheAdj(grafo, adj, v1, v2):
	#procura os vértices no grafo e retorna a posição deles na matris de adjs
	x = getCoord(grafo, v1)
	y = getCoord(grafo, v2)

	i1, i2, d = checaDiag(grafo, v1, v2)

	#atribui o valor proprio para a aresta (raiz(2) para diagonais e 1 para verticais e horizontais)

	if i1 - i2 == 1 and d:
		val = math.sqrt(2)
		# val = 2 
	elif i1 - i2 == -1 and d:
		val = math.sqrt(2)
		# val = 2
	elif i1 - i2 == 0:
		val = 1
	elif i1 - i2 == 1: 
		val = 1
	elif i1 - i2 == -1:
		val = 1

	#teste que impossibilita erro de índice caso o usuário coloque o vértice mais distante antes do mais proximo quando requisitado
	if y < x:
		#testa se aresta ja foi colocada antes
		if adj[x][y] > 0:
			return False, adj
		#caso contrario preenche a matriz com seu respectivo valor em seu respectivo lugar
		else:
			adj[x][y] = val
	else:
		if adj[y][x] > 0:
			return False, adj
		else:
			adj[y][x] = val
	#retorna a matriz atualizada com a aresta
	return True, adj

#printa grafo com as arestas desenhadas
def grafoFormatado(grafo, adj):
	pass


#prompta o usuário com a quantidade de vértices que queira usar
while True:	
	try:
		vertices = int(raw_input('Especifique a quantidade de vertices: '))
		#testa se está dentro do valor permitido
		#caso esteja o laço de repetição é quebrado, ao contrario, se repete a rotina
		if vertices >= 1 and vertices <= 20:
			print ''
			break
	#obriga o usuário á colocar um número
	except ValueError:
		print 'Por favor, não coloque letras aqui\n'

#chama a função para gerar o grafo e a matriz de adjs
grafo, adjs = geraGrafo(vertices)
#imprime o grafo na tela
printaGrafo(adjs)

#inicializa o contador global das arestas
v = 1
#habilita a trava do laço
sair = False
#limpa a tela
os.system('clear')

arestas = {}
#repete enquanto o lock estiver trancado
while not sair:
	#caso não haja vértices suficientes para percorrer, termina-se a execução
	if len(grafo[0]) <= 1:
		os.system('clear')
		print 'Não existem vértices suficientes para percorrer'
		quit()
	#prompta o usuário a dar o primeiro vértice da aresta n
	while True:
		barra()
		printaGrafo(grafo)
		barra()
		prompt = 'Entre "Z" para encerrar a entrada das arestas. \nEntre com o primeiro vértice da aresta v'+ str(v) +': '
		opt = raw_input(prompt)
		#caso entre com "z" libera o lock do superlaço e quebra o laço presente
		if opt.lower() == 'z':
			sair = True 
			break
		#caso não se encontre o vértice entrado repete-se a rotina
		if not procuraVertice(grafo, opt):
			os.system('clear')
			print 'Vértice não encontrado.'
		#caso seja encontrado, grava a opção desejada e quebra o laço
		else:	
			opt1 = opt
			break
	#rotina igual a de cima, só que para o segundo vértice da aresta
	while True:
		#caso o lock seja desabilitado, quebra a o laço e sai da rotina
		if sair:
			break
		os.system('clear')
		barra()
		printaGrafo(grafo)
		barra()
		prompt = 'Entre "Z" para encerrar a entrada das arestas.\nEntre com o segundo vértice da aresta v'+ str(v) +': '
		opt = raw_input(prompt)
		if opt.lower() == 'z':
			sair = True
			break
		if not procuraVertice(grafo, opt):
			os.system('clear')
			print 'Vértice não encontrado.'
		else:
			opt2 = opt
			os.system('clear')
			break
	#enquanto o lock estiver trancado
	if not sair:
		#checa se a vizinhança entre as duas opções é real
		if checaVizinho(grafo, opt1, opt2):
			check, adjs = preencheAdj(grafo, adjs, opt1, opt2)

			if not check:
				os.system('clear')

				print 'Aresta já existente.'
			else:
				arestas['v'+str(v)] = [opt1, opt2]
				#variavel usada para notificar o usuário que a aresta é outra
				v += 1
		#avisa o usuário caso os vértices não sejam vizinhos
		else:
			os.system('clear')
			print 'Vertices "'+opt1+'"" e "'+opt2+ '" não são vizinhos.'
		
os.system('clear')
while True:
	barra()
	printaGrafo(grafo)
	barra()
	inicio = raw_input('Selecione o ponto inicial: ')
	if procuraVertice(grafo, inicio):
		break
	else:
		os.system('clear')
		print 'Vértice não encontrado.'
		barra()

while True:
	barra()
	printaGrafo(grafo)
	barra()
	final = raw_input('Selecione o ponto final: ')
	if procuraVertice(grafo, inicio):
		break
	else:
		os.system('clear')
		print 'Vértice não encontrado.'

def geraLAberturas(v):
	ab = {}
	for i1, g in enumerate(adjs):
		for i2, l in enumerate(g):
			if l > 0:
				if alfabeto(i1) not in ab:
					ab[alfabeto(i1)] = True
				if alfabeto(i2) not in ab:
					ab[alfabeto(i2)] = True
					
	return ab

def geraLAntecessores(v):
	ant = {}
	for i1, g in enumerate(adjs):
		for i2, l in enumerate(g):
			if l > 0:
				if alfabeto(i1) not in ant:
					ant[alfabeto(i1)] = None
				if alfabeto(i2) not in ant:
					ant[alfabeto(i2)] = None
	return ant

def geraLRelax(v):
	rel = {}
	for i1, g in enumerate(adjs):
		for i2, l in enumerate(g):
			if l > 0:
				if alfabeto(i1) not in rel:
					rel[alfabeto(i1)] = 999999999
				if alfabeto(i2) not in rel:
					rel[alfabeto(i2)] = 999999999
	return rel

def relax(peso, v1, v2):
	#print v1
	#print v2
	if relaxVal[v1] + peso < relaxVal[v2]:
		relaxVal[v2] = relaxVal[v1] + peso
		listaAnt[v2] = v1



def fecha(ab, key):
	ab[key] = False
	return ab

def isAberto(ab, key):
	if ab[key]:
		return True
	else:
		return False

def checaAbertura(ab, get=False):
	for key in ab:
		if ab[key] == True:
			if not get:
				return True
			else:
				return key

def procuraVerticePorCount(grafo, c):
	cr = 0
	for g in grafo:
		for l in g:
			if c == cr:
				return l
			cr += 1

def getMenor(rel, ab):
	abertos = {}
	for key in rel:
		if isAberto(ab, key):
			abertos[key] = rel[key]

	menor = min(abertos.itervalues())
	for key in abertos:
		if abertos[key] == menor:
			return key 
	return False

def showCaminho(ant, inicio, fim):
	at = fim
	cam = []
	cam.append(fim)
	while True:
		if ant[at] == None:
			if at != inicio:
				return None, False
			else:
				break
		at = ant[at]
		cam.append(at)
		if at == inicio:
			break
	l = []
	for i in reversed(cam):
		l.append(i)
	return l, True

def getDistancia(fim, rel):
	return rel[fim]

def getManhattan(inicio, fim, grafo):
	x=[]
	y=[]
	for e1, g in enumerate(grafo):
		for e, l in enumerate(g):
			if l == inicio or l == fim:
				x.append(e)
				y.append(e1)

	xx = modulo(x[0] - x[1])
	yy = modulo(y[0] - y[1])
	a = xx + yy
	return a

def modulo(numero):
	if numero < 0:
		return numero * -1
	else:
		return numero

listaAb = geraLAberturas(vertices)
listaAnt = geraLAntecessores(vertices)
relaxVal = geraLRelax(vertices)



if inicio == final:
	os.system('clear')
	print 'Caminho: '+final
	print 'Distância percorrida: 0'
	print 'Distância Manhattan: 0'
	print 'Matriz de adjacências minimizada: '
	printaAdj(adjs)
	print 'Algoritmo usado: Dijkstra'
else:
	somaCaminho = 0
	relaxVal[inicio] = 0
	while checaAbertura(listaAb) and isAberto(listaAb, final):
		atual = getMenor(relaxVal, listaAb)
		fecha(listaAb, atual)
		coord = getCoord(grafo, atual)
		i2= 0
		i= 0
		for i, g in enumerate(adjs):

			# print 'index', i
			# print 'coord', coord

			# if i == coord:
			# 	if adjs[i][coord - 1] > 0:
			# 		proxPeso = adjs[i][coord - 1]
			# 		prox = procuraVerticePorCount(grafo, coord - 1)
			# 		if isAberto(listaAb, prox):
			# 			relaxVal[prox] = relax(relaxVal, proxPeso, atual, prox)
			# 			listaAnt[prox] = atual
			# 			print 'fez', prox

			# if i > coord:
			# 	if adjs[i][coord] > 0:
			# 		proxPeso = adjs[i][coord]
			# 		prox = procuraVerticePorCount(grafo, i)
			# 		if isAberto(listaAb, prox):
			# 			if prox == 'e': print 'CHEOGO PORRA VAI FAZE SIM'
			# 			relaxVal[prox] = relax(relaxVal, proxPeso, atual, prox)
			# 			listaAnt[prox] = atual
			# 			print 'fez ', prox


			try:
				for i2, l in enumerate(g):
					if i == coord:
						if l > 0:
							proxPeso = l
					 		prox = procuraVerticePorCount(grafo, i2)
					 		if isAberto(listaAb, prox):
					 			# listaAb[prox], relaxVal[prox] = relax(relaxVal, proxPeso, atual, prox)
					 			relax(proxPeso, atual, prox)

					elif i2 == coord:
						if l > 0:
							proxPeso = l
							prox = procuraVerticePorCount(grafo, i)
							if isAberto(listaAb, prox):
								# listaAb[prox], relaxVal[prox] = relax(relaxVal, proxPeso, atual, prox)
					 			relax(proxPeso, atual, prox)

			except IndexError:
				pass

	printaGrafo(grafo)

	caminho, achou = showCaminho(listaAnt, inicio, final)

	if not achou:
		os.system('clear')
		print 'Inicial e final em árvores diferentes. Caminho impossível.'
	else:
		os.system('clear')
		print 'Algoritmo usado: Dijkstra'
		print 'Caminho:', caminho
		print 'Distância percorrida:'+str(getDistancia(final, relaxVal))
		print 'Distância Manhattan:', getManhattan(inicio, final, grafo)
		print 'Lista de arestas:', arestas
		print 'Matriz de adjacências minimizada: '
		printaAdj(adjs)
		print ''