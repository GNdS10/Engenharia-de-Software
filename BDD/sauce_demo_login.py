from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializar o WebDriver do Selenium e abrir a página de login do SauceDemo
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Inserir nome de usuário e senha válidos
usuario = "standard_user"
senha = "secret_sauce"
driver.find_element(By.ID, "user-name").send_keys(usuario)
driver.find_element(By.ID, "password").send_keys(senha)

# Clicar no botão "Login"
driver.find_element(By.ID, "login-button").click()

# Verificar se o usuário foi redirecionado para a página principal
pagina_principal = driver.find_element(By.XPATH, "//div[@class='product_label']").text
assert "Products" in pagina_principal

# Fechar o navegador
driver.quit()