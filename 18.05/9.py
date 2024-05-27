from selenium import webdriver

driver = webdriver.Chrome()

driver.implicitly_wait(10) # in seconds

driver.get("https://www.lambdatest.com/")

element = driver.find_element_by_id("testing_form")
