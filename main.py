introdução = input("Deseja jogar este jogo? (sim/não):")
if introdução.lower() == "não":
  quit()
elif introdução.lower() == "sim":

 nome = input("Insira o seu nome: ") 
 print("\n==================BEM VINDO A FLORESTA OBSCURA========================")
print(f"\nBem vindo {nome}, a floresta obscura. Neste jogo vais ter varias opções que têm a sua historia, mas o objetivo final é sair da floresta.")

#-------------------------------------------------------------------------------------------
#O Começo
vida = 100

inventario = []
comida = "comida"
lanterna = "lanterna"
equipamento = "equipamneto"

def adicionar_item(item):
    inventario.append(item)
    print(f"{item} foi adicionado ao seu inventario")

def remover_item(item):
    if item in inventario:
        inventario.remove(item)
        print(f"{item} foi removido do seu inventario")
    else:
        print(f"{item} não está no seu inventario")
resposta = []
#-------------------------------------------------------------------------------------------

print("Escolhe um caminho que quer se dirigir (ESQUERDA (e)/MEIO (m) ou DIREITA (d):")
opcao = input('\nopção aqui: ')

if opcao == "e":
  print('\nEscolheste o lado esquerdo que segue para uma caverna')
  print("Ao entrar na caverna encontras alguns hilichurls. Ao ver-te, eles pegam nas suas armas e correm todos para te atacar.")
  defesa = input("\ndecides: defenderes-te(d) ou fujir da caverna e voltar mais tarde(e): ")
  if defesa == "d":
    print("Preparaste-te para a batalha, mas como não tinhas equipamento morreste") 
    quit()

  elif defesa == "e":
    print("Correstes para o fundo da caverna e conseguiste fugir para uma aldeia!")
    

elif opcao == "m":
  print("\nEscolheste o caminho do meio.")
  print("\nFoste explorar a floresta e encontraste um labirinto.")
  print("\nAo entrar no labirinto, passaste muitas horas lá e não conseguiste sair.Com isso tu morreste pois não tinhas como se alimentar.FIM")
  
  resposta = input("Você quer jogar novamente? (s/n): ").strip().lower()
  if resposta == "sim":
   print("o jogo sera ")
  elif resposta == "não":
    quit()

elif opcao == "d":
  print('\nescolheste o caminho da direita e segues para uma aldeia.')
  print("\nAo entrar na aldeia, encontras uma casa que tem várias coisas para te defenderes.")

#-------------------------------------------------------------------------------------------



while len(inventario) < 1:
 escolha = input("\nEscolhe um equipamento para coletar (1/2/3): ")
 if escolha == '1' and "espada mágica" not in inventario:
      inventario.append("espada mágica")
      print("\nBoa, coletaste espada mágica!")
 elif escolha == '2' and "arquiflexa" not in inventario:
        inventario.append("arquiflexa ")
        print("\nColetaste arquiflexa encantada!")
 elif escolha == '3' and "escudo de escama de dragão" not in inventario:
  ("escudo ")
  print("\nColetaste escudo!")

 if escolha == "1":
     print("Muito bem agora que tens uma espada podes ir a caverna e derrotar os  hilichurls")

 elif escolha == "2":
  print("Boa escolheste um arquiflexa, agora podes seguir o teu caminho para a caverna")

 elif escolha == "3":
  print("Um escudo?? acho que não vais conseguir fazer nada so com um escudo")

  

 print("Boa, chegaste até a caverna.Agora esta na hora de vencer")
 input("O hillichurl atacou te como vais te desviar ( direita(d) ou esquerda(e)?")

 if opcao == "e":
  print("o hillichurl estava a espera desta e acertou te com a espada(-25 de vida)")
  vida = 75
 elif opcao == "d":
   print("\nO hillichurl não estava a espera disso e morreu. ")
   print("A batalha continuou, com sorte tu ganhas os hillichurls e segues em frente")
   print("\nAo andar algum tempo encontras um bau cheio de ouro e com um mapa que mostra a saida da floresta")

print("Parabens Conseguiste sair da floresta")
  
print("\nOBRIGADO POR JOGARES O JOGO")


  
