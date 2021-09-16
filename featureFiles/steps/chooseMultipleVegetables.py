import time
from behave import *
from selenium import webdriver


@then('select six kilos of carrots')
def select_six_kilos_of_carrots(context):
    plus_button = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[5]/div[2]/a[2]"
    for i in range(5):
        context.driver.find_element_by_xpath(plus_button).click()
        time.sleep(2)


@then('remove three kilos from carrots')
def remove_carrots(context):
    minus_button = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[5]/div[2]/a[1]"
    for i in range(3):
        context.driver.find_element_by_xpath(minus_button).click()
        time.sleep(2)


@then('add to cart carrots')
def add_to_cart_carrots(context):
    cart_button = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[5]/div[3]/button[1]"
    context.driver.find_element_by_xpath(cart_button).click()
    time.sleep(2)


@then('select two kilo of pears')
def select_a_kilo_of_pears(context):
    plus_button = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[21]/div[2]/a[2]"
    context.driver.find_element_by_xpath(plus_button).click()
    time.sleep(2)


@then('add to cart pears')
def add_to_cart_pears(context):
    cart_button = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[21]/div[3]/button[1]"
    context.driver.find_element_by_xpath(cart_button).click()
    time.sleep(2)


@then('search for walnuts')
def search_walnuts(context):
    search_bar = "//header/div[1]/div[2]/form[1]/input[1]"
    context.driver.find_element_by_xpath(search_bar).send_keys("walnuts")
    time.sleep(2)


@then('select one kilo of walnuts')
def select_walnuts(context):
    plus_button = "//a[contains(text(),'+')]"
    for i in range(3):
        context.driver.find_element_by_xpath(plus_button).click()
        time.sleep(2)


@then('add to cart walnuts')
def add_to_cart(context):
    cart_button = "//button[contains(text(),'ADD TO CART')]"
    context.driver.find_element_by_xpath(cart_button).click()
    time.sleep(2)


@then('click bag button')
def bag_button(context):
    bags_button = "//header/div[1]/div[3]/a[4]/img[1]"
    context.driver.find_element_by_xpath(bags_button).click()
    time.sleep(2)


@then('remove kilo of pears from cart')
def remove_pears(context):
    remove_button = "//header/div[1]/div[3]/div[2]/div[1]/div[1]/ul[1]/li[1]/a[1]"
    context.driver.find_element_by_xpath(remove_button).click()
    time.sleep(2)


@then('Close the browser')
def close_browser(context):
    context.driver.close()
