## Função é um bloco de código que contem instruções de resolver alguma coisa
import sys


def exibir_menu():
    print("Escolha uma opção:")
    print("1 - Cadastrar aluno")
    print("2 - Remover Aluno")
    print("3 - Editar Aluno")
    print("4 - Listar Aluno")
    print("5 - Sair")


def cadastrar_aluno():
    print("Vai salvar esse aluno no formato json em um arquivo")
    # Fazer uma exception para verificar se CPF tem 11 digitos
    # (Opcional) Para bater as paradas: Validar o email, para verificar se é válido


def remover_aluno():
    print("Remove o aluno da lista ou arquivo ou banco de dados")


def editar_aluno():
    print("Remover da lista e criar um novo atualizado")


def listar_aluno():
    print("Mostrar os alunos cadastrados na lista/arquivo/banco")


def fechar_programa():
    sys.exit()


while True:
    exibir_menu()
    escolha = input()
    if escolha == "1":
        cadastrar_aluno()
    elif escolha == "2":
        remover_aluno()
    elif escolha == "3":
        editar_aluno()
    elif escolha == "4":
        listar_aluno()
    elif escolha == "5":
        # Fazer tratamento de exceção para não permitir deixar número maior que 5 e menor que 1
        fechar_programa()
    else:
        print("Digite uma opção válida")
