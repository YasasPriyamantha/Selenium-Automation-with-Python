import time
from behave import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select


@then(u'choose a country')
def step_impl(context):
    drop_list = "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/select[1]"
    drop = Select(context.driver.find_element_by_xpath(drop_list))
    drop.select_by_visible_text("Angola")
    time.sleep(2)
