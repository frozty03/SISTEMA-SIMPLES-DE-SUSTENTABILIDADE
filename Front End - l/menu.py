import getpass #getpass é para censurar, só que eu nao sei como usar

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


def menu_login(usuario):
    while True:
        print('\n                                             MENU')
        print('====================================================================================================')
        print(f'| * Usuário: {usuario}                                                                                     |')
        print('|--------------------------------------------------------------------------------------------------|')
        print('|    1. Cadastro de informações | 2. Lista de gráficos | 3. Ações (recomendações) | 4. Relatório   |')
        print('|                   5. Parâmetros   |   6. Histórico de cadastros   |   7. Sair                    |')
        print('====================================================================================================')

        opcao = input('Escolha uma opção (1-7): ')
        if opcao == '7': #por as outras opções em cima, em ordem(depois substituir por elif)
            print('Voltando a área de login...')
            break



area_login()

#CADASTRO DE INFORMAÇÕES: abrir parte de inserir as informações de cada parametro, calcular (usa a tabela de parametros que está figma)
#LISTA DE GRÁFICOS: colocar opções de período (gráficos da semana, do dia e do mês) e criar gráfico com base nos cadastros de informações
#AÇÕES: mostrar as notas do último cadastro e recomendar ações para melhora com base nisso
#RELATÓRIO: mostrar as notas dos 3 ultimos cadastros, simbolizar se melhorou ou se piorou
#PARÂMETROS: colocar a tabela de parâmetros
#HISTÓRICO DE CADASTROS: mostrar todos os outros cadastros e opção de editar informação

