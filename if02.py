#Descubra seu imc

massa = float(input("Informe sua massa corporal: "))
altura = float(input("Informe sua altura: "))

imc = massa / (altura * altura)

if(imc < 18):
    print("Abaixo do recomendado.")

if(imc >= 18 and imc < 26):
    print("Recomendado.")

if(imc >= 26):
    print("Não recomendado.")

print("Você é linda. Seu IMC não te define!")