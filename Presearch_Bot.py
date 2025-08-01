#--------------MADE BOT WHICH EARNS POINTS 4 ME!!!!!!!----------------------------------


import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import google.generativeai as genai
import time



web = uc.Chrome()
web.get("https://mail.google.com/mail/u/0/#sent")

genai.configure(api_key="Your api key")
model = genai.GenerativeModel('gemini-2.0-flash')

prompt = """
Generate one example of text which can be used to search presearch, in order to get Presearch reward points.
It can be abotu anything, related to science, politics, countries, etc.(just make it random and it should lead to me getting points)
P.S: JUST GIVE ME THE TEXT, NOTHING ELSE!!!!!!!!!!!!!!!!
Example Output: Population of Iceland
"""

#SIGN IN PART
usern = web.find_element('xpath', '//*[@id="identifierId"]')
usern.send_keys('your gmail address')
usern.send_keys(Keys.ENTER)

passw= WebDriverWait(web, 20).until(
                EC.presence_of_element_located(('xpath', '//*[@id="password"]/div[1]/div/div[1]/input'))
            )
passw.send_keys('your gmail password')
passw.send_keys(Keys.ENTER)


web.get("https://presearch.com/")
time.sleep(5)
actions = ActionChains(web)

login = web.find_element('xpath', '//*[@id="Home"]/div[1]/div[3]/div/div[2]/div[2]/div/div/button[1]')
login.click()

login2 = web.find_element('xpath', '//*[@id="user-info"]/div[3]/div/div[4]/div[5]/a[1]')
login2.click()

time.sleep(2)
answer = model.generate_content([prompt], stream=False)
response = answer.text.strip()

search= WebDriverWait(web, 20).until(
                EC.presence_of_element_located(('xpath', '//*[@id="search-form"]/div[1]/input'))
            )
search.send_keys(f'{response}')
actions.send_keys(Keys.ENTER).perform()

time.sleep(20)
