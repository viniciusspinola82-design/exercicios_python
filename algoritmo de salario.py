salario = float (input("Digite seu salário atual: \n"))
if salario <500:
   reajuste = salario *0.15
   novo_salario = salario + reajuste
   print (f"O Reajuste é de R$: {reajuste:.2f} \n seu Salário atual é de R$: {novo_salario}")
elif (salario >= 500) and (salario<1200):
   reajuste = salario *0.10
   novo_salario = salario + reajuste
   print (f"O reajuste salarial é de R$: {reajuste:.2f} \n seu Salário atual é de R$: {novo_salario}")
elif (salario > 1000):
   reajuste = salario *0.05
   novo_salario = salario + reajuste
   print (f"O reajuste salárial é de R$: {reajuste:.2f} \n seu Salário atual é de R$: {novo_salario}")
else:
   print("Saindo..")
