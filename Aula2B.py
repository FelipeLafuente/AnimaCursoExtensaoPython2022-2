# Parte B da Aula 2 - 26/10/2022

#Pede o nome do aluno e sua nota (de 0 a 10) e, se ele tirou nota 10, " mostra {nome}, você é bichão, mesmo..."

nome = input("Informe seu nome: ")
nota = float(input("Informe sua nota: "))

if nota == 10:
  print(f" {nome}, você é bixao mesmo hein")

elif (nota >= 6 and nota < 10):
 print(f" Bom Trabalho {nome} ")
else:
  print("Precisa estudar mais")
  