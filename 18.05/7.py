from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_id('city'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)