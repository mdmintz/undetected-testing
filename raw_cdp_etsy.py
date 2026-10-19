from seleniumbase import sb_cdp

try:
    sb = sb_cdp.Chrome(incognito=True)
    sb.goto("https://www.etsy.com/")
    sb.sleep(2.5)
    sb.solve_captcha()
    sb.sleep(1.5)
    search = "FIFA Keychains"
    required_text = "keychain"
    sb.press_keys('input[data-id="search-query"]', search)
    sb.sleep(1)
    sb.click('button[aria-label="Search"]')
    sb.sleep(2.5)
    sb.solve_captcha()
    sb.sleep(1)
    for i in range(15):
        sb.scroll_down(15)
        sb.sleep(0.15)
    sb.click_if_visible('button[aria-label="Ok"]')
    soup = sb.get_beautiful_soup()
    items = soup.select("div.v2-listing-card__info")
    num = 0
    print('*** Etsy search for "%s":' % search)
    print('    (Results must contain "%s")' % required_text)
    for item in items:
        title_element = item.select_one("h3.v2-listing-card__title")
        price_element = item.select_one("div.n-listing-card__price")
        if title_element and price_element:
            title = title_element.get_text()
            price = price_element.get_text()
            if required_text.lower() in title.lower():
                num += 1
                title = " ".join(title.split()).strip()
                price = price.replace("Sale Price", "").strip().split("\n")[0]
                print(f"* <====== {num} ======>")
                print(title)
                print(price.strip().split("\n")[0])
    print(f"*** {num} total items found!")
    folder = "downloaded_files"
    file_name = "etsy_results.html"
    file_name_2 = "etsy_results.png"
    file_name_3 = "etsy_results.pdf"
    sb.save_as_html(file_name, folder)
    sb.save_screenshot(file_name_2, folder)
    sb.save_as_pdf(file_name_3, folder)
    print('"./%s/%s" was saved!' % (folder, file_name))
except Exception as e:
    print(e)
