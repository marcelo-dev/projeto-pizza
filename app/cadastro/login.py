from app.painel.painel import *
from app.cadastro.signup import *
import json

def login():
    # Abre o arquivo no modo append, ou seja, cria o arquivo, caso não exista.
    arquivo = open('cadastro.txt','a')
    arquivo.close()
    
    arquivo = open('cadastro.txt','r') #modo read
    #arquivo.tell()
    #Retorna a posição atual do ponteiro de leitura. Cada caractere no arquivo 
    #ocupa uma posição. Caracteres de quebra de linha são considerados também.
    
    #arquivo.seek(2)
    #Define a posição atual do ponteiro de leitura. Neste caso está definindo 
    #a posição 2.
    
    #arquivo.read() lê todo o arquivo a partir da posição do ponteiro e o 
    #retorna em uma única string. A posição inicial do ponteiro é zero se não 
    #foi alterada com seek(). Após executado o read() o ponteiro passa a ser a 
    #última posição no arquivo.
    
    #arquivo.readlines() lê todo o arquivo e retorna cada linha como um item 
    #de uma lista.
    users = arquivo.readlines()
    arquivo.close()
    
    if users == []:
        print("Arquivo vazio.")
        cadastrando_usuario()
    else:
        print("Arquivo não vazio.")
    
    arquivo = open('cadastro.txt','r')
    users = arquivo.readlines()
    arquivo.close()
    
    
login()



