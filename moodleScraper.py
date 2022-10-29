from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import requests
# this block doesn't allow to open tab
"""from selenium.webdriver.chrome.options import Options

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")"""

# Set path to chromedriver as per my configuration
webdriver_service = Service(f"../chromedriver/stable/chromedriver")

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service) # add options=chrome_options if you don't want chrome tab to open

###### open sso login page and puts in credentials
credentials = []
login_url = "https://elearning.unipd.it/dfa/auth/shibboleth/index.php"
driver.get(login_url)

t = 10 # tempo d'attesa 

# save session's cookies
s = requests.Session()
selenium_user_agent = driver.execute_script("return navigator.userAgent;")
s.headers.update({"user-agent": selenium_user_agent})
for cookie in driver.get_cookies():
    s.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'])


username = WebDriverWait(driver, t).until(EC.element_to_be_clickable(
    {By.CSS_SELECTOR, "input[name='j_username_js']"}))
username.clear() # makes sure field is empty
username.send_keys(credentials[0]) # prints a1.bains in the field

password = WebDriverWait(driver, t).until(EC.element_to_be_clickable(
    {By.CSS_SELECTOR, "input[name='j_password']"}))
password.clear() # makes sure field is empty
password.send_keys(credentials[1]) # prints a1.bains in the field

button0 = WebDriverWait(driver, t).until(EC.element_to_be_clickable(
    {By.CSS_SELECTOR, "input[value='@studenti.unipd.it']"})).click()
accedi = WebDriverWait(driver, t).until(EC.element_to_be_clickable(
    {By.CSS_SELECTOR, "button[name='_eventId_proceed']"})).click()

#### navigate to moodle page

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get('https://elearning.unipd.it/dfa/course/view.php?id=1169')
# gets all the links in the page 
soup = BeautifulSoup(driver.page_source, 'html.parser')
linkers = []  
resources = []  
folders = []
for a in soup.find_all('a', href=True):
    linkers.append([a['href'],a.get_text()])

# gets all items
for item in linkers:
    for word in item:
        if "resource" in word:
            resources.append(item)
        if "folder" in word:
            folders.append(word)

# download pdf resources
for address, name in resources:
    response = s.get(address)
    size = len(name)
    open(name[:size-5]+".pdf", 'wb').write(response.content)

for folder in folders:
    driver.get(folder)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    linkers = []
    contents = []
    for a in soup.find_all('a', href=True):
        linkers.append([a['href'],a.get_text()])
    for item in linkers:
        for word in item:
                if "content" in word:
                        contents.append(item)
    for address, name in contents:
        response = s.get(address)
        open(name, 'wb').write(response.content)
