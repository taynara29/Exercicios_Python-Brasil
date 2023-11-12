# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

#traducao: enquanto for verdade
while True:
    #tente
    try:
        numero = float(input("digite um numero "))
        # quebra do loop (while)
        break
    # faca a exceção
    except:
        print("Digite apenas numeros")

print(numero)