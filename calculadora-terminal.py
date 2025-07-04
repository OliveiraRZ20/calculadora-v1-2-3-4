from os import system, name

def limpar_terminal() -> None:
    # limpar o terminal dependendo do sistema operacional
    # 'nt' é para Windows, qualquer outro é para Unix/Linux/Mac
    system("cls" if name == "nt" else "clear")

def somar(a: float, b: float) -> float:
    return a + b

def subtrair(a: float, b: float) -> float:
    return a - b

def multiplicar(a: float, b: float) -> float:
    return a * b

def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("- ERRO: Divisão por 0 detectada!")
    return a / b

def calcular(a: float, b: float, operador: int) -> float:
    match operador:
        case 1:
            print(f"\nResultado da soma: {a} + {b} = {somar(a, b)}")
        case 2:
            print(f"\nResultado da subtração: {a} - {b} = {subtrair(a, b)}")
        case 3:
            print(f"\nResultado da multiplicação: {a} * {b} = {multiplicar(a, b)}") 
        case 4:
            print(f"\nResultado da divisão: {a} / {b} = {dividir(a, b)}")

def captar_operador() -> int:
    try:
        operador: int = int(input("Digite o número da operação desejada (1-4): "))
        while operador not in (1, 2, 3, 4):
            print("- ERRO: Operação inválida. Por favor, escolha entre 1 e 4.")
            operador = int(input("Digite o número da operação desejada (1-4): "))
    except ValueError:
        print("- ERRO: Entrada inválida. Por favor, insira um número entre 1 e 4.")
        return captar_operador()
    return operador

def captar_entrada() -> tuple[float, float]:
    try:
        a: float = float(input("Digite o primeiro número: "))
        b: float = float(input("Digite o segundo número: "))
        return a, b
    except ValueError:
        print("- ERRO: Entrada inválida. Por favor, insira números válidos.")
        return captar_entrada()

def checar_finalizacao() -> bool:
    resposta: str = input("Deseja realizar outra operação? (s/n): ").strip().lower()
    if resposta == 's':
        return True
    elif resposta == 'n':
        print("Obrigado por usar a calculadora! Até logo!")
        return False
    else:
        print("- ERRO: Resposta inválida. Por favor, responda com 's' ou 'n'.")
        return checar_finalizacao()

def calculadora() -> None:
    limpar_terminal()
    print("| =============================================================== |")
    print("|             Bem-vindo à Calculadora no Terminal!                |")
    print("| =============================================================== |")
    print("| Operações disponíveis:                                          |")
    print("| 1. Soma                                                         |")
    print("| 2. Subtração                                                    |")
    print("| 3. Multiplicação                                                |")
    print("| 4. Divisão                                                      |")
    print("| =============================================================== |")
    operador: int = captar_operador()
    a, b = captar_entrada()
    calcular(a, b, operador)

if __name__ == "__main__":
    while True:
        calculadora()
        if not checar_finalizacao():
            break