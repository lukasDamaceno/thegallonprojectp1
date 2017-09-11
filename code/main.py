# -*- coding: latin-1 -*-
import math
def alfabeto(n):
	a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
	n = n-1
	for a in range(0, n):
		yield a[n]
def barra():
	print '-------------------------------------------------------\n'

while True:
	print 'Especifique a quantidade de vertices'	
	try:
		vertices = int(raw_input())
		if vertices >= 1 and vertices <= 10:
				break
	except ValueError:
		print '\nPor favor, não coloque letras aqui'
		barra()

x = 0
v = 1
while True:
	if x == 0:
		print('Entre com o primeiro vertice da aresta v%n. Entre "Z" para encerrar a entrada das arestas' % v)
		opt = raw_input()
		if opt.lower() == 'z': 
			break
		x = 1
	if x == 1:
		print('Entre com o segundo vértice da aresta v%n. Entre com "Z" para encerrar a entrada das arestas' % v)
		opt = raw_input()
		if opt.lower() == 'z': 
			break
		x = 0

print 'caboooo'		