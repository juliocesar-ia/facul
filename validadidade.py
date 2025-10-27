try:
    idade = int(input("Idade: "))
    if idade < 0:
        raise ValueError("Idade nao pode ser negativa.")
    print(f"Idade valida: {idade} anos!")
except ValueError as e:
    print("Erro:", e)