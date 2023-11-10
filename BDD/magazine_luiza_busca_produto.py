from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializar o WebDriver do Selenium e abrir o site do Magazine Luiza
driver = webdriver.Chrome()
driver.get("https://www.magazineluiza.com.br/")

# Localizar a barra de pesquisa e inserir "smartphone"
barra_pesquisa = driver.find_element(By.ID, "inpHeaderSearch")
barra_pesquisa.send_keys("smartphone")

# Pressionar Enter
barra_pesquisa.send_keys(Keys.RETURN)

# Verificar se a lista de resultados de pesquisa contém a palavra "smartphone"
resultados = driver.find_elements(By.XPATH, "//div[contains(@class, 'ResultItems')]")
assert any("smartphone" in resultado.text for resultado in resultados)

# Fechar o navegador
driver.quit()