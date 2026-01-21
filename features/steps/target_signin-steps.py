from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when ('click on account button')
def click_account_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[aria-label='Account, sign in']").click()


@when('click on signin button')
def click_signin_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test='accountNav-signIn']").click()


@then('signin button is displayed')
def signin_button(context):
    expected_result = "login"
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "#login").button
    print(actual_result)
    assert expected_result in actual_result, f"Expected_result {expected_result} not in actual result {actual_result}"