# -*- coding: utf-8 -*-

from business.model.funcionario import *

class Vendedor(Funcionario):
	def __init__(self, nome, cpf, cargo = "vendedor", salario = 1064.23):
		super().__init__(nome, cpf, cargo, salario)

	def getDados(self):
		print("Nome: " + self.getNome() + 
			"\nCPF: " + self.getCPF() + 
			"\nCargo: "	+ self.getCargo() + 
			"\nSalario: " + str(self.getSalario()))
