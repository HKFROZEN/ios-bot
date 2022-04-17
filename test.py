from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import sys

def Start_Web():

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.get("https://www.nike.com/launch")
    return driver
def Find_Item(driver,iten_name):
    '''
    <img alt="Air Jordan 7 'Sapphire' (DJ2636-204) Release Date" class="image-component mod-image-component u-full-width"
    src="https://static.nike.com/a/images/t_prod_ss/w_960,c_limit,f_auto/112b93b2-c6a7-4897-8e6c-59690ec137aa/air-jordan-7-sapphire-dj2636-204-release-date.jpg"
    srcset="" style="opacity: 1; transition: opacity 1s ease 0s;">
    '''
    items = driver.find_elements(By.XPATH, '//img')
    print(items)
    for poss_item in items:
        print(poss_item)
        print(poss_item.value_of_css_property(''))
    return True

def Test(argv):
    item_name = 'Air Jordan 7 \'Sapphire\''
    driver = Start_Web()
    Find_Item(driver,item_name)

def Print_Usage():

    return "py main.py item_name username password"
def main(argv):
    if '-h' in argv:
        print(Print_Usage())
    if '-test' in argv:
        Test(argv)
        return True
    item_name = argv[1] #name of item on sale
    user_info = {'username':argv[2], 'pass':argv[3]}
    Start_Web()

main(sys.argv)
