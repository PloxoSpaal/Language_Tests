import time

from selenium.webdriver.common.by import By


def test_btn_add_to_cart(browser):
    browser.get(
        'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207')
    time.sleep(3)
    btn_cart = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    assert btn_cart.is_displayed() == True, 'Button "Add to cart" is not displayed on page.'