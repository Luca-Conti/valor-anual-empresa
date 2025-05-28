from colorama import Fore, Style
import os
import matplotlib.pyplot as plt
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
        escolha_tipo = int(input('escolha 1 para anual \n e 2 para mensal \n e 3 para semanal \n e 4 para sair:  '))

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

    for i in range(1,4):
        print(f'Preparando grafico em {i} segundos')
        sleep(1)
    Semanas = list(range(1, quantidade_de_semanas + 1))
    escolha_grafico(tempo=Semanas, dinheiro=faturamentos,titulo='Grifico Semanal',  texto_de_baixo='Semanas', texto_lateral='Dinheiro')
    input('Digite algo para voltar ao menu')
    os.system('cls')
    escolha()

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
    for i in range(1,4):
        print(f'Preparando grafico em {i} segundos')
        sleep(1)
    meses = list(range(1, quantidade_de_mes + 1))
    escolha_grafico(tempo=meses, dinheiro=faturamentos,titulo='Grifico Mensal',  texto_de_baixo='Meses', texto_lateral='Dinheiro')
    input('Digite algo para voltar ao menu')
    os.system('cls')
    escolha()

def anual():
    
    '''Essa função é responsavel pelo faturamento anual'''

    titulo(texto='FATURAMNETO ANUAL')
    quantidade_anos = int(input('quantos anos vc vai analizar: '))
    faturamentos = []



    for i in range(1, quantidade_anos + 1):
        faturamento = float(input(f'qual foi o faturamento anual do {i}° ano: '))
        faturamentos.append(faturamento)

    soma = sum(faturamentos)
    anos = list(range(1, quantidade_anos + 1))
    media = soma / quantidade_anos
    sleep(0.5)
    print(Fore.GREEN + f'o faturamento de {quantidade_anos} anos foi {media} e o total foi {soma}' + Fore.RESET)
    for i in range(1,4):
        print(f'Preparando grafico em {i} segundos')
        sleep(1)
    escolha_grafico(tempo=anos,dinheiro=faturamentos,titulo='Grifico Anual', texto_de_baixo='Anos', texto_lateral='Dinheiro')
    input('Digite algo para voltar ao menu')
    os.system('cls')
    escolha()


def erro():

    """Essa função é responsavel pela mensagem de erro"""

    titulo(texto='Você digitou algo errado')
    input('Digite algo para voltar para escolha: ')
    escolha()


def escolha_grafico(tempo = '', dinheiro = '',titulo = '', texto_de_baixo = '', texto_lateral = ''):

    """
    Função que o usuario escolho o tipo de grafico "talvez add grafico de pizza dps"
    """

    try:
        escolha =  int(input('escolha 1 para grafico de barra \n e 2 para grafico de linha: '))
        if escolha == 1:
            plt.bar(tempo, dinheiro)
            plt.xlabel(texto_de_baixo)
            plt.ylabel(texto_lateral)
            plt.title(titulo)
            plt.show()
        elif escolha == 2:
            plt.plot(tempo, dinheiro)
            plt.xlabel(texto_de_baixo)
            plt.ylabel(texto_lateral)
            plt.title(titulo)
            plt.show()
        else:
            erro()
    except:
        erro()
    

def fim():

    """Essa função é chamada para sair do programa"""
    
    titulo(texto='SAINDO DO PROGRAMA')
    input('clique para sair do jogo: ')
    sleep(4.5)


if __name__ == '__main__':
    escolha()