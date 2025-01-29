from contextlib import suppress
from seleniumbase import SB

with SB(uc=True, test=True, incognito=True) as sb:
    url = "https://chatgpt.com/"
    sb.activate_cdp_mode(url)
    sb.sleep(2)
    query = "Compare Playwright to SeleniumBase in under 178 words"
    try:
        sb.type("#prompt-textarea", query)
    except Exception:
        print(sb.get_page_source())
        sb.press_keys("#prompt-textarea", query)
    send_button = 'button[data-testid="send-button"]'
    sb.hover_and_click(send_button, send_button)
    sb.sleep(2)
    if sb.is_element_visible(send_button):
        sb.cdp.gui_click_element(send_button)
    print('*** Input for ChatGPT: ***\n"%s"' % query)
    with suppress(Exception):
        # The "Send" button reappears when ChatGPT is done typing a response
        sb.wait_for_element(send_button, timeout=22)
    try:
        chat = sb.find_element('[data-message-author-role="assistant"]')
    except Exception:
        chat = sb.find_element("main.relative")
    soup = sb.get_beautiful_soup(chat.get_html()).get_text("\n").strip()
    print("*** Response from ChatGPT: ***\n%s" % soup.replace("\n:", ":"))
    sb.sleep(3)
