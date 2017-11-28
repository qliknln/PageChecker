from mail import MyMail
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import localtime, strftime, sleep, time
import json, os


class PageChecker(object):
    def __init__(self, url, elem_class, wait_time, log_file, title):
        self.file_str = log_file
        self.url = url
        self.elem_class = elem_class
        self.wait_time = wait_time
        self.title = title

    def check_page(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get(self.url)
        sleep(3)
        try:
            start = time()
            wait = WebDriverWait(driver, self.wait_time)
            element = wait.until(ec.presence_of_element_located((By.CLASS_NAME, self.elem_class)))
            stop = time()
            assert element is not None, 'Page not properly loaded'
            with open(self.file_str, 'a') as f:
                f.write(strftime('%Y-%m-%d %H:%M:%S', localtime()) + ';' + self.url + ';' + self.title + ';Up;' + str(stop-start)+'\r\n')
        except:
            with open(self.file_str, 'a') as f:
                f.write(strftime('%Y-%m-%d %H:%M:%S', localtime()) + ';' + self.url + ';' + self.title + ';Down;' + 'N/A\r\n')
            MyMail.send_mail(self.url + ' Down!', "Sorry for spamming!...still testing", 'qlikatqlik@qlik.com')
        finally:
            driver.quit()


if __name__ == '__main__':
    conf_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config.json')
    with open(conf_file) as json_data:
        d = json.load(json_data)
        for obj in d[1]:
            pc = PageChecker(obj["pageUrl"], obj["elemClass"], obj["elementWait"], d[0]['LogFile'], obj['title'])
            pc.check_page()
            sleep(5) # Wait 5 before testing next page

