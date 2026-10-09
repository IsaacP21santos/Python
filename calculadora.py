import tkinter as tk


def abrir_calculadora(janela_principal):
    calculadora = tk.Toplevel(janela_principal)

    calculadora.title("Calculator")
    calculadora.geometry("350x350")
    calculadora.resizable(False, False)

    titulo = tk.Label(
        calculadora,
        text="Calculator",
        font=("Arial", 20)
    )
    titulo.pack(pady=20)

    label_num1 = tk.Label(
        calculadora,
        text="Type the first number:"
    )
    label_num1.pack()

    campo_num1 = tk.Entry(calculadora)
    campo_num1.pack(pady=5)

    label_num2 = tk.Label(
        calculadora,
        text="Type the second number:"
    )
    label_num2.pack()

    campo_num2 = tk.Entry(calculadora)
    campo_num2.pack(pady=5)

    result = tk.Label(
        calculadora,
        text="Result:",
        font=("Arial", 12)
    )
    result.pack(pady=15)

    def obter_numeros():
        num1 = float(campo_num1.get())
        num2 = float(campo_num2.get())

        return num1, num2

    def somar():
        try:
            num1, num2 = obter_numeros()
            resultado = num1 + num2

            result.config(
                text=f"Result: {resultado}"
            )

        except ValueError:
            result.config(
                text="Please enter valid numbers."
            )

    def subtrair():
        try:
            num1, num2 = obter_numeros()
            resultado = num1 - num2

            result.config(
                text=f"Result: {resultado}"
            )

        except ValueError:
            result.config(
                text="Please enter valid numbers."
            )

    def multiplicar():
        try:
            num1, num2 = obter_numeros()
            resultado = num1 * num2

            result.config(
                text=f"Result: {resultado}"
            )

        except ValueError:
            result.config(
                text="Please enter valid numbers."
            )

    def dividir():
        try:
            num1, num2 = obter_numeros()

            if num2 == 0:
                result.config(
                    text="Cannot divide by zero."
                )
                return

            resultado = num1 / num2

            result.config(
                text=f"Result: {resultado}"
            )

        except ValueError:
            result.config(
                text="Please enter valid numbers."
            )

    area_botoes = tk.Frame(calculadora)
    area_botoes.pack()

    botao_somar = tk.Button(
        area_botoes,
        text="Sum",
        width=12,
        command=somar
    )
    botao_somar.grid(row=0, column=0, padx=5, pady=5)

    botao_subtrair = tk.Button(
        area_botoes,
        text="Subtract",
        width=12,
        command=subtrair
    )
    botao_subtrair.grid(row=0, column=1, padx=5, pady=5)

    botao_multiplicar = tk.Button(
        area_botoes,
        text="Multiply",
        width=12,
        command=multiplicar
    )
    botao_multiplicar.grid(row=1, column=0, padx=5, pady=5)

    botao_dividir = tk.Button(
        area_botoes,
        text="Divide",
        width=12,
        command=dividir
    )
    botao_dividir.grid(row=1, column=1, padx=5, pady=5)