class Calculator():

    @staticmethod
    def somar(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtrair(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiplicar(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def dividir(a: float, b: float) -> float | None:
        if b == 0:
            print("- ERRO: Divisão por 0 detectada!")
            return None
        return a / b

    @staticmethod
    def calcular(a: float, b: float, operador: int) -> float | None:
        match operador:
            case 1:
                return Calculator.somar(a, b)
            case 2:
                return Calculator.subtrair(a, b)
            case 3:
                return Calculator.multiplicar(a, b)
            case 4:
                return Calculator.dividir(a, b)