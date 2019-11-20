#!/usr/bin/python
# -*- coding: utf-8 -*-

from controladorAssentos import ControladorAssentos
import os
import time

def clear():
	''' Função para limpar a tela do console. '''
	if os.name == 'nt':	# Será executado caso o sistema seja Windows
		return os.system('cls')
	else:	# Será executado para mac e linux.
		return os.system('clear')


def menu():
	''' Menu de apresentação do sistema. '''
	print("\nBem vindo ao sistema de venda de ingressos")
	print("Escolha a operação:")
	print("1 - Comprar ingressos")
	print("2 - Devolver ingressos")
	print("3 - Resumo das vendas")
	print("4 - Sair")
	escolha = int(input("Digite sua escolha: "))
	clear()
	return escolha


quantFilas = int(input("Informe o número de linhas: "))
quantColunas = int(input("Informe o número de colunas: "))


# O cinema não pode ter mais do que 20 filas, portanto há uma restrição.
while quantFilas > 20:
	print('Inválido. O cinema não tem mais de 20 filas.')
	quantFilas = int(input("Informe o número de linhas: "))

# CONTROLADOR DE ASSENTOS:
controlador = ControladorAssentos(quantColunas, quantFilas)

# CRIANDO OS ARQUIVOS:
cadeiras = open('cadeiras.txt', 'a+')	# criando/editando arquivo cadeiras.txt
resumo = open('resumo.txt', 'a+')	# criando/editando arquivo cadeiras.txt


for i in range(quantFilas * quantColunas):
	
	# Adicionando a cadeira à lista de assentos.
	controlador.adicionaCadeira('%02d' % i)

	# Escrevendo a cadeira no arquivo cadeiras.txt
	cadeiras.write('%02d' % i)

	if i % quantColunas == 0:
		cadeiras.write('\n')
	else:
		cadeiras.write(' ')


cadeiras.close()
resumo.close()

while True:
	escolha = menu()

	# Chamada para a opção de comprar ingresso
	if escolha == 1:
		controlador.comprarCadeiras()
	# Opção para caso o cliente queira devolver o ingresso
	elif escolha == 2:
		controlador.devolverIngressos()
	# Chamada para caso o "gerente" queira imprimir o resumo das vendas.
	elif escolha == 3:
		controlador.resumo()
	# Se o usuário escolheu a quarta opção, ele sai do loop.
	elif escolha == 4:
		break
	else:
		print('Opção inválida.')

	time.sleep(0.5)	# Tempo para dar um refresh...
	clear()	# Limpando a tela.