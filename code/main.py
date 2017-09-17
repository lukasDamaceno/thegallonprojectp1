# -*- coding: latin-1 -*-
#IA monstrona pra percorrer um grafo
#Autor: emão z1k4 (tenho que mudar o nome antes de entregar)
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
		for i2 in range(0, i):
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
#preenche matriz de adjs de acordo com a aresta passada por parâmetro
def preencheAdj(grafo, adj, v1, v2):
	#procura os vértices no grafo e retorna a posição deles na matris de adjs
	x, a = procuraVertice(grafo, v1, True)
	y, b = procuraVertice(grafo, v2, True)

	#itera sobre o grafo e testa para diagonalidade (vizinhos horizontais e diagonais retornam o mesmo valor)
	for g in grafo:
		for i, l in enumerate(g):
			if l == v1:
				i1 = i
			if l == v2:
				i2 = i
		d = True

	#atribui o valor proprio para a aresta (raiz(2) para diagonais e 1 para verticais e horizontais)
	if i1 - i2 == 1 and d:
		val = math.sqrt(2) 
	elif i1 - i2 == -1 and d:
		val = math.sqrt(2)
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
			print 'Aresta já existente'
			pause()
		#caso contrario preenche a matriz com seu respectivo valor em seu respectivo lugar
		else:
			adj[x][y] = val
	else:
		if adj[y][x] > 0:
			print 'Aresta já existente'
			pause()
		else:
			adj[y][x] = val
	#retorna a matriz atualizada com a aresta
	return adj


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
			barra()
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
			barra()
		else:
			opt2 = opt
			break
	#enquanto o lock estiver trancado
	if not sair:
		#checa se a vizinhança entre as duas opções é real
		if checaVizinho(grafo, opt1, opt2):
			print ''
			#prompta o usuário á confirmar a aresta
			opt = raw_input('Aresta é v'+str(v)+'('+opt1+', '+opt2+'). Entre "S" para confirmar ou "N" para descartar. Entre com "Z" para encerrar: ')
			#se o usuário entrar com z encerra a rotina das arestas
			if opt.lower() == 'z':
				sair = True
				break
			#caso entre com s preenche a matriz de adjs no lugar correto
			if opt.lower() == 's':
				os.system('clear')
				adjs = preencheAdj(grafo, adjs, opt1, opt2)
				#printa a matriz só pra teste
				printaGrafo(adjs)
				#variavel usada para notificar o usuário que a aresta é outra
				v += 1
		#avisa o usuário caso os vértices não sejam vizinhos
		else:
			os.system('clear')
			print 'Vertices "'+opt1+'"" e "'+opt2+ '" não são vizinhos.'
			
