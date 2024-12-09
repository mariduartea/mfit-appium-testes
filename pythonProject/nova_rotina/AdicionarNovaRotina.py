from appium import webdriver
from appium.options.common.base import AppiumOptions
import unittest
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class AdicionarNovaRotinaReserva(unittest.TestCase):
    def test_adicionar_nova_rotina(self):
        options = AppiumOptions()
        options.load_capabilities({
            "platformName": "Android",
            "appium:automationName": "uiautomator2",
            "appium:deviceName": "Pixel 9 Pro XL API 35",
            "appium:app": "C:/apks/mfit_personal.apk",
            "appium:ensureWebviewsHavePages": True,
            "appium:nativeWebScreenshot": True,
            "appium:newCommandTimeout": 3600,
            "appium:connectHardwareKeyboard": True
        })

        driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

        wait_time = 100
        mfit_icon = (AppiumBy.CLASS_NAME, "android.widget.ImageView")
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located(mfit_icon))
        WebDriverWait(driver, 10).until_not(EC.invisibility_of_element_located(mfit_icon))
        # WebDriverWait(driver, wait_time).until(EC.presence_of_element_located(loading))
        # driver.find_element(*loading).click()
        allow_button = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located(allow_button))
        driver.find_element(*allow_button).click()
        personal_login = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"I am a personal trainer\")")
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located(personal_login))
        loading = (AppiumBy.ID, "app.mfit.personal:id/progressBar")
        WebDriverWait(driver, wait_time).until_not(EC.presence_of_element_located(loading))
        driver.find_element(*personal_login).click()
        WebDriverWait(driver, wait_time).until_not(EC.presence_of_element_located(loading))
        input_email = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className("
                                                     "\"android.widget.EditText\").instance(0)")
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located(input_email))
        driver.find_element(*input_email).click()
        driver.find_element(*input_email).send_keys("abas@cesar.school")
        input_password = (AppiumBy.ANDROID_UIAUTOMATOR,
                          "new UiSelector().className(\"android.widget.EditText\").instance(1)")

        driver.find_element(*input_password).click()
        driver.find_element(*input_password).send_keys("14051993")
        signin_button = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Sign in\")")
        signin_button.click()
        login_success = (AppiumBy.CLASS_NAME, "android.widget.Image")
        time.sleep(5)
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located(login_success))
        element = driver.find_element(*login_success)
        assert element.is_displayed(), "O elemento não está visível!"
        time.sleep(2)
        driver.swipe(470, 1400, 470, 900, 400)
        biblioteca_treino = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=' "
                                                                         "Biblioteca de treinos']/android.view.View")
        biblioteca_treino.click()
        adicionar_button = (AppiumBy.XPATH, "//android.widget.Button[@text='Adicionar']")
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located(adicionar_button))
        driver.find_element(*adicionar_button).click()
        nova_rotina_button = (AppiumBy.ACCESSIBILITY_ID, "Nova Rotina")
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located(nova_rotina_button))
        element = driver.find_element(*nova_rotina_button)
        element.click()
        WebDriverWait(driver, wait_time).until_not(EC.presence_of_element_located(loading))
        nome_rotina_input = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className("
                                                     "\"android.widget.EditText\").instance(0)")
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located(nome_rotina_input))

        element = driver.find_element(*nome_rotina_input)
        element.click()
        WebDriverWait(driver, wait_time).until_not(EC.presence_of_element_located(loading))
        expected_text = "Teste"
        element.send_keys(expected_text)
        tipo_treino = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                  value="new UiSelector().text(\"Dia da Semana - Ex: Segunda, Terça ...\")")
        tipo_treino.click()
        tipo_treino_popup = (AppiumBy.ANDROID_UIAUTOMATOR,"new UiSelector().text(\"Dia da Semana - Ex: Segunda, "
                                                          "Terça ...\")")
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located(tipo_treino_popup))

        tipo_treino_escolhido = driver.find_element(*tipo_treino_popup)
        tipo_treino_escolhido.click()
        objetivo = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                  value="new UiSelector().className(\"android.view.View\").instance(30)")
        objetivo.click()
        hipertrofia_option = AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Hipertrofia\")"
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located(hipertrofia_option))
        element = driver.find_element(*hipertrofia_option)
        element.click()
        dificuldade = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                  value="new UiSelector().className(\"android.view.View\").instance(32)")
        dificuldade.click()
        adaptacao_option = (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Adaptação\")")
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located(adaptacao_option))
        element = driver.find_element(*adaptacao_option)
        element.click()
        time.sleep(2)
        driver.swipe(470, 1400, 470, 900, 400)
        salvar_button = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Salvar\")")
        salvar_button.click()
        rotina_criada = (AppiumBy.XPATH, "(//android.view.View/following-sibling::android.widget.TextView)[1]")
        WebDriverWait(driver, wait_time).until_not(EC.presence_of_element_located(loading))
        WebDriverWait(driver, wait_time).until(EC.presence_of_element_located(rotina_criada))
        element = driver.find_element(*rotina_criada)
        element_text = element.text
        self.assertEqual(element_text, expected_text,
                         f'O texto esperado era "{expected_text}", mas o encontrado foi "{element_text}"')
        driver.quit()
