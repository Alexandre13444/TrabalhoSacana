A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

Soma = A + B
print("A soma de A e B é:", Soma)

if Soma < C:
    print("A soma de A e B é menor que C")
elif Soma == C:
    print("A soma de A e B é igual C")
elif Soma > C:
    print("A soma de A e B é maior que C")
