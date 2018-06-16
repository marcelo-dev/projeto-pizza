def tamanho_pizza(nome_usuario):   
    while True:
        tamanho = input("""
          **** Ola {}! ****\n  
          Vamos começar escolhendo um de nossos tamanhos:
          - P, pizza Pequena de 6 pedaços até 2 sabores por R$29,90.
          - M, pizza Média de 9 pedaços até 3 sabores por R$35,90.
          - G, pizza Grande de 12 pedaços até 4 sabores por R$41,90
          \n\n\n""".format(nome_usuario)).capitalize()
        # VERIFICADOR DE OPCAO            
        if tamanho.isalpha() and len(tamanho)==1:
            if tamanho == "P":
                print("\nVocê tem direito a 1 sabor de pizza no tamanho pequeno!")                
                return tamanho
            elif tamanho == "M":
                print("\nVocê tem direito a 1 sabor de pizza no tamanho médio!")
                return tamanho
            elif tamanho == "G":
                print("\nVocê tem direito a 1 sabor de pizza no tamanho grande!")
                return tamanho 
        else: 
            print("\nEnquanto voce digitar qualquer coisa diferente de P, M ou G, serei obrigado a te perguntar de novo...")         
    print("\nTamanho escolhido foi {}, confere?".format(tamanho))
    
def busca_valor_pizza(tamanho):
    # if e elif para retornar valor correspondente ao tamanho de pizza escolhido
    if tamanho == "P":
        return 29.90
    elif tamanho == "M":
        return 35.90
    elif tamanho == "G":
        return 41.90

def escolha_sabor():
    while True:
      print('''
        MENU DE SABORES\n      
        1: Bacon - (mussarela, tomate, bacon e azeitona)	                                        
        2: Baianinha - (mussarela, calabresa, ovos, pimenta, cebola e azeitona)	                        
        3: Beringela - (mussarela, beringela, pimentão e azeitona)	                                
        4: Brócolis - (mussarela, brócolis, bacon e azeitona)	                                        
        5: Brócolis Catupiry - (mussarela, brócolis, catupiry, bacon e azeitona)	                
        6: Calabresa - (mussarela, calabresa, cebola e azeitona)	                                
        7: Calabresa Catupiry - (mussarela, calabresa, cebola, catupiry e azeitona)	                
        8: Camarão - (mussarela, camarão, ervilha, palmito, catupiry e azeitona)	                
        9: Carne Seca com Catupiry - (mussarela, carne seca, catupiry e azeitona)	                
        10: Frango Catupiry - (mussarela, frango desfiado, catupiry e azeitona)	                        
        11: Frango Catupiry Milho - (mussarela, frango desfiado, catupiry, milho e azeitona)	        
        12: Frango Cheedar - (mussarela, frango desfiado, cheedar e azeitona)	                        
        13: Frango Crocante - (mussarela, frango desfiado, milho, batata palha e azeitona)
        14: Frango Especial com Bacon - (mussarela, frango desfiado, requeijão, bacon e azeitona)	
        15: Marguerita - (mussarela, tomate, parmesão, manjericão fresco e azeitona)	                
        16: Peito de Peru - (mussarela, peito de peru, catupiry e azeitona)	                        
        17: Peperoni - (mussarela, peperoni e azeitona)	                                                
        18: Portuguesa - (mussarela, presunto, ovos, cebola, ervilha, palmito e azeitona)	        
        19: Quatro Queijos - (mussarela, catupiry, parmesão, gorgonzola e azeitona)\n\n	                
        PIZZAS DOCES\n
        20: Banana - (banana, açúcar e canela)	                                                        
        21: Brigadeiro - (chocolate e granulado)	                                                
        22: Confeti - (chocolate e confeti)	                                                        
        23: Choquito - (chocolate, doce de leite e castanha)	                                        
        24: Doce de Leite - (doce de leite e coco ralado)	                                        
        25: Nutella - (nutella)\n	                                                                        
      ''')
      escolhasabor = int(input("Qual sabor você deseja? "))
      
      if escolhasabor == 1:
        return("Bacon")
      elif escolhasabor == 2:
        return("Baianinha")
      elif escolhasabor == 3:
        return("Beringela")
      elif escolhasabor == 4:
        return("Brócolis")
      elif escolhasabor == 5:
        return("Brócolis Catupiry")
      elif escolhasabor == 6:
        return("Calabresa")
      elif escolhasabor == 7:
        return("Calabresa Catupiry")
      elif escolhasabor == 8:
        return("Camarão")
      elif escolhasabor == 9:
        return("Carne Seca com Catupiry")
      elif escolhasabor == 10:
        return("Frango Catupiry")
      elif escolhasabor == 11:
        return("Frango Catupiry Milho")
      elif escolhasabor == 12:
        return("Frango Cheedar")
      elif escolhasabor == 13:
        return(" Frango Crocante")
      elif escolhasabor == 14:
        return("Frango Especial com Bacon")
      elif escolhasabor == 15:
        return("Marguerita")
      elif escolhasabor == 16:
        return("Peito de Peru")
      elif escolhasabor == 17:
        return("Peperoni")
      elif escolhasabor == 18:
        return("Portuguesa")
      elif escolhasabor == 19:
        return("Quatro Queijos")
      elif escolhasabor == 20:
        return("Bananaa")
      elif escolhasabor == 21:
        return("Brigadeiro")
      elif escolhasabor == 22:
        return("Confeti")
      elif escolhasabor == 23:
        return("Choquito")
      elif escolhasabor == 24:
        return("Doce de leite")
      elif escolhasabor == 25:
        return("Nutella")
      else:
        print("Escolha um sabor de 1 à 25.")
        continue 

def pizza(nome_usuario="Marcelo"): 
  tamanho = tamanho_pizza(nome_usuario)
  valor = busca_valor_pizza(tamanho)
  sabor = escolha_sabor()
  return [tamanho,valor,sabor]


