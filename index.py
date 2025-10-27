import math 
import operacoes

resultado = operacoes.soma(5, 3)
print(resultado) # Saida: 8

raio = float(input("Raio: "))
area = math.pi * math.pow(raio, 2)
print(f"Área: {area:.2f}")