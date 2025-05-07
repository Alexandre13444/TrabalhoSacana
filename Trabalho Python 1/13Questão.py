nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(nome, "é", "maior de idade" if idade >= 18 else "menor de idade")
