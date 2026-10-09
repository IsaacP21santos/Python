import tkinter as tk
janela = tk.Tk()
janela.title('HOME')
janela.geometry('500x400')

#saudação
titulo = tk.Label(janela, text='Seja bem-vindo!', font=('Arial', 24))
titulo.pack(pady=20)

question = tk.Label(janela, text='Como você se chama?', font=('Arial',14))
question.pack()

campo_nome = tk.Entry(janela, font=('Arial',14))
campo_nome.pack(pady=10)

mensagem = tk.Label(janela,text='', font=('Arial',14))
mensagem.pack(pady=10)

#buttons space
area_botoes = tk.Frame(janela)

def confirmar_nome():
    nome = campo_nome.get()
    mensagem.config(text=f'Prazer em te conhecer, {nome}!\nO que você quer fazer agora?')
    area_botoes.pack(pady=20)

botao_confirmar = tk.Button(janela, text='Confirmar',command=confirmar_nome)
botao_confirmar.pack()

#layout dos botoes
botao_1 = tk.Button(area_botoes, text='Calculadora', width=18, height=2)
botao_1.grid(row=0, column=0, padx=10, pady=10)
botao_2 = tk.Button(area_botoes, text='Que número estou pensando?', width=18, height=2)
botao_2.grid(row=0, column=1, padx=10, pady=10)
botao_3 = tk.Button(area_botoes, text='em breve', width=18, height=2)
botao_3.grid(row=1, column=0, padx=10, pady=10)
botao_4 = tk.Button(area_botoes, text='em breve', width=18, height=2)
botao_4.grid(row=1, column=1, padx=10, pady=10)

janela.mainloop()