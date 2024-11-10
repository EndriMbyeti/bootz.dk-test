from pages.page_actions import *


# Helper function to initialize WebDriver
def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.boozt.com/dk/da")
    return driver


def test_boozt_dress_purchase():
    driver = setup_driver()

    try:
        # Step 1: Accept cookies if the prompt is present
        close_cookies(driver)

        # Set language to English
        set_lenguage_english(driver)

        # Step 2: Verify page title contains "Boozt.com | New styles every day"
        assert "Boozt.com | New styles every day" in driver.title
        print("Page title verified.")

        # Step 3: Wait for the search field to be present and search for a product (e.g., "dress")
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.global-search__header"))
        )
        search_box.click()
        time.sleep(2)
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.skip-generic-styling"))
        )
        search_input.send_keys("dress")
        search_input.send_keys(Keys.RETURN)
        print("Searched for 'dress'.")
        time.sleep(2)

        # Step 4: Apply filters

        # Select color
        xpathcolour = "//span[contains(@class, 'palette-button__label') and text()='Colour']"
        scroll_until_visible(driver, By.XPATH, xpathcolour)
        click_element_by_xpath(driver, xpathcolour)
        time.sleep(1)

        xpathblack = "//span[text()='Black']"
        scroll_until_visible(driver, By.XPATH, xpathblack)
        click_element_by_xpath(driver, xpathblack)
        time.sleep(1)

        print("colour filter is set to 'black'.")

        # Select material
        filtermaterial = driver.find_element(By.XPATH, "//span[text()='Material']")
        driver.execute_script("arguments[0].click();", filtermaterial)
        time.sleep(1)

        velour = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//span[contains(@class, 'palette-toggle__label') and text()='Velour']"))
        )
        velour.click()
        time.sleep(1)

        driver.execute_script("arguments[0].click();", filtermaterial)
        time.sleep(2)
        print("material filter is set to 'Velour'.")

        # Step 5: Sort by popularity
        sorting = driver.find_element(By.XPATH, "//span[text()='Sorting']")
        sorting.click()
        time.sleep(1)

        velour = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//span[text()='Newest']"))
        )
        velour.click()
        time.sleep(1)

        driver.execute_script("arguments[0].click();", sorting)
        time.sleep(2)
        print("Products sorted by 'Newest'.")

        # Step 6: Click on the first product in the results
        first_product = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//div[@class='palette-product-card palette-product-card--boozt "
                                        "palette-product-card--vertical product-listing__card impression-product' and "
                                        "@data-order='0']"))
        )
        first_product.click()
        time.sleep(2)
        print("Clicked on first product.")

        # Step 7: Verify product details (name, colour, price)
        product_name = driver.find_element(By.XPATH,
                                           "//span[contains(@class, 'pp-info__nav-name')]").text
        product_colour = driver.find_element(By.XPATH,
                                             "//span[contains(@class, 'typography typography--body2 "
                                             "typography--color-light typography--weight-regular') and text("
                                             ")='BLACK']").text
        product_price = driver.find_element(By.XPATH,
                                            "//span[contains(@class, 'pp-price__text')]").text
        assert product_name and product_colour and product_price  # Ensuring product details are visible
        print(f"Product name: {product_name}, Product colour: {product_colour}, Product price: {product_price}")

        # Step 8: Add the product to the cart
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Add to cart']"))
        )
        assert add_to_cart_button
        add_to_cart_button.click()

        # select dress size
        dress_size = driver.find_element(By.XPATH, "//button[text()='M']")
        driver.execute_script("arguments[0].click();", dress_size)
        print("Dress size selected")
        time.sleep(1)

        driver.execute_script("arguments[0].click();", add_to_cart_button)
        time.sleep(2)
        print("Product added to cart.")

        # Step 9: Proceed to the cart
        go_to_cart = driver.find_element(By.XPATH, "//span[text()='GO TO CART']")
        assert go_to_cart
        go_to_cart.click()
        time.sleep(2)
        print("Navigated to cart.")

        # Step 10: Proceed to checkout
        checkout_button = driver.find_element(By.XPATH, "//span[text()='Checkout']")
        assert checkout_button
        driver.execute_script("arguments[0].click();", checkout_button)
        time.sleep(2)

        assert driver.find_element(By.XPATH, "//span[text()='Go to secure payment']")
        print("Proceeded to checkout.")

    finally:
        # Close the browser after test completion
        driver.quit()
