import os

restaurantes = [{'nome': 'Feijoada', 'categoria': 'portuguesa', 'ativo': False},
                {'nome': 'Lasanha', 'categoria': 'comida boa', 'ativo': True},
                {'nome': 'Filé de Peixe', 'categoria': 'prato gostoso', 'ativo': False}]


def exibir_nome_do_programa():
    """
    Exibe o nome do programa de forma estilizada.
    """
    print("""
      
██████████████████████████████████████████████████████████████████████████
█─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
█▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
      """)


def exibir_opcoes():
    """
    Exibe as opções disponíveis para o usuário.
    """
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair')


def finalizar_app():
    """
    Finaliza a execução do programa.
    """
    exibir_subtitulo('Finalizando o app \n')


def voltar_ao_menu_principal():
    """
    Pede ao usuário para digitar uma tecla para voltar ao menu principal.
    """
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()


def opcao_invalida():
    """
    Exibe uma mensagem de opção inválida.
    """
    print('Opção inválida\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    """
    Exibe um subtítulo formatado.
    """
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():
    """
    Cadastra um novo restaurante na lista de restaurantes.
    """
    exibir_subtitulo('Cadastrar Novo Restaurante\n')
    nome_do_restaurante = input('\nDigite o nome do restaurante: ')
    categoria = input('Digite a categoria do restaurante: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante ({nome_do_restaurante}) e sua categoria ({categoria}) foram cadastrados com sucesso')
    voltar_ao_menu_principal()


def listar_restaurantes():
    """
    Lista os restaurantes cadastrados.
    """
    exibir_subtitulo('Listando restaurantes')
    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    """
    Alterna o estado (ativo/inativo) de um restaurante.
    """
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('\nDigite o nome do restaurante: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')

    voltar_ao_menu_principal()


def escolhendo_opcoes():
    """
    Lê a opção escolhida pelo usuário e chama a função correspondente.
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            print('Finalizando aplicativo')
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()


def main():
    """
    Função principal do programa.
    """
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolhendo_opcoes()


if __name__ == '__main__':
    main()
