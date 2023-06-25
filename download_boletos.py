from time import sleep
import pandas as pd
from datetime import date
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
# driver.maximize_window()

diaDeHoje = date.today().day
tabela = pd.read_excel('testeBoletos.xlsx')

for indice, linha in tabela.iterrows():
    if linha["VENCIMENTO"] == diaDeHoje:
        login = linha["LOGIN"]
        senha = linha["SENHA"]
        if linha["SEGURADORA"] == "Unimed":
            login_url = "https://www.unimedrio.com.br/login/"
            driver.get(login_url)
            sleep(5)
            driver.find_element(
                "xpath", '//*[@id="form_login"]/div[1]/div[1]/input').send_keys(login)
            driver.find_element(
                "xpath", '//*[@id="form_login"]/div[2]/div[1]/input').send_keys(senha)
            driver.find_element(
                "xpath", '//*[@id="form_login"]/div[3]/div[1]/button').click()
            sleep(3)
        elif linha["SEGURADORA"] == "SulAmérica":
            cod_empresa = linha["CÓDIGO DA EMPRESA"]
            login = "Master"
            login_url = "https://saude.sulamericaseguros.com.br/empresa/login/"
            driver.get(login_url)
            sleep(5)
            driver.find_element(
                "xpath", '//*[@id="code"]').send_keys(cod_empresa)
            driver.find_element("xpath", '//*[@id="user"]').send_keys(login)
            driver.find_element("xpath", '//*[@id="senha"]').send_keys(senha)
            driver.find_element("xpath", '//*[@id="entrarLogin"]').click()
