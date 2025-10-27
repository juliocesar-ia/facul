try:
    a = int(input("Digite o primeiro numero:  "))
    b = int(input("Digite o segundo numero"))

    resultado = a / b
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Erro: Divisao por zero nao e permitida.")
except ValueError:
    print("Erro: Valor invalido.")
finally:
    print("Encerrando execução...")

