import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


class SwitchToWindow:

    def test_Sample(self):
        service = Service(executable_path='/home/ee212783/Documents/chromedriver_linux64/chromedriver')
        driver = webdriver.Chrome(service=service)
        baseurl = 'https://letskodeit.teachable.com/'
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(2)

        practiceButton = driver.find_element(By.XPATH, '//*[@id="navbar"]/div/div/div/ul/li[1]/a')
        practiceButton.click()

        LinkText = driver.find_element(By.XPATH, '//*[@id="block-1069048"]/div/div/div/h1[2]/a')
        LinkText.click()

        parentHandle = driver.current_window_handle
        print("Parent Handle : " + parentHandle)

        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)

        for handle in driver.window_handles:
            print("Handle : " + handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Switched to Window :: " + handle)
                searchBox = driver.find_element(By.NAME, 'course')
                searchBox.send_keys("python")
                time.sleep(2)
                # clickOnSearchBtn = driver.find_element(By.XPATH, '//*[@id="chroPathEleContainer"]/div/span[1]')
                # clickOnSearchBtn.click()
                driver.close()
                break

        time.sleep(2)
        driver.switch_to.window(parentHandle)
        driver.find_element(By.ID, 'name').send_keys('testing')
        time.sleep(1)


obj = SwitchToWindow()
obj.test_Sample()
