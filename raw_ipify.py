from seleniumbase import Driver

driver = Driver()
driver.get("https://api.ipify.org")
print(driver.page_source)
driver.quit()
