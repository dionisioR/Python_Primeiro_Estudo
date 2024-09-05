a = 3
print(a)

b = 5
print(b)

c = "10"

print(a + b)
# print(a + c) # Erro - não é possível soma número e string

print(type(a))
print(type(b))
print(type(c))

# convertendo
d = int(c)
print(d, type(d))

# Convertendo o valor da soma para string
e = str(a + b + d)
print(e, type(e))

a, b, c = 55, 44, 33
print(a, b, c)