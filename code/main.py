# -*- coding: latin-1 -*-
import math
import os

os.system('clear')

#retorna uma letra do alfabeto no índice
def alfabeto(n):
	a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't']
	return a[n]

def barra():
	print '-------------------------------------------------------'

def matrizAdj(x):
	m=[]
	M=[]
	for i in range(1, x+1):
		for i2 in range(0, i):
			m.append(0)
		M.append(m)
		m =[]
	return M

def pause():
	print ''
	os.system('read -n1 -r -p "Pressione qualquer tecla para continuar"')

def geraGrafo(x):
	g = []
	l1 = []
	l2 = []
	m = matrizAdj(x)
	for i in range(0, x):
		if i >= x/2:
			l1.append(alfabeto(i))
		else:
			l2.append(alfabeto(i))

	
	g.append(l2)
	g.append(l1)
	return g, m

def printaGrafo(grafo):
	for g in grafo:
		for i, l in enumerate(g):
			print l,
			if i == len(g) - 1:
				print ''

def procuraVertice(grafo, elem, v=False):
	c = 0
	for g in grafo:
		for l in g:
			if elem == l:
				if v:
					return c, True
				else: 
					return True
			c +=1
	return False

def checaVizinho(grafo, v1, v2):
	for g in grafo:
		for i, l in enumerate(g):
			if l == v1:
				i1 = i
			if l == v2:
				i2 = i

	if i1 - i2 == 0 or i1 - i2 == 1 or i1 - i2 == -1:
		return True
	else:
		return False

def preencheAdj(adj, v1, v2):
	x, a = procuraVertice(grafo, v1, True)
	y, b = procuraVertice(grafo, v2, True)

	if y < x:
		if adj[x][y] != 1:
			print 'Aresta já existente'
			pause()
		else:
			adj[x][y] = 1
	else:
		if adj[y][x] != 0:
			print 'Aresta já existente'
			pause()
		else:
			adj[y][x] = 1
	return adj


while True:	
	try:
		vertices = int(raw_input('Especifique a quantidade de vertices: '))
		if vertices >= 1 and vertices <= 20:
			print ''
			break
	except ValueError:
		print 'Por favor, não coloque letras aqui\n'

grafo, adjs = geraGrafo(vertices)
printaGrafo(adjs)

arestas = []
v = 1
sair = False

while not sair:
	if len(grafo[0]) <= 1:
		os.system('clear')
		print 'Não existem vértices suficientes para percorrer'
		quit()
	c = 0
	while True:
		os.system('clear')
		barra()
		printaGrafo(grafo)
		barra()
		prompt = 'Entre "Z" para encerrar a entrada das arestas. \nEntre com o primeiro vértice da aresta v'+ str(v) +': '
		opt = raw_input(prompt)
		if opt.lower() == 'z':
			sair = True 
			break
		if not procuraVertice(grafo, opt):
			os.system('clear')
			print 'Vértice não encontrado.'
			barra()
		else:	
			opt1 = opt
			break
	while True:
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
			barra()
		else:
			opt2 = opt
			break
	if not sair:
		aresta = [opt1, opt2]
		if checaVizinho(grafo, opt1, opt2):
			print ''
			opt = raw_input('Aresta v'+str(v)+' é ('+opt1+', '+opt2+'). Entre "S" para confirmar ou "N" para descartar. Entre com "Z" para encerrar: ')
			if opt.lower() == 'z':
				break
			if opt.lower() == 's':
				
				adjs = preencheAdj(adjs, opt1, opt2)

				printaGrafo(adjs)
			v += 1
		else:
			print ''
			print 'Vertices "'+opt1+'"" e "'+opt2+ '" não são vizinhos.'
			
