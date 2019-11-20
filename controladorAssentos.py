#!/usr/bin/python
# -*- coding: utf-8 -*-

from assento import Assento
import time

class ControladorAssentos:
	def __init__(self, comprimentoFila, totalFilas):
		self.__listaAssentos = {}
		self._comprimentoFila = comprimentoFila
		self._totalFilas = totalFilas
		self._cadeirasOcupadas = 0
		self._saldo = 0
		self._devolvidos = 0

	def getListaAssentos(self):
		''' Retorna a lista de assentos. '''
		return self.__listaAssentos

	def getComprimentoFila(self):
		''' Retorna o comprimento de uma fila. '''
		return self._comprimentoFila

	def getTotalFilas(self):
		''' Retorna o total de filas de um cinema. '''
		return self._totalFilas

	def adicionaCadeira(self, cadeira):
		''' Adiciona uma cadeira à lista de assentos.'''
		fila = int(cadeira) // self.getComprimentoFila()
		self.getListaAssentos()[cadeira] = Assento(cadeira, fila)

	def getCadeira(self, cadeira):
		''' Retorna uma cadeira. '''
		return self.getListaAssentos()[cadeira]

	def isDisponivel(self, cadeira):
		''' Informa se um lugar está disponível ou não. '''
		return self.getCadeira().getDisponivel()

	# SALDO DO CINEMA: 
	def getSaldo(self):
		''' Retorna o saldo do cinema. '''
		return self._saldo

	def alteraSaldo(self, valor):
		''' Modifica o saldo, seja por compra ou devolução.'''
		self._saldo += valor

	# OCUPAÇÃO DOS ASSENTOS:
	def getOcupacao(self):
		''' Retorna a quantidade de assentos ocupados. '''
		return self._cadeirasOcupadas

	def setOcupacao(self, quantidadeLugares):
		''' Altera o número de cadeiras ocupadas '''
		self._cadeirasOcupadas += quantidadeLugares

	# INGRESSOS DEVOLVIDOS:	
	def getDevolvidos(self):
		''' Retorna a quantidade de ingressos devolvidos. '''
		return self._devolvidos

	def setDevolvidos(self, quantidadeLugares):
		''' Altera o número de cadeiras devolvidas. '''
		self._devolvidos += quantidadeLugares

	def comprarCadeiras(self):
		''' Método que será chamado quando um usuário quiser 
		comprar cadeiras. '''
		
		# Chamando o arquivo cadeiras para uma simples leitura.
		arquivo = open('cadeiras.txt')
		arquivo.read()
		filas = arquivo.readlines()
		print(filas)
		arquivo.close()

		# Perguntando quais cadeiras o usuário deseja comprar
		cadeiras = input("\nQuais assentos deseja comprar: ").split(',')
		cont = 0	# Quantidade de cadeiras compradas

		# Verificando a disponibilidade de cada cadeira...
		for c in cadeiras:
			cadeira = self.getCadeira(c)	# Pegando a nó referente à cadeira
			if cadeira.isDisponivel():	# Verifica se a cadeira está disponível para venda.
				self.alteraSaldo(cadeira.getPreco())	# Adicionando o valor da venda da cadeira ao saldo do cinema
				cadeira.setDisponivel()	# Deixando a cadeira indisponível.
				filas[cadeira.getFila()].replace(c, 'xx')

				cont += 1	# Como a cadeira foi comprada, a quantidade de cadeiras compradas será incrementada.

			else:	# Se a cadeira não estiver disponível:
				print('Ops! A cadeira %s não está disponível.' % c)

		self.setOcupacao(cont)	# Alterando o número de cadeiras ocupadas.

		arquivo = open('cadeiras.txt', 'w')
		for fileira in filas:
			arquivo.write(fileira)

		arquivo.close()


	def devolverIngressos(self):
		''' Método que será chamado caso um cliente queira devolver um ingresso. '''

		cadeiras = input("\nQuais assentos deseja devolver: ").split(',')
		cont = 0

		arquivo = open('cadeiras.txt')
		filas = arquivo.readlines()	# Fila de cadeiras
		arquivo.close()

		for c in cadeiras:
			cadeira = self.getCadeira(c)
			if not cadeira.isDisponivel():
				self.alteraSaldo(-(0.9 * cadeira.getPreco()))	# Subtraindo o valor da cadeira do saldo do cinema.
				cadeira.setDisponivel()	# Deixa a cadeira disponível novamente para um venda futura.

				fila = cadeira.getFila()	# Fila a qual a cadeira pertence.
				pos = int(cadeira.getNumero()) % self.getComprimentoFila()	# Posicao de uma cadeira na fila

				filas[fila][3*pos:].replace('xx', c)	# Desocupando a cadeira do cenário

				cont += 1	# Como uma cadeira foi desocupada, o total de cadeiras ocupadas será alterado. Bem como o total de cadeiras devolvidas.

			else:	# Se a cadeira estiver disponível:
				print('Parece que a cadeira %s já está disponível...' % c)

		self.setOcupacao(-cont)	# Alterando o número de cadeiras ocupadas.
		self.setDevolvidos(cont)	# Alterando o total de cadeiras devolvidas.

		arquivo = open('cadeiras.txt', 'w')
		for fileira in filas:
			arquivo.write(fileira)

		arquivo.close()


	def resumo(self):
		''' Método que retorna o resumo de vendas. '''

		arquivo = open('resumo.txt', 'w')

		arquivo.write('Ocupação da sala no momento: %d\n' % self.getOcupacao())
		arquivo.write('Quantidade de ingressos devolvidos: %d\n' % self.getDevolvidos())
		arquivo.write('Valor total apurado: %.02f' % self.getSaldo())

		arquivo.close()

		arquivo = open('resumo.txt')	# Abrindo em modo de leitura
	
		for line in arquivo.readlines():	# Lendo o conteúdo do arquivo pós-alterações
			line.replace('\n', '')	# Para não imprimir o '\n'
			print(line)

		time.sleep(2.5)
		arquivo.close()