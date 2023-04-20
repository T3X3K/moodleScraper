########### PRELIMINARI ###########
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import requests
import sys
import os
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime

def cookies(driver):
    s = requests.Session()
    selenium_user_agent = driver.execute_script("return navigator.userAgent;")
    s.headers.update({"user-agent": selenium_user_agent})
    for cookie in driver.get_cookies():
        s.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'])
    return s

def convert_time(stringa):
    newest_entry_datetime = stringa.rsplit(" ", maxsplit=1)[0]
    dt_newest = datetime.strptime(newest_entry_datetime, "%a, %d %b %Y %H:%M:%S" )
    return dt_newest

def scavage_links(driver):
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    linkers = []  
    
    for a in soup.find_all('a', href=True):
        if 'https' in a['href']:
            linkers.append([a['href'],a.get_text().replace('(','').replace(')','').replace(' ','_').replace('/','.')])
    return linkers

def download(address, fpath, name):
    response = s.get(address)
    if 'Last-Modified' in response.headers:
        fsdate = convert_time(response.headers['Last-Modified'])
        if fsdate > last:
            i = 1
            while os.path.exists(fpath):
                if fpath[-6].isdigit() and fpath[-5] == ")":
                    i = i + 1
                    fpath[-5] = str(i)
                else:
                    fpath = fpath[0:-4] + "_(" + str(i) + ")" + fpath[-4:]
            open(fpath, 'wb').write(response.content)
            print("Downloaded " + name)
    else:
        print("Non si può scaricare" + name)

### CHROME SETTINGS
# this block doesn't allow to open tab
from selenium.webdriver.chrome.options import Options

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensures GUI is off
chrome_options.add_argument("--no-sandbox")

# Set path to chromedriver as per my configuration
webdriver_service = Service(f"../chromedriver/stable/chromedriver")

# Choose Chrome Browser
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options) # add options=chrome_options if you don't want chrome tab to open

########### LOGIN ACCESS ###########
###### open sso login page and puts in credentials
credentials = [sys.argv[1], sys.argv[2]]
login_url = "https://stem.elearning.unipd.it/dfa/auth/shibboleth/index.php"
driver.get(login_url)

t = 15 # tempo d'attesa 

# save session's cookies
s = cookies(driver)

# puts in credentials
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
driver.get(sys.argv[3])
driver.get('https://stem.elearning.unipd.it/login/index.php')
driver.get('https://stem.elearning.unipd.it/auth/shibboleth/index.php')
s = cookies(driver)

print("Login effettuato")

N = len(sys.argv)
for i in range(3, N, 2):
    driver.get(sys.argv[i])
    s = cookies(driver)
    path = sys.argv[i+1]
    print("start " + path)

    ### Gets today's date and checks last time code was used
    # to know which files to download
    now = datetime.now()
    stamp = mktime(now.timetuple())
    today = format_date_time(stamp)
    with open(path+'.last_date','r') as f:
        last = f.read()
    last = convert_time(last)

    ########### FILE DOWNLOAD ###########
    # gets all the links in the page 
    linkers = scavage_links(driver)  
    resources = []  
    folders = []
    contents = []
    assignments = []

    # gets all items
    for item in linkers:
        for word in item:
            if "resource" in word:
                resources.append(item)
            if "/folder/" in word:
                folders.append(item)
            if "content" in word:
                contents.append(item)
            if "assign" in word:
                assignments.append(item)

    # download from main page
    for address, name in resources:
        full_name = path+name[:-5]+".pdf"
        download(address, full_name, name)
    for address, name in contents:
        download(address, path+name, name)
    print("Scaricata Pagina Principale")

    # download from folders
    for folder, folder_name in folders:
        npath = path+folder_name[:-9]
        if not os.path.exists(npath):
            os.mkdir(npath)
        driver.get(folder)
        linkers = scavage_links(driver)
        contents = []
        for item in linkers:
            for word in item:
                    if "content" in word:
                            contents.append(item)
        for address, name in contents:
            download(address, npath+"/"+name, name)
    print("Scaricate Cartelle")
    # download from assignments
    for assign, assign_name in assignments:
        npath = path+assign_name[:-8]
        if not os.path.exists(npath):
            os.mkdir(npath)
        driver.get(assign)
        linkers = scavage_links(driver)
        contents = []
        for item in linkers:
            for word in item:
                    if "pluginfile" in word:
                            contents.append(item)
        for address, name in contents:
            download(address, npath+"/"+name, name)
    print("Scaricati Compiti")
    with open(path+'.last_date','w') as f:
        f.write(today)