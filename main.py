from random import randint
from time import sleep

#Cores
RED   = "\033[1;31m"
YELLOW = "\033[1;33m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

while True:
  print("""ESCOLHA ESSAS OPÇÕES PARA JOGAR

  [0] - Pedra
  [1] - Papel
  [2] - Tesoura
  """)

  #opções
  escolha = ('pedra', 'papel', 'tesoura')

  computador = randint(0,2)
  usuario = int(input("Digite o seu numero jogar: "))

  #validação
  if usuario != 0 and usuario !=1 and usuario !=2:
    print("Digite um numero valido")
  else:
    print(13*'-=-')
    print(RED + "VAMOS JOGAR!!!!" + RESET)
    sleep(1)
    print(BLUE + "JO" + RESET)
    sleep(2)
    print(GREEN + "KEN" + RESET)
    sleep(2)
    print(YELLOW + "PO" + RESET)
    sleep(0.5)
    print(13*'-=-')

    #escolhas
    print(CYAN + f'Você escolheu {escolha[usuario]}' +     RESET)
    print(CYAN + f'O computador escolheu {escolha[computador]}' + RESET)
    print(13*'-=-')

    if computador == 0: # se o computador escolher pedra
      if usuario == 0:
        print('EMPATOU!')
      elif usuario == 1:
        print ('VOCÊ PERDEU!')
      elif usuario == 2:
        print('VOCÊ VENCEU!')
    
    elif computador == 1: # se o computador escolher papel
      if usuario == 0:
        print('VOCÊ PERDEU!')
      elif usuario == 1:
        print('EMPATOU!')
      elif usuario == 2:
        print('VOCÊ VENCEU!')
    
    else: # se o computador escolher tesoura
      if usuario == 0:
        print('VOCÊ VENCEU!')
      elif usuario == 1:
        print('VOCÊ PERDEU!')
      elif usuario == 2:
        print('EMPATE!')
  reiniciar = input("Deseja jogar novamente? (s/n): ")
  if reiniciar.lower() != 's':
    break
  