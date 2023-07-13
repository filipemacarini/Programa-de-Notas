from programaParaNotas.Lib.dados import *


def titulo(titulo):
    print(f'{cor[6]}{"-"*50}\n{titulo:^50}\n{"-"*50}{cor[7]}')

def exibir(lista, opcoes=True):
    for index, item in enumerate(lista):
        if opcoes:
            print(f'{cor[2]}{index+1} - {cor[3]}{item}{cor[7]}')
        else:
            linha = caracteres(f'{cor[2]}{index + 1} - {cor[3]}{item["Nome"]}{cor[7]}', 50 - len(moeda(item['Valor'])), False)
            print(f'{linha}{cor[6]}{moeda(item["Valor"])}{cor[7]}')

def visualizarNota(nota):
    print(f'{cor[2]}Nome:{cor[7]} {cor[3]}{caracteres(nota["Nome"], 44)}{cor[7]}')
    print(f'{cor[2]}CPF:{cor[7]} {cor[3]}{caracteres(nota["CPF"], 45)}{cor[7]}')
    print(f'{cor[6]}{"-" * 50}{cor[7]}')
    for index, produto in enumerate(nota['Produtos']):
        linha = caracteres(f'{cor[2]}{index+1} - {cor[3]}{produto["Nome"]}{cor[7]}', 49 - len(moeda(produto['Valor'])), False)
        print(f'{linha} {cor[6]}{moeda(produto["Valor"])}')
    print(f'{cor[6]}{"-" * 50}{cor[7]}')
    print(caracteres(f'{cor[2]}Desconto: {cor[7]}{cor[6]}{nota["Desconto"]}%{cor[7]}', 50 - len(f'Sub-total: {moeda(nota["Sub-Total"])}'), False), end=f'{cor[2]}Sub-total: {cor[7]}{cor[6]}{moeda(nota["Sub-Total"])}\n')
    print(f'{cor[6]}{"-" * 50}{cor[7]}')
    if len(nota['Parcelas']) > 1:
        print(f'{cor[2]}Parcelas:{cor[7]}', end=' ')
        for index, parcela in enumerate(nota['Parcelas']):
            print(f'{cor[6]}{moeda(parcela):>40}{cor[7]}' if index == 0 else f'{cor[6]}{moeda(parcela):>50}{cor[7]}')
    else:
        print(f'{cor[2]}Total: {cor[7]}{cor[6]}{moeda(nota["Total"]):>43}{cor[7]}')