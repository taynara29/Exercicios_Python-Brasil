# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

pi = 3.14

while True:
    try:
        raio = float(input("Digite o raio do circulo: "))
        area = pi * raio**2
        break
    
    except:
        print("Invalido. Por favor digite um numero!")
    
print(f"A area do circulo e: {area}")