distancia = float (input("Qual seria a distância da viagem?: \n"))
consumo = float (input("Consumo do carro: \n"))
custo = 0
preço = float (input("preço da gasolina: \n"))
litros = distancia/consumo
custo = litros*preço
print("Litros necessários: %.2f"%(litros))
print("Custo da viagem: %.2f"%(custo))