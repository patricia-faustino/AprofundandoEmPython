devas = ["Alini", "Alicia","Luciana", "Renata", "Fabricia"]
nome_com_a = 0

for nome in devas:
     if nome[0] == "A" or nome[0] == "a":
        nome_com_a +=1

print(f"Temos {nome_com_a} desenvolvedoras que tem a inicial A")