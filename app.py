import os
restaurantes=[{'nome':'minha cozinha','categoria':'salgada','ativo':False},
              {'nome':'minha cozinha','categoria':'mineiro','ativo':True},
              {'nome':'almoco','categoria':'comida mineira','ativo':False},]

def exibir_nome_do_programa():
    print ('minha cozinha\n')

def exibir_opções():
    print('1- Cadastrar restaurante')
    print('2- Listar restaurante')
    print('3- Ativar restaurante')
    print('4- Sair\n')
    
def Encerrando_programa():
    exibir_subtitulo("encerrando programa")
   
    
    
def cadastrar_novo_restaurante():
    exibir_subtitulo("cadastrando novo restaurante")
    nome_do_restaurante=input('digite o nome do restaurante que deseja cadastrar:')
    restaurantes.append(nome_do_restaurante)
    print(f'o restaurante{nome_do_restaurante} foicadastrado com secesso!')
    voltar_ao_menu_principal()
    
def opcao_invalida():
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()

    
def escolher_opcao():
    try:
        opcao_escolhida= int(input('Escolha uma opção: '))
        print (f'Você escolheu a opção: {opcao_escolhida}\n')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            print('Ativar restaurantes')
        elif opcao_escolhida == 4:
            Encerrando_programa()
        else:
            opcao_invalida()
    except:
         opcao_invalida()
         
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opções()
    escolher_opcao()
    

def voltar_ao_menu_principal():
    input("\ndigite uma tecla para voltar ao menu principal")
    main()
def exibir_subtitulo(texto):
    os.system("cls") 
    print(texto)
    print()
    
def listar_restaurante():
    exibir_subtitulo('listando os restaurantes')
    for restaurante in restaurantes:
        nome_restaurante=restaurante['nome']
        print(f' -{nome_restaurante}')
    voltar_ao_menu_principal()
        
if __name__ == '__main__':
    main()