from infra.LoginException import *
from infra.SenhaException import *

def validaLogin(login):
	try:
		if(len(login) > 20):
			raise LoginGrandeException()
		elif(len(login) == 0):
			raise LoginVazioException()
		elif(any(char.isdigit() for char in login)):
			raise LoginComDigitoException()
	except (LoginGrandeException):
		print("\nO login tentado possui mais de 20 caracteres")
		print("Não foi possível cadastrar seu login")
		return -1
	except (LoginVazioException):
		print("\nO login tentado é vazio")
		print("Não foi possível cadastrar seu login")
		return -2
	except (LoginComDigitoException):
		print("\nO login tentado possui digito numérico")
		print("Não foi possível cadastrar seu login")
		return -3

def validaSenha(senha):
	try:	
		if(len(senha) > 12):
			raise SenhaGrandeException()
		elif(len(senha) < 8):
			raise SenhaPequenaException()
		elif(not(senha.isdigit())):
			raise SenhaSemLetraException()
		else:
			for char in senha:
				if(char.isdigit()):
					numeros += 1

			if(numeros == 1):
				raise SenhaSemDoisDigitosException()
	except (SenhaGrandeException):
		print("A sua senha não pode conter mais de 12 caracteres")
		print("Não foi possível cadastrar sua senha")
		return -4
	except (SenhaPequenaException):
		print("A sua senha não pode conter menos de 8 caracteres")
		print("Não foi possível cadastrar sua senha")
		return -5
	except (SenhaSemLetraException):
		print("A sua senha deverá conter ao menos uma letra")
		print("Não foi possível cadastrar sua senha")
		return -6
	except (SenhaSemDoisDigitosException):
		print("Sua senha deve conter no mínimo 2 números")
		print("Não foi possível cadastrar sua senha")
		return -7