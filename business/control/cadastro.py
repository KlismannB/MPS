# -*- coding: utf-8 -*-

from business.model.funcionario import *
from business.control.validaCadastro import *

def cadastrarVendedor():
	numeros = 0

	print("Digite seu nome: ", end="")
	nome = input()
	print("Digite seu cargo: ", end="")
	cargo = input()
	print("Digite seu CPF: ", end="")
	CPF = input()
	print("Digite um login para sua conta: ", end="")
	login = input()
	validaLogin(login)
	print("Digite uma senha para sua conta: ", end="")
	senha = input()
	validaSenha(senha)
	print("Cadastro realizado com sucesso!")