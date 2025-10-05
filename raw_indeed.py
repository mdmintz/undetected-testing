from seleniumbase import SB

with SB(
    uc=True, test=True, xvfb=True, xvfb_metrics="1920,1080", ad_block=True
) as sb:
    url = "https://www.indeed.com/companies/search"
    sb.activate_cdp_mode(url)
    sb.sleep(3)
    sb.uc_gui_click_captcha()
    sb.sleep(2)
    company = "NASA Jet Propulsion Laboratory"
    sb.press_keys("input#company-search", company)
    sb.click('button[type="submit"]')
    sb.click('a:contains("%s")' % company)
    sb.sleep(3)
    sb.uc_gui_click_captcha()
    sb.sleep(1)
    sb.cdp.highlight('div[itemprop="name"]')
    sb.sleep(1)
    sb.cdp.highlight('h2:contains("About the company")')
    sb.sleep(1)
    for i in range(10):
        sb.cdp.scroll_down(12)
        sb.sleep(0.15)
    info = sb.find_element('[data-testid="AboutSection-section"]')
    soup = sb.get_beautiful_soup(info.get_html()).get_text("\n").strip()
    print("*** %s: ***\n%s" % (company, soup.replace("\n:", ":")))
    sb.save_screenshot_to_logs()
