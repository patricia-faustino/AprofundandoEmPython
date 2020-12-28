valorRefrigerantePessoa = (4 * 4) / 10

valorCoxinhaPessoa = 0.5 * 10


numerosParticipantes = int(input("Quantas mulheres participaram do curso: "))

valorCoxinhaTotal = valorCoxinhaPessoa * numerosParticipantes

valorRefrigeranteTotal = valorRefrigerantePessoa * numerosParticipantes

numeroTotalCoxinha = 10 * numerosParticipantes

litrosRefri = numerosParticipantes * 0.4

valorTotal = valorRefrigeranteTotal + valorCoxinhaTotal

print(f"Temos que comprar {litrosRefri} litros de refrigerante e {numeroTotalCoxinha} coxinhas."
      f" O valor a ser gasto será R${valorTotal:.2f}")

