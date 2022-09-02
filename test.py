from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

serv = Service("/Users/diegorosales/PycharmProjects/Sele/Driver/chromedriver")


driver = webdriver.Chrome(service = serv)

driver.get("http://localhost:8121/")
elemento1 = driver.find_element(By.ID, "user")
elemento1.clear()
elemento1.send_keys("root")

wait = WebDriverWait(driver, 3)

elemento2 = driver.find_element(By.NAME, "pass")
elemento2.clear()
elemento2.send_keys("password")

driver.find_element(By.XPATH, '//*[@id="login"]/div[3]/div/input').click()

wait = WebDriverWait(driver, 3)

driver.get("http://localhost:8121/")

"""driver.find_element(By.XPATH, '//*[@id="CreateTicketInQueue"]/div[2]/input').click()"""

wait = WebDriverWait(driver, 3)

elemento3 = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[1]/div[4]/div/div/div[2]/div/form/div[1]/div[1]/div[2]/input')
elemento3.clear()
elemento3.send_keys("PRUEBA PARA LA PRUEBA")

driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div[1]/div[4]/div/div/div[2]/div/form/div[2]/div/div/div[2]/input").click()


"""driver.close()"""