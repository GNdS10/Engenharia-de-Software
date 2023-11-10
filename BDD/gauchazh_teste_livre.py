from selenium import webdriver

# Inicializar o WebDriver do Selenium e abrir o site GaúchaZH
driver = webdriver.Chrome()
driver.get("https://gauchazh.clicrbs.com.br/esportes/ultimas-noticias/")



# Fechar o navegador
driver.quit()