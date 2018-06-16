def forma_pagamento():
    while True:
        forma_pagamento = int(input('''
                Formas de Pagamento
                
                1:Cartão
                2:Dinheiro
                   
               Qual forma de pagamento o(a) senhor(a) deseja?''' ))
        if forma_pagamento == 1:
            return "Cartão"
        elif forma_pagamento == 2:
            return "Dinheiro"