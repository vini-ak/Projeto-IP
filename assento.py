#!/usr/bin/python
# -*- coding: utf-8 -*-

class Assento:
	def __init__(self, numero, fila, preco = 20, disponivel = True):
		self._numero = numero
		self._fila = fila
		self._preco = preco - fila
		self._disponivel = disponivel

	def getNumero(self):
		return self._numero

	def setNumero(self, novo_numero):
		self._numero = novo_numero

	def getPreco(self):
		return self._preco

	def getFila(self):
		return self._fila

	def getDisponivel(self):
		return self._disponivel

	def setDisponivel(self):
		self._disponivel = not self._disponivel 