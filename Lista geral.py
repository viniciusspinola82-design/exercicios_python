##uma lista com comandos de indíce (começo e fim)
##ex: "print (variavel [1:3])", ele vai começar do indíce 1 e vai acabar no 2, pq a barreira seria o 3
#ou seja, é uma subtração. ex: 3-1= 2
uma_lista = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(uma_lista[1:4])
print (uma_lista[:4])
print (uma_lista[3:])
print (uma_lista[:])
print (uma_lista[0:6])
print(uma_lista[1])
print (uma_lista)
uma_lista[1:1] = ['b','c']
print (uma_lista)
del uma_lista[0]
uma_lista[4:4] = ['e']
uma_lista [9:9] = ['x', 'y']
print (uma_lista)
##serve para armazenar dados de forma mais rapida no (enquanto/while)
uma_lista.append (10)
print (uma_lista)
#sort serve para organizar de forma crescente numa lista automaticamente
#lista.sort (reverse=True) ordena valores de ordem reserva
print ("\n")
a = [88,82,88,81,83,88]
b = ["Vinicius", "Batista", "Spinola"]
a.sort()
b.sort()
print (a)
print (b)
#########################################################################
a.sort(reverse=True)
b.sort(reverse=True)
print(a)
print(b)
##index serve para localizar um indíce da lista
#ex:
print (a.index(83))
##insert serve para implementar um número ou nome numa posição da lista, assim como o append
#ex:
a.insert(1,2043)
print (a)
## count serve para mostrar quantos numeros ou letras repetem na lista
#ex:
print (a)
print(a.count(88))
##O pop serve para deletar algo dentro da lista, independente da posição, assim como o del
#ex:
a.pop()
print(a)
##OU
print ("\n")
a.pop(0)
print (a)

##Sum serve para somar itens da lista de forma rápida