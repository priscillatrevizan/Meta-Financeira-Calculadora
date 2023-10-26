import tkinter as tk
from tkinter import font as tkFont


def calcular_tempo():
    try:
        meta_financeira = float(meta_financeira_entry.get())
        economia_mensal = float(economia_mensal_entry.get())

        if economia_mensal <= 0:
            resultado_label.config(text="A economia mensal deve ser maior que zero")
            return

        tempo = round(meta_financeira / economia_mensal)
        if tempo == int(tempo):
            resultado_label.config(
                text=f"Tempo estimado para atingir a meta: {int(tempo)} meses"
            )
        else:
            resultado_label.config(text=f"Aproximadamente {int(tempo)} meses")
    except ValueError:
        resultado_label.config(text="Certifique-se de inserir valores válidos")


def criar_interface():
    janela = tk.Tk()
    janela.title("Calculadora de Meta Financeira")
    janela.geometry("600x400")

    montserrat_font = tkFont.Font(family="Montserrat", size=14)

    global meta_financeira_entry, economia_mensal_entry, resultado_label

    meta_financeira_entry = criar_entrada(janela, "Meta Financeira:", montserrat_font)
    economia_mensal_entry = criar_entrada(janela, "Economia Mensal:", montserrat_font)
    criar_botao(janela, "Calcular", calcular_tempo, montserrat_font)
    resultado_label = criar_etiqueta(janela, montserrat_font)

    janela.mainloop()


def criar_entrada(janela, texto, fonte):
    label = tk.Label(janela, text=texto, font=fonte, bg="#F2F2F2", fg="#163E73")
    label.pack()
    entrada_variavel = tk.StringVar()
    entrada = tk.Entry(
        janela, textvariable=entrada_variavel, font=fonte, justify="center"
    )
    entrada.pack()
    return entrada_variavel


def criar_botao(janela, texto, comando, fonte):
    botao = tk.Button(
        janela,
        text=texto,
        command=comando,
        font=fonte,
        bg="#163E73",
        fg="#F2F2F2",
        bd=12,
    )
    botao.pack()


def criar_etiqueta(janela, fonte):
    etiqueta = tk.Label(janela, text="", font=fonte, bg="#F2F2F2")
    etiqueta.pack()
    return etiqueta


if __name__ == "__main__":
    criar_interface()
