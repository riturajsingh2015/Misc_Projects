import os, sys
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

my_username = "riturajsingh2015@gmail.com"
my_password = "github786"


folder_name=sys.argv[1]
desc=sys.argv[2]
base_dir="C:/Users/Singh/Desktop/Projects"
os.chdir(base_dir)
if not(os.path.exists(folder_name)):# checks if diretory exits
    os.mkdir(folder_name)
os.chdir(folder_name) # now we are inside proejct folder


options = Options()
options.headless = True
CHROMEDRIVER_PATH=r'C:\Users\Singh\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)

site_url='https://github.com/login'

driver.get(site_url)

username=driver.find_element_by_css_selector('input[type="text"]')
password=driver.find_element_by_css_selector('input[type="password"]')

username.send_keys(my_username)
password.send_keys(my_password)
login_submit=driver.find_element_by_css_selector('input[type="submit"]')
login_submit.click()
time.sleep(1)

repo_url="https://github.com/new"
driver.get(repo_url)
repo_name=driver.find_element_by_css_selector('input[name="repository[name]"]')
repo_desc=driver.find_element_by_css_selector('input[name="repository[description]"]')
repo_name.send_keys(folder_name)
repo_desc.send_keys(desc)
time.sleep(1)

repo_submit=driver.find_element_by_xpath("//*[@id='new_repository']/div[3]/button") # This element was dynamically loaded
#that why i had to use xpath
time.sleep(1)
repo_submit.click()
filename="README.md"
if not(os.path.exists(filename)):# checks if diretory exits
    readme_= open("README.md","w+")
    readme_.write('\"# '+desc+'\"')
    readme_.close()

#repo_url=driver.find_element_by_xpath('//*[@id="empty-setup-clone-url"]').get_attribute('value')

#print(repo_url)

driver.close()
