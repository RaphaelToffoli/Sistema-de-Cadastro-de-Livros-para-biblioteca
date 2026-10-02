# 📚 Sistema de Cadastro para Biblioteca

Um sistema prático e intuitivo desenvolvido em Python para gerenciamento e cadastro de acervo bibliográfico. O projeto conta com uma interface gráfica amigável e realiza a integração com planilhas Excel para armazenamento e persistência dos dados.

---

## 📸 Demonstração da Interface

| Tela de Cadastro / Login | Visualização da Interface |
| :---: | :---: |
| ![Tela 1]() | ![Tela 2]() |

---

## 🎯 Objetivo do Sistema

O objetivo principal deste sistema é automatizar e simplificar o processo de organização e controle de acervo em bibliotecas ou coleções pessoais. 

Através de uma interface gráfica centralizada, o usuário pode:
- Cadastrar novos livros preenchendo informações essenciais.
- Consultar livros cadastrados no acervo.
- Armazenar todos os registros de forma persistente em uma planilha Excel (`cadastro_livros.xlsx`).

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

O projeto foi construído utilizando as seguintes linguagens e bibliotecas Python:

- **[Python](https://www.python.org/)** — Linguagem principal do projeto.
- **[Tkinter](https://docs.python.org/3/library/tkinter.html)** — Construção da Interface Gráfica de Usuário (GUI).
- **[Pandas](https://pandas.pydata.org/)** e **[openpyxl](https://openpyxl.readthedocs.io/)** — Manipulação, leitura e escrita dos dados na planilha Excel.
- **[Pillow (PIL)](https://pillow.readthedocs.io/)** — Manipulação e renderização de imagens dentro da interface gráfica.

---

## 📂 Estrutura do Projeto

```text
.
├── Trabalho/
│   ├── images/
│   │   ├── images.jpg          # Recursos visuais da interface
│   │   └── imagem2.jpg         # Recursos visuais da interface
│   ├── cadastro_livros.xlsx    # Banco de dados em formato Excel
│   └── index.py                # Código-fonte principal da aplicação
└── README.md                   # Documentação do repositório
```

---

## ⚙️ Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o **Python 3.x** instalado em sua máquina.

### Passo a Passo

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Instale as dependências necessárias:**
   ```bash
   pip install pandas openpyxl pillow
   ```
   *(Nota: O `tkinter` costuma vir pré-instalado com o Python na maioria dos sistemas operacionais).*

3. **Execute a aplicação:**
   ```bash
   python Trabalho/index.py
   ```

---

## 🔄 Fluxo de Funcionamento

1. **Abertura do Sistema:** Ao rodar o arquivo `index.py`, a janela principal da aplicação é carregada.
2. **Entrada de Dados:** O operador insere as informações necessárias nos campos do formulário (Título, Autor, Gênero, etc.).
3. **Validação:** Ao clicar no botão de cadastro, o sistema verifica se as informações foram preenchidas corretamente.
4. **Persistência dos Dados:** Os dados salvos são automaticamente inseridos como uma nova linha dentro da planilha `cadastro_livros.xlsx`.
5. **Confirmação:** A interface exibe uma confirmação e atualiza a exibição para o usuário.

---

## 📄 Licença

Este projeto foi desenvolvido para fins acadêmicos/estudo. Sinta-se à vontade para utilizar, modificar e contribuir!
