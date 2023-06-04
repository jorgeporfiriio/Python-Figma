import tkinter as tk


def criar_janela3():
    janela3 = tk.Tk()
    janela3.geometry("1440x1024")
    janela3.title("Adm clientes")
    janela3.resizable(False, False)

    imagem_fundo3 = tk.PhotoImage(file="cadastro.png")
    lbl_fundo3 = tk.Label(janela3, image=imagem_fundo3)
    lbl_fundo3.place(x=0, y=0, relwidth=1, relheight=1)

    label3 = tk.Label(janela3, text="Nome", bg="#D9D9D9", highlightthickness=0, relief="flat")
    label3.place(x=732, y=305, width=195, height=35)

    entry3 = tk.Entry(janela3, bg="#D9D9D9", highlightthickness=0, relief="flat", font=("Arial", 16))
    entry3.place(x=732, y=305, width=195, height=35)

    label4 = tk.Label(janela3, text="CPF", bg="#D9D9D9", highlightthickness=0, relief="flat")
    label4.place(x=1008, y=305, width=195, height=35)

    entry4 = tk.Entry(janela3, bg="#D9D9D9", highlightthickness=0, relief="flat", font=("Arial", 16))
    entry4.place(x=1008, y=305, width=195, height=35)

    label5 = tk.Label(janela3, text="Data de nascimento", bg="#D9D9D9", highlightthickness=0, relief="flat")
    label5.place(x=732, y=405, width=195, height=35)

    entry5 = tk.Entry(janela3, bg="#D9D9D9", highlightthickness=0, relief="flat", font=("Arial", 16))
    entry5.place(x=732, y=405, width=195, height=35)

    label6 = tk.Label(janela3, text="Data da matricula", bg="#D9D9D9", highlightthickness=0, relief="flat")
    label6.place(x=1020, y=400, width=195, height=35)

    entry6 = tk.Entry(janela3, bg="#D9D9D9", highlightthickness=0, relief="flat", font=("Arial", 16))
    entry6.place(x=1020, y=400, width=195, height=35)

    janela3.mainloop()



def criar_janela2():
    janela2 = tk.Tk()
    janela2.geometry("1440x1024")
    janela2.title("Adm clientes")
    janela2.resizable(False, False)

    imagem_fundo2 = tk.PhotoImage(file="Funções (1).png")
    lbl_fundo2 = tk.Label(janela2, image=imagem_fundo2)
    lbl_fundo2.place(x=0, y=0, relwidth=1, relheight=1)

    def botao_clicado2():
        janela2.destroy()  
        criar_janela3()  

    botao_img2 = tk.PhotoImage(file="Frame 2.png")
    botao2 = tk.Button(janela2, image=botao_img2, bg="#7B768F", bd=0, highlightthickness=0,command=botao_clicado2 )
    botao2.place(x=255, y=400, width=265, height=40)

    janela2.mainloop()



def criar_janela():
    janela = tk.Tk()
    janela.geometry("1440x1024")
    janela.title("Adm clientes")
    janela.resizable(False, False)

    imagem_fundo = tk.PhotoImage(file="Login (1).png")
    lbl_fundo = tk.Label(janela, image=imagem_fundo)
    lbl_fundo.place(x=0, y=0, relwidth=1, relheight=1)

    def botao_clicado():
        janela.destroy()  
        criar_janela2()  

    label = tk.Label(janela, text="Nome", bg="#8E8181", highlightthickness=0, relief="flat")
    label.place(x=835, y=383, width=310, height=48)

    entry = tk.Entry(janela, bg="#8E8181", highlightthickness=0, relief="flat", font=("Arial", 16))
    entry.place(x=835, y=383, width=310, height=48)

    label2 = tk.Label(janela, text="Senha", bg="#8E8181", highlightthickness=0, relief="flat")
    label2.place(x=835, y=445, width=310, height=48)

    entry2 = tk.Entry(janela, bg="#8E8181", highlightthickness=0, relief="flat", show='l', font=("Wingdings", 16))
    entry2.place(x=835, y=445, width=310, height=48)

    botao_img = tk.PhotoImage(file="botaoentrar.png")
    botao = tk.Button(janela, image=botao_img, bg="#E5E1E1", bd=0, highlightthickness=0, command=botao_clicado)
    botao.place(x=879, y=523, width=220, height=75)

    janela.mainloop()

criar_janela()



