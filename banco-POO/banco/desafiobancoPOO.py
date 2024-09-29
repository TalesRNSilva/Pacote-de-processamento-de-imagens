import datetime as dt
from classesBanco import Banco, depositarMenu, saqueMenu
from functionsBanco import getExtratoMenu, infoMenu
from abc import ABC, abstractmethod
from random import randint


#Essa é uma resolução do desafio empregando datas para contagem de saques.
#O extrato agora é uma tupla (data, saldo, valor)
#A checagem de saques é feita contra o número de saques do dia.


Bradesco = Banco('Bradesco')
hoje = dt.date.today()


menu = f"""
[d] Depositar
[s] Sacar
[e] Extrato
[i] Informações

[c] Cadastrar Cliente (C para ver lista de clientes)
[k] Cadastrar Conta   (K para ver a lista de contas)

[q] Sair
=> """


while True:

    opcao = input(menu)

    if opcao == "d":
        depositarMenu(Bradesco)
        
    elif opcao == "s":
        saqueMenu(Bradesco)

    elif opcao == "e":
        getExtratoMenu(Bradesco)

    elif opcao == 'c':
        Bradesco.cadastrarCliente()

    elif opcao == 'C':
        Bradesco.printClientes()

    elif opcao == 'k':
        Bradesco.cadastrarConta()
              
    elif opcao == 'K':
        Bradesco.printContas()

    elif opcao == "i":
        infoMenu(Bradesco)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")