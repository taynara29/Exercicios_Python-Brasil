# Faça um Programa que peça dois números e imprima a soma.

while True:
    try:
        numero1 = float(input("Digite o primeiro numero "))
        numero2 = float(input("Digite o segundo numero "))
        break
    except:
        print("Digite apenas numeros")
        
soma = numero1 + numero2

print(soma)