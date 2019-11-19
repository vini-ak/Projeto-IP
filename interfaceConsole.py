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
while quantFilas > 20 and :
	print('Inválido. O cinema não tem mais de 20 filas.')
	quantFilas = int(input("Informe o número de linhas: "))


# CONTROLADOR DE ASSENTOS:
controlador = controladorAssentos.ControladorAssentos()


for i in range(quantFilas * quantColunas):
	# Definindo um novo assento:
	novoAssento = Assento('%02d' % i)

	fila = i // quantColunas	# definindo a fila que a cadeira pertence
	novoAssento.setPreco(fila)	# definindo o PREÇO DO INGRESSO a partir da fila onde a cadeira está

	# Adicionando a cadeira à lista de assentos.
	controlador.adicionaCadeira(novoAssento)


while True:
	escolha = menu()

	# Se o usuário escolheu a quarta opção, ele sai do loop.
	if escolha == 4:
		break