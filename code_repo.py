# code_repo.py
def main():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))

    print("a =", a)
    print("b =", b)
    print("soma (a + b) =", a + b)
    print("subtração (a - b) =", a - b)
    print("multiplicação (a * b) =", a * b)
    if b != 0:
        print("divisão (a / b) =", a / b)
    else:
        print("divisão por zero não é permitida")

if __name__ == "__main__":
    main()