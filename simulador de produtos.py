cont= 0
valor =  0.0
media = 0.0
total = 0.0
imposto = 0.12
desconto = 0.05

nome = (input("Digite o seu nome: \n"))
while (cont<3):
 produto = float (input("Digite o valor do produto: \n"))
 cont = cont+1
 valor = valor + produto
 total = valor
media = total/3 
print("Total da compra: R$ %.2f "%(total), "\nA média dos produtos será de R$: %.2f"%(media))

extrato= (total*imposto) - desconto

print ("incluindo os descontos e impostos: %.2f "% (extrato))

print ("Extrato: \n")
print("Nome: ",nome, "\n","total da compra: %.2f "% (total), "\n", "média das compras: %.2f"% (media), " e os valores com descontos e impostos: %.2f"% (extrato))