import datetime as dt
from abc import ABC, abstractmethod
from random import randint


def formatoHora(data):
    return data.strftime("%d/%m/%y %H:%M:%S")

def dataValida(data = '29/09/1994'):
    lista = data.split('/')
    if len(lista) > 3:
        return False
    lista = list(map(int, lista))
    diacorreto = lista[0] > 1 and lista[0] < 31
    mescorreto = lista[1] > 1 and lista[1] < 12
    anocorreto = lista[2] > 1990 and lista [2] < 2024
    if diacorreto and mescorreto and anocorreto:
        return True
    else:
        return False

def getData():
    while True:
        data = input("Informe sua data de nascimento no formato dd/mm/yyyy\n")
        if data == 'q':
            return False
        elif dataValida(data):
            return dt.datetime.strptime(data,'%d/%m/%Y').date()
        else:
            print('Por favor, informe uma data válida.') 

def getExtratoMenu(banco):
    conta = int(input("Por favor, digite o número da conta:\n"))
    if not banco.getConta(conta):
        return
    else:
        banco.getConta(conta).extrato()

def infoMenu(banco):
    num = int(input('Por favor, informe o número da conta:\n'))
    conta = banco.getConta(num)

    if not conta:
        return
    
    print(f"O número máximo de transações diárias é {conta.limiteDiario}. Hoje você realizou {conta.saquesHoje} saques.")
    print(f"O limite máximo de saque é R$ {conta.limite}. Seu saldo atual é R$ {conta.saldo}.")
