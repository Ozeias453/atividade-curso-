import tkinter as tk
from tkinter import messagebox


class Aluno:
    def __init__(self):
        self.nome = ""
        self.serie = ""
        self.historico_notas = []
        self.frequencia = 0

    def registrar_dados(self, nome, serie):
        """Registra o nome e a série do aluno."""
        self.nome = nome
        self.serie = serie

    def registrar_frequencia(self, frequencia):
        """Registra a frequência do aluno."""
        self.frequencia = frequencia

    def adicionar_nota(self, nota):
        """Adiciona uma nova nota ao histórico."""
        self.historico_notas.append(nota)

    def calcular_media(self):
        """Calcula a média das notas do aluno."""
        if not self.historico_notas:
            return 0
        return sum(self.historico_notas) / len(self.historico_notas)

    def avaliar_evasao(self):
        """Determina se o aluno está em risco de evasão."""
        media = self.calcular_media()
        return self.frequencia < 75 or media < 70

    def gerar_relatorio(self):
        """Gera um relatório do aluno com frequência, histórico, média e status de evasão."""
        media = self.calcular_media()
        risco_evasao = self.avaliar_evasao()
        return {
            "Nome": self.nome,
            "Série": self.serie,
            "Frequência": f"{self.frequencia}%",
            "Histórico": self.historico_notas,
            "Média": round(media, 2),
            "Evasão": "Sim" if risco_evasao else "Não",
        }


class AlunoApp:
    def __init__(self, root):
        self.aluno = Aluno()

        # Nome do aplicativo
        app_name = "ATENA.APP"
        root.title(app_name)  # Define o título da janela principal

        # Exibindo o nome do aplicativo como um título na interface
        tk.Label(root, text=app_name, font=("Arial", 18, "bold"), fg="dark blue").grid(row=0, column=0, columnspan=2, pady=15)

        # Nome do aluno
        tk.Label(root, text="Nome do Aluno:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_nome = tk.Entry(root)
        self.entry_nome.grid(row=1, column=1, padx=5, pady=5)

        # Série
        tk.Label(root, text="Série do Aluno:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_serie = tk.Entry(root)
        self.entry_serie.grid(row=2, column=1, padx=5, pady=5)

        # Frequência
        tk.Label(root, text="Frequência (%):").grid(row=3, column=0, padx=5, pady=5)
        self.entry_frequencia = tk.Entry(root)
        self.entry_frequencia.grid(row=3, column=1, padx=5, pady=5)

        # Nota
        tk.Label(root, text="Adicionar Nota:").grid(row=4, column=0, padx=5, pady=5)
        self.entry_nota = tk.Entry(root)
        self.entry_nota.grid(row=4, column=1, padx=5, pady=5)

        # Botões
        tk.Button(root, text="Registrar Dados", command=self.registrar_dados).grid(row=5, column=0, padx=5, pady=5)
        tk.Button(root, text="Registrar Frequência", command=self.registrar_frequencia).grid(row=5, column=1, padx=5, pady=5)
        tk.Button(root, text="Adicionar Nota", command=self.adicionar_nota).grid(row=6, column=0, padx=5, pady=5)
        tk.Button(root, text="Gerar Relatório", command=self.gerar_relatorio).grid(row=6, column=1, padx=5, pady=5)

    def registrar_dados(self):
        nome = self.entry_nome.get()
        serie = self.entry_serie.get()
        if nome and serie:
            self.aluno.registrar_dados(nome, serie)
            messagebox.showinfo("Sucesso", "Dados do aluno registrados com sucesso!")
        else:
            messagebox.showerror("Erro", "Por favor, insira o nome e a série do aluno.")

    def registrar_frequencia(self):
        try:
            frequencia = int(self.entry_frequencia.get())
            if 0 <= frequencia <= 100:
                self.aluno.registrar_frequencia(frequencia)
                messagebox.showinfo("Sucesso", "Frequência registrada com sucesso!")
            else:
                raise ValueError("Frequência deve estar entre 0 e 100.")
        except ValueError as e:
            messagebox.showerror("Erro", f"Entrada inválida: {e}")

    def adicionar_nota(self):
        try:
            nota = float(self.entry_nota.get())
            if 0 <= nota <= 100:
                self.aluno.adicionar_nota(nota)
                messagebox.showinfo("Sucesso", "Nota adicionada com sucesso!")
            else:
                raise ValueError("Nota deve estar entre 0 e 100.")
        except ValueError as e:
            messagebox.showerror("Erro", f"Entrada inválida: {e}")

    def gerar_relatorio(self):
        if not self.aluno.nome or not self.aluno.serie:
            messagebox.showerror("Erro", "Por favor, registre os dados do aluno primeiro.")
            return
        relatorio = self.aluno.gerar_relatorio()
        texto_relatorio = (
            f"Nome: {relatorio['Nome']}\n"
            f"Série: {relatorio['Série']}\n"
            f"Frequência: {relatorio['Frequência']}\n"
            f"Histórico de Notas: {relatorio['Histórico']}\n"
            f"Média: {relatorio['Média']}\n"
            f"Risco de Evasão: {relatorio['Evasão']}"
        )
        messagebox.showinfo("Relatório do Aluno", texto_relatorio)


if __name__ == "__main__":
    root = tk.Tk()
    app = AlunoApp(root)
    root.mainloop()
