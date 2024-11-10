from pages.page_actions import *


# Helper function to initialize WebDriver
def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.boozt.com/dk/da")
    return driver


def test_boozt_personal_cart_change():
    driver = setup_driver()

    try:
        # Step 1: Accept cookies if the prompt is present
        close_cookies(driver)

        # Set language to English
        set_lenguage_english(driver)

        # Step 2: Verify page title contains "Boozt.com | New styles every day"
        assert "Boozt.com | New styles every day" in driver.title
        print("Page title verified.")

        # Step 3: Wait for the account button to load and the presses on it
        account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Account']"))
        )
        assert account_button
        account_button.click()
        print("Pressed the 'account' button.")
        time.sleep(2)

        # Step 4: Login with username and password

        # Insert username
        username = "endrimbyeti@gmail.com"
        username_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='email' and @data-property='username']"))
        )
        username_input.click()
        username_input.send_keys(username)
        time.sleep(1)
        print(f"Inserted username {username}.")

        # Insert password
        password = "Test1234!"
        password_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='password' and @data-property='password']"))
        )
        password_input.click()
        password_input.send_keys(password)
        time.sleep(1)
        print(f"Inserted password {password}.")

        # Submit credentials
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        submit_button.click()
        time.sleep(1)
        assert "My Boozt" in driver.title
        print("logged into personal account.")

        # Step 5: Select 'The shopping cart'
        shopping_cart = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Shopping Cart']"))
        )
        shopping_cart.click()
        time.sleep(1)
        assert "Shopping Bag" in driver.title
        print("Selected 'My cart'.")

        # Step 6: Select product 'ICHI IHNANA DR' in cart
        cart_product = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@alt='ICHI IHNANA DR']"))
        )
        cart_product.click()
        time.sleep(1)
        element = driver.find_element(By.XPATH, "//div[@data-product='32697086']")
        product_value = element.get_attribute("data-product")
        assert product_value == "32697086"
        print("Selected product 'IHNANA DR'.")

        # Step 7: Add the product to the cart
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Add to cart']"))
        )
        assert add_to_cart_button
        add_to_cart_button.click()

        # select dress size
        dress_size = driver.find_element(By.XPATH, "//button[text()='XL']")
        driver.execute_script("arguments[0].click();", dress_size)
        print("Dress size selected")
        time.sleep(1)

        driver.execute_script("arguments[0].click();", add_to_cart_button)
        time.sleep(2)
        print("Product added to cart.")

        # Step 8: Proceed to the cart and verify the product is added
        go_to_cart = driver.find_element(By.XPATH, "//span[text()='GO TO CART']")
        assert go_to_cart
        go_to_cart.click()
        time.sleep(2)
        print("Navigated to cart.")

        # Step 9: Delete old product
        delete_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, "
                                                      "'palette-button--secondary-icon-only')]"))
        )
        delete_button.click()
        time.sleep(2)
        print("Old product deleted.")
        time.sleep(2)

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
