rosa, roxo, azul = map(int, input("Digite a quantidade,separado por vírgula, de pessoas que preferem os brindes na cor rosa, roxo,azul: ")
                       .split(","))
total = rosa + roxo + azul

porcentagemRosa = (rosa / total) * 100
porcentagemRoxo = (roxo / total) * 100
porcentagemAzul = (azul / total) * 100

print(f"A porcentagem de pessoas que preferem o brinde na cor rosa: {porcentagemRosa:.2f}%")
print(f"A porcentagem de pessoas que preferem o brinde na cor roxo: {porcentagemRoxo:.2f}%")
print(f"A porcentagem de pessoas que preferem o brinde na cor azul: {porcentagemAzul:.2f}%")
