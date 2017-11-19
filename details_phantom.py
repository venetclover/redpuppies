from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AsycDownloader():
    SELECTOR_TYPES = {
        'class': (By.CLASS_NAME, find_elements_by_css_selector)
    }

    def __init__(self):
        cap = webdriver.DesiredCapabilities.PHANTOMJS
        cap["phantomjs.page.settings.javascriptEnabled"] = True
        cap["phantomjs.page.settings.loadImages"] = True
        cap["phantomjs.page.settings.userAgent"] = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
        self.driver = webdriver.PhantomJS('phantom/bin/phantomjs', desired_capabilities=cap)

    def get_async_element(self, url, asyc_element_selector, selector_type='class', waiting_time=10):
        driver = webdriver.PhantomJS('phantom/bin/phantomjs', desired_capabilities=cap)
        driver.get("url")
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((SELECTOR_TYPES[selector_type], asyc_element_selector))
            )
        finally:
            driver.quit()
