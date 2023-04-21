from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class ExplicitWaitDemo:

    def test(self):
        service = Service(executable_path='/home/ee212783/Documents/chromedriver_linux64/chromedriver')
        driver = webdriver.Chrome(service=service)
        baseurl = 'http://10.1.33.16/'
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(2)

        emailUser = driver.find_element(By.ID, 'Username')
        emailUser.send_keys('karthi')
        passUser = driver.find_element(By.ID, 'Password')
        passUser.send_keys('Test@123')
        LoginUser = driver.find_element(By.XPATH, '//*[@id="login-div"]/div[3]/div/input')
        LoginUser.click()
        destinationFileName = "/home/ee212783/Desktop/test.png"

        try:
            driver.save_screenshot(destinationFileName)
            print("Screenshot is saved to directory --> :: " + destinationFileName)

        except NotADirectoryError:
            print('Not Found Directory Issue')


obj = ExplicitWaitDemo()
obj.test()
