def painel(titulo, menu):
  opcao = 0
  while True:
    print("\n{}\n".format(titulo))
    for enum, element in enumerate(menu):
      print("{} - {}".format(enum + 1, element))

    try:
      opcao = int(input("Digite a opção desejada: "))
    except ValueError:
      print("Valor inválido. Digite novamente.")
    if opcao <= len(menu) and opcao > 0:
      return opcao
    else:
      print("Opção inválida.")

def painel_principal():

  menu = ["Pedir Pizza",
  "Pedir bebida",
  "Alterar cadastro",
  "Consultar pedido",
  "Efetuar pagamento",
  "Sair"]
  opcao_menu = painel("Menu Principal", menu)
  return [opcao_menu, len(menu)]






