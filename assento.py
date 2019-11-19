class Assento:
	def __init__(self, numero, preco = 20, disponivel = True):
		self._numero = numero
		self._preco = preco
		self._disponivel = disponivel

	def getNumero(self):
		return self._numero

	def setNumero(self, novo_numero):
		self._numero = novo_numero

	def getPreco(self):
		return self._preco

	def setPreco(self, fila):
		self._preco = 20 - fila

	def getDisponivel(self):
		return self._disponivel

	def setDisponivel(self):
		self._disponivel = not self._disponivel 