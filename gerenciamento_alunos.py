import time
import unittest

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from config import locators, test_data
from setup import SetUp


class TestStringMethods(SetUp, unittest.TestCase):

    def test_adicionar_novo_aluno(self):
        driver = self.driver

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

        time.sleep(2)
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

        btn_salvar = WebDriverWait(driver, 15).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["btn_salvar"])))
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

            assert test_data["nome_aluno"] in titulo_texto, f"Nome '{test_data["nome_aluno"]}' não encontrado no título da tela."
            assert test_data["modalidade"] in modalidade_texto, f"personal_opt '{test_data["modalidade"]}' não encontrada no título da tela."
            print("Cadastro validado com sucesso!")
        except Exception as erro:
            print(f"Erro ao validar o cadastro: {erro}")


    def test_excluir_aluno(self):
        driver = self.driver

        btn_inicio = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"\")")
        btn_inicio.click()

        for i in range(5):  # Tentativas de fazer o scroll até o topo
            try:
                driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, locators["alunos_cadastrados"])

                driver.swipe(500, 1500, 500, 500, 1000)  # Realiza um swipe manual

                break
            except Exception as e:
                print(f"Tentativa {i + 1} de scroll falhou:", e)
                continue

        alunos_cadastrados = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["alunos_cadastrados"])))
        alunos_cadastrados.click()

        aluno_inserido = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["aluno_inserido"])))
        print(aluno_inserido)
        aluno_inserido.click()
        btn_opcoes = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["btn_opcoes"])))
        btn_opcoes.click()
        btn_excluir_aluno = WebDriverWait(driver, 10).until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["btn_excluir_aluno"])))
        btn_excluir_aluno.click()

        try:
            msg_aluno_excluido = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, locators["msg_aluno_excluido"]))
            )

            mensagem_exclusao = msg_aluno_excluido.text

            assert "Esse aluno foi excluído" in mensagem_exclusao, f"Mensagem '{"Esse aluno foi excluído"}' não encontrada."

            print("Aluno excluído com sucesso!")
        except Exception as erro:
            print(f"Erro ao localizar mensagem de exclusão: {erro}")



