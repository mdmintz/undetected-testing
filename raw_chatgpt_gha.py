from contextlib import suppress
from seleniumbase import SB

with SB(uc=True, test=True, ad_block=True) as sb:
    url = "https://chatgpt.com/"
    sb.uc_open_with_disconnect(url)
    sb.sleep(2.5)
    query = "Compare Playwright to SeleniumBase in under 178 words"
    sb.uc_gui_press_keys(query + "\n")
    print('*** Input for ChatGPT: ***\n"%s"' % query)
    sb.sleep(7.5)
    sb.connect()
    with suppress(Exception):
        # The "Stop" button disappears when ChatGPT is done typing a response
        sb.wait_for_element_not_visible(
            'button[data-testid="stop-button"]', timeout=12
        )
    chat = sb.find_element('[data-message-author-role="assistant"] .markdown')
    soup = sb.get_beautiful_soup(chat.get_attribute("outerHTML"))
    soup = soup.get_text("\n").strip()
    print("*** Response from ChatGPT: ***\n%s" % soup.replace("\n:", ":"))
    sb.sleep(1)
