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
	print("\nEscolha a operação:")
	print("1 - Comprar ingressos")
	print("2 - Devolver ingressos")
	print("3 - Resumo das vendas")
	print("4 - Sair")
	escolha = int(input("\nDigite sua escolha: "))
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

# ==================== CRIANDO OS ARQUIVOS CASO ELES NÃO EXISTAM ==========================


try:	# CRIANDO O ARQUIVO 'resumo.txt' CASO ELE NÃO EXISTA
	resumo = open('resumo.txt')
except:
	resumo = open('resumo.txt', 'a+')	# criando/editando arquivo cadeiras.txt
resumo.close()


try:	# CRIANDO O ARQUIVO 'cadeiras.txt' CASO ELE NÃO EXISTA
	cadeiras = open('cadeiras.txt')
	cadeiras.close()

except:
	total_cadeiras = quantFilas * quantColunas
	cadeiras = open('cadeiras.txt', 'w')	# criando arquivo cadeiras.txt

	for i in range(total_cadeiras):
		# Adicionando a cadeira à lista de assentos.
		controlador.adicionaCadeira('%02d' % i)

		if i % quantColunas != 0 or i == 0:
			# Escrevendo a cadeira no arquivo cadeiras.txt
			cadeiras.write('%02d' % i)
			cadeiras.write(' ')
		else:
			cadeiras.write('\n')
			# Escrevendo a cadeira no arquivo cadeiras.txt
			cadeiras.write('%02d' % i)
			cadeiras.write(' ')
	cadeiras.close()


total_cadeiras = quantFilas * quantColunas
for j in range(total_cadeiras):
	# Adicionando a cadeira à lista de assentos.
	controlador.adicionaCadeira('%02d' % j)


while True:
	escolha = menu()
	time.sleep(1)

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

	time.sleep(1.5)	# Tempo para dar um refresh...
	clear()	# Limpando a tela.