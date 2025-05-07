a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Triângulo Equilátero")
    elif a == b or b == c or a == c:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Não é um triângulo válido")
