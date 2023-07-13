catalogo = list()

with open(r'C:\Users\manau\PycharmProjects\programaNotas\programaParaNotas\arquivos\catalogo.txt', 'r', encoding='utf-8') as produtos:
    for linha in produtos.readlines():
        produto = linha.strip().split(';')
        catalogo.append({'Nome': produto[0],
                         'Valor': float(produto[1])})

cor = [
    '\033[1;31m',  # 0 - Vermelho
    '\033[1;32m',  # 1 - Verde
    '\033[1;33m',  # 2 - Amarelo
    '\033[1;34m',  # 3 - Azul
    '\033[1;35m',  # 4 - Magenta
    '\033[1;36m',  # 5 - Ciano
    '\033[1m',     # 6 - Branco
    '\033[m'       # 7 - Sem formatação
]

opcoes = {
    'Menu Principal': {
        'Criar nova nota': {
            'Adicionar produto': [
                'Adicionar por nome e valor',
                'Adicionar por código'
            ],
            'Ver produto(s)': [],
            'Excluir produto': [],
            'Parcelar nota': [],
            'Adicionar desconto': [],
            'Ver nota': [],
            'Finalizar e salvar nota': []
        },
        'Ver nota(s)': [],
        'Exluir nota(s)': [],
        'Ver catálogo': [],
        'Adicionar produto ao catálogo': [],
        'Sair do programa': []
    }
}

notaBase = {
    'Nome': '<não informado>',
    'CPF': '<não informado>',
    'Produtos': [],
    'Sub-Total': 0,
    'Parcelas': [],
    'Total': 0,
    'Desconto': 0
}

# Modificar dados
def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')

def caracteres(texto, max, pular=True):
    if pular:
        if len(texto) > max:
            substrings = [texto[i:i + max] for i in range(0, len(texto), max)]
            return "\n".join(substrings)
        else:
            return texto
    else:
        max += 17
        if len(texto) <= max:
            return texto.ljust(max)[:max]
        else:
            return texto[:max - 3] + "..."

def notaString(notaDados):
    linha = f'{"-"*50}\n'
    arquivoString = linha + f'Nome: {notaDados["Nome"]}\nCPF: {notaDados["CPF"]}\n' + linha
    for index, item in enumerate(notaDados['Produtos']):
        nItem = caracteres(f'{index + 1} - {item["Nome"]}', 33 - len(moeda(item['Valor'])), False)
        arquivoString += f'{nItem}{moeda(item["Valor"])}\n'
    arquivoString += linha + caracteres(f'Desconto: {notaDados["Desconto"]}%', 33 - len(f'Sub-total: {moeda(notaDados["Sub-Total"])}'), False) + f'Sub-total: {moeda(notaDados["Sub-Total"])}\n' + linha
    if len(notaDados['Parcelas']) > 1:
        arquivoString += f'Parcelas: '
        for index, parcela in enumerate(notaDados['Parcelas']):
            arquivoString += f'{moeda(parcela):>40}\n' if index == 0 else f'{moeda(parcela):>50}\n'
    else:
        arquivoString += f'Total: {moeda(notaDados["Total"]):>43}'
    arquivoString += f'\n{linha}'
    return arquivoString

# Ler dados
def lerOpcaoNumerica(f, msg='Digite sua opção: ', linha=True, i=1):
    if linha:
        print(f'{cor[6]}{"-" * 50}{cor[7]}')
    while True:
        opcao = input(f'{cor[2]}{msg}{cor[7]}').strip()
        if opcao.isnumeric() and int(opcao) in list(range(i, f + 1)):
            break
        print(f'{cor[0]}[ERRO] Opção inválida! Tente novamente.{cor[7]}')
    return int(opcao)

def lerOpcao(msg, linha=True):
    while True:
        opcao = input(f'{cor[2]}{msg}{cor[7]}').strip().upper()
        if opcao == 'S' or opcao == 'N':
            break
        print(f'{cor[0]}[ERRO] Opção inválida! Tente novamente.{cor[7]}')
    if linha:
        print(f'{cor[6]}{"-" * 50}{cor[7]}')
    return True if opcao == 'S' else False

def lerNome(msg):
    while True:
        nome = input(f'{cor[2]}{msg}{cor[7]}').strip()
        if nome != '':
            break
        print(f'{cor[0]}[ERRO] Nome inválido! Tente novamente.{cor[7]}')
    print(f'{cor[6]}{"-" * 50}{cor[7]}')
    return nome

def lerValor():
    while True:
        valor = input(f'{cor[2]}Qual o valor do produto: R${cor[7]}').strip().replace(',', '.')
        if valor.replace('.', '').isnumeric():
            break
        print(f'{cor[0]}[ERRO] Valor inválido! Tente novamente.{cor[7]}')
    return float(valor)

def lerCPF():
    while True:
        valido = False
        res = str(input(f'{cor[2]}Digite o CPF [xxx.xxx.xxx-xx]: {cor[7]}')).strip()
        for index, char in enumerate(res):
            if len(res) != 14:
                valido = False
            else:
                if index in [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13]:
                    if char.isnumeric():
                        valido = True
                    else:
                        valido = False
                if valido:
                    if index in [3, 7]:
                        if char == '.':
                            valido = True
                        else:
                            valido = False
                    if valido:
                        if index == 11:
                            if char == '-':
                                valido = True
                            else:
                                valido = False
            if not valido:
                break
        if valido:
            break
        else:
            print(f'{cor[0]}[ERRO] CPF inválido! Tente novamente.{cor[7]}')
    print(f'{cor[6]}{"-" * 50}{cor[7]}')
    return res