peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura ** 2)

print("Seu IMC é:", round(imc, 2))

if imc < 18.5:
    print("Abaixo do peso")
elif imc <= 24.9:
    print("Peso ideal (parabéns)")
elif imc <= 29.9:
    print("Levemente acima do peso")
elif imc <= 34.9:
    print("Obesidade grau I")
elif imc <= 39.9:
    print("Obesidade grau II (severa)")
else:
    print("Obesidade grau III (mórbida)")
