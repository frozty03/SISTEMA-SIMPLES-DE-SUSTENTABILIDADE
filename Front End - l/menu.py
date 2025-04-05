from datetime import date
import os
from tabulate import tabulate


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


limpar_tela()
print('\t\t\t\t\t==========================================================')
print('\t\t\t\t\t|  BEM-VINDO AO SISTEMA DE CÁLCULO DE SUSTENTABILIDADE  |')
print('\t\t\t\t\t==========================================================')

print('\n                                          OBJETIVO:')
print('====================================================================================================')
print('| ATRIBUIR, POR MEIO DE CÁLCULOS E PARÂMETROS PRÉ DEFINIDOS, UMA NOTA DE 1 A 5 DE SUSTENTABILIDADE,|')
print('| ALÉM DE RELATÓRIOS, GRÁFICOS E RECOMENDAÇÕES, COM O FITO DE ESTIMULAR O CRESCIMENTO SUSTENTÁVEL! |')
print('====================================================================================================')
print('| PARA CÁLCULO MAIS PRECISO, CONFIRA A ABA PARÂMETROS PARA REALIZAR AS MEDIÇÕES DE CONSUMO.        |')
print('====================================================================================================')

usuarios = {}  # simular bd
registros = {}  # guarda valores em matrizes 2D. registros[chave][matriz][valor da matriz]


# ADICIONAR EMAIL P/ RECUPERAÇÃO DE SENHA
def cadastro():
    limpar_tela()
    print('\n                                       CADASTRO')
    print('====================================================================================================')
    usuario = input('* Digite um nome de usuário: ')

    if usuario in usuarios:
        print('* ❌ Erro: Usuário já existe!')
        return

    senha = input('* Digite uma senha: ')
    senha2 = input('* Confirme a senha: ')

    if senha != senha2:
        print('* ❌ Erro: As senhas não coincidem!')
    else:
        usuarios[usuario] = senha  # salvar a senha ao usuario
        registros[usuario] = []  # cria uma chave
        print('* ✅ Cadastro realizado com sucesso!')
    print('====================================================================================================')


# ADICIONAR OPÇÃO P RECUPERAR SENHA
def login():
    limpar_tela()
    print('\n                                           LOGIN')
    print('====================================================================================================')
    usuario = input('* Usuário: ')
    senha = input('* Senha: ')

    if usuario in usuarios and usuarios[usuario] == senha:  # se o usuario estiver no dict e a senha corresponder
        print(f' ✅ Login bem-sucedido! Bem-vindo, {usuario}!')
        print('====================================================================================================')
        menu_login(usuario)  # iniciar o menu pós login
    else:
        print('* ❌ Erro: Usuário ou senha incorretos!')
        print('====================================================================================================')


def area_login():
    while True:
        limpar_tela()
        print('\n                                       ÁREA DE LOGIN')
        print('====================================================================================================')
        print('|             1. Cadastrar         |          2. Login          |          3. Sair                 |')
        print('====================================================================================================')

        opcao = input('Escolha uma opção (1-3): ')

        if opcao == '1':
            cadastro()
        elif opcao == '2':
            login()
        elif opcao == '3':
            print('Saindo do sistema...')
            break
        else:
            print('⚠️ Opção inválida! Tente novamente.')


def parametros(usuario):
    while True:
        limpar_tela()
        tabela_parametros = [
            {
                'titulo': '1. CONSUMO DE ÁGUA',
                'descricao': 'Medido em litros por dia (L/dia) atráves do hidrômetro',
                'dados': [
                    ['Faixa de Consumo', 'Nota', 'Classificação'],
                    ['Mais de 250L', 1, 'Alto consumo'],
                    ['Entre 250 a 200L', 2, 'Consumo elevado'],
                    ['Entre 199 a 150L', 3, 'Consumo moderado'],
                    ['Entre 149 a 100L', 4, 'Baixo consumo'],
                    ['Menos que 100L', 5, 'Consumo excelente']
                ]
            },
            {
                'titulo': '2. CONSUMO DE ENERGIA',
                'descricao': 'Medido em kWh/dia, obtido na conta de luz',
                'dados': [
                    ['Faixa de Consumo', 'Nota', 'Classificação'],
                    ['Mais que 15kW', 1, 'Alto consumo'],
                    ['Entre 15 a 12kW', 2, 'Consumo elevado'],
                    ['Entre 11 a 8kW', 3, 'Consumo moderado'],
                    ['Entre 8 a 5 kW', 4, 'Baixo consumo'],
                    ['Menos que 5kW', 5, 'Consumo excelente']

                ]
            },
            {
                'titulo': '3. USO DE TRANSPORTES',
                'descricao': 'Baseado no tipo de transporte utilizado regularmente',
                'dados': [
                    ['Tipo de transporte', 'Nota', 'Classificação'],
                    ['Transporte privado', 1, 'Alto impacto'],
                    ['Misto (público e privado)', 2, 'Impacto elevado'],
                    ['Transporte público', 3, 'Impacto moderado'],
                    ['Transporte elétrico', 4, 'Baixo impacto'],
                    ['Bicicleta/caminhada', 5, 'Nenhum impacto']
                ]
            },

            {
                'titulo': '4. LIXO RECICLÁVEL',
                'descricao': 'Baseado no percentual em relação ao total de lixo produzido por dia',
                'dados': [
                    ['Percentual', 'Nota', 'Classificação'],
                    ['Menos que 20%', 1, 'Alto impacto'],
                    ['Entre 20 a 30%', 2, 'Impacto elevado'],
                    ['Entre 31 a 40%', 3, 'Impacto moderado'],
                    ['Entre 41 a 50%', 4, 'Baixo impacto'],
                    ['Mais que 50%', 5, 'Impacto irrelevante']
                ]
            }
        ]

        print('\n' + '=' * 60)
        print(f'| Olá, {usuario}!                                          |')
        print('|       PARÂMETROS DE AVALIAÇÃO DE SUSTENTABILIDADE        |')
        print('|' + '-' * 58 + '|')
        print('|   A NOTA FINAL SERÁ OBTIDA A PARTIR DA MÉDIA ARITMÉTICA  |')
        print('=' * 60)

        for i in tabela_parametros:
            print(f'\n{i['titulo']}')
            print(f'Descrição: {i['descricao']}')
            print(tabulate(i['dados'], headers='firstrow', tablefmt='grid'))
        opcao = input('\nAperte ENTER para retornar ao menu: ')
        if opcao == '':
            return


def menu_login(usuario):
    while True:
        limpar_tela()
        print('\n                                             MENU')
        print('====================================================================================================')
        print(
            f'| * Usuário: {usuario}                                                                                     |')
        print('|--------------------------------------------------------------------------------------------------|')
        print('|    1. Cadastro de informações | 2. Lista de gráficos | 3. Ações (recomendações) | 4. Relatório   |')
        print('|                                  5. Parâmetros   |    6. Sair                                    |')
        print('====================================================================================================')

        opcao = input('Escolha uma opção (1-6): ')
        if opcao == '1':  # por as outras opções em cima, em ordem(depois substituir por elif)
            print('Navegando para tela de cadastro...')
            cadastro_inf(usuario)
        elif opcao == '2':
            grafico(usuario)
        elif opcao == '3':
             mostrar_tela_recomendacoes(usuario)
        elif opcao == '5':
            parametros(usuario)
        elif opcao == '6':  # por as outras opções em cima, em ordem(depois substituir por elif)
            print('Voltando a área de login...')
            break


def cadastro_inf(usuario):
    while True:
        limpar_tela()
        print('\n                                       CADASTRO DE INFORMAÇÕES')
        print('====================================================================================================')
        print(
            f'| * Usuário: {usuario}                                                                                     |')
        print('|--------------------------------------------------------------------------------------------------|\n')

        data = date.today()  # pegando data atual
        print(f'Data do registro: {data}')
        print(f'Para retornar ao MENU: insira os valores ou aperte ENTER\n')
        try:
            energia = float(input("Informe seu consumo de energia (kW/dia): "))
            agua = float(input("Informe seu consumo de energia (L/dia): "))
            residuo = float(input("Informe sua geração de resíduos recicláveis (%): "))

            # cabeçalho explicando o último input
            print("\nPV - Privado\nPVU - Público e privado\nPU - Público\nE - Elétrico\nBC - Bicleta e/ou caminhada")
            transporte = input(
                "Informe o tipo de transporte utilizado (PV/PVU/PU/E/BC): ").upper()  # upper() transforma em maiúsculo

            # Verificando se a opção do transporte é válida
            if transporte not in ["PV", "PVU", "PU", "E", "BC"]:
                raise  # Leva para o except
        except:
            print("\nValor inválido inserido, voltando para o menu...")
            return

        calculo = []  # inicializando vetor

        # formato: [data, nota_energia, nota_água, nota_resíduo, nota_transporte, nota_sustentabilidade]
        calculo[:] = (data, *calcular_nota(energia, agua, residuo,
                                           transporte))  # atribui data e os retornos da função no vetor calculo
        registros[usuario].append(calculo[:])  # faço o registro

        print(f'\nNota eneriga:    {calculo[1]}')  # apresento a nota
        print(f'Nota água:       {calculo[2]}')
        print(f'Nota resíduo:    {calculo[3]}')
        print(f'Nota transporte: {calculo[4]}')
        print(f'Nota geral:      {calculo[5]}')

        return


def input_enter():
    return


def calcular_nota(energia, agua, residuo, transporte):
    # Cálculo do parâmetro de água
    if (agua > 250):
        n_agua = 1
    elif (agua >= 200 and agua <= 250):
        n_agua = 2
    elif (agua >= 150 and agua <= 199):
        n_agua = 3
    elif (agua >= 100 and agua <= 149):
        n_agua = 4
    else:
        n_agua = 5

    # Cálculo do parâmetro de energia
    if (energia > 15):
        n_energia = 1
    elif (energia >= 12 and energia <= 15):
        n_energia = 2
    elif (energia >= 8 and energia <= 11):
        n_energia = 3
    elif (energia >= 5 and energia <= 8):
        n_energia = 4
    else:
        n_energia = 5

    # Cálculo do parâmetro de resíduos
    if (residuo > 50):
        n_residuo = 5
    elif (residuo >= 41 and residuo <= 50):
        n_residuo = 4
    elif (residuo >= 31 and residuo <= 40):
        n_residuo = 3
    elif (residuo >= 20 and residuo <= 30):
        n_residuo = 2
    else:
        n_residuo = 1

    # Cálculo do parâmetro de transporte
    if (transporte == 'PV'):
        n_transporte = 1
    elif (transporte == 'PVU'):
        n_transporte = 2
    elif (transporte == 'PU'):
        n_transporte = 3
    elif (transporte == 'E'):
        n_transporte = 4
    elif (transporte == 'BC'):
        n_transporte = 5

    # Média geral
    n_sustentabilidade = (n_energia + n_agua + n_residuo + n_transporte) / 4
    return n_energia, n_agua, n_residuo, n_transporte, n_sustentabilidade


def grafico(usuario):
    limpar_tela()
    print('\n                                     GRÁFICO DE NOTAS')
    print('====================================================================================================')
    print('|                     GRÁFICO CONSTRUIDO COM BASE NOS ÚLTIMOS 5 REGISTROS                          |')
    print('====================================================================================================')

    if usuario not in registros or not registros[usuario]:
        print("* ❌ Nenhum registro encontrado!")
        input("\nPressione ENTER para voltar...")
        return

    registros_usuario = registros[usuario][-5:]  # pegar os ultimos 5 registros
    datas = [r[0].strftime('%d/%m') for r in registros_usuario]
    notas = [r[5] for r in registros_usuario]

    # desenho do gráfico
    print(f"\nEvolução da nota de sustentabilidade - {usuario}")
    print(f"Datas: {' | '.join(datas)}\n") #pegar as datas dos registros

    for y in range(5, 0, -1):  # notas de 5 a 1
        linha = f"{y} | "
        for nota in notas:
            linha += "■ " if nota >= y else "  "
        print(linha)

    print("  +" + "―" * (len(notas) * 2))
    print("    " + " ".join(str(i + 1) for i in range(len(notas))))

    opcao = input("\nAperte ENTER para retornar ao menu: ")
    if opcao == '':
        return

def mostrar_tela_recomendacoes(usuario):
    limpar_tela()
    print("\n" + "=" * 80)
    print(f"   ANÁLISE E RECOMENDAÇÕES - {usuario.upper()}")
    print("=" * 80)

    if usuario not in registros or not registros[usuario]:
        print("* ❌ Nenhum dado de sustentabilidade encontrado.")
        input("\nPressione ENTER para voltar...")
        return

    dados_atuais = registros[usuario][-1]  # Último registro
    nota_energia = dados_atuais[1]
    nota_agua = dados_atuais[2]
    nota_residuo = dados_atuais[3]
    nota_transporte = dados_atuais[4]

    # Mapeamento das classificações baseado na tabela de parâmetros
    classificacoes = {
        "energia": {
            1: "Alto consumo",
            2: "Consumo elevado",
            3: "Consumo moderado",
            4: "Baixo consumo",
            5: "Consumo excelente"
        },
        "agua": {
            1: "Alto consumo",
            2: "Consumo elevado",
            3: "Consumo moderado",
            4: "Baixo consumo",
            5: "Consumo excelente"
        },
        "residuo": {
            1: "Alto impacto",
            2: "Impacto elevado",
            3: "Impacto moderado",
            4: "Baixo impacto",
            5: "Impacto irrelevante"
        },
        "transporte": {
            1: "Alto impacto",
            2: "Impacto elevado",
            3: "Impacto moderado",
            4: "Baixo impacto",
            5: "Nenhum impacto"
        }
    }

    dados = {
        "Consumo de energia": {
            "nota": nota_energia,
            "classificacao": classificacoes["energia"][nota_energia],
            "recomendacao": "Trocar lâmpadas por LED, Evite deixar celular carregando a noite toda e Apague as luzes ao sair de um cômodo."
        },
        "Consumo de água": {
            "nota": nota_agua,
            "classificacao": classificacoes["agua"][nota_agua],
            "recomendacao": "Instalar redutores de vazão, consertar vazamentos e reduzir tempo do banho."
        },
        "Geração de resíduos": {
            "nota": nota_residuo,
            "classificacao": classificacoes["residuo"][nota_residuo],
            "recomendacao": "Separar o lixo reciclável, evitar descartáveis e reutilizar embalagens."
        },
        "Uso de transporte": {
            "nota": nota_transporte,
            "classificacao": classificacoes["transporte"][nota_transporte],
            "recomendacao": "Usar bicicleta, transporte público ou incentivar caronas e veículos elétricos."
        }
    }

    for acao, info in dados.items():
        print(f"\n🔹 {acao}")
        print(f"   Nota: {info['nota']} - {info['classificacao']}")
        if info["nota"] < 5:
            print(f"   🔧 Recomendações: {info['recomendacao']}")
        else:
            print("   ✅ Excelente! Continue assim!")

    print("\nPressione ENTER para voltar ao menu.")
    input()



area_login()

