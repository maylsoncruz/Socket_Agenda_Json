import json
from socket import *

serverName = 'localhost'
serverPort = 12345
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))


while True:
	opcao = input("Selecione uma opcao:\n1. Novo contato\n2. Ver contatos\n")

	
	if int(opcao) == 1:
		nome = input("Nome: ")
		ddd = input("DDD: ")
		numero = input("Numero: ")
		email = input("Email: ")
		#salvando em um json, a mensagem
		mensagem = {
			'opcao':opcao,
			'Nome': nome,
			'DDD':ddd,
			'Numero':numero,
			'Email':email,
		}
		#transforma json em uma string
		mensagemstr = json.dumps(mensagem)
		#envia a string mensagemstr
		clientSocket.send(mensagemstr.encode(encoding='utf-8'))
		print ("Preparando pra enviar")
		#recebe o contato do servidor
		contato = clientSocket.recv(1024)

	elif int(opcao) == 2:
		mensagem = {
			'opcao':opcao,
		}
		#transforma json em uma string
		mensagemstr = json.dumps(mensagem)
		#envia a string mensagemstr
		clientSocket.send(mensagemstr.encode(encoding='utf-8'))
		print ("Preparando pra enviar")
		#recebe o contato do servidor
		contato = clientSocket.recv(1024)
		# pega a string contato e converte para json (json.loads(contato))
		lista = json.loads(contato)
		#percorre a lista, para imprimir cada contato
		print("Agenda\n")
		for comp in lista:
			print("Nome:" + comp['nome'] + '\n' + "DDD:" + comp['ddd'] + '\n' +"Numero:" + comp['numero'] + '\n' +"Email:" + comp['email'] + '\n')

	
	
clientSocket.close()
