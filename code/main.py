# -*- coding: latin-1 -*-
import math
def alfabeto(n):
	a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
	return a[n]

def barra():
	print '-------------------------------------------------------'

def geraGrafo(x):
	g = []
	l1 = []
	if x > 5:
		l2 = []
	for i in range(0, x):
		if i < 5:
			l1.append(alfabeto(i))
		else:
			l2.append(alfabeto(i))
	if x >= 5:
		g.append(l1)
		g.append(l2)
	else:
		g.append(l1)

	return g

def printaGrafo(grafo):
	for g in grafo:
		for i, l in enumerate(g):
			print l,
			if i == len(g) - 1:
				print ''

def procuraVertice(grafo, elem):
	for g in grafo:
		for l in g:
			if elem in g:
				return True
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




while True:	
	try:
		vertices = int(raw_input('Especifique a quantidade de vertices: '))
		if vertices >= 1 and vertices <= 10:
			print ''
			break
	except ValueError:
		print 'Por favor, não coloque letras aqui\n'

grafo = geraGrafo(vertices)
barra()
print 'Grafo gerado!'
printaGrafo(grafo)
barra()
print ''

arestas = []
v = 1
sair = False

while not sair:
	if len(grafo[0]) == 1:
		print 'Não existem vértices suficientes para percorrer'
		quit()
	c = 0
	while True:
		prompt = 'Entre "Z" para encerrar a entrada das arestas.\nEntre "V" para mostrar o grafo.\nEntre com o primeiro vértice da aresta v'+ str(v) +': '
		opt = raw_input(prompt)
		if opt.lower() == 'z':
			sair = True 
			break
		if opt.lower() == 'v':
			barra()
			printaGrafo(grafo)
			barra()
		elif not procuraVertice(grafo, opt):
			print 'Vértice não encontrado.'
		else:
			opt1 = opt
			break
	while True:
		if sair:
			break
		prompt = '\nEntre "Z" para encerrar a entrada das arestas.\nEntre "V" para mostrar o grafo\nEntre com o segundo vértice da aresta v'+ str(v) +': '
		opt = raw_input(prompt)
		if opt.lower() == 'z':
			sair = True
			break
		if opt.lower() == 'v':
			barra()
			printaGrafo(grafo)
			barra()
		elif not procuraVertice(grafo, opt):
			print 'Vértice não encontrado.'
		else:
			opt2 = opt
			break
	if not sair:
		aresta = [opt1, opt2]
		if checaVizinho(grafo, opt1, opt2):
			print ''
			opt = raw_input('Aresta v'+str(v)+' é ('+opt1+', '+opt2+'). Entre "S" para confirmar ou "N" para descartar. Entre com "Z" para encerrar.')
			if opt.lower() == 'z':
				break
			if opt.lower() == 's':
				
				arestas.append(aresta)
			v += 1
		else:
			print ''
			print 'Vertices "'+opt1+'"" e "'+opt2+ '" não são vizinhos.'
		barra()
