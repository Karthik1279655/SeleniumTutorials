from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class ImplicitWaitDemo:

    def test_Sample(self):
        options = Options()
        options.add_argument('--headless')
        service = Service(executable_path='/home/ee212783/Documents/chromedriver_linux64/chromedriver')
        driver = webdriver.Chrome(options=options, service=service)
        baseurl = 'http://10.1.33.16/'
        driver.get(baseurl)
        print(driver.title)
        driver.implicitly_wait(2)
        print("Successfully Implicitly Waited the Browser")
        driver.close()


obj = ImplicitWaitDemo()
obj.test_Sample()
