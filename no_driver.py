import nodriver
import time
from sbvirtualdisplay import Display


async def main():
    display = Display(visible=False, size=(1366, 768))
    display.start()
    browser = await nodriver.start()
    page = await browser.get("https://www.virtualmanager.com/en/login")
    time.sleep(3)
    print(await page.evaluate("document.title"))
    display.stop()

if __name__ == "__main__":
    nodriver.loop().run_until_complete(main())
