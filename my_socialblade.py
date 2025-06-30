"""Bypass bot-detection to view SocialBlade ranks for YouTube"""
from seleniumbase import SB

with SB(uc=True, test=True, ad_block=True, pls="none") as sb:
    url = "https://socialblade.com/youtube/channel/UCSQElO8vQmNPuTgdd83BHdw"
    sb.activate_cdp_mode(url)
    sb.sleep(2)
    if not sb.is_element_present('[class*="grid lg:hidden"]'):
        sb.uc_gui_click_captcha()
        sb.sleep(1.5)
    sb.cdp.remove_elements("#lngtd-top-sticky")
    sb.sleep(1)
    name = sb.cdp.get_text("h3")
    ch_name = name.split(" ")[-1]
    name = name.split(" @")[0]
    link = "https://www.youtube.com/%s" % ch_name
    print("********** SocialBlade Stats for %s: **********" % name)
    print(">>> (Link: %s) <<<" % link)
    print(sb.get_text('[class*="grid lg:hidden"]'))
    print("********** SocialBlade Ranks: **********")
    print(sb.get_text('[class*="gap-3 flex-1"]'))
    for i in range(17):
        sb.cdp.scroll_down(6)
        sb.sleep(0.1)
    sb.sleep(2)
