from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.support import expected_conditions as EC
from config import locators,test_data


class SetUp:
    @classmethod

    def setUpClass(cls):
        options = AppiumOptions()
        options.load_capabilities({
            "platformName": "Android",
            "appium:automationName": "UiAutomator2",
            "appium:ensureWebviewsHavePages": True,
        })

        cls.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        cls.pacote = "app.mfit.personal"
        cls.driver.activate_app(cls.pacote)

        #login
        cls.login(cls.driver)

    @classmethod
    def login(cls, driver):

        try:
            entrar_novamente = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["entrar_novamente"])))

            entrar_novamente.click()

        except TimeoutException:
            pass

        personal_opt = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["personal_opt"])))
        personal_opt.click()

        email_personal = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["email_personal"])))
        email_personal.send_keys(test_data["email_personal"])

        senha_personal = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["senha_personal"])))
        senha_personal.send_keys(test_data["senha_personal"])

        btn_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["btn_login"])))
        btn_login.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


