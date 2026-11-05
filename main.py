    #PC Cleaner

#Limpeza de arquivos tempórarios e desnecessarios do sistema operacional Windows

import cmd
import tkinter as tk
import os


#-------------------------------
#janela principal
#-------------------------------

janela = tk.Tk()
janela.title("PC Cleaner")
janela.geometry("800x600")
janela.configure(bg="#101114")

#-------------------------------
#Titulo
#-------------------------------

titulo = tk.Label(
    janela,
    text="Pc Cleaner",
    font=("Arial", 30, "bold"),
    fg="White",
    bg="#101113"

    )
titulo.pack(pady=20)


#-------------------------------
 #Comandos Cleaner Windows
#-------------------------------
comandos = [ 
    ("Limpar", "%temp%", "Limpar arquivos temporários do usuário"),
    ("Limpar", "temp", "Limpar arquivos temporários do sistema"),
    ("Limpar", "cleanmgr", "ferramenta de limpeza de disco do Windows"),
    ("Limpar", "recent", "Limpar arquivos recentes do Windows"),
    ]

#-------------------------------
 #Sistema Windows
#-------------------------------
sistema = [
  ("Sistema", "services.msc", "Abre o Gerenciador de Serviços do Windows"),
  ("Sistema", "taskmgr", "Abre o Gerenciador de Tarefas do Windows"),
  ("Sistema", "appwiz.cpl", "Abre o Painel de Controle do Windows"), 
  ("Sistema", "regedit", "Abre o Editor de Registro do Windows"),
  ("Sistema", "diskmgmt.msc", "Abre o Gerenciamento de Disco do Windows"),
  ("Sistema", "devmgmt.msc", "Abre o Gerenciador de Dispositivos do Windows"),

]

#-------------------------------
 #Informações do Sistema
#-------------------------------
informações = [
    ("Informações do Sistema", "dxdiag", "Abre a ferramenta de diagnóstico do DirectX, fornecendo informações detalhadas sobre o sistema, incluindo hardware, drivers e recursos de áudio e vídeo."),
    ("Informações do sistema", "resmon", "Abre o Monitor de Recursos do Windows, permitindo monitorar o uso de CPU, memória, disco e rede em tempo real."),
    ("Informações do sistema", "perfmon", "Abre o Monitor de Desempenho do Windows, permitindo criar gráficos e relatórios personalizados para monitorar o desempenho do sistema."),
    ("Informações dosistema","control", "Abre o Painel de Controle do Windows"),
    ("Informações do sistema", "msinfo32", "Abre as Informações do Sistema do Windows"),
]

#-------------------------------
 #Manutenção do Sistema
#-------------------------------
manutenção = [
    ("Manutenção do Sistema", "sfc /scannow", "Verifica e repara arquivos de sistema corrompidos no Windows"),
    ("Manutenção do Sistema", "chkdsk", "Verifica e repara erros"),
    ("Manutenção do Sistema", "dism /online /cleanup-image /restorehealth", "Repara a imagem do sistema operacional Windows"),
    ("Manutenção do Sistema", "cleanmgr", "Abre a ferramenta de limpeza de disco do Windows")

]


#-------------------------------
 #Função para executar os comandos
#-------------------------------


container = tk.Frame(janela, bg="#101114")
container.pack(fill="both", expand=True, padx=30)

canvas = tk.Canvas(container, bg="#101114", highlightthickness=0)
scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

area = tk.Frame(canvas, bg="#101114")
janela_area = canvas.create_window((0, 0), window=area, anchor="nw")

area.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.bind("<Configure>", lambda e: canvas.itemconfig(janela_area, width=e.width))

# Rolar com o mouse (Windows e Linux)
canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-e.delta / 120), "units"))
canvas.bind_all("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))
canvas.bind_all("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))

def copiar(cmd):
    janela.clipboard_clear()
    janela.clipboard_append(cmd)

for categoria, comando, descrição in comandos + sistema + informações + manutenção:
    card = tk.Frame(area, bg="#1E1E1E", padx=20, pady=10)
    card.pack(fill="x", pady=5)

    categoria_label = tk.Label(
        card, text=categoria, font=("Arial", 14, "bold"),
        fg="#f0f4f0", bg="#1E1E1E"
    )
    categoria_label.pack(anchor="w")

    descrição_label = tk.Label(
        card, text=descrição, font=("Arial", 12),
        fg="#ee0000", bg="#1E1E1E"
    )
    descrição_label.pack(anchor="w")

    comando_label = tk.Label(
        card, text=comando, font=("Consolas", 13, "bold"),
        fg="#0053ee", bg="#101114", padx=10, pady=4
    )
    comando_label.pack(anchor="w", pady=(5, 0))

    botao = tk.Button(
        card, text="Copiar",
        command=lambda c=comando: copiar(c)
    )
    botao.pack(anchor="e")




#-------------------------------
 #Inicialização da janela principal
#-------------------------------

janela.mainloop()



    