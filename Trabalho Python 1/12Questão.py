valor = float(input("Digite o valor do produto: "))
print("1 - À Vista Dinheiro/Pix (15% desc)")
print("2 - À Vista no Cartão (10% desc)")
print("3 - 2x no Cartão (sem juros)")
print("4 - 3x ou mais no Cartão (10% juros)")
codigo = int(input("Escolha a forma de pagamento (1 a 4): "))

if codigo == 1:
    total = valor * 0.85
elif codigo == 2:
    total = valor * 0.90
elif codigo == 3:
    total = valor
elif codigo == 4:
    total = valor * 1.10
else:
    total = valor
    print("Código inválido, valor original considerado.")

print("Valor a ser pago: R$", round(total, 2))
