def confirma_compra(escolha_sabor,tamanho_pizza,bebida_escolhida,preco_final):
    while True:
        confirma_compra = int(input('''
                Confirmação de Pedido
                
                1:Sim
                2:Não
                   
               Pizza no sabor {}, de tamanho {}, acompanhada da bebida {} no valor de {}. O(a) senhor(a) confirma este pedido?'''.format(escolha_sabor,tamanho_pizza,bebida_escolhida,preco_final)))


        if confirma_compra == 1:
            return "Senhor(a) {}, iremos entregar sua Pizza no endereço {} dentro de 50 minutos!".format(nome_usuario,endereco_usuario)
        elif confirma_compra == 2:
            return  "Que pena que o(a) senhor(a) desistiu do seu pedido, esperamos tê-lo novamente como cliente."
