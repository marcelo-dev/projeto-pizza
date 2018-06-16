from app.painel.painel import *
from app.pedidos.pizza import *
from app.pedidos.bebida import *
from app.pagamento.confirmar_pedidos import *
from app.pagamento.extrato import *
from app.pagamento.pagamento import *

id_user = 1
lista_pizza = []
lista_bebida = []
tipo_bebida = 0

opcao = []
while True:
	opcao = painel_principal()
	if opcao[0] == opcao[1]:
		break
	elif opcao[0] == 1:
		lista_pizza.extend([id_user, pizza()])
		print(lista_pizza)
	elif opcao[0] == 2:
		lista_bebida.extend([id_user, bebida()])
		print(lista_bebida)
	elif opcao[0] == 3:
		#alterar_cadastro(id_user)
		break
	elif opcao[0] == 4:
		#consultar_pedido(id_user)
		break
	elif opcao[0] == 5:
		#efetuar_pagamento(id_user)
		break
	elif opcao[0] == 6:
		#sair_fim()
		break
"""

lista_pizza = [["Calabreza",6.58,"Pequena"],["Frango",8.58,"Grande"]]
lista_bebida = [["Coca",6.58,"600"],["Qualquer Uma",8.58,"1L"]]
id_user = 0

menu = -1
while menu != 0: 
  menu = menu()

# CADASTRANDO USUARIO

nome_usuario = recebe_nome_usuario()
numero_usuario = recebe_numero_usuario()
endereco_usuario = recebe_endereco_usuario()
print("Cadastro realizado com sucesso.")
        
# FAZENDO O PEDIDO
tamanho_pizza = tamanho_pizza(nome_usuario)    
valor_pizza = busca_valor_pizza(tamanho_pizza)
escolha_sabor = escolha_sabor()
bebida_escolhida = escolha_bebida()
opcao = int(bebida_escolhida[0])
valor_bebida = valor_bebida(opcao)
sabor_bebida = sabor_bebida(opcao)
forma_pagamento = forma_pagamento()
confirma_compra = confirma_compra(escolha_sabor,tamanho_pizza,bebida_escolhida,preco_final)
print("{} - {} por R${}".format(bebida_escolhida[2:],sabor_bebida, valor_bebida))
preco_final = preco_final(valor_bebida, valor_pizza)
"""
