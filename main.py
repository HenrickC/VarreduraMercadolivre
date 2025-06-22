#0 - abrir o navegador
#1 - Navegar até o site(url)
#2 - Pesquisar por produto
#3 - Extrair o titulo e preço
#4 - Navegar até a proxima pagina
#5 - Agendar a execução

from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 0 - Abrir o navegador
path_driver = os.getcwd() + os.sep + 'chromedriver.exe'
service = Service(executable_path=path_driver)
driver = webdriver.Chrome(service=service)

#rodar python de forma interativa : python -i nome_arquivo.py
#1 - Navegar até o site
driver.get('https://www.mercadolivre.com.br')
#clicar no campo de pesquisa
campo_pesquisa = driver.find_element(By.XPATH, "//input[@class='nav-search-input']")
campo_pesquisa.click()
#2- pesquisar pelo produto
campo_pesquisa.send_keys('fone hyperx') 
#enter
campo_pesquisa.send_keys(Keys.ENTER)
#3 - Extrair o titulo e preço
fones = driver.find_elements(By.XPATH, "//a[@class='poly-component__title']") 
for fone in fones:   
    print(fone.text)

#4 - Navegar até a proxima pagina

#5 - Agendar a execução


#titulo quando mais relevantes //a[@class="poly-component__title"] - por enquanto parece que da pra usar isso pra todos os caso

#titulo quando menor preço 

#titulo quando maior preço
