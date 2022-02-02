import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

# First Unit test for Chrome browser- for maximized window
class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_chrome(self):

        driver = webdriver.Chrome()
        driver.get("https://qasvus.wordpress.com/")
        driver.maximize_window()
        # Set waiting time after get.url() - 3 seconds for Chrome
        driver.implicitly_wait(3)
        print(driver.find_element(By.XPATH, '//*[@href="https://qasvus.wordpress.com"]').get_attribute("href"))
        print(driver.find_element(By.XPATH, "//img[@class='wp-image-55 size-full']").get_attribute("src"))

        # Set wait.until() for Submit button in Chrome using "XPath"

        driver.implicitly_wait(3)
        print(driver.find_element(By.XPATH, '//*[@href="https://qasvus.wordpress.com"]').get_attribute("href"))
        print(driver.find_element(By.XPATH, "//img[@class='wp-image-55 size-full']").get_attribute("src"))

        # Do assertions for driver title
        # Print driver title with custom explanation string
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print(driver.title)
        if "California Real Estate – QA at Silicon Valley Real Estate" not in driver.title:
            raise Exception("Title for California Real Estate page is wrong!")
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH, "//h2[contains(text(),'Send Us a Message')]").get_attribute(
            "value")

        # Clear fields: Text area, Name, Email
        elem = driver.find_element(By.NAME, "g2-name")
        elem.clear()
        elem = driver.find_element(By.ID, "g2-email")
        elem.clear()
        elem = driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']")
        elem.clear()


        # Fill out all fields and click on Submit button
        driver.implicitly_wait(1)
        driver.find_element(By.NAME, "g2-name").send_keys("Katia Semionel")
        driver.implicitly_wait(1)
        driver.find_element(By.ID, "g2-email").send_keys("katiakatia123@gmail.com")
        driver.implicitly_wait(1)
        driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").send_keys(
            "Hello")
        driver.find_element(By.CLASS_NAME, "pushbutton-wide").send_keys('\n')
        driver.implicitly_wait(3)
        time.sleep(1)

        # Use "try/except" method to wait "go back" link is VISIBLE and click it after
        driver.find_element(By.LINK_TEXT, "go back").send_keys('\n')
        time.sleep(2)
        print(driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").get_attribute("type"))

        # Do assertion for page title and print it with custom string
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print(driver.title)
        if "California Real Estate – QA at Silicon Valley Real Estate" not in driver.title:
            raise Exception("Title for California Real Estate page is wrong!")
        driver.implicitly_wait(2)

        driver.quit()

    def test_chrome1120x550(self):

        driver = webdriver.Chrome()
        driver.get("https://qasvus.wordpress.com/")
        driver.set_window_size(1120, 550)
        driver.implicitly_wait(3)
        print(driver.find_element(By.XPATH, '//*[@href="https://qasvus.wordpress.com"]').get_attribute("href"))
        print(driver.find_element(By.XPATH, "//img[@class='wp-image-55 size-full']").get_attribute("src"))

        driver.implicitly_wait(3)
        print(driver.find_element(By.XPATH, '//*[@href="https://qasvus.wordpress.com"]').get_attribute("href"))
        print(driver.find_element(By.XPATH, "//img[@class='wp-image-55 size-full']").get_attribute("src"))

        # Do assertions for driver title
        # Print driver title with custom explanation string
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print(driver.title)
        if "California Real Estate – QA at Silicon Valley Real Estate" not in driver.title:
            raise Exception("Title for California Real Estate page is wrong!")
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH, "//h2[contains(text(),'Send Us a Message')]").get_attribute(
            "value")

        # Clear fields: Text area, Name, Email
        elem = driver.find_element(By.NAME, "g2-name")
        elem.clear()
        elem = driver.find_element(By.ID, "g2-email")
        elem.clear()
        elem = driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']")
        elem.clear()

        # Fill out all fields and click on Submit button
        driver.implicitly_wait(1)
        driver.find_element(By.NAME, "g2-name").send_keys("Katia Semionel")
        driver.implicitly_wait(1)
        driver.find_element(By.ID, "g2-email").send_keys("katiakatia123@gmail.com")
        driver.implicitly_wait(1)
        driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").send_keys(
            "Hello")
        driver.find_element(By.CLASS_NAME, "pushbutton-wide").send_keys('\n')
        driver.implicitly_wait(3)
        time.sleep(1)

        # Use "try/except" method to wait "go back" link is VISIBLE and click it after
        driver.find_element(By.LINK_TEXT, "go back").send_keys('\n')
        time.sleep(2)
        print(driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").get_attribute("type"))

        # Do assertion for page title and print it with custom string
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print(driver.title)
        if "California Real Estate – QA at Silicon Valley Real Estate" not in driver.title:
            raise Exception("Title for California Real Estate page is wrong!")
        driver.implicitly_wait(2)

        driver.quit()


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_firefox(self):

        driver = webdriver.Firefox()
        driver.get("https://qasvus.wordpress.com/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        print(driver.find_element(By.XPATH, '//*[@href="https://qasvus.wordpress.com"]').get_attribute("href"))
        print(driver.find_element(By.XPATH, "//img[@class='wp-image-55 size-full']").get_attribute("src"))

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print(driver.title)
        if "California Real Estate – QA at Silicon Valley Real Estate" not in driver.title:
            raise Exception("Title for California Real Estate page is wrong!")
        driver.implicitly_wait(2)

        # Clear fields: Text area, Name, Email
        elem = driver.find_element(By.NAME, "g2-name")
        elem.clear()
        elem = driver.find_element(By.ID, "g2-email")
        elem.clear()
        elem = driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']")
        elem.clear()
        driver.find_element(By.XPATH, "//h2[contains(text(),'Send Us a Message')]").get_attribute(
            "value")
        driver.implicitly_wait(1)
        driver.find_element(By.NAME, "g2-name").send_keys("Katia Semionel")
        driver.implicitly_wait(1)
        driver.find_element(By.ID, "g2-email").send_keys("katiakatia123@gmail.com")
        driver.implicitly_wait(1)
        driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").send_keys("Hello")
        driver.find_element(By.CLASS_NAME, "pushbutton-wide").send_keys('\n')
        driver.implicitly_wait(3)
        print(driver.find_element(By.XPATH, "//button[@class='pushbutton-wide']").get_attribute("type"))

        # Do assertion for page title and print it with custom string
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print(driver.title)
        if "California Real Estate – QA at Silicon Valley Real Estate" not in driver.title:
            raise Exception("Title for California Real Estate page is wrong!")

        driver.quit()

    def test_firefox_1250x850(self):
        driver = webdriver.Firefox()
        driver.get("https://qasvus.wordpress.com/")
        driver.set_window_size(1250, 850)
        driver.implicitly_wait(5)
        print(driver.find_element(By.XPATH, '//*[@href="https://qasvus.wordpress.com"]').get_attribute("href"))
        print(driver.find_element(By.XPATH, "//img[@class='wp-image-55 size-full']").get_attribute("src"))

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print(driver.title)
        if not "California Real Estate – QA at Silicon Valley Real Estate" in driver.title:
            raise Exception("Title for California Real Estate page is wrong!")
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH, "//h2[contains(text(),'Send Us a Message')]").get_attribute(
            "value")

        # Clear fields: Text area, Name, Email
        elem = driver.find_element(By.NAME, "g2-name")
        elem.clear()
        elem = driver.find_element(By.ID, "g2-email")
        elem.clear()
        elem = driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']")
        elem.clear()

        driver.implicitly_wait(1)
        driver.find_element(By.NAME, "g2-name").send_keys("Katia Semionel")
        driver.implicitly_wait(1)
        driver.find_element(By.ID, "g2-email").send_keys("katiakatia123@gmail.com")
        driver.implicitly_wait(1)
        driver.find_element(By.XPATH, "//textarea[@id='contact-form-comment-g2-message']").send_keys(
            "Hello")
        driver.find_element(By.CLASS_NAME, "pushbutton-wide").send_keys('\n')

        # Do assertion for page title and print it with custom string
        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print(driver.title)
        if "California Real Estate – QA at Silicon Valley Real Estate" not in driver.title:
            raise Exception("Title for California Real Estate page is wrong!")
        driver.implicitly_wait(2)
        driver.quit()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()