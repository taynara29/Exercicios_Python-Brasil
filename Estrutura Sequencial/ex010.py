# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.  "15 x 1,8 = 27 + 32 = 59 ºF"

# enquanto for verdade
while True:
    #tente
    try: 
        temperatura = float(input("Informe a temperatura em graus Celsius: "))
        Fahrenheit = (temperatura * 1.8) + 32
        # quebrar (sair do laco "while")
        break
    # excecao - faca a excecao
    except:
        print("Digite apenas numeros")

print(Fahrenheit)