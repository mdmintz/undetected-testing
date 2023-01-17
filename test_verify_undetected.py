"""Determine if your browser is detectable by anti-bot services.
Some sites use scripts to detect Selenium and then block you."""
from seleniumbase import BaseCase

if __name__ == "__main__":
    from pytest import main
    main([__file__, "--uc", "--incognito", "-s"])


class UndetectedTest(BaseCase):
    def test_browser_is_undetected(self):
        if not self.undetectable or not self.incognito:
            self.get_new_driver(undetectable=True, incognito=True)
        self.open("https://nowsecure.nl/#relax")
        try:
            self.assert_text("OH YEAH, you passed!", "h1", timeout=6.75)
            self.post_message("Selenium wasn't detected!", duration=2.8)
            self._print("\n Success! Website did not detect Selenium! ")
            self.save_screenshot_to_logs()
        except Exception:
            self.fail('Selenium was detected! Try using: "pytest --uc"')
