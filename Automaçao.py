from customtkinter import *
from time import sleep 
from pyautogui import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
PAUSE = 2

def auto_importaçao():
    service = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=service)
    navegador.get("http://127.0.0.1:2186/cgi-bin/wxis.exe?IsisScript=phl84.xis&cipar=phl84.cip&lang=por")
    navegador.maximize_window()
    sleep(2)
    navegador.get("http://127.0.0.1:2186/cgi-bin/wxis.exe?IsisScript=phl84/021.xis&opc=form_login&tmp=C:/Users/MEUCOM~1/AppData/Local/Temp/TMP6.$$$&counter=18")
    navegador.find_element(By.NAME, "login").send_keys("super")
    navegador.find_element(By.NAME, "pwd").send_keys("super" + Keys.RETURN)
    sleep(2)
    click(x=42, y=276, duration=0.5)
    sleep(2)
    click(x=493, y=18, duration=0.5)
    sleep(2)
    click(x=252, y=17, duration=0.5)
    sleep(2)
    click(x=290, y=17, duration=0.5)
    sleep(2)
    write("https://acervo.bn.gov.br/sophia_web/")
    press("enter")
    sleep(2)
    with open ("importaçao.txt", "r") as arquivo:
        for linha in arquivo:
            livros = [x.strip() for x in linha.split(",") if x.strip()]
            for livro in livros:
                navegador.find_element(By.ID, "PalavraChave").send_keys(livro + Keys.RETURN)
                try:
                    capa = navegador.find_element("class name" , "capa-ficha")
                    if capa:
                        capa.click()
                    else:
                        continue 
                except ImageNotFoundException:
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
                copiar = navegador.find_element(By.CLASS_NAME, "btn btn-default")
                navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", copiar)
                espera = WebDriverWait(navegador, 10)
                espera.until(EC.element_to_be_selected(copiar))
                copiar.click()
                sleep(2)
                abas = navegador.window_handles
                navegador.switch_to.window(abas[0])
set_appearance_mode("dark")
api = CTk()
api.title("Automatização do PHL84")
api.geometry("400x400")
introduçao = CTkLabel(api,text= "Automatizar importação de dados do PHL84")
introduçao.pack(pady= 20)

botao = CTkButton(api, text= "Importar dados do documento", command = auto_importaçao)
botao.pack(pady = 20) 
api.mainloop()