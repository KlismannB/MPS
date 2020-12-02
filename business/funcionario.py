# -*- coding: utf-8 -*-

class Funcionario:
	def __init__(self, nome, CPF, cargo, salario):
		self.__nome = nome
		self.__CPF = CPF
		self.__cargo = cargo
		self.__salario = salario

	def getNome(self):
		return self.__nome	
	def getCPF(self):
		return self.__CPF
	def getCargo(self):
		return self.__cargo
	def getSalario(self):
		return self.__salario

	def setCPF(self, CPF):
		self.__CPF = CPF
	def setNome(self, nome):
		self.__nome = nome
	def setCargo(self, cargo):
		self.__cargo = cargo
	def setSalario(self, salario):
		self.__salario = salario

