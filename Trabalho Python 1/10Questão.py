notas = []
for i in range(3):
    notas.append(float(input(f"Digite a {i+1}ª nota: ")))
media = sum(notas) / 3
print("Média das notas:", round(media, 2))
