import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec

#INICIO WEB DRIVER
driver = webdriver.Chrome(executable_path=r"C:\AUTOMATIZACION\WebDriver\chromedriver.exe")

#CLASES PARA VALIDACIONES
class personal_validations():
    def explicit_wait_located(search_val,value):
        try:
            WebDriverWait(driver,10).until(ec.visibility_of_element_located((search_val,value)))
            last_value1 = "Found"
        except:
            last_value1 = "NotFound"
        return last_value1

    def explicit_wait_clickeable(search_val,value):
        try:
            WebDriverWait(driver,10).until(ec.element_to_be_clickable((search_val,value)))
            last_value1 = "Found"
        except:
            last_value1 = "NotFound"
        return last_value1

#VARIABLES
first_name="JUANITO"
last_name="PEREZ"
email="JUANITOPE@GMAIL.COM"
month="July"
day="13"
year="1995"
languages="Czech"
password="1024508503Juanito*"

#INICIO AUTOMATIZACION

#Inicia la pagina a la que haremos la prueba
initial_path = "https://www.utest.com/"
driver.get(initial_path)
driver.maximize_window()

# Se clikea el boton Join Today
if personal_validations.explicit_wait_clickeable(By.CLASS_NAME,"unauthenticated-nav-bar__sign-up") != "Found":
    print("Error al buscar boton Join Today")
    driver.quit()
driver.find_element(By.CLASS_NAME,"unauthenticated-nav-bar__sign-up").click()

#Se genera error si no encuentra el boton Joyn Today
if personal_validations.explicit_wait_located(By.ID,"firstName") != "Found":
    print("Error al buscar boton Join Today")
    driver.quit()

# PRIMER PASO

# Se llena el campo first name
driver.find_element(By.ID,"firstName").send_keys(first_name)

# Se llena el campo last name
driver.find_element(By.NAME,"lastName").send_keys(last_name)

# Se llena campo email address
driver.find_element(By.XPATH,"//*[@id='email']").send_keys(email)

# Se llena los tres campos de date of birth
select = Select(WebDriverWait(driver,10).until(ec.element_to_be_clickable((By.ID,"birthMonth"))))
select.select_by_visible_text(month)
select = Select(WebDriverWait(driver,10).until(ec.element_to_be_clickable((By.ID,"birthDay"))))
select.select_by_visible_text(day)
select = Select(WebDriverWait(driver,10).until(ec.element_to_be_clickable((By.ID,"birthYear"))))
select.select_by_visible_text(year)

# Se llena campo de languages
driver.find_element(By.XPATH,"//*[@id='languages']/div[1]/input").send_keys(languages)
driver.find_element(By.XPATH,"//*[@id='languages']/div[1]/input").send_keys(Keys.ENTER)

# Se avanza al siguiente paso
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='regs_container']/div/div[2]/div/div[2]/div/form/div[2]/a/i").click()

# SEGUNDO PASO

# En este paso la misma pagina tiene automatizado todos los campos

# Se avanza al siguiente paso
time.sleep(10)
driver.find_element(By.XPATH,"//*[@id='regs_container']/div/div[2]/div/div[2]/div/form/div[2]/div/a").click()

# TERCER PASO

# Se llena campo Your Mobile Device
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='mobile-device']/div[1]/div[2]/div/div[1]/span/span[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='ui-select-choices-row-6-1']/span/div").click()

# Se llena campo Model
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='mobile-device']/div[2]/div[2]/div/div[1]/span/span[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='ui-select-choices-row-7-3']/span/div").click()

# Se llena campo Operating System
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='mobile-device']/div[3]/div[2]/div/div[1]/span/span[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='ui-select-choices-row-8-12']/span/div").click()

# Se avanza al siguiente paso
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='regs_container']/div/div[2]/div/div[2]/div/div[2]/div/a").click()

# CUARTO PASO

# Se llena campo Create your uTest password
driver.find_element(By.ID,"password").send_keys(password)

# Se llena Confirm password
driver.find_element(By.ID,"confirmPassword").send_keys(password)

# Se clikea los campos

driver.find_element(By.XPATH,"//*[@id='regs_container']/div/div[2]/div/div[2]/div/form/div[4]/label/span").click()
driver.find_element(By.XPATH,"//*[@id='regs_container']/div/div[2]/div/div[2]/div/form/div[5]/label/span[1]").click()
driver.find_element(By.XPATH,"//*[@id='regs_container']/div/div[2]/div/div[2]/div/form/div[6]/label/span[1]").click()

# Finaliza Proceso
time.sleep(8)
driver.find_element(By.XPATH,"//*[@id='laddaBtn']").click()
