nome = input("Digite o nome do aluno: ")
notas = []
for i in range(4):
    notas.append(float(input(f"Digite a {i+1}ª nota: ")))
media = sum(notas) / 4
print("Aluno:", nome)
print("Média:", round(media, 2))
print("Situação:", "Aprovado" if media >= 7 else "Reprovado")
