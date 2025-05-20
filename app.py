from colorama import Fore
import os

def titulo(texto=''):
    os.system('cls')
    print(texto)
    print('')

titulo(texto="""
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
    escolha_tipo = int(input('escolha 1 para anual e 2 para mensal e 3 para semanal e 4 para sair: '))
    if escolha_tipo == 1:
        anual()

    elif escolha_tipo == 2:
        mensal()

    elif escolha_tipo == 3
    pass

def mensal():
    titulo(texto='FATURAMENTO MENSAL')
    quantidade_de_mes = int(input('quanto meses você vai analizar: '))
    faturamento = []

    c=0
    for i in range(1, quantidade_de_mes + 1):
        c+=1
        faturamentos = float(input(f'Qual foi o faturamento mensal da empresas no {c}° mes: '))
        faturamento.append(faturamentos)
    soma = sum(faturamento)
    media = soma / quantidade_de_mes

    print(f'o faturamento de {quantidade_de_mes} anos foi {media} e o total foi {soma}')

def anual():
    titulo(texto='FATURAMNETO ANUAL')
    quantidade_anos = int(input('quantos anos vc vai analizar: '))
    faturamentos = []

    c = 0

    for i in range(1, quantidade_anos + 1):
        c+=1
        faturamento = float(input(f'qual foi o faturamento anual do {c}° ano: '))
        faturamentos.append(faturamento)

    soma = sum(faturamentos)
    media = soma / quantidade_anos
    print(f'o faturamento de {quantidade_anos} anos foi {media} e o total foi {soma}')


escolha()