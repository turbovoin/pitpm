# Go to the domain
driver.get("[https://www.lambdatest.com/](https://www.lambdatest.com/)")

# Now set the cookie.
cookie = {'name' : 'user', 'value' : 'vinayak'}
driver.add_cookie(cookie)