import os

Restaurantes = [{'nome': 'Sr.Coffe', 'categoria': 'Cafe expresso' , 'ativo': False} ,    
                {'nome': 'Sr. Sushi','categoria': 'Comida japonesa', 'ativo': True} ]

def exibir_nome_do_programa():
    print(''' 
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░████████████████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀░░████████████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█
█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░░░▄▀░░░░████████████████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░███░░▄▀░░██████████████████░░▄▀░░█████████░░▄▀░░████░░▄▀░░███░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█
█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░███░░▄▀░░███░░░░░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
█░░░░░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░███░░▄▀░░███░░░░░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░░░███░░▄▀░░░░░░░░░░█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█
█████████░░▄▀░░█░░▄▀░░██░░▄▀░░█████████░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░██████████████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████░░▄▀░░█████████████████░░▄▀░░█░░▄▀░░██░░▄▀░░█
█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░░░▄▀░░░░████████████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░░░░░░░░░█░░░░░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀░░████████████████░░▄▀░░█████████░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█
█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░████████████████░░░░░░█████████░░░░░░██░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█
██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
      
      ''')

def exibir_opcoes():
    print('1. Cadastrar Restaurante ')
    print('2. Listar restaurante')
    print('3. Alternar restaurante')
    print('4. Sair da Conta\n')

def finalizar_app():
    os.system('cls')
    #os.system('clear')
    print('Encerrar o aplicativo')

def voltar_ao_menu_principal(): 
    input('\n Digite uma tecla para voltar para o menu inicial')   
    main()       
  
def opcao_invalida():
      print('opcao invalida!\n')
      
      voltar_ao_menu_principal()

def exibir_subtitulos(texto):
    os.system('cls')
    linha = '$' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulos('Cadastrar restaurante')
    nome_do_restaurante = input(F'Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(F'digite a categoria do restaurante que deseja cadastrar {nome_do_restaurante}:')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo':False}
    Restaurantes.append(dados_do_restaurante)
    print(f'- O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def Listar_restaurante():
     exibir_subtitulos('listando do restaurante')

     for restaurante in Restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'-{nome_restaurante.ljust(10)}  |  {categoria.ljust(10)}  |  {ativo}')

     voltar_ao_menu_principal()
        
def Alternar_restaurante():
    os.system('cls')
    print(' voce escolheu sair ')

    voltar_ao_menu_principal()
     
def alternar_estado_do_restaurante(): 
    exibir_subtitulos('alternando estado do restaurante')
    nome_restaurante = input('digite o nome do restuarante que deseja alternar o estado:\n' )
    restaurante_encontrado = False
    for restaurante in Restaurantes:
         if nome_restaurante == restaurante ['nome']: 
              restaurante_encontrado = True
              restaurante['ativo'] = not restaurante ['ativo']
              mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso\n' if restaurante ['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso\n'
              print(mensagem)
    if not restaurante_encontrado:
         print('O restaurante não foi encontrado\n')

         voltar_ao_menu_principal()  
           
def escolher_opcoes():
    try:
        opcao_escolhida = int(input('escolha uma opcao: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
                cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
                Listar_restaurante()
        elif opcao_escolhida == 3:
                alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
                finalizar_app()
        else:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    voltar_ao_menu_principal()

if __name__ == '__main__':
    main()
