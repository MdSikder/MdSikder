from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com/")

var = driver.find_element(By.XPATH, "//body[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]")
print(var.is_displayed())
print(var.is_enabled())

print(var.)
driver.quit()
