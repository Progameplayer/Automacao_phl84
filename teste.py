from customtkinter import *
import random, time
from pyautogui import moveTo, click, write, press, hotkey
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Funções auxiliares
def pausa(min_s=0.8, max_s=2.5):
    time.sleep(random.uniform(min_s, max_s))

def digitar_lento(elemento, texto):
    for letra in texto:
        elemento.send_keys(letra)
        time.sleep(random.uniform(0.05, 0.2))

def auto_importaçao():
    service = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=service)
    navegador.get("http://127.0.0.1:2186/cgi-bin/wxis.exe?IsisScript=phl84.xis&cipar=phl84.cip&lang=por")
    navegador.maximize_window()
    pausa(1.5, 3)

    # Login
    moveTo(791, 154, duration=random.uniform(0.3, 0.8))
    click()
    pausa()
    write("super", interval=random.uniform(0.05, 0.15))
    pausa()
    press("tab")
    pausa()
    write("super", interval=random.uniform(0.05, 0.15))
    pausa()
    press("enter")
    pausa(4, 6)

    # Nova aba
    #navegador.execute_script("window.open('https://acervo.bn.gov.br/sophia_web/', '_blank');")
    #navegador.switch_to.window(navegador.window_handles[-1])
    
    abas = navegador.window_handles
    navegador.switch_to.window(abas[1])

    # Leitura do arquivo e busca
    with open("importaçao.txt", "r") as arquivo:
        for linha in arquivo:
            livros = [x.strip() for x in linha.split(",") if x.strip()]
            for livro in livros:
                pausa(5, 7)
                campo = navegador.find_element(By.ID, "PalavraChave")
                campo.clear()
                digitar_lento(campo, livro)
                pausa(2, 4)
                campo.send_keys(Keys.ENTER)
                pausa(5, 7)

                try:
                    capa = navegador.find_element(By.CLASS_NAME, "capa-ficha").click()
                except:
                    with open("livros_nao_encontrados.txt", "a") as arq_nf:
                        arq_nf.write(f"# {livro}\n")
                    try:
                        navegador.find_element(By.ID, "logotipoTerminal").click()
                    except:
                        pass
                    continue

                # Botão MARC tags
                botoes = navegador.find_elements(By.CLASS_NAME, "btn")
                for botao in botoes:
                    if "MARC tags" in botao.text:
                        botao.click()
                        break

                # Botão copiar
                copiar = navegador.find_element(By.CLASS_NAME, "btn")
                navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", copiar)
                WebDriverWait(navegador, 10).until(EC.element_to_be_clickable(copiar))
                copiar.click()
                pausa(1, 2)

                # Volta para a primeira aba
                abas = navegador.window_handles
                navegador.switch_to.window(abas[0])
                pausa(1.5, 3)

# Interface gráfica
set_appearance_mode("dark")
api = CTk()
api.title("Automatização do PHL84")
api.geometry("300x300")

introducao = CTkLabel(api, text="Automatizar importação de dados do PHL84")
introducao.pack(pady=20)

botao = CTkButton(api, text="Importar dados", command=auto_importaçao)
botao.pack(pady=20)

api.mainloop()
