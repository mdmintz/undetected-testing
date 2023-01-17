import time
from seleniumbase import page_actions
from seleniumbase import DriverContext


with DriverContext(uc=True, incognito=True) as driver:
    driver.get("https://nowsecure.nl/#relax")
    page_actions.wait_for_text(
        driver, "OH YEAH, you passed!", "h1", by="css selector"
    )
    print("\n Success! Website did not detect Selenium!")
    time.sleep(2)
    screenshot_name = "now_secure_image.png"
    driver.save_screenshot(screenshot_name)
    print("\nScreenshot saved to: %s" % screenshot_name)
