n1= float (input("Digite a n1: "))
n2= float (input("Digite a n2: "))
n3= float (input("Digite a n3: "))
n4= float (input("Digite a n4: "))

media = (n1+n2+n3+n4) / 4

if media >= 7:
    print (f"MEDIA: {media} ->>> Aprovado! \n")
elif media < 6 and media >= 4.0:
    print(f"MEDIA: {media} ->>> EXAME!")
else:
    print (f"MEDIA:{media} ->>> Reprovado! \n")