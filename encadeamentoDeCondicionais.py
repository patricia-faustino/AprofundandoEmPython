#Descubra seu imc

massa = float(input("Informe sua massa corporal: "))
altura = float(input("Informe sua altura: "))

imc = massa / (altura * altura)

if(imc < 18):
    print("Abaixo do recomendado.")

else:
    if(imc >= 18 and imc < 26):
        print("Recomendado")

    else:
        print("Não recomendado.")

print(imc)
print("Independente do seu IMC, ame-se.")