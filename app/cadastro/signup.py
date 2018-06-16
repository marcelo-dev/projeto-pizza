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

def recebe_senha_usuario():
    while True:
        senha = input("Cadastre uma senha: ")
        aux = senha.find(" ")
        if aux != -1:
            print("A senha não pode conter espaço em branco.")
        elif len(senha) <= 5:
            print("A senha tem que possuir no mínimo 6 dígitos.")
        elif senha.isalpha() or senha.isnumeric():
            print("A senha terá que ter letras e números.")
        elif senha.isalnum():
            criptografia = "{}{}{}".format("dgSFHt4568gfhe", senha, "fdgfhQT12tyjhet")
            break
    
    print("Cadastre agora uma pergunta secreta que só você sabe a resposta caso esqueça seu e-mail ou senha.")
    print("Caso esqueça seu e-mail ou senha será feito esta pergunta e você terá de responder corretamente para recuperar o acesso.")
    print("Cadastre a resposta com cuidado. Será considerado a igualdade de todos os caracteres para conferência.")
    while True:
        pergunta = input("Digite a pergunta secreta com no máximo 60 caracteres: ").strip()
        if len(pergunta) <= 60:
            break
    while True:
        resposta = input("Digite a resposta secreta com no máximo 20 caracteres: ").strip()
        if len(resposta) <= 20:
            criptografia2 = "{}{}{}".format("345ghghjGJGHK%$245", resposta, "dsfgSFGeretertwer3452435")
            break
    return [criptografia, criptografia2]

# CADASTRANDO USUARIO
def cadastrando_usuario():
    nome_usuario = recebe_nome_usuario()
    numero_usuario = recebe_numero_usuario()
    endereco_usuario = recebe_endereco_usuario()
    senha_usuario = recebe_senha_usuario()
    print("Cadastro realizado com sucesso.")
    arquivo = open('cadastro.txt','a')
    arquivo.writelines([nome_usuario, senha_usuario, numero_usuario, endereco_usuario])
    arquivo.close()
