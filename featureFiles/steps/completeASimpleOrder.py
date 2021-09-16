import time
from behave import *
from selenium import webdriver


@given('launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(r"C:\Users\yaprlk\Downloads\chromedriver_win32\chromedriver.exe")

@when('open the Green Kart website')
def open_the_website(context):
    context.driver.get(r"https://rahulshettyacademy.com/seleniumPractise/#/")

@then('type the vegetable name (carrot) in the searchbar')
def type_the_vegetable_name(context):
    context.driver.find_element_by_xpath("//header/div[1]/div[2]/form[1]/input[1]").send_keys("carrot")
    time.sleep(2)

@then('click one time on the plus icon')
def click_plus_icon(context):
    context.driver.find_element_by_xpath("//a[contains(text(),'+')]").click()
    time.sleep(2)

@then('click Add to cart icon')
def click_add_to_cart_icon(context):
    context.driver.find_element_by_xpath("//button[contains(text(),'ADD TO CART')]").click()
    time.sleep(2)

@then('click bag icon to purchase order')
def click_bag_icon(context):
    context.driver.find_element_by_xpath("//header/div[1]/div[3]/a[4]/img[1]").click()
    time.sleep(2)

@then('check out button')
def check_out_button(context):
    context.driver.find_element_by_xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
    time.sleep(2)

@then('click place order')
def click_place_order(context):
    context.driver.find_element_by_xpath("//button[contains(text(),'Place Order')]").click()
    time.sleep(2)

@then('tick terms and condition button')
def tick_terms_and_condition_button(context):
    context.driver.find_element_by_xpath("//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/input[1]").click()
    time.sleep(2)

@then('click proceed to complete order')
def click_proceed(context):
    context.driver.find_element_by_xpath("//button[contains(text(),'Proceed')]").click()
    time.sleep(2)

@then('Close browser')
def close_browser(context):
    context.driver.close()
