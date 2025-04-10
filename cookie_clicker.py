import time
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
url = "http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

cookie = driver.find_element(By.ID, value="cookie")

start_time = time.time()
elapsed = 0
is_on = True

# cursor = driver.find_element()




try:
    while is_on:
        cookie.click()
        balance = float(driver.find_element(By.ID, value="money").text.split("-")[-1].strip().replace(",", ""))
        elapsed = int(time.time() - start_time)

        if elapsed % 30 == 0:
            right_panel = driver.find_elements(By.CSS_SELECTOR, value="#store div")
            for index in range(len(right_panel) - 2, -1, -1):
                try:
                    # Attempt to extract the price fresh each time
                    price_text = right_panel[index].find_element(By.TAG_NAME, "b").text
                    price = float(price_text.split("-")[-1].strip().replace(",", ""))
                    print(price)

                    if balance >= price:
                        right_panel[index].click()
                except Exception as e:
                    continue
        time.sleep(0.001)
except KeyboardInterrupt:
    print("Stopped clicking.")





