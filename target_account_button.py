from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

# click account button
driver.find_element(By.XPATH, "//span[@class='sc-f6835537-3 iyNjUL h-margin-r-x3']").click()

# Wait for 5 sec
sleep(5)

# Click SignIn btn from side navigation
driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']").click()

# Wait for 5 sec
sleep(5)

# Verify
expected_text = driver.find_element(By.XPATH, "//h1[text()='Sign in or create account')]").text
expected_result = driver.find_element(By.XPATH, "//button[contains(@class='styles_ndsBaseButton')]").button

print(expected_text, expected_button)

driver.quit()
# sleep(5)
Footer