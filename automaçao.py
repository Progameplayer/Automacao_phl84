import pyautogui as py
from time import sleep
from customtkinter import *
from selenium import webdriver
py.FAILSAFE = True

janela = CTk()
janela.title("AUTOMATIZÇÃO DE TAREFAS")
janela.geometry("500x300")
set_appearance_mode("Dark")


py.PAUSE = 2

def automatizar_importacao():
    with open("importação.txt","r") as f:
        for linha in f:
            livros = [x.strip() for x in linha.split(",") if x.strip()]
            for livro in livros: 
                navegador = webdriver.Chrome()
                pesquisar = navegador.find_elements("id" , "PalavraChave").send_keys(f"{livro}")
                pesquisar.click()
                try:
                    marc = py.locateOnScreen("marc_tags.png")
                    if marc:
                        py.click(marc)
                    else:
                        continue 
                except py.ImageNotFoundException:
                    with open("livros_nao_encontrados.txt", "a") as arquivo:
                        livroNotFound = f'# {livro}\n'
                        arquivo.write(livroNotFound)
                        py.hotkey("ctrl", "w")  
                    continue

auto_cadastro = CTkLabel(janela, text = "Automatize a importação de dados:")
auto_cadastro.pack(padx = 20, pady = 20)
botao = CTkButton(janela, text = "Automatizar Importação", command = automatizar_importacao, fg_color=("black", "blue"))
botao.pack( padx = 20 , pady = 20)

janela.mainloop()