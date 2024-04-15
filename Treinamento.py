import os

def exbir_nome_do_programa():

    print('Cyber.TI\n')

def opcao_de_escolha():
    print('1. Quem somos')
    print('2. Serviços gerenciados')
    print('3. Contratar seriços')
    print('4. Suporte ao cliente')
    print('5. Sair do aplicativo\n')
    
def opcao_invalida():
    print('opcao invalida!\n')
    input('Digite uma tecla para voltar para o menu inicial')
    main()

def exbir_informacoes():
    os.system('cls')
    print('Somos empresa de suprote de T.I com o melhor atendimento e suporte ao cliente do mercado, tendo com base dessa afirmacao a opniao de diversos de diretores como:')
    input('\ndigite uma tecla para voltar ao menu')
    main()   

def opcao_escolhida():
    try: 
        opcao_escolhida = int(input('escolha uma opcao: '))
      
        # opcao_escolhida = int(opcao_escolhida)
        os.system('cls')
        if opcao_escolhida == 1 :
            exbir_informacoes()

        elif opcao_escolhida == 2:
            print('WebProtection, antivirus, data recovery, backup')

        elif opcao_escolhida == 3 :
            print('para consultar valores entre em contato com o nosso time comercial')

        elif opcao_escolhida == 4 :
            print(' Clique nesse link e te encaminharemos para um de nossos analistas')

        elif opcao_escolhida == 5 :
            print('Até mais!')

        else:
            opcao_invalida()
    except:
        opcao_invalida()      


def main():
    os.system('cls')
exbir_nome_do_programa()
opcao_de_escolha()
opcao_escolhida()




if __name__ == '__main__':
    main()




