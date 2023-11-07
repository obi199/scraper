# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import Firefox #Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from db_schema import table, engine
from sqlalchemy.orm import sessionmaker

options = Options()
#options.add_argument('--headless')
options.add_argument("--start-maximized")
options.add_argument('log-level=3')

driver = webdriver.Firefox(options=options) 

url = "https://duckduckgo.com/"
driver.get(url)
element = "//*[@id="searchbox_input"]"
driver.find_element(By.XPATH,element)

###...do something here....

driver.quit()

###for database###
#Session = sessionmaker(bind = engine)
#session = Session()

#ins = table(name = element) #insert in table
#session.add(ins)
#session.commit()
