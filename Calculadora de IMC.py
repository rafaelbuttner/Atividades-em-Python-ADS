import tkinter as tk

class CalculadoraIMC:
    def __init__(self, master):
        self.master = master
        self.master.title("> Calculadora de IMC <")

        # Criação dos widgets
        self.label_peso = tk.Label(self.master, text="Peso(kg):")
        self.label_peso.grid(row=0, column=0)
        self.entry_peso = tk.Entry(self.master)
        self.entry_peso.grid(row=0, column=1)

        self.label_altura = tk.Label(self.master, text="Altura(m):")
        self.label_altura.grid(row=1, column=0)
        self.entry_altura = tk.Entry(self.master)
        self.entry_altura.grid(row=1, column=1)

        self.botao_calcular = tk.Button(self.master, text="Calcular!", command=self.calcular_imc)
        self.botao_calcular.grid(row=2, column=0, columnspan=2)

        self.label_resultado = tk.Label(self.master, text="")
        self.label_resultado.grid(row=3, column=0, columnspan=2)

    def calcular_imc(self):
        peso = float(self.entry_peso.get())
        altura = float(self.entry_altura.get())
        imc = peso / (altura ** 2)
        categoria = self.classificar_imc(imc)
        self.label_resultado.config(text=f"IMC: {imc:.2f} - Categoria: {categoria}")

    def classificar_imc(self, imc):
        if imc < 18.5:
            return 'Abaixo do peso'
        elif 18.5 <= imc < 25:
            return 'Peso normal'
        elif 25 <= imc < 30:
            return 'Sobrepeso'
        else:
            return 'Obesidade'

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraIMC(root)
    root.mainloop()
