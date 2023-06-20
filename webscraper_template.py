# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import Firefox #Chrome
from selenium.webdriver.chrome.options import Options
from db_schema import table, engine
from sqlalchemy.orm import sessionmaker


def check_exists_by_xpath(xpath, driver):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

Session = sessionmaker(bind = engine)
session = Session()

ooptions = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
options.add_argument('log-level=3')
driver = Firefox(options=options)

base_url = ""
url_list = []
for url in url_list:
    driver.get(url)
    if check_exists_by_xpath(xpath, driver):
        element1 = driver.find_elements_by_xpath('//html/body').text ###look for xpath elements
    ins = table(name = element1) #insert in table
    session.add(ins)
    session.commit()

driver.quit()
