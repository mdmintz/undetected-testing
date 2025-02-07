from seleniumbase import SB

with SB(uc=True, test=True) as sb:
    url = "https://www.indeed.com/companies/search"
    company = "NASA Jet Propulsion Laboratory"
    search_box = 'input[data-testid="company-search-box"]'
    sb.activate_cdp_mode(url)
    sb.sleep(2)
    if not sb.is_element_present(search_box):
        sb.uc_gui_click_captcha()
        sb.sleep(2)
    if not sb.is_element_present(search_box):
        sb.uc_gui_click_captcha()
        sb.sleep(2)
    if not sb.is_element_present(search_box):
        html = sb.cdp.get_element_html("body")
        soup = sb.get_beautiful_soup(html)
        print(soup.prettify())
    sb.press_keys(search_box, company)
    sb.click('button[type="submit"]')
    sb.click('a:contains("%s")' % company)
    sb.sleep(3)
    sb.cdp.highlight('div[itemprop="name"]')
    sb.sleep(1)
    sb.cdp.highlight('h2:contains("About the company")')
    sb.sleep(2)
    for i in range(10):
        sb.cdp.scroll_down(12)
        sb.sleep(0.14)
    info = sb.find_element('[data-testid="AboutSection-section"]')
    soup = sb.get_beautiful_soup(info.get_html()).get_text("\n").strip()
    print("*** %s: ***\n%s" % (company, soup.replace("\n:", ":")))
