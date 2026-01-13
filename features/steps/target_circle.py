from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

added_value_field = (By.CSS_SELECTOR, "h2[class*='styles_ndsHeading']")
storycards_field = (By.CSS_SELECTOR, ".sc-448837bd-1 ZtQGh storycard--text, .sc-448837bd-1 ZtQGh storycard--text")


@given("open target circle page")
def open_circle(context):
    context.driver.get("https://www.target.com/circle")


@when("unlock added value is displayed")
def two_storycards(context):
    context.driver.find_element(*added_value_field).text


@then("verify two storycards are displayed under unlock value field")
def verify_two_storycards(context):
  expected_result = "circle card, circle 360"
  actual_result = context.driver.find_element(*storycards_field).text
  print(actual_result)
  assert expected_result in actual_result, f"Expected result {expected_result} not found in actual result {actual_result}"