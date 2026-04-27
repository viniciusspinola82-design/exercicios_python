nota1 = float (input("Qual é o valor da n1? \n"))
nota2 = float (input("Qual é o valor da n2? \n"))
media = (nota1+nota2)/2
if media <7:
    print(f"Reprovado! \n Sua nota é de {media:.2f}")
elif (media == 10):
    print(f"Aprovado com distinção! \n Sua nota é de {media:.2f}")
elif media >=7:
    print (f"Aprovado! \n Sua nota é de {media:.2f}")
else:
    print("Encerrando.")