from programaParaNotas.Lib.interface import *
from random import choice
from ast import literal_eval


while True:
    titulo('Menu Principal')
    exibir(opcoes['Menu Principal'].keys())
    opcao = lerOpcaoNumerica(len(opcoes['Menu Principal'].keys()))
    if opcao == 1:
        nota = notaBase.copy()
        while True:
            titulo('Criar Nova Nota')
            if nota['CPF'] == '<não informado>' and nota['Nome'] == '<não informado>':
                opcao = lerOpcao('Deseja adicionar o nome do consumidor [S/N]: ')
                if opcao:
                    nota['Nome'] = lerNome('Digite o nome do consumidor: ')
                opcao = lerOpcao('Deseja adicionar o CPF do consumidor [S/N]: ')
                if opcao:
                    nota['CPF'] = lerCPF()
            exibir(opcoes['Menu Principal']['Criar nova nota'].keys())
            opcao = lerOpcaoNumerica(len(opcoes['Menu Principal']['Criar nova nota'].keys()))
            if opcao == 1:
                titulo('Adicionar Produto')
                exibir(opcoes['Menu Principal']['Criar nova nota']['Adicionar produto'])
                opcao = lerOpcaoNumerica(len(opcoes['Menu Principal']['Criar nova nota']['Adicionar produto']))
                if opcao == 1:
                    titulo('Adicionar Produto - Não Catalogado')
                    produto = {
                        'Nome': lerNome('Digite o nome do produto: '),
                        'Valor': lerValor()
                    }
                    nota['Produtos'].append(produto.copy())
                    nota['Sub-Total'] += produto['Valor']
                if opcao == 2:
                    titulo('Adicionar Produto - Catalogado')
                    exibir(catalogo, False)
                    opcao = lerOpcaoNumerica(len(catalogo))
                    nota['Produtos'].append(catalogo[opcao-1])
                    nota['Sub-Total'] += catalogo[opcao-1]['Valor']
                quantidadeParcelas = len(nota['Parcelas'])
                nota['Parcelas'] = []
                for parcela in range(quantidadeParcelas):
                    nota['Parcelas'].append(nota['Sub-Total'] / quantidadeParcelas)
            elif opcao == 2:
                titulo('Produto(s)')
                if len(nota['Produtos']) == 0:
                    print(f'{cor[0]}[ERRO] Não há nenhum produto! Tente novamente.{cor[7]}')
                else:
                    exibir(nota['Produtos'], False)
            elif opcao == 3:
                titulo('Excluir Produto')
                if len(nota['Produtos']) == 0:
                    print(f'{cor[0]}[ERRO] Não há nenhum produto! Tente novamente.{cor[7]}')
                else:
                    exibir(nota['Produtos'], False)
                    opcao = lerOpcaoNumerica(len(nota['Produtos']))
                    nota['Sub-Total'] -= nota['Produtos'][opcao-1]['Valor']
                    nota['Total'] -= nota['Produtos'][opcao-1]['Valor']
                    nota['Produtos'].remove(nota['Produtos'][opcao-1])
                quantidadeParcelas = len(nota['Parcelas'])
                nota['Parcelas'] = []
                for parcela in range(quantidadeParcelas):
                    nota['Parcelas'].append(nota['Sub-Total'] / quantidadeParcelas)
            elif opcao == 4:
                titulo('Forma de Pagamento')
                while True:
                    if nota['Desconto'] > 0:
                        print(f'{cor[0]}Anteriormente foi adicionado um desconto! Portanto\né possível apenas pagar a vista.{cor[7]}')
                        print(f'{cor[6]}{"-" * 50}{cor[7]}')
                        opcao = lerOpcao('Deseja remover desconto [S/N]: ')
                        if opcao:
                            nota['Desconto'] = 0
                            continue
                        nota['Parcelas'] = [nota['Sub-Total']]
                        break

                    quantidadeParcelas = lerOpcaoNumerica(12, 'Digite em quantas parcela [2 - 12]: ', False, 2)
                    nota['Total'] = nota['Sub-Total']
                    nota['Parcelas'] = []
                    for parcela in range(quantidadeParcelas):
                        nota['Parcelas'].append(nota['Sub-Total'] / quantidadeParcelas)
                    break
            elif opcao == 5:
                titulo('Adionar Desconto')
                while True:
                    if len(nota['Parcelas']) > 1:
                        print(f'{cor[0]}Não é possível adicionar desconto! A nota está par\ncelada em {len(nota["Parcelas"])} vezes.{cor[7]}')
                        print(f'{cor[6]}{"-" * 50}{cor[7]}')
                        opcao = lerOpcao('Deseja pagar a vista [S/N]: ', False)
                        if opcao:
                            nota['Parcelas'] = [nota['Sub-Total']]
                    nota['Desconto'] = lerOpcaoNumerica(100, 'Digite quantos por cento é o desconto: ', False, 1)
                    break
            elif opcao == 6:
                titulo('Nota')
                nota['Total'] = nota['Sub-Total'] * (1 - nota['Desconto']/100)
                visualizarNota(nota)
            elif opcao == 7:
                nome_txt = ''
                for char in range(6):
                    nome_txt += str(choice(list(range(0, 10))))
                nome_arquivo = f'arquivos\\notas\\{nome_txt}.txt'
                with open(nome_arquivo, 'w') as arquivo:
                    arquivo.write(notaString(nota))
                with open(r'arquivos\notas\notas-dict.txt', 'a', encoding='utf-8') as arquivo:
                    arquivo.write(f'{str(nota)}\n')
                break
    if opcao == 2 or opcao == 3:
        titulo('Notas' if opcao == 2 else 'Excluir Nota')
        notas = list()
        with open(r'arquivos\notas\notas-dict.txt', 'r', encoding='utf-8') as arquivo:
            for linha in arquivo.readlines():
                nota = literal_eval(linha.strip())
                notas.append(nota)
        for index, nota in enumerate(notas):
            print(f'{cor[3]}{index+1}º Nota{cor[7]}')
            print(f'{cor[6]}{"-"*50}{cor[7]}')
            visualizarNota(nota)
            if index+1 != len(notas):
                print(f'{cor[6]}{"-"*50}{cor[7]}')
        if opcao == 3:
            notaExcluir = lerOpcaoNumerica(len(notas))
            notas.remove(notas[notaExcluir-1])
            with open(r'arquivos\notas\notas-dict.txt', 'a+', encoding='utf-8') as arquivo:
                for nota in notas:
                    arquivo.write(f'{nota}\n')
    if opcao == 6:
        break
