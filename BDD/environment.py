from selenium import webdriver

def before_all (conetext):
    conetext.web = webdriver.Chrome()

def after_stp(context, step):
    print()

def after_all(conetext):
    conetext.web.quit()
