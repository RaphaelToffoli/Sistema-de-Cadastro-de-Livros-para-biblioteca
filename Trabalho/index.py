import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import openpyxl

def selecionar_imagem():
    caminho = filedialog.askopenfilename(
        title="Selecionar imagem",
        filetypes=[("Arquivos de Imagem", "*.png;*.jpg;*.jpeg;*.bmp")]
    )
    if caminho:
        lbl_caminho_imagem.config(text=caminho, fg="green")
    else:
        lbl_caminho_imagem.config(text="Nenhuma imagem selecionada", fg="red")

def limpar_caminhos():
    entry_titulo.delete(0, tk.END)
    entry_autor.delete(0, tk.END)
    entry_ano.delete(0, tk.END)
    combo_genero.set("")
    var_formato.set("Fisico")
    var_especial.set(False)
    var_brinde.set(False)
    lbl_caminho_imagem.config(text="Nenhum imagem selecionada ", fg="red")

def salvar_cadastro():
    titulo = entry_titulo.get().strip()
    autor = entry_autor.get().strip()
    ano = entry_ano.get().strip()
    genero = combo_genero.get().strip()
    formato = var_formato.get().strip()

    ed_especial = "Sim" if var_especial.get() else "Não"
    possui_brinde = "Sim" if var_brinde.get() else "Não"

    caminho_imagem = lbl_caminho_imagem.cget("text")

    if not titulo or not autor or not ano or not genero:
        messagebox.showwarning("Campos Ausentes", "Por favor preencha todos os campos obrigatorios(Titulo, Autor, Ano, Genero)!")
        return
    
    if caminho_imagem == "Nenhuma imagem selecionada":
        messagebox.showwarning("Imagem Ausente", "Por favor selecione uma imagem")
        return
    
    nome_arquivo = "cadastro_livros.xlsx"

    if not os.path.exists(nome_arquivo):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Livros"

        ws.append(["Título", "Autor", "Ano", "Gênero", "Formato", "Ed. Especial", "Possui Brinde", "Caminho da Imagem"])
    else:
        wb = openpyxl.load_workbook(nome_arquivo)
        ws = wb.active 

    ws.append([titulo, autor, ano, genero, formato, ed_especial, possui_brinde, caminho_imagem])

    wb.save(nome_arquivo)

    messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso no arquivo Excel!")
    limpar_caminhos()
    
janela = tk.Tk()
janela.title("Sistema de gestão de biblioteca")
janela.geometry("550x500")
janela.resizable(False, False)

lbl_sistema = tk.Label(janela, text="CADASTRO DE LIVROS", font=("Arial", 16, "bold"), fg="blue")
lbl_sistema.grid(row=0, column=0, columnspan=2, pady=15)

tk.Label(janela, text="Título do livro *:", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", padx=20, pady=5)
entry_titulo = tk.Entry(janela, width=40)
entry_titulo.grid(row=1, column=1, padx=20, pady=5)

tk.Label(janela, text="Autor *:", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w", padx=20, pady=5)
entry_autor = tk.Entry(janela, width=40)
entry_autor.grid(row=2, column=1, padx=20, pady=5)

tk.Label(janela, text="Ano de Publicação *:", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="w", padx=20, pady=5)
entry_ano = tk.Entry(janela, width=40)
entry_ano.grid(row=3, column=1, padx=20, pady=5)

tk.Label(janela, text="Gênero Literário *:", font=("Arial", 10, "bold")).grid(row=4, column=0, sticky="w", padx=20, pady=5)
lista_genero = ["Ficção Científica", "Romance", "Terror / Suspense", "Fantasia", "Biografia", "História"]
combo_genero = ttk.Combobox(janela, values=lista_genero, width=37, state="readonly")
combo_genero.grid(row=4, column=1, padx=20, pady=5)

tk.Label(janela, text="Formato *:", font=("Arial", 10, "bold")).grid(row=5, column=0, sticky="w", padx=20, pady=5)
var_formato = tk.StringVar(value="Físico")
frame_radio = tk.Frame(janela)
frame_radio.grid(row=5, column=1, sticky="w", padx=20, pady=5)

rb_fisico = tk.Radiobutton(frame_radio, text="Físico", variable=var_formato, value="Físico")
rb_fisico.pack(side="left", padx=5)
rb_ebook = tk.Radiobutton(frame_radio, text="E-book", variable=var_formato, value="E-book")
rb_ebook.pack(side="left", padx=5)

tk.Label(janela, text="Preferências / Detalhes:", font=("Arial", 10, "bold")).grid(row=6, column=0, sticky="w", padx=20, pady=5)

var_especial = tk.BooleanVar()
var_brinde = tk.BooleanVar()

frame_check = tk.Frame(janela)
frame_check.grid(row=6, column=1, sticky="w", padx=20, pady=5)

cb_especial = tk.Checkbutton(frame_check, text="Edição Especial", variable=var_especial)
cb_especial.pack(side="left", padx=5)

cb_brinde = tk.Checkbutton(frame_check, text="Acompanha Brinde", variable=var_brinde)
cb_brinde.pack(side="left", padx=5)

tk.Label(janela, text="Capa do Livro *:", font=("Arial", 10, "bold")).grid(row=7, column=0, sticky="w", padx=20, pady=10)

btn_imagem = tk.Button(janela, text="Selecionar Imagem...", command=selecionar_imagem, bg="#dcdcdc")
btn_imagem.grid(row=7, column=1, sticky="w", padx=20, pady=10)

lbl_caminho_imagem = tk.Label(janela, text="Nenhuma imagem selecionada", font=("Arial", 8, "italic"), fg="red", wraplength=300, justify="left")
lbl_caminho_imagem.grid(row=8, column=1, sticky="w", padx=20, pady=2)

frame_botoes = tk.Frame(janela)
frame_botoes.grid(row=9, column=0, columnspan=2, pady=30)

btn_limpar = tk.Button(frame_botoes, text="Limpar Campos", command=limpar_caminhos, width=15, bg="#ffcccb")
btn_limpar.pack(side="left", padx=15)

btn_salvar = tk.Button(frame_botoes, text="Salvar Cadastro", command=salvar_cadastro, width=15, bg="#90ee90", font=("Arial", 10, "bold"))
btn_salvar.pack(side="left", padx=15)

janela.mainloop()
