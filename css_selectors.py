from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Start Chrome browser:
driver = webdriver.Chrome()
driver.get('https://www.amazon.com/')


# CSS Selectors, by id #
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')  # same as => driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')

# by class, .
driver.find_element(By.CSS_SELECTOR, ".nav-progressive-attribute")
# multiple classes
driver.find_element(By.CSS_SELECTOR, ".nav-progressive-attribute.nav-input")
# classes + tag
driver.find_element(By.CSS_SELECTOR, "input.nav-progressive-attribute.nav-input")
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-progressive-attribute.nav-input")

# Atrributes []
driver.find_element(By.CSS_SELECTOR, "[role='searchbox']")
driver.find_element(By.CSS_SELECTOR, "[role='searchbox'][type='text'][...][...]")
# attr + tag
driver.find_element(By.CSS_SELECTOR, "input[role='searchbox']")

# attr + class + tag  (Recommended order: tag + id + class + attr)
driver.find_element(By.CSS_SELECTOR, "input.nav-input[role='searchbox']")
driver.find_element(By.CSS_SELECTOR, ".nav-input[role='searchbox']")
driver.find_element(By.CSS_SELECTOR, "#id.nav-input[role='searchbox']")

# partial match (contains) *=
driver.find_element(By.CSS_SELECTOR, "[href*='/books-used-books-textbooks/']")
driver.find_element(By.CSS_SELECTOR, "[class*='styles_ndsHeading']")
driver.find_element(By.CSS_SELECTOR, "[class*='styles_ndsHeading'][class*='styles_fontSize']")

#homework
driver.find_element(By.CSS_SELECTOR, ".flex--item fs-headline1 fw-bold lh-xs mb8 ws-nowrap")"
driver.find_element(By.CSS_SELECTOR,".flex--item js-terms fs-caption fc-black-400 ta-left")
driver.find_element(By.CSS_SELECTOR,"#email")
driver.find_element(By.CSS_SELECTOR,"#password")
driver.find_element(By.CSS_SELECTOR, "#submit-button")
driver.find_element(By.CSS_SELECTOR, ".flex--item s-btn s-btn__icon s-btn__google bar-md ba bc-black-225")
driver.find_element(By.CSS_SELECTOR,".flex--item s-btn s-btn__icon s-btn__github bar-md ba bc-black-225")
