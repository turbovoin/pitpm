from selenium import webdriver

# create webdriver object
driver = webdriver.Chrome()

# get lambdatest
driver.get("[https://www.lambdatest.com/](https://www.lambdatest.com/)")

# get element
element = driver.find_element_by_id("useremail")

# send keys
element.send_keys("[emailid@lambdatest.com](mailto:emailid@lambdatest.com)")

# get element
button_element = driver.find_element_by_link_text("Start Free Testing")

# click the element
button_element.click()