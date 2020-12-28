a = 10
b = 5

aux = a

a = b

b = aux

print(a)
print(b)

#Melhor forma de fazer em Python

a, b = b, a

print(a)
print(b)