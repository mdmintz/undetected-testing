import os
from seleniumbase import SB

with SB(uc=True, test=True, proxy=os.environ["proxy_1"]) as sb:
    url = "https://chatgpt.com/"
    sb.uc_open_with_reconnect(url, 3)
    sb.uc_gui_click_captcha()
    sb.sleep(1)
    sb.uc_gui_handle_captcha()
    sb.disconnect()
    sb.sleep(1)
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
        print("*** Response from ChatGPT: ***\n%s" % soup.replace("\n:", ":"))
        success = True
    except Exception:
        print(sb.get_page_source())
    finally:
        if not success:
            print("\n Unable to find ChatGPT response in HTML!")
    sb.sleep(1)
