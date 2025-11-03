import os
from seleniumbase import Driver

try:
    proxy = os.environ["proxy_1"]
except Exception:
    proxy = None

driver = Driver(proxy=proxy)
driver.get("https://api.ipify.org")
print(driver.page_source)
driver.quit()
