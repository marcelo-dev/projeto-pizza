def escolha_bebida():
  while True:
    tipo_bebida = int(input("""
    Escolha sua bebida!
    1: Refrigerante lata         R$ 4,00
    2: Refrigerante 600 ml       R$ 6,00
    3: Refrigerante 2 L          R$ 7,50
    4: Cerveja lata              R$ 4,50
    5: Cerveja 600 ml            R$ 8,00
    6: Cerveja Artesanal 1L      R$ 15,00  
    """))
    
    if tipo_bebida == 1:
      return "1: Refrigerante lata"
    elif tipo_bebida == 2:
      return "2: Refrigerante 600ml"
    elif tipo_bebida == 3:
      return "3: Refrigerante 2L"
    elif tipo_bebida == 4:
      return "4: Cerveja lata"
    elif tipo_bebida == 5:
      return "5: Garrafa cerveja 600ml"
    elif tipo_bebida == 6:
      return "6: Garrafa cerveja artesanal 750ml"
            
            
def valor_bebida(bebida):
  while True:
    if bebida == 1:
      return 4.00
    elif bebida == 2:
      return 6.00
    elif bebida == 3:
      return 7.50
    elif bebida == 4:
      return 4.50
    elif bebida == 5:
      return 8.00
    elif bebida == 6:
      return 15.00
            
            
def sabor_bebida(bebida):
  sabor = ""
  while True:
    if bebida >= 1 and bebida < 4:
      sabor = int(input("""
      1. Coca
      2. Pepsi Twist
      3. Fanta
      4. Fanta Uva
      5. Guaraná Antartica
      6. Puresa
      7. Lanranjinha
      """))
    elif bebida > 3 and bebida < 7:
      sabor = int(input("""
      8. Pilsen
      9. Ale
      10. Sol
      11. Skol
      """))
    else:
      print("Melhor escolher o tipo da bebida antes...")
    
    if sabor == 1:
      return "Coca"
    elif sabor == 2:
      return "Pepsi Twist"
    elif sabor == 3:
      return "Fanta"
    elif sabor == 4:
      return "Fanta Uva"
    elif sabor == 5:
      return "Guaraná Antartica"
    elif sabor == 6:
      return "Puresa"
    elif sabor == 7:
      return "Lanranjinha"
    elif sabor == 8:
      return "Pilsen"
    elif sabor == 9:
      return "Ale"
    elif sabor == 10:
      return "Sol"
    elif sabor == 11:
      return "Skol"
    else:
      print("Tenha certeza de escolher uma opção disponível no cardápio. Para refri de 1 à 7. Cervejas de 8 à 11.")

def bebida(): 
  tipo = escolha_bebida()
  bebida_codigo = int(tipo[:1])
  valor = valor_bebida(bebida_codigo)
  marca = sabor_bebida(bebida_codigo)
  return [tipo,valor,marca]