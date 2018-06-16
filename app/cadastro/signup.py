def recebe_nome_usuario():

    while True:
        nome = input("Digite seu nome: ")
        is_nome_alpha = nome.replace(" ","").isalpha()
        if is_nome_alpha:
            return nome 
        else: 
            print("Você escreveu seu nome mesmo?")

        print("{0}").format(nome)

    
def recebe_numero_usuario():

    while True:
        numero = input("Digite seu numero de telefone: ")
        if len(numero) <= 8 or len(numero) > 9:
            print("Telefone deve conter 9 dígitos. ") 
        elif numero.isnumeric():
            return int(numero)
        
    
def recebe_endereco_usuario():
    while True:
        endereco = input("Informe o endereço: ")
        if len(endereco) <= 5:
            print("Endereço tem que possuir no mínimo 6 dígitos")
        elif endereco.isalpha() or endereco.isnumeric():
            print("Senha terá que ter letras e números")
        elif (endereco.replace(" ","").isalnum()):
            return endereco
