import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    # variable
    time_t = '17:42'
    type_w = 'С2'
    last_name = 'Шумило'
    first_name = 'Володимир'
    email = 'shumilophysic@gmail.com'
    cnum = '5169 3600 0111 3749'
    expire_month = '10'
    expire_year = '26'
    input_cvv = '694'
    # driver.get("https://www.google.com")
    # driver.find_element_by_name("q").send_keys("webdriver")
    # time.sleep(1)
    # driver.find_element_by_name('btnK').click()
    # WebDriverWait(driver, 10).until(EC.title_is("webdriver - Поиск в Google"))
    show_star_page(driver)
    table_rows = []
    while len(table_rows) == 0:
        driver.find_element_by_css_selector('.button button').click()
        time.sleep(7)
        s = '//div[text()="' + time_t + '"]/parent::*/parent::*//*[@data-wagon-id="'+type_w+'"]'
        table_rows = driver.find_elements_by_xpath(s)
        if len(table_rows):
            table_rows[0].click()
            time.sleep(2)
            if len(driver.find_elements_by_css_selector('.place.fr[place]')):
                driver.find_element_by_css_selector('.place.fr[place]').click()
                driver.find_element_by_css_selector('input[value="Оформить билеты"]').click()
                time.sleep(1)
                driver.find_element_by_name('lastname').send_keys(last_name)
                driver.find_element_by_name('firstname').send_keys(first_name)
                for element in driver.find_elements_by_css_selector('.service .g-form-checkbox'):
                    if len(element.find_elements_by_css_selector('[checked="checked"]')) != 0:
                        element.click()
                time.sleep(2)
                driver.find_element_by_css_selector('input[value="В корзину"]').click()
                time.sleep(2)
                driver.find_element_by_css_selector('input[value="Оплатить"]').click()
                time.sleep(2)
                driver.find_element_by_css_selector('.popup-body [name=email]').send_keys(email)
                driver.find_element_by_class_name('g-form-checkbox').click()
                driver.find_element_by_css_selector('.popup-body [type="submit"]').click()
                time.sleep(5)
                driver.find_element_by_name('cnum').send_keys(cnum)
                driver.find_element_by_name('expire_month').send_keys(expire_month)
                driver.find_element_by_name('expire_year').send_keys(expire_year)
                driver.find_element_by_id('input-cvv').send_keys(input_cvv)
                time.sleep(100)
                driver.find_element_by_id('service_confirm_payment_button').click()
                time.sleep(3)
            else:
                table_rows = []
                show_star_page(driver)

    WebDriverWait(driver, 5).until(EC.title_is("iShop - Оплата"))


def show_star_page(driver):

    hour_from = '17'
    town_from = 'Киев'
    town_to = 'Знаменка-Пасс.'
    month = ''
    day = '11'

    driver.get("https://booking.uz.gov.ua/ru/")

    driver.find_element_by_name("from-title").send_keys(town_from)
    time.sleep(2)
    element = driver.find_elements_by_xpath('//li[text()="' + town_from + '"]')
    if len(element) and element[0].is_displayed() and element[0].is_enabled():
        element[0].click()
    else:
        show_star_page(driver)
    element = driver.find_elements_by_xpath('//*[@aria-selected="true"][text()="'+town_from+'"]')
    if len(element) == 0:
        show_star_page(driver)

    driver.find_element_by_name("to-title").send_keys(town_to)
    time.sleep(1)
    element = driver.find_elements_by_xpath('//li[text()="' + town_to + '"]')
    if len(element) and element[0].is_displayed() and element[0].is_enabled():
        element[0].click()
    else:
        show_star_page(driver)
    element = driver.find_elements_by_xpath('//*[@aria-selected="true"][text()="'+town_to+'"]')
    if len(element) == 0:
        show_star_page(driver)

    date_selector = '//a[text()='+day+']'
    driver.find_element_by_name('date-hover').click()
    driver.find_element_by_xpath(date_selector).click()

    driver.find_element_by_name('time').click()
    driver.find_element_by_css_selector('[value="'+hour_from+':00' + '"]').click()
