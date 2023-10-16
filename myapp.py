import tkinter as tk


def calcular_tempo():
    try:
        meta_financeira = float(meta_financeira_entry.get())
        economia_mensal = float(economia_mensal_entry.get())

        if economia_mensal <= 0:
            resultado_label.config(
                text="A economia mensal deve ser maior que zero.")
            return

        tempo = meta_financeira / economia_mensal
        resultado_label.config(
            text=f"Tempo estimado para atingir a meta: {tempo:.2f} meses")
    except ValueError:
        resultado_label.config(
            text="Certifique-se de inserir valores válidos.")


def criar_interface():
    janela = tk.Tk()
    janela.title("Calculadora de Meta Financeira")
    janela.geometry("300x200")

    global meta_financeira_entry, economia_mensal_entry, resultado_label

    meta_financeira_entry = criar_entrada(janela, "Meta Financeira:")
    economia_mensal_entry = criar_entrada(janela, "Economia Mensal:")
    criar_botao(janela, "Calcular", calcular_tempo)
    resultado_label = criar_etiqueta(janela)

    janela.mainloop()


def criar_entrada(janela, texto):
    label = tk.Label(janela, text=texto)
    label.pack()
    entrada_variavel = tk.StringVar()
    entrada = tk.Entry(janela, textvariable=entrada_variavel)
    entrada.pack()
    return entrada_variavel


def criar_botao(janela, texto, comando):
    botao = tk.Button(janela, text=texto, command=comando)
    botao.pack()


def criar_etiqueta(janela):
    etiqueta = tk.Label(janela, text="")
    etiqueta.pack()
    return etiqueta


if __name__ == "__main__":
    criar_interface()
