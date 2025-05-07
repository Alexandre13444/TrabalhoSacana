A = int(input("Digite 1 (VERDADEIRO) ou 0 (FALSO) para A: "))
B = int(input("Digite 1 (VERDADEIRO) ou 0 (FALSO) para B: "))

if A == B:
    print("Ambos são", "VERDADEIRO" if A == 1 else "FALSO")
elif A + B >= 3:
    print("Os valores não são booleanos")
