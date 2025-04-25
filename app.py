import os
restaurantes=[{'nome':'minha cozinha','categoria':'salgada','ativo':False},
              {'nome':'minha cozinha','categoria':'mineiro','ativo':True},
              {'nome':'almoco','categoria':'comida mineira','ativo':False},]

def exibir_nome_do_programa():
    '''exibe o nome estilizado do programa na tela'''
    print ('minha cozinha\n')

def exibir_opções():
    '''exibe as opcoes disponiveis no menu principal'''
    print('1- Cadastrar restaurante')
    print('2- Listar restaurante')
    print('3- Alternar estado de restaurante')
    print('4- Sair\n')

def Encerrando_programa():
    '''exibe mensagem de finalizacao do aplicativo'''
    exibir_subtitulo('Encerrando o programa')

def voltar_ao_menu_principal():
    '''solicita uma tecla para voltar ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    '''exibe mensagem de opcoes invalida e retorna ao menu principal'''
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''exibe um subtitulo estilizado na tela'''
    os.system('cls')
    linha = '-' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
    
def cadastrar_novo_restaurante():
    '''essa funcao e responsavel por cadastrar um novo restaurante'''

    exibir_subtitulo('Cadastro de novos restaurantes')
    
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante ={'nome': nome_do_restaurante,'categoria': categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()

def listar_restaurantes():
    '''lista os restaurantes presentes na lista'''
    exibir_subtitulo('Listando os restaurantes')

    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f' - {nome_restaurante} | {categoria} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    '''altera o estado ativo/desativado de um restaurante'''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
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

def escolher_opcao():
    '''solicita e executa a opcao escolhida pelo usuario'''
    try:
        opcao_escolhida= int(input('Escolha uma opção: '))
        print (f'Você escolheu a opção: {opcao_escolhida}\n')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            Encerrando_programa()
        else:
         opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''funcao principal que inicia o programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opções()
    escolher_opcao()

if __name__ == '__main__':
    main()