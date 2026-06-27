from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("site") #Site desejado

driver.find_element(By.NAME,"nome").send_keys("Nome") #Nome do usuário

driver.find_element(By.NAME,"email").send_keys("@email.com")#E-mail do usuário

driver.find_element(By.NAME,"idade").send_keys("00")#Idade do usuário

driver.find_element(By.TAG_NAME,"button").click

print("Formulário enviado!")

driver.quit()