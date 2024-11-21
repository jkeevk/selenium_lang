import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestMainPage:

    def test_add_to_cart_exist(self, browser):
        link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        
        browser.get(link)
        time.sleep(30)
        
        try:
            button = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "btn-add-to-basket"))
            )
            assert button, "Кнопка 'Добавить в корзину' не найдена!"
            print("Кнопка 'Добавить в корзину' найдена!")
        except Exception as e:
            print(f"Ошибка при поиске кнопки: {e}")
            assert False, "Кнопка 'Добавить в корзину' не найдена!"

        time.sleep(3)
