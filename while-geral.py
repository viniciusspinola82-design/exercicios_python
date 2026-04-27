i= 50
while i >= 0:
    print (i)
    i = i -1
    print ("\n")
print ("end")
print ("\n")

x = 10
while not (x == 0):
    x= x-1
    if x % 2 != 0:
        print (x)
terminou = False
p = i = 0
while (not terminou):
    n = int (input("Digite um número, ou zero para terminar: \n"))
    if n == 0:
        terminou = True

    else:
        if n % 2== 0:
            p = p +1
        else:
            i = i +1 
print ("P = ", p)
print("I = ", i)
frutas = ["banana", "Maçã", "uva", "morango"]
for item in frutas:
    print (item)

lista = [12,33,4,6,553,5,3,444,56,45,22,45,76,88,66]
for i in lista:
    print (i)