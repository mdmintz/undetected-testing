import time
from seleniumbase import page_actions
from seleniumbase import DriverContext
from sbvirtualdisplay import Display


def verify_success(driver):
    page_actions.wait_for_text(
        driver, "OH YEAH, you passed!", "h1", by="css selector"
    )
    print("\n Success! Website did not detect Selenium!")


def fail_me():
    raise Exception('Selenium was detected! Try using: "pytest --uc"')


display = Display(visible=0, size=(1440, 1880))
display.start()
with DriverContext(uc=True, headless=False) as driver:
    driver.get("https://nowsecure.nl/#relax")
    try:
        verify_success(driver)
    except Exception:
        if page_actions.is_element_visible(
            driver, 'input[value*="Verify"]'
        ):
            element = driver.find_element(
                "css selector", 'input[value*="Verify"]'
            )
            element.click()
        elif page_actions.is_element_visible(
            driver, 'iframe[title*="challenge"]'
        ):
            element = driver.find_element(
                "css selector", 'iframe[title*="challenge"]'
            )
            driver.switch_to.frame(element)
            driver.find_element("css selector", "span.mark").click()
        else:
            fail_me()
        try:
            verify_success(driver)
        except Exception:
            fail_me()
    time.sleep(2)
    screenshot_name = "now_secure_image.png"
    driver.save_screenshot(screenshot_name)
    print("\nScreenshot saved to: %s\n" % screenshot_name)
display.stop()
