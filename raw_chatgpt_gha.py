import os
from seleniumbase import SB

try:
    proxy = os.environ["proxy_1"]
except Exception:
    proxy = None

with SB(uc=True, test=True, proxy=proxy) as sb:
    url = "https://chatgpt.com/"
    sb.uc_open_with_reconnect(url, 2.5)
    sb.uc_gui_click_captcha()
    sb.sleep(0.75)
    sb.uc_gui_handle_captcha()
    sb.disconnect()
    sb.sleep(0.75)
    query = "Compare Playwright to SeleniumBase in under 178 words"
    sb.uc_gui_write(query)
    sb.uc_gui_press_key("ENTER")
    print('*** Input for ChatGPT: ***\n"%s"' % query)
    sb.sleep(10)
    sb.connect()
    success = False
    try:
        chat = sb.find_element(
            '[data-message-author-role="assistant"] .markdown'
        )
        soup = sb.get_beautiful_soup(chat.get_attribute("outerHTML"))
        soup = soup.get_text("\n").strip()
        soup = soup.replace("\n\n\n", "\n\n")
        soup = soup.replace("\n\n\n", "\n\n")
        print("*** Response from ChatGPT: ***\n%s" % soup)
        success = True
    except Exception:
        print(sb.get_page_source())
    finally:
        if not success:
            print("\n Unable to find ChatGPT response in HTML!")
    sb.sleep(1)
