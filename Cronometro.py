import tkinter as tk
import time

class Cronometro:
    def __init__(self, master):
        self.master = master
        self.master.title("> Cronômetro <")
        self.tempo = 0
        self.running = False
        self.display = tk.Label(self.master, text="00:00:00", font=("Helvetica", 56), bg="blue")
        self.display.pack()
        self.btn_iniciar = tk.Button(self.master, text="Iniciar!", command=self.iniciar, width=13)
        self.btn_iniciar.pack(side=tk.LEFT)
        self.btn_parar = tk.Button(self.master, text="Parar!", command=self.parar, state=tk.DISABLED, width=13)
        self.btn_parar.pack(side=tk.LEFT)
        self.btn_resetar = tk.Button(self.master, text="Reset", command=self.resetar, state=tk.DISABLED, width=13)
        self.btn_resetar.pack(side=tk.LEFT)

    def atualizar_tempo(self):
        if self.running:
            self.tempo += 1
            self.display.config(text=time.strftime("%H:%M:%S", time.gmtime(self.tempo)))
            self.master.after(1000, self.atualizar_tempo)

    def iniciar(self):
        if not self.running:
            self.running = True
            self.btn_iniciar.config(state=tk.DISABLED)
            self.btn_parar.config(state=tk.NORMAL)
            self.btn_resetar.config(state=tk.NORMAL)
            self.atualizar_tempo()

    def parar(self):
        if self.running:
            self.running = False
            self.btn_iniciar.config(state=tk.NORMAL)
            self.btn_parar.config(state=tk.DISABLED)

    def resetar(self):
        self.tempo = 0
        self.display.config(text="00:00:00")
        self.btn_resetar.config(state=tk.DISABLED)
        self.btn_parar.config(state=tk.DISABLED)
        self.btn_iniciar.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    cronometro = Cronometro(root)
    root.mainloop()
