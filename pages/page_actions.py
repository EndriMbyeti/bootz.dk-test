import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def scroll_until_visible(driver, by, value, timeout=10, scroll_amount=400):
    """
    Scroll down the page until the specified element is visible.

    :param driver: The Selenium WebDriver instance.
    :param by: The type of locator (e.g., By.ID, By.CSS_SELECTOR).
    :param value: The locator value for the target element.
    :param timeout: Maximum time to wait for the element to become visible.
    :param scroll_amount: The number of pixels to scroll down each time.
    :return: The WebElement if found, else raises TimeoutException.
    """
    end_time = time.time() + timeout
    while time.time() < end_time:
        try:
            # Check if the element is visible
            element = WebDriverWait(driver, 1).until(EC.visibility_of_element_located((by, value)))
            return element  # Return the element if it's visible
        except:
            # Scroll down a bit and try again
            driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
            time.sleep(0.5)  # Short sleep to allow for scrolling

    raise TimeoutException(f"Element with locator ({by}, {value}) not found within {timeout} seconds.")


def click_element_by_xpath(driver, xpath):
    """
    Clicks on the first element matching the given XPath.

    :param driver: The Selenium WebDriver instance.
    :param xpath: The XPath to locate the element.
    """
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    element.click()


def close_cookies(driver):
    """
    closes the cookies popup

    :param driver: The Selenium WebDriver instance.
    """
    try:
        cookies_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button#onetrust-accept-btn-handler"))
        )
        cookies_button.click()
        print("\nCookies accepted.")
        time.sleep(1)  # Short wait after accepting cookies
    except:
        print("Cookies acceptance button not found; continuing with the test.")


def set_lenguage_english(driver):
    """
    set the lenguage of the app to english

    :param driver: The Selenium WebDriver instance.
    """
    xpathlanguage = "//button[@aria-label='Choose your language']"
    click_element_by_xpath(driver, xpathlanguage)
    time.sleep(1)

    xpathenglish = "//span[text()='English']"
    click_element_by_xpath(driver, xpathenglish)
    print("Language set to English.")
