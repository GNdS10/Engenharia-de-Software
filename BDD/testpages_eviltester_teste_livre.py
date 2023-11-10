from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://testpages.eviltester.com/styled/key-click-display-test.html")



# Fechar o navegador
driver.quit()