import json
from socket import *
import _thread
import random

serverPort = 12345
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

arquivo = ('Agenda.txt')
def novoContato(nome, ddd, numero, email, arq):
	contato = {
		'Nome': nome,
		'DDD':ddd,
		'Numero':numero,
		'Email':email,
	}
	
	fw = open(arq, 'ab')
	contato = json.dumps(contato)
	print(contato)
	fw.write(contato.encode())

	return True

def getContato(arq):
	fr = open(arq, 'r')
	tx = fr.readlines()
	list = []
	for cont in tx:
		list.append(json.loads(cont))
	return list


def task(connection, client):
	print (connection)
	print (client)
	id = random.randint(0, 10000)
	while True:
		received = connection.recv(1024)
		print ("servidor recebeu mensagem ", received, " do cliente ", id)
		mensagemjson = json.loads(received)
		mensagemjson['opcao']
		if mensagemjson['opcao']==str(1):
			resultado = novoContato(mensagemjson['Nome'],mensagemjson['DDD'],mensagemjson['Numero'],mensagemjson['Email'], arquivo)
			connection.send(bytes("[]", 'utf-8'))

		elif mensagemjson['opcao']==str(2):
			resultado = getContato(arquivo)
		'''connection.send(bytes(json.dumps(resultado), 'utf-8'))


	connection.close()

print ("Servidor esta esperando")
while 1:
	connection, addr = serverSocket.accept()
	_thread.start_new_thread(task, (connection, addr))
