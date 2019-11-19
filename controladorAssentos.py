import assento

class ContraladorAssentos:
	def __init__(self, comprimentoFila, totalFilas):
		self.__listaAssentos = []
		self._status = open('cinema.txt', 'a+')	# Status das cadeiras do cinema
		self._comprimentoFila = comprimentoFila
		self._totalFilas = totalFilas
		self._saldo = 0

	def getListaAssentos(self):
		''' Retorna a lista de assentos. '''
		return self.__listaAssentos

	def adicionaCadeira(self, cadeira):
		''' Adiciona uma cadeira à lista de assentos.'''
		self.getListaAssentos().append(cadeira)

	def getCadeira(self, cadeira):
		''' Retorna uma cadeira. '''
		return self.__getListaAssentos()[int(cadeira)]

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

	# STATUS DAS CADEIRAS:
	def getStatus(self):
		''' Retorna o status das cadeiras. '''
		return self._status

	def statusCinema(self):
		''' Retorna o status das cadeiras do cinema. '''
		for linha in self.getStatus().readlines():
			print(linha)

	def comprarCadeira(self):
		''' Método que será chamado quando um usuário quiser 
		comprar cadeiras. '''
		self.statusCinema()

		cadeiras = input("\nQuais cadeiras você deseja comprar? ").split(',')



