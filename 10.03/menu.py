import getpass #getpass é para censurar, só que eu nao sei como usar

from tabulate import tabulate
import os

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

usuarios = {} #simular bd
#ADICIONAR EMAIL P/ RECUPERAÇÃO DE SENHA
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
        usuarios[usuario] = senha #salvar a senha ao usuario
        print('* ✅ Cadastro realizado com sucesso!')
    print('====================================================================================================')

#ADICIONAR OPÇÃO P RECUPERAR SENHA
def login():
    limpar_tela()
    print('\n                                           LOGIN')
    print('====================================================================================================')
    usuario = input('* Usuário: ')
    senha = input('* Senha: ')

    if usuario in usuarios and usuarios[usuario] == senha: #se o usuario estiver no dict e a senha corresponder
        print(f' ✅ Login bem-sucedido! Bem-vindo, {usuario}!')
        print('====================================================================================================')
        menu_login(usuario) #iniciar o menu pós login
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




def parametros():
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

        print('\n' + '='*60)
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
            break


def menu_login(usuario):
    while True:
        limpar_tela()
        print('\n                                             MENU')
        print('====================================================================================================')
        print(f'| * Usuário: {usuario}                                                                                     |')
        print('|--------------------------------------------------------------------------------------------------|')
        print('|    1. Cadastro de informações | 2. Lista de gráficos | 3. Ações (recomendações) | 4. Relatório   |')
        print('|                                  5. Parâmetros   |    6. Sair                                    |')
        print('====================================================================================================')

        opcao = input('Escolha uma opção (1-7): ')
        if opcao == '5':
            parametros()
        elif opcao == '6': #por as outras opções em cima, em ordem(depois substituir por elif)
            print('Voltando a área de login...')
            break
        else:
            print('⚠️ Opção inválida! Tente novamente.')





area_login()

