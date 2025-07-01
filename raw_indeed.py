from seleniumbase import SB
from seleniumbase import config as sb_config

with SB(uc=True, test=True) as sb:
    url = "https://www.indeed.com/companies/search"
    sb.uc_open_with_reconnect(url, 3)
    sb.uc_gui_click_captcha()
    sb.sleep(3)
    if (
        hasattr(sb_config, "_saved_cf_x_y")
        and not sb.is_element_visible(
            'input[data-testid="company-search-box"]'
        )
    ):
        x, y = sb_config._saved_cf_x_y
        sb.uc_open_with_disconnect(url, 3)
        sb.uc_gui_click_x_y(x, y)
        sb.sleep(3)
        sb.reconnect()
    company = "NASA Jet Propulsion Laboratory"
    sb.press_keys('input[data-testid="company-search-box"]', company)
    sb.click('button[type="submit"]')
    sb.click('a:contains("%s")' % company)
    if hasattr(sb_config, "_saved_cf_x_y"):
        sb.disconnect()
        x, y = sb_config._saved_cf_x_y
        sb.uc_gui_click_x_y(x, y)
        sb.sleep(3)
    elif sb.is_text_visible("Additional Verification Required"):
        sb.sleep(3)
        sb.uc_gui_click_captcha()
        sb.sleep(3)
        if sb.is_text_visible("Additional Verification Required"):
            sb.refresh()
            sb.disconnect()
            x, y = sb_config._saved_cf_x_y
            sb.uc_gui_click_x_y(x, y)
            sb.sleep(3)
    sb.reconnect()
    sb.highlight('div[itemprop="name"]')
    sb.sleep(1)
    sb.highlight('h2:contains("About the company")')
    sb.sleep(2)
    info = sb.find_element('[data-testid="AboutSection-section"]')
    info = info.text.strip().replace("\n\n", "\n")
    print("*** %s: ***\n%s" % (company, info.replace("\n:", ":")))
