import pyautogui as py
from time import sleep
from customtkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
                navegador.get("https://bibliotecaresende.phlnet.com.br/cgi-bin/wxis.exe?IsisScript=phl84.xis&cipar=phl84.cip&lang=por")
                logins = navegador.find_elements("class name", "inv12")
                for login in logins:
                    if "Serviços" in login.text:
                        login.click()
                nome = navegador.find_elements("name" , "login").send_keys("suzy")
                nome.click()
                senha = navegador.find_elements("name", "pwd").send_keys("123456")
                senha.click()
                navegador.execute_script("window_open('https://acervo.bn.gov.br/Sophia_web/Resultado/Listar?guid=1736868286439')")
                abas = navegador.window_handles
                abas.switch_to(abas(1))
                pesquisar = navegador.find_elements("id" , "PalavraChave").send_keys(f"{livro}" + Keys.ENTER)
                pesquisar.click()
                try:
                    capa = navegador.find_element("class name" , "capa-ficha")
                    if capa:
                        capa.click()
                    else:
                        continue 
                except py.ImageNotFoundException:
                    with open("livros_nao_encontrados.txt", "a") as arquivo:
                        livroNotFound = f'# {livro}\n'
                        arquivo.write(livroNotFound)
                        icone = navegador.find_element("id", "logotipoTerminal")
                        icone.click()  
                    continue
                marctags = navegador.find_elements("class name", "btn btn-default")
                for marctag in marctags:
                    if "MARC tags" in marctag.text:
                        marctag.click()
                

auto_cadastro = CTkLabel(janela, text = "Automatize a importação de dados:")
auto_cadastro.pack(padx = 20, pady = 20)
botao = CTkButton(janela, text = "Automatizar Importação", command = automatizar_importacao, fg_color=("black", "blue"))
botao.pack( padx = 20 , pady = 20)

janela.mainloop()