import asyncio
import os
import sys
from bs4 import BeautifulSoup as Soup
from seleniumbase.core import sb_cdp
from seleniumbase.undetected import cdp_driver

binary_location = None
if "linux" in sys.platform.lower():
    if os.path.exists("/bin/google-chrome-stable"):
        binary_location = "/bin/google-chrome-stable"
    elif os.path.exists("/usr/bin/google-chrome"):
        binary_location = "/usr/bin/google-chrome"

url = "https://www.indeed.com/companies"
loop = asyncio.new_event_loop()
driver = cdp_driver.cdp_util.start_sync(
    browser_executable_path=binary_location
)
page = loop.run_until_complete(driver.get(url))
sb = sb_cdp.CDPMethods(loop, page, driver)

company = "NASA Jet Propulsion Laboratory"
search_box = 'input[data-testid="company-search-box"]'
captcha_grid = '[style="display: grid;"]'

if sb.is_element_present(captcha_grid):
    sb.gui_click_element(captcha_grid)

sb.press_keys(search_box, company)
sb.click('button[type="submit"]')
if not sb.is_element_present('a:contains("%s")' % company):
    if sb.is_element_present(captcha_grid):
        sb.gui_click_element(captcha_grid)

sb.click('a:contains("%s")' % company)
sb.sleep(3)
sb.highlight('div[itemprop="name"]')
sb.sleep(1)
sb.highlight('h2:contains("About the company")')
sb.sleep(2)
for i in range(10):
    sb.scroll_down(12)
    sb.sleep(0.14)
info = sb.find_element('[data-testid="AboutSection-section"]')
soup = Soup(info.get_html()).get_text("\n").strip()
print("*** %s: ***\n%s" % (company, soup.replace("\n:", ":")))
