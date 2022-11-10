# Parte A da Aula 3 - 09/11/2022

contador = 1

# Exibir do 1 ate o 10 repetidamente

while (contador <=10):
  print(contador)
  contador = contador+1
  
# Laço for (python for = for each)

fruta = "morango"
print(fruta)

fruta1 = "morango"
fruta2 = "laranja"
fruta3 = "pêra"

# Lista 

frutas = ["morango", "laranja", "pêra"]

# Mostra todas 

print(frutas)

# Quero exibir apenas a 3a. fruta

print(frutas[2])

# Exibir quantas frutas tem na minha lista 

print(len(frutas)) # length = tamanho

# Quero incluir uma fruta nova
frutas.append("manga")

print(len(frutas)) # length = tamanho
print(frutas)

print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
#print(frutas[4])

print("Exemplo das frutas com while")
frutas.append('uva')

i=0
while(i<len(frutas)):
  print(frutas[i])
  i = i+1

print("Exemplo das frutas com FOR")
for fruta in frutas:
  print(fruta)