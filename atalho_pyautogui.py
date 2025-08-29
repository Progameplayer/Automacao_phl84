#   Codigo de automação de tarefas em Python.
#   Para automatizar tarefas manuais no python optei pela utilização da bilbioteca pyautogui o qual automatiza mouse e teclado.
#   Importação das bibliotecas necessárias 
from pyautogui import *
from time import sleep
import keyboard
PAUSE = 1
FAILSAFE = True
# Interface Grafica - É uma camuflagem para os codigos a fim de esconder a parte complexa do usuario.
from customtkinter import *

# Mini interface grafica (configurações)
janela = CTk()
janela.title("AUTOMATIZÇÃO DE TAREFAS")
janela.geometry("300x300")
set_appearance_mode("Dark")

# Função que automatiza a importação de livros para a biblioteca de forma automática
def automatizar_importaçao():
    sleep(2)
    press("win")
    sleep(2)
    write("Chrome")
    sleep(2)
    press("enter")
    sleep(6)
    click(x=165, y=84,  duration=1)
    sleep(3)
    click(x=1340, y=122,duration=1)
    sleep(6)
    click(x=673, y=112, duration=1)
    sleep(2)
    # Alterei o "real" nome de usuario para fins de segurança
    write("super")
    sleep(2)
    press("tab")
    sleep(2)
    # Alterei a "real" senha para fins de segurança
    write("super")
    sleep(2)
    press("enter")
    sleep(4)
    click(x=856, y=312 , duration=1)
    sleep(3)
    click(x=1207 , y=331, duration=1)
    sleep(2)
    hotkey("ctrl", "t")
    sleep(2)
    click(x=299, y=88, duration=1)
    sleep(5)
    with open("importação.txt", "r", encoding= "utf-8") as arquivo:
        for linha in arquivo:
            livros = [x.strip() for x in linha.split(",") if x.strip()]
            for livro in livros:
                sleep(5)
                try:
                    pesquisar = locateOnScreen("pesquisa_icon.png")
                    if pesquisar:
                        click(pesquisar)
                    else:
                        continue
                except ImageNotFoundException:
                    icone = locateOnScreen("Biblioteca_icone.png")
                    click(icone)
                    continue
                sleep(3)
                write(livro)
                press("enter")
                sleep(8)
                click(x=464, y=358, duration = 1)
                sleep(8)
                click(x=949, y=355, duration = 1)
                sleep(8)
                try:
                    marc = locateOnScreen("marc_tag.png")
                    if marc:
                        click(marc)
                    else:
                        continue 
                except ImageNotFoundException:
                    with open("livros_nao_encontrados.txt", "a", encoding= "utf-8") as f:
                        livroNotFound = f'# {livro}\n'
                        f.write(livroNotFound)
                        icone = locateOnScreen("Biblioteca_icone.png")
                        click(icone)
                        sleep(2)
                    continue 
                scroll(-99999)
                sleep(7)
                copiar = locateOnScreen("copiar.png")
                click(copiar)
                sleep(4)
                icone = locateOnScreen("Biblioteca_icone.png")
                click(icone)
                sleep(6)
                hotkey("ctrl", "tab")
                sleep(2)
                click(x=63, y=372, duration = 1)
                sleep(2)
                click(x=391, y=226, duration = 1)
                sleep(3)
                click(x=828, y=354, duration = 1)
                hotkey("ctrl", "v")
                sleep(3)
                click(x=828, y=560, duration = 1)
                sleep(3)
                scroll(-99999)
                click(x=582, y=696, duration = 1)
                sleep(5)
                hotkey("ctrl" , "tab")

# Interação da Interface Grafica com o Usuário 
auto_cadastro = CTkLabel(janela, text = "Automatize a importação de dados:")
auto_cadastro.pack(padx = 20, pady = 20)
botao = CTkButton(janela, text = "Automatizar Importação", command = automatizar_importaçao, fg_color=("black", "blue"))
botao.pack( padx = 20 , pady = 20)

janela.mainloop()








