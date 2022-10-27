# Parte A da Aula 2 - 26/10/2022

# comando input(): quero permitir que o usuário digite algo 

nome = input("Digite seu nome: ")

# comando de saída - exibir na tela

print(f"Boa noite, senhor(a) {nome}")

# Pede a idade ao usuário - Qual sua idade?

idade = int(input("Qual sua idade: "))

# Exiba sua idade

print(f"Sua idade é {idade}")

# E seu eu quisesse mostra o dobro da idade informada

dobro = idade * 2
print(f"O dobro da idade informada é {dobro}")

# Estrutura condicional - o famoso "SE" (if) 
# Se a pessoa for maior de idade, mostre "Você é maior de idade, ótimo! Ja pode beber ou dirigir"

if idade >= 18:
  print("Você é maior de idade, ótimo! Já pode começar a beber ou dirigir")
else:
  print("Você é menor de idade, sem bebida para você")

# E se eu quiser perguntar o genêro ( M = Masculino e F = Feminino)
# Mostre se você precisa prestar ou prestou o servico militar obrigatório

genero = input("Informe o genêro M = Masculino, F = Feminino, O = Outros: ")
if idade >=18 and genero == "M":
 print("... e você também precisa/precisou prestar serviço militar obrigatório")