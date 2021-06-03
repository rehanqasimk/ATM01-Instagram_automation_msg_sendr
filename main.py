
path = ".\chromedriver.exe"
# The webdriver__ which will open your browser(chrome)
from selenium import webdriver
# to send keys from keyboard
from selenium.webdriver.common.keys import Keys
# see the documentation for explicit wait in slenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from time import sleep
from bs4 import BeautifulSoup as bsoup
import pandas as pd
import random
from IPython.core.display import clear_output


# In[7]:


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'






driver = webdriver.Chrome(path)

driver.get('https://www.instagram.com/')


# In[12]:


# login to the account
username = 'rehanqasim6'
password = 'GOOGLEyoutube1,'

#reading the file and extracting the accounts
file_path = 'test.csv'
data = pd.read_csv(file_path)
accounts = data['Account']
message = """HEllo """

try:
    # trying to wait for the main content div to load and then do our work , (other wise finding some other thing will throw error)
    field1 = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME ,'username'))
    )
    field1.send_keys(Keys.CONTROL +'a')
    field1.send_keys(username)

    field2 = driver.find_element_by_name('password')
    field2.send_keys(Keys.CONTROL +'a')
    field2.send_keys(password)
    login = driver.find_element_by_css_selector('button[type="submit"]')
    ActionChains(driver).click(login).perform()
except:
    print('Something went wrong')
account_number = 1
i = 0

for account in accounts:
    # getting into message
    try:
        pop_up = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'svg[aria-label="Direct"]')))
        pop_up.click()

        pop_up = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'HoLwm')))

        pop_up.click()
    except:
        print('something went wrong')

    # click on write message
    driver.find_element_by_css_selector('svg[aria-label="New Message"]').click()
    print('Total accounts:' + color.BOLD + str(len(accounts)) + color.END)
    print('Sending message to Account Number:' + color.BOLD + str(
        account_number) + color.END + ' UserName: ' + color.BOLD + account + color.END)
    # search the name of the influencer
    try:
        search = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'queryBox'))
        )
        search.send_keys(account)
    except:
        print('something went wrong')

    # click on the first search that appeared
    try:
        # first appearence of the user will be selected
        first_appear = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span[aria-label="Toggle selection"]'))
        )
        first_appear.click()
        # to be extra safe with class selection of div used button also
        driver.find_element_by_css_selector('button>div.rIacr').click()
    except:
        print('something went wrong')

    # writing and sending the message
    try:
        message_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea[placeholder="Message..."]'))
        )
        # wait a while before sending a message
        sleep(2)
        message_box.send_keys(Keys.CONTROL + 'a')
        for part in message.split('\n'):
            message_box.send_keys(part)
            ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(
                Keys.ENTER).perform()
        message_box.send_keys(Keys.RETURN)
    except:
        print('something went wrong')

    # testing condition
    i += 1;
    # if i == 1:
    #     break
    # sleep(random.randint(15, 20))
    # clear_output(wait=True)
    account_number += 1
