from pages.page_actions import *


# Helper function to initialize WebDriver
def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.boozt.com/dk/da")
    return driver


def test_boozt_personal_account():
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

        # Step 5: Select 'My Wallet' page
        my_wallet = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'My Wallet')]"))
        )
        my_wallet.click()
        time.sleep(1)
        assert "My Wallet" in driver.title
        print("Selected page 'My Wallet'.")

        # Step 6: Select 'My Boozt' page
        my_boozt = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(., 'My Boozt')]"))
        )
        my_boozt.click()
        time.sleep(1)
        assert "My Boozt" in driver.title
        print("Selected page 'My Boozt'.")

        # Step 7: Select 'My orders' page
        my_orders = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='dashboard-stats__item dashboard-stats__item--orders']"))
        )
        my_orders.click()
        time.sleep(1)
        assert "My Orders" in driver.title
        print("Selected page 'My orders'.")

        # Step 8: Select 'Find inspiration' button
        my_profile = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(., 'GET INSPIRED')]"))
        )
        my_profile.click()
        time.sleep(1)
        assert "Boozt.com | New styles every day" in driver.title
        print("Opened homepage.")

        # Step 9: Search for dress category
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

        # Step 10: Add the first product to the cart
        first_product = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@data-order='3']"))
        )
        first_product.click()
        time.sleep(2)
        print("Clicked on a product.")

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

    finally:
        # Close the browser after test completion
        driver.quit()
