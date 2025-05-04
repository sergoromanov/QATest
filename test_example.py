from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

service = Service("C:/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://example.com")

    assert "Example" in driver.title, "Заголовок не содержит 'Example'"

    link = driver.find_element(By.LINK_TEXT, "More information...")
    link.click()
    time.sleep(2)
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[-1])

    current_url = driver.current_url
    print("Текущий URL:", current_url)

    assert "iana.org/help/example-domains" in current_url, "Переход не выполнен на ожидаемый адрес"

    print("Тест пройден успешно!")

finally:
    driver.quit()
