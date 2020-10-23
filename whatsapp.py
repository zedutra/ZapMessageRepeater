from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

qrcode = input("Scaneie o QR CODE e pressione enter")
contato = str(input('Insira o contato: '))
mensagem = str(input('Insira a mensagem: '))
repeticao = int(input('Numero de repeticoes: '))
contato = driver.find_element_by_xpath("//span[@title='{}']".format(contato))
contato.click()

count = 0
while count < repeticao:
    time.sleep(2)
    inputmensagem = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    inputmensagem.click()
    inputmensagem.send_keys(mensagem)
    inputenviar = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
    inputenviar.click()
    count += 1
