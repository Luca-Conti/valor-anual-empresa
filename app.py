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
    escolha_tipo = int(input('escolha 1 para anual e 2 para mensal e 3 para sair: '))
    if escolha_tipo == 1:
        anual()

    elif escolha_tipo == 2:
        mensal()

def mensal():
    titulo(texto='FATURAMENTO MENSAL')

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
    print(f'o faturamento da {quantidade_anos} foi {media} e o total foi {soma}')


escolha()