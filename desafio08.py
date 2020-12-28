quemJaFoi = int(input("Paticipantes que já participaram do evento: "))
totalParticipantes = int(input("Total de participantes: "))
totalIngressos = int(input("Total de ingressos: "))

quemNuncaFoi = totalParticipantes - quemJaFoi

if(totalIngressos >= totalParticipantes):
    print("Todos irão!")
elif(quemNuncaFoi <= totalIngressos):
    print("Todos que nunca foram, irão")

else:
    print("Será necessário sorteio.")

