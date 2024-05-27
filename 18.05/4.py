from selenium import webdriver

# create webdriver object
driver = webdriver.Chrome()

# get lambdatest
driver.get("[https://www.lambdatest.com/](https://www.lambdatest.com/)")

# get element
element = driver.find_element_by_id("useremail")

# send keys
element.clear()