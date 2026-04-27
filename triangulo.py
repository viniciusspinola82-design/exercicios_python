n1= float (input("Digite o valor do n1: \n"))
n2 = float (input("Digite o valor do n2: \n"))
n3 = float (input("digite o valor do n3: \n"))
if (n1==n2==n3):
    print("Triângulo equilátero \n")
elif (n1==n2 or n1==n3 or n2==n3):
    print("Triângulo Isósceles \n")
else: 
    print("Triângulo Escaleno")