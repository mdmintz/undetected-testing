"""Reddit Search / Bypasses reCAPTCHA."""
from seleniumbase import sb_cdp
from seleniumbase import shared_utils

search = "reddit+scraper"
url = f"https://www.reddit.com/r/webscraping/search/?q={search}"
try:
    if shared_utils.is_linux():
        sb = sb_cdp.Chrome(url)
    else:
        sb = sb_cdp.Chrome(url, use_chromium=True)
    sb.solve_captcha()  # Might not be needed
    post_title = '[data-testid="post-title"]'
    sb.wait_for_element(post_title)
    for i in range(8):
        sb.scroll_down(25)
        sb.sleep(0.2)
    posts = sb.select_all(post_title)
    print('*** Reddit Posts for "%s":' % search)
    for post in posts:
        print("* " + post.text)
    sb.save_screenshot_to_logs()
except Exception as e:
    print(e)
