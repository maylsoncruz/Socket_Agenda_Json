import json
from socket import *
import _thread
import random

serverPort = 12345
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

#Define o nome do arquivo usado para guardar os dados
arquivo = ('Agenda.txt')
#Funcao para guardar um novo contato
def novoContato(nome, ddd, numero, email, arq):
	#Monta o json(dicionario) que representa o contato que sera guardado em disco
	contato = {
		'Nome': nome,
		'DDD':ddd,
		'Numero':numero,
		'Email':email,
	}
	#Abre o arquivo com nome definido na string fileName passada como parametro no modo 'append' (a) que faz com que o conteudo seja adicionado ao arquivo, e nao apague o arquivo todo ao abrir
	# "a" permite que sejam adicionadas mais textos ao arquivo, sem apagar o que já tem
	# abre o arquivo
	fw = open(arq, 'ab')
	# escreve no arquivo
	# converte (json.dumps(contato)) em uma string
	contato = json.dumps(contato)
	print(contato)
	fw.write(contato.encode())

	return True

def getContato(arq):
	#abre o arquivo e prepara pra leitura
	fr = open(arq, 'r')
	#cada linha do arquivo se transforma em uma string, as strings serão salvas em uma lista
	tx = fr.readlines()
	#lista que guardara o mesmo conteudo da lista anterior (tx), porem ao inves de strings, tera json's ja interpretados
	list = []
	#declara uma variável line, que recebe o conteúdo de tx. A cada iteração, line recebe o conteúdo de tx
	for cont in tx:
		#para cada string (cada linha) de tx, converte em json cont (json.loads(cont)) e adiciona o json resultante em list
		list.append(json.loads(cont))
	#Retorna a lista de json que tem uma facil manipulacao- list[0][descricao]
	#list[posicao do contato][atributo de contato]
	return list


def task(connection, client):
	print (connection)
	print (client)
	id = random.randint(0, 10000)
	while True:
		received = connection.recv(1024)
		print ("servidor recebeu mensagem ", received, " do cliente ", id)
		mensagemjson = json.loads(received)
		#json.loads(json_string) serve pra ler a string e transformá-la em json
		mensagemjson['opcao']
		#pega o atributo opcao, json permite acessar partes da string separadamente
		if mensagemjson['opcao']==str(1):
			resultado = novoContato(mensagemjson['Nome'],mensagemjson['DDD'],mensagemjson['Numero'],mensagemjson['Email'], arquivo)
			#resultado final da operação, converte string em byte
			connection.send(bytes("ok, recebido", 'utf-8'))

		elif mensagemjson['opcao']==str(2):
			resultado = getContato(arquivo)
			
			#converte a lista resultado, para uma array em json
			connection.send(bytes(json.dumps(resultado), 'utf-8'))


	connection.close()

print ("Servidor esta esperando")
while 1:
	connection, addr = serverSocket.accept()
	_thread.start_new_thread(task, (connection, addr))
