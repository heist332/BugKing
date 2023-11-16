from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

options = ChromeOptions()

options.add_argument("lang=ko_KR")   
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36') 

service = ChromeService(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)


url = "https://burgerkingevent.com/"
driver.get(url)
driver.implicitly_wait(10) # seconds

p_b = driver.find_element(By.CLASS_NAME, "btn-play")
p_b.click()

element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "byy-word"))
	)

text = ['블', '양', '양', '블', '피', '화', '와', '와', '화', '와', '와', '화', '블']

table = {

}

sequence = driver.find_elements(By.CLASS_NAME, 'btn-item')

time.sleep(5)

for idx, v in enumerate(sequence):
    table[v.get_attribute('data-word')] = v
    
for a in text:
    b = table[a]

    actionChains = ActionChains(driver, duration=1)
    actionChains.move_to_element(b).click().perform()


time.sleep(10)

driver.quit()