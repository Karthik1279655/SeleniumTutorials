from selenium.webdriver.chrome.service import Service
from selenium import webdriver


class WindowSize:

    def test(self):
        service = Service(executable_path='/home/ee212783/Documents/chromedriver_linux64/chromedriver')
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        baseurl = 'http://10.1.33.16/'
        driver.get(baseurl)
        driver.implicitly_wait(2)
        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")
        print("Height is :: " + str(height))
        print("Width is :: " + str(width))
        driver.quit()


obj = WindowSize()
obj.test()
