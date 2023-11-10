from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializar o WebDriver do Selenium e abrir o site do UOL Esporte
driver = webdriver.Chrome()
driver.get("https://www.uol.com.br/esporte/")

# Localizar a notícia e clicar nela
noticia = driver.find_element(By.XPATH, "//a[@class='hard-h__hard-h__link']")
noticia_text = noticia.text
noticia.click()

# Obter a manchete da notícia atual
manchete_atual = noticia_text

# Obter a manchete da nova página
time.sleep(2)  
manchete_nova_pagina = driver.find_element(By.XPATH, "//h1").text

# Verificar se as manchetes são iguais
assert manchete_atual == manchete_nova_pagina

# Fechar o navegador
driver.quit()