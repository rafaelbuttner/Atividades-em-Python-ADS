import tkinter as tk
from tkinter import messagebox

class ListaDeTarefas:
    def __init__(self, master):
        self.master = master
        self.master.title('>>> Lista de Tarefas <<<')

        self.tarefas = []

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.texto_tarefa = tk.Entry(self.frame, width=50)
        self.texto_tarefa.pack(side=tk.LEFT)

        self.btn_adicionar = tk.Button(self.frame, text='Adicionar', command=self.adicionar_tarefa)
        self.btn_adicionar.pack(side=tk.LEFT)

        self.lista_box = tk.Listbox(self.master, width=50, height=10)
        self.lista_box.pack()

        self.btn_remover = tk.Button(self.master, text='Remover', command=self.remover_tarefa)
        self.btn_remover.pack()

    def adicionar_tarefa(self):
        tarefa = self.texto_tarefa.get()
        if tarefa:
            self.tarefas.append(tarefa)
            self.lista_box.insert(tk.END, tarefa)
            self.texto_tarefa.delete(0, tk.END)
        else:
            messagebox.showwarning('Aviso', 'Tarefa vazia.')

    def remover_tarefa(self):
        try:
            indice = self.lista_box.curselection()[0]
            del self.tarefas[indice]
            self.lista_box.delete(indice)
        except IndexError:
            messagebox.showwarning('Aviso', 'Selecione uma tarefa para remover.')

if __name__ == '__main__':
    root = tk.Tk()
    app = ListaDeTarefas(root)
    root.mainloop()
