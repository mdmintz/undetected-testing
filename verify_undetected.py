import time
from seleniumbase import page_actions
from seleniumbase import DriverContext
from sbvirtualdisplay import Display


def verify_success(driver):
    page_actions.wait_for_text(
        driver, "OH YEAH, you passed!", "h1", by="css selector"
    )
    print("\nSuccess! Website did not detect Selenium!")


def fail_me():
    raise Exception('Selenium was detected! Try using: "pytest --uc"')


def save_screenshot(driver):
    time.sleep(2)
    screenshot_name = "now_secure_image.png"
    driver.save_screenshot(screenshot_name)
    print("\nScreenshot saved to: %s\n" % screenshot_name)


display = Display(visible=0, size=(1440, 1880))
display.start()
try:
    with DriverContext(uc=True, incognito=True, headless=False) as driver:
        driver.get("https://nowsecure.nl/#relax")
        verify_success(driver)
        save_screenshot(driver)
except Exception:
    with DriverContext(
        devtools=True, uc=True, incognito=True, headless=False
    ) as driver:
        try:
            verify_success(driver)
            save_screenshot(driver)
        except Exception:
            fail_me()
display.stop()
