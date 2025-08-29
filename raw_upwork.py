from seleniumbase import SB
from seleniumbase import config as sb_config

with SB(uc=True, test=True) as sb:
    url = "https://www.upwork.com/nx/search/jobs/"
    sb.uc_open_with_reconnect(url, 4)
    sb.uc_gui_click_captcha()
    sb.sleep(4)
    if (
        hasattr(sb_config, "_saved_cf_x_y")
        and not sb.is_element_visible('input[type="search"]')
    ):
        x, y = sb_config._saved_cf_x_y
        sb.uc_open_with_disconnect(url, 4)
        sb.uc_gui_click_x_y(x, y)
        sb.sleep(4)
        sb.reconnect()
    sb.press_keys('input[type="search"]', "WordPress\n")
    sb.sleep(2)
    print(sb.get_text('[data-test="JobsList"]'))
