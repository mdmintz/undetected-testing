# undetected-testing

Learn how [SeleniumBase](https://github.com/seleniumbase/SeleniumBase) can evade detection by sites with anti-bot services.

First:

```bash
> pip install -U seleniumbase
```

Now you can try running a test ([raw_gitlab.py](https://github.com/mdmintz/undetected-testing/blob/master/raw_gitlab.py)) to see if SeleniumBase can fool the GitLab welcome page, which won't let you through if they detect an automation framework:

```bash
> python raw_gitlab.py

 Success! Website did not detect SeleniumBase!

```

The code:

```python
from seleniumbase import SB

with SB(uc=True, test=True, locale_code="en") as sb:
    url = "https://gitlab.com/users/sign_in"
    sb.activate_cdp_mode(url)
    sb.uc_gui_click_captcha()
    sb.assert_text("Username", '[for="user_login"]', timeout=3)
    sb.assert_element('label[for="user_login"]')
    sb.highlight('button:contains("Sign in")')
    sb.highlight('h1:contains("GitLab.com")')
    sb.post_message("SeleniumBase wasn't detected", duration=4)
```

--------

Here's a more advanced example, ([raw_bestwestern.py](https://github.com/mdmintz/undetected-testing/blob/master/raw_bestwestern.py))

```python
from seleniumbase import SB

with SB(uc=True, test=True, locale_code="en") as sb:
    url = "https://www.bestwestern.com/en_US.html"
    sb.activate_cdp_mode(url)
    sb.sleep(2.5)
    sb.cdp.click_if_visible("div.onetrust-close-btn-handler")
    sb.sleep(1)
    sb.cdp.click("input#destination-input")
    sb.sleep(2)
    location = "Palm Springs, CA, USA"
    sb.cdp.press_keys("input#destination-input", location)
    sb.sleep(1)
    sb.cdp.click("ul#google-suggestions li")
    sb.sleep(1)
    sb.cdp.click("button#btn-modify-stay-update")
    sb.sleep(4)
    sb.cdp.click("label#available-label")
    sb.sleep(2.5)
    print("Best Western Hotels in %s:" % location)
    summary_details = sb.cdp.get_text("#summary-details-column")
    dates = summary_details.split("ROOM")[0].split("DATES")[-1].strip()
    print("(Dates: %s)" % dates)
    flip_cards = sb.cdp.select_all(".flipCard")
    for i, flip_card in enumerate(flip_cards):
        hotel = flip_card.query_selector(".hotelName")
        price = flip_card.query_selector(".priceSection")
        if hotel and price:
            print("* %s: %s => %s" % (
                i + 1, hotel.text.strip(), price.text.strip())
            )
```

--------

SeleniumBase Undetected Mode has been successful in bypassing detection on several sites that use automation-detection services:

<img width="568" alt="Undetected SeleniumBase" src="https://user-images.githubusercontent.com/6788579/213031519-0220d19f-e210-4858-b6b5-9253b112efe4.png">
