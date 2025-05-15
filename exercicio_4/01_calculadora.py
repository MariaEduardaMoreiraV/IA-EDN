while True:
    try:
        numero1 = float(input("Digite primeiro número: "))
        numero2 = float(input("Digite o segundo número"))
        operacao = input("Digite a operação (+, -, *, /):")
        if operacao == "+":
            resultado = numero1 + numero2
        elif operacao == "-":
            resultado = numero1 - numero2
        elif operacao == "*":
            resultado = numero1 * numero2
        elif operacao == "/":
            resultado = numero1 / numero2
            if numero2 == 0:
                print("Erro: divisão por zero")
                continue
            resultado = numero1 / numero2
        else:
            print("Erro operação inválida: Use (+, -, *, /): ")
            continue 
        print(f"Resultado: {resultado:.2f}")
        break
    except ValueError:
        print("Erro: digite apenas números.")