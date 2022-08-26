from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
import csv
import codecs


# Initializing Bot
print('Bot started, if it fails, make sure you havent reached your upload limit Or adjust the sleep time and retry.')
options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-data-dir=C:\\Users\\python\\AppData\\Local\\Google\\Chrome Beta\\User Data")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.binary_location = 'C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe'
driver = webdriver.Chrome(executable_path = "chromedriver.exe", options = options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source":
        "const newProto = navigator.__proto__;"
        "delete newProto.webdriver;"
        "navigator.__proto__ = newProto;"
    })
driver.get('https://www.redbubble.com/portfolio/images/new')

def auto_upload():
    #Read Tags
    file_path = "data/tags.txt"
    #check if file is present
    if os.path.isfile(file_path):
        #open text file in read mode
        text_file = open(file_path, "r")
    
        #read whole file to a string
        data = text_file.read()
    
        #close file
        text_file.close()

    # Loop for uploading
    with open('data/data.csv', 'rb') as f:
        next(f)
        reader = csv.reader(codecs.iterdecode(f, 'utf-8'), delimiter=';')
        for row in reader:
            uploadButton = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[2]/form/div/div[1]/div[1]/input')
            uploadButton.send_keys(row[0])
            time.sleep(10)
            title = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[2]/form/div/div[3]/div/div/div[1]/div/div[1]/input')
            title.send_keys(row[1])
            time.sleep(5)
            description = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[2]/form/div/div[3]/div/div/div[1]/div/div[3]/textarea')
            description.send_keys(row[2])
            time.sleep(5)
            tags = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[2]/form/div/div[3]/div/div/div[1]/div/div[2]/textarea')
            tags.send_keys(data)
            time.sleep(5)
            clicks = driver.find_elements(By.XPATH, '//div[@class="rb-button disable-all green"]')
            for click in clicks:
                try:
                    click = click.click()
                    time.sleep(1)
                except Exception:
                    pass
            time.sleep(2)
            enableSticker = driver.find_element(By.XPATH, '//*[@id="add-new-work"]/section[1]/div/div[14]/div[2]/div[4]/div[2]/div[2]')
            enableSticker.click()
            time.sleep(5)
            media = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[2]/form/section[2]/div[1]/div[1]/div/div/label[2]/input[2]')
            media.click()
            time.sleep(2)
            defaultProduct = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[2]/form/section[2]/div[2]/div[1]/select/option[70]')
            defaultProduct.click()
            time.sleep(2)
            matureButton = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[2]/form/section[2]/div[2]/div[2]/div/label[2]/input')
            matureButton.click()
            time.sleep(2)
            rightsButton = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[2]/form/section[2]/div[3]/input')
            rightsButton.click()
            time.sleep(2)
            saveWorkButton = driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div[2]/form/section[2]/div[4]/div/input')
            saveWorkButton.click()
            time.sleep(20)
            print('You have successfully uploaded your design.')
            restartButton = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div/div/div/div[1]/div/div/div[2]/div/a/span')
            restartButton.click()
            time.sleep(10)

    print('You have successfully uploaded all the designs!')

if __name__ == "__main__":
    auto_upload()