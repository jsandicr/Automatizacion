from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from common.globalparam import img_path
import time
from selenium.common.exceptions import NoSuchElementException
from common.log import Log

class cierraactividad:
    def cierraactividad(self):
        self.wait = WebDriverWait(self.driver, 20)
        try:
            btn_cierrasesionactiva = self.driver.find_element(By.XPATH, "//button[@class = 'p-continuebutton']")
            if btn_cierrasesionactiva.is_displayed():
                btn_cierrasesionactiva.click()
                Log().info(" Se cerro la actividad")   
        except NoSuchElementException:
            pass