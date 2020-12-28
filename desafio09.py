temperatura= int(input("Digite a temperatura: "))
umidade = int(input("Digite a umidade do ar: "))

if(umidade>=0 and umidade < 40):
    if(temperatura > 10 and temperatura < 15):
        print("Blusa de frio e regata.")
    elif(temperatura >= 15 and temperatura < 20):
        print("Blusa de frio e regata .")

    else:
        print("Regata")

else:
    if(temperatura > 10 and temperatura <15):
        print("Blusa de frio, regata e guarda-chuva")

    elif(temperatura >= 15 and temperatura < 20):
        print("Blusa de frio, regata e guarda-chuva")

    else:
        print("Regata e guarda-chuva")



