from seleniumbase import SB

with SB(uc=True, test=True, ad_block=True) as sb:
    url = "https://iphey.com"
    sb.activate_cdp_mode()
    sb.open(url)
    sb.sleep(8)
    trustworthy = "div.trustworthy span"
    sb.wait_for_element(trustworthy)
    sb.remove_elements(".banner")  # Remove ad banner
    sb.sleep(1)
    sb.assert_text("Trustworthy", trustworthy)
    sb.highlight(trustworthy, loops=10)
    sb.sleep(1)
    section = '''[onclick="window.location='#%s'"] .verified'''
    sb.highlight(section % "browser")
    sb.highlight(section % "location")
    sb.highlight(section % "ip-address")
    sb.highlight(section % "hardware")
    sb.highlight(section % "software")
    sb.save_screenshot_to_logs()
