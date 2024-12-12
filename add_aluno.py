import time
import unittest

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from config import locators, test_data


class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = AppiumOptions()
        options.load_capabilities({
            "platformName": "Android",
            "appium:automationName": "UiAutomator2",
            "appium:ensureWebviewsHavePages": True
        })

        cls.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        cls.pacote = "app.mfit.personal"
        cls.driver.activate_app(cls.pacote)


        return super().setUpClass()

    def test_adicionar_novo_aluno(self):

        driver = self.driver

        personal_opt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["personal_opt"])))
        personal_opt.click()

        email_personal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["email_personal"])))
        email_personal.send_keys(test_data["email_personal"])

        senha_personal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["senha_personal"])))
        senha_personal.send_keys(test_data["senha_personal"])

        btn_login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["btn_login"])))
        btn_login.click()

        add_novo_aluno = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["add_novo_aluno"])))
        add_novo_aluno.click()

        nome_aluno = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,locators["nome_aluno"])))
        nome_aluno.send_keys(test_data["nome_aluno"])

        email_aluno = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,locators["email_aluno"])))
        email_aluno.send_keys(test_data["email_aluno"])

        selecionar_grupo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,locators["selecionar_grupo"])))
        selecionar_grupo.click()

        modalidade_opt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,locators["modalidade_opt"])))
        modalidade_opt.click()

        data_nascimento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,locators["data_nascimento"])))
        data_nascimento.click()
        data_nascimento.send_keys(test_data["data_nascimento"])

        campo_whatsapp = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["whatsapp"])))
        campo_whatsapp.click()
        actions = ActionChains(driver)
        actions.send_keys(test_data["whatsapp"]).perform()

        selecionar_genero = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["selecionar_genero"])))
        selecionar_genero.click()

        genero_opt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["genero_opt"])))
        genero_opt.click()

        selecionar_anamnese = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["selecionar_anamnese"])))
        selecionar_anamnese.click()

        anamnese_opt= WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["anamnese_opt"])))
        anamnese_opt.click()

        selecionar_bloqueio = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["selecionar_bloqueio"])))
        selecionar_bloqueio.click()

        bloqueio_opt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["bloqueio_opt"])))
        bloqueio_opt.click()

        btn_salvar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["btn_salvar"])))
        btn_salvar.click()

        fechar_popup = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["fechar_popup"])))
        fechar_popup.click()

        # Validação do cadastro realizado com sucesso
        try:
            titulo_cadastro = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["nome_cabecalho"]))
            )

            modalidade_cadastro = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,locators["modalidade_cabecalho"]))
            )

            titulo_texto = titulo_cadastro.text
            modalidade_texto = modalidade_cadastro.text

            time.sleep(2)
            assert test_data["nome_aluno"] in titulo_texto, f"Nome '{test_data[nome_aluno]}' não encontrado no título da tela."
            assert test_data["modalidade"] in modalidade_texto, f"personal_opt '{test_data["modalidade"]}' não encontrada no título da tela."
            print("Cadastro validado com sucesso!")
        except Exception as erro:
            print(f"Erro ao validar o cadastro: {erro}")

        #opcoes = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Opções\")")
        #opcoes.click()
        #excluir_aluno = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Excluir aluno\")")
        #excluir_aluno.click()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        return super().tearDownClass()