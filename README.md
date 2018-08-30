# Socket_Agenda_Json
Agenda usando socket cliente-servidor, onde o usuário pode adicionar e ver contatos

Opção 1 o usuário pode adicionar um novo contatoOpção 1 o usuário pode adicionar um novo contato

Opção 2 o usuário pode ver uma lista de contato

mensagens ficam em formato Json

	Formato da mensagem que o cliente pode enviar:
	{
		'opcao':opcao,
		'Nome': nome,
		'DDD':ddd,
		'Numero':numero,
		'Email':email,		
	}

	
	Formato da mensagem que o cliente recebe:
	 {
	 	contato1,
	 	contato 2,
	 	contato...
	 }
	 
O servidor pode armazenar um novo nome ou enviar uma lista de contatos




