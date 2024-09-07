"""from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller

def find_voter(voter_id_value):
    # Instalar o ChromeDriver automaticamente
    chromedriver_autoinstaller.install()

    # Inicializar o WebDriver com o ChromeDriver
    driver = webdriver.Chrome()

    # Navegar até a URL
    driver.get('https://www.tse.jus.br/servicos-eleitorais/autoatendimento-eleitoral#/atendimento-eleitor')

    # Aguardar até que a página esteja completamente carregada
    WebDriverWait(driver, 20).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )


    # Fechar o modal de cookies
    try:
        cookie = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[9]/div/div/div[2]/button"))
        )
        cookie.click()
    except Exception as e:
        print("Erro ao fechar o modal de cookies:", str(e))

    # Clicar no botão 'Consultar situação eleitoral'
    try:
        Titulo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Consultar situação eleitoral')]"))
        )
        Titulo.click()
    except Exception as e:
        print("Erro ao clicar no botão 'Consultar situação eleitoral':", str(e))

    # Aguardar o campo de número do eleitor aparecer e preenchê-lo
    try:
        Numero_eleitor = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div[3]/div/div/app-root/app-modal-auth/div/div/div/div/div[2]/div[2]/form/div[1]/div/input'))
        )
        Botao_verificacao = driver.find_element(By.XPATH, '/html/body/main/div/div/div[3]/div/div/app-root/app-modal-auth/div/div/div/div/div[2]/div[2]/form/div[2]/button[2]')

        Numero_eleitor.send_keys(voter_id_value)
        Botao_verificacao.click()
    except Exception as e:
        print("Erro ao preencher o número do eleitor ou clicar no botão de verificação:", str(e))

    # Verificar a situação da inscrição
    try:
        situacao_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div[3]/div/div/app-root/div/app-consultar-situacao-titulo-eleitor/div[1]/div[1]/p/span'))
        )
        situacao_texto = situacao_element.text

        if "REGULAR" in situacao_texto:
            return "REGULAR"
        else:
            return "IRREGULAR"
    except Exception as e:
        print("Falha ao verificar a situação da inscrição:", str(e))

    # Fechar o navegador
    driver.quit()
"""
