import os
from seleniumbase import Driver

try:
    proxy = os.environ["proxy_1"]
except Exception:
    proxy = None

print("First part of proxy IP:")
print(proxy.split("@")[-1].split(":")[0].split(".")[0])

driver = Driver(proxy=proxy, uc=True)
driver.uc_activate_cdp_mode("https://api.ipify.org")
print("Full IP from ipify:")
print(driver.page_source)
driver.quit()
