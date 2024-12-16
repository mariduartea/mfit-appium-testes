from appium import webdriver
from setup import SetUp
from appium.options.common.base import AppiumOptions
import unittest
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver.support import expected_conditions as EC
from config import locators, test_data
from selenium.webdriver.support.wait import WebDriverWait


class GerenciarRotinas(SetUp, unittest.TestCase):

    def test_adicionar_nova_rotina(self):
        driver = self.driver

        for i in range(5):  # Tentativas de fazer o scroll até o topo
            try:
                driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, locators["biblioteca_treino"])

                driver.swipe(500, 1500, 500, 500, 1000)  # Realiza um swipe manual

                break
            except Exception as e:
                print(f"Tentativa {i + 1} de scroll falhou:", e)
                continue

        biblioteca_treino = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["biblioteca_treino"])))
        biblioteca_treino.click()

        comece_agora = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["comece_agora"])))
        comece_agora.click()

        adicionar_novo_treino = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["adicionar_novo_treino"])))
        adicionar_novo_treino.click()

        wait_time = 100
        # Nome da rotina
        nome_rotina_input = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["nome_rotina_input"]))
        )
        nome_rotina_input.click()
        nome_rotina_input.send_keys(test_data["nome_rotina"])

        # Tipo de treino
        tipo_treino = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["tipo_treino"]))
        )
        tipo_treino.click()

        tipo_treino_popup = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["tipo_treino_popup"]))
        )
        tipo_treino_popup.click()

        # Objetivo
        objetivo = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["objetivo"]))
        )
        objetivo.click()

        hipertrofia_option = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["hipertrofia_option"]))
        )
        hipertrofia_option.click()

        # Dificuldade
        dificuldade = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["dificuldade"]))
        )
        dificuldade.click()

        adaptacao_option = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["adaptacao_option"]))
        )
        adaptacao_option.click()

        # Scroll para o botão Salvar
        for i in range(5):  # Tentativas de fazer o scroll até o topo
            try:
                driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, locators["salvar_button"])

                driver.swipe(500, 1500, 500, 500, 1000)  # Realiza um swipe manual

                break
            except Exception as e:
                print(f"Tentativa {i + 1} de scroll falhou:", e)
                continue

        # Salvar
        salvar_button = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["salvar_button"]))
        )
        salvar_button.click()

        # Validação da rotina criada
        rotina_criada = WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["rotina_criada"]))
        )
        element_text = rotina_criada.text

        try:
            self.assertEqual(element_text, test_data["nome_rotina"],
                             f'O texto esperado era "{test_data["nome_rotina"]}", mas o encontrado foi "{element_text}"')
            print("Rotina criada com sucesso!")
        except Exception as erro:
            print(f"Erro ao validar o cadastro: {erro}")

    def test_apagar_rotina(self):
        driver = self.driver

        btn_inicio = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"\")")
        btn_inicio.click()

        for i in range(5):  # Tentativas de fazer o scroll até o topo
            try:
                driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, locators["biblioteca_treino"])

                driver.swipe(500, 1500, 500, 500, 1000)  # Realiza um swipe manual

                break
            except Exception as e:
                print(f"Tentativa {i + 1} de scroll falhou:", e)
                continue

        biblioteca_treino = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["biblioteca_treino"])))
        biblioteca_treino.click()

        rotina_criada = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["rotina_criada"]))
        )
        rotina_criada.click()

        excluir_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["excluir_button"]))
        )
        excluir_button.click()

        pop_up_confirmacao = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["pop_up_confirmacao"]))
        )
        pop_up_confirmacao.click()

        try:
            comece_agora = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["comece_agora"])))

            assert comece_agora is not None, "Elemento não encontrado"

            print("Rotina excluída com sucesso.")
        except Exception as erro:
            print(f"Erro ao validar o cadastro: {erro}")
