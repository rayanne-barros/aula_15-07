try:
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    resultado = numero1 / numero2
    print("O resultado da divisão é: ", resultado)

except ValueError:
    print("Digite apenas números inteiros.")

except ZeroDivisionError:
    print("Não é possível dividir por zero.")