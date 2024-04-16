import os

def exibir_nome_da_AI():
  print('''
    ███╗░░░███╗░█████╗░███╗░░██╗████████╗███████╗██████╗░░█████╗░
    ████╗░████║██╔══██╗████╗░██║╚══██╔══╝██╔════╝██╔══██╗██╔══██╗
    ██╔████╔██║██║░░██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝██║░░██║
    ██║╚██╔╝██║██║░░██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗██║░░██║
    ██║░╚═╝░██║╚█████╔╝██║░╚███║░░░██║░░░███████╗██║░░██║╚█████╔╝
    ╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░╚════╝░
  ''')

def exibir_opções():
  print(' 1. Iniciar AI') 
  print(' 2. Selecionar opções da AI')
  print(' 3. Voltar para o meunu')
  print(' 4. Sair da AI')
  print(' 5. Fechar Montero\n')

def Você_escolheu_me_encerrar_a_Montero():
    #opções de escolha 5
    os.system('cls')
    #os.system('cls')
    print('Você encerrou a Montero AI')

def Voltar_ao_menu_principal():
    #opções de escolha 1#opções de escolha 3
    input('Você escolheu voltar para o menu principal, digite uma tecla\n')
    main()

def opção_invalida():
    print('Você digitou uma opção invalida')
    
    Voltar_ao_menu_principal()
    
def Você_escolheu_me_iniciar():
    #opções de escolha 1
    os.system('cls')
    print('Bem vindo a Montero, a AI mais poderosa!\n')

def Selecionar_opções_da_Ai():
    #opções de escolha 2
    os.system('cls')
    print('Selecione as opções a seguir:')

def Saindo_da_AI():
    #opções de escolha 4
    os.system('cls')
    print('Você escolheu sair da AI')

def opçao_selecionada():
    try:
        opçao_selecionada = int(input('escolha uma opcao:'))
        # opcao_escolhida = int(opcao_escolhida)
        if opçao_selecionada == 1 :
                Você_escolheu_me_iniciar()
        elif opçao_selecionada == 2 :
                Selecionar_opções_da_Ai()
        elif opçao_selecionada == 3 :
                Voltar_ao_menu_principal()
        elif opçao_selecionada == 4 :
                Saindo_da_AI()
        elif opçao_selecionada == 5 :
                Você_escolheu_me_encerrar_a_Montero()   
        else: 
                opção_invalida()    
    except:
        opção_invalida()

def main():
## Chamando as funções
    os.system('cls')
    exibir_nome_da_AI()
    exibir_opções() 
    opçao_selecionada()
    

if __name__ == '__main__':
    main()