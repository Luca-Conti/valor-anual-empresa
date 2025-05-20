from colorama import Fore, Style
import os
from time import sleep

def titulo_sem_(texto=''):
    """
    Essa função é responsavel pelo titulo só que sem '-'
    """
    os.system('cls')
    print(Fore.RED + texto + Fore.RESET)

def titulo(texto=''):
    """
    Essa função é responsavel pelo titulo
    """
    os.system('cls')
    print(Fore.RED + '-' * len(texto))
    print(texto)
    print('-' * len(texto) + Fore.RESET)

    print('')

titulo_sem_(texto="""
███╗░░░███╗███████╗██████╗░██╗░█████╗░  ░█████╗░███╗░░██╗██╗░░░██╗░█████╗░██╗░░░░░  ██████╗░███████╗
████╗░████║██╔════╝██╔══██╗██║██╔══██╗  ██╔══██╗████╗░██║██║░░░██║██╔══██╗██║░░░░░  ██╔══██╗██╔════╝
██╔████╔██║█████╗░░██║░░██║██║███████║  ███████║██╔██╗██║██║░░░██║███████║██║░░░░░  ██║░░██║█████╗░░
██║╚██╔╝██║██╔══╝░░██║░░██║██║██╔══██║  ██╔══██║██║╚████║██║░░░██║██╔══██║██║░░░░░  ██║░░██║██╔══╝░░
██║░╚═╝░██║███████╗██████╔╝██║██║░░██║  ██║░░██║██║░╚███║╚██████╔╝██║░░██║███████╗  ██████╔╝███████╗
╚═╝░░░░░╚═╝╚══════╝╚═════╝░╚═╝╚═╝░░╚═╝  ╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝  ╚═════╝░╚══════╝

███████╗███╗░░░███╗██████╗░██████╗░███████╗░██████╗░█████╗░░██████╗
██╔════╝████╗░████║██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝
█████╗░░██╔████╔██║██████╔╝██████╔╝█████╗░░╚█████╗░███████║╚█████╗░
██╔══╝░░██║╚██╔╝██║██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗██╔══██║░╚═══██╗
███████╗██║░╚═╝░██║██║░░░░░██║░░██║███████╗██████╔╝██║░░██║██████╔╝
╚══════╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░╚═╝╚═════╝░""")

def escolha():
    """essa função é responsavel pela escolha do usuario"""
    try:
        print('-----')
        print(Fore.RED +'Opção' + Fore.RESET)
        print('-----')
        escolha_tipo = int(input('escolha 1 para anual e 2 para mensal e 3 para semanal e 4 para sair: '))

        if escolha_tipo == 1:
            sleep(1)
            anual()

        elif escolha_tipo == 2:
            sleep(1)
            mensal()

        elif escolha_tipo == 3:
            sleep(1)
            semenal

        elif escolha_tipo == 4:
            sleep(1)
            fim()

        else:
            sleep(1)
            erro()
    except:
        erro()

def semenal():

    '''Essa função é responsavel pelo faturamento semanal'''

    titulo(texto='FATURAMENTO SEMANAL')
    quantidade_de_semanas = int(input('quantas semanas você vai analizar: '))
    faturamento = []

    for i in range(1,quantidade_de_semanas +1):
        faturamentos = float(input('qual o faturamento da {i}° semana: '))
        faturamento.append(faturamentos)
    soma = sum(faturamento)
    media = soma / quantidade_de_semanas
    sleep(0.5)
    print(Fore.GREEN + f'o faturamento de {quantidade_de_semanas} semanas foi {media} e o total foi {soma}' + Fore.RESET)

def mensal():
    
    '''Essa função é responsavel pelo faturamento mensal'''

    titulo(texto='FATURAMENTO MENSAL')
    quantidade_de_mes = int(input('quantos meses você vai analizar: '))
    faturamento = []


    for i in range(1, quantidade_de_mes + 1):
        faturamentos = float(input(f'Qual foi o faturamento mensal da empresas no {i}° mes: '))
        faturamento.append(faturamentos)
    soma = sum(faturamento)
    media = soma / quantidade_de_mes

    sleep(0.5)

    print(Fore.GREEN + f'o faturamento de {quantidade_de_mes} meses foi {media} e o total foi {soma}' + Fore.RESET)

def anual():
    
    '''Essa função é responsavel pelo faturamento anual'''

    titulo(texto='FATURAMNETO ANUAL')
    quantidade_anos = int(input('quantos anos vc vai analizar: '))
    faturamentos = []



    for i in range(1, quantidade_anos + 1):
        faturamento = float(input(f'qual foi o faturamento anual do {i}° ano: '))
        faturamentos.append(faturamento)

    soma = sum(faturamentos)
    media = soma / quantidade_anos
    sleep(0.5)
    print(Fore.GREEN + f'o faturamento de {quantidade_anos} anos foi {media} e o total foi {soma}' + Fore.RESET)


def erro():

    """Essa função é responsavel pela mensagem de erro"""

    titulo(texto='Você digitou algo errado')
    input('Digite algo para voltar para escolha: ')
    escolha()


def fim():

    """Essa função é chamada para sair do programa"""
    
    titulo(texto='SAINDO DO PROGRAMA')
    input('clique para sair do jogo: ')
    sleep(4.5)


escolha()