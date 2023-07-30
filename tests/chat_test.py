import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time


class ChatTests(unittest.TestCase):
    
    def test_image_reception(self):
        # Configurações para o navegador Chrome em modo headless (sem interface gráfica)
        #chrome_options = Options()
        #chrome_options.add_argument('--headless')
        #chrome_options.add_argument('--disable-gpu')
        driver_send = webdriver.Firefox()
        driver_receive = webdriver.Firefox()

        try:
            # Abre a página da web para o usuário que envia mensagens
            driver_send.get('http://localhost:3000/')

            # Abre a página da web para o usuário que recebe mensagens
            driver_receive.get('http://localhost:3000/')

            # Aguarde um tempo suficiente para que a mensagem seja recebida e a imagem seja renderizada
            canvas_receive = WebDriverWait(driver_receive, timeout=20).until(lambda d: d.find_element(By.TAG_NAME, 'flt-glass-pane'))
            print(canvas_receive)
            # Obtenha o elemento "canvas" no navegador do usuário que recebe para obter o conteúdo inicial
            shadow_root = canvas_receive.shadow_root
            canvas_shadow = shadow_root.find_element(By.CSS_SELECTOR, 'canvas')
            initial_canvas_content = canvas_shadow.get_attribute('toDataURL')  # Armazene o conteúdo inicial do canvas

            # Simula o envio de uma mensagem com a imagem no navegador do usuário que envia
            # Realize as ações necessárias para enviar a mensagem com a imagem no navegador driver_send

            #clica no elemento textarea
            """ escreve x
            pressiona enter
            clica no elemento input .flt-text-editing
            escreve y 
            clica enter
            -> y entrou no chat  """
            
            textarea_send = shadow_root.find_element(By.CSS_SELECTOR, 'textarea')
            textarea_send.send_keys('Mensagem de teste')  # Digite a mensagem na textarea
            textarea_send.send_keys(u'\ue007')
            driver_send.implicitly_wait(30)
            input_send = shadow_root.find_element(By.CSS_SELECTOR, 'input')
            driver_send.implicitly_wait(30)
            input_send.send_keys('UsuarioTeste')  # Digite a mensagem na textarea
            input_send.send_keys(u'\ue007')
            actions = ActionChains(driver_send)
            actions.send_keys(u'\ue007')
            actions.perform()

            # Registra o tempo de envio da mensagem
            send_time = time.time()

            # Verifique se o elemento "canvas" no navegador do usuário que recebe contém alterações
            canvas_content = canvas_shadow.get_attribute('toDataURL')  # Obtém o conteúdo atualizado do canvas após o recebimento da mensagem
            if canvas_content != initial_canvas_content:
                # Registra o tempo de recebimento da mensagem
                receive_time = time.time()

                # Calcule a latência
                latency = receive_time - send_time
                print(f"Msg recebida com sucesso! Latência: {latency:.2f} segundos")
            else:
                print("A Msg não foi recebida corretamente.")

        finally:
            # Fecha os navegadores
            driver_send.quit()
            driver_receive.quit()

    """ def setUp(self):
        self.driver = webdriver.Ie()

    def test_seila(self):
        self.driver.get("http://localhost:3000/")
        

    def tearDown(self):
        self.driver.close() """


if __name__ == '__main__':
    unittest.main()
