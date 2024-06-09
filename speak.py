from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.headless = True

driver = webdriver.Chrome(options=chrome_options)
website = r"https://ttsmp3.com/"
driver.get(website)
driver.maximize_window()

buttonselection = Select(driver.find_element(by=By.ID, value='sprachwahl'))
buttonselection.select_by_visible_text("British English / Brian")

def speak(Text):
    lengthoftext = len(str(Text))
    if lengthoftext == 0:
        pass
    else:
        print("")
        print(f"AI: {Text}.")
        print("")
        Data = str(Text)
        driver.find_element(By.ID, "voicetext").send_keys(Data)
        driver.find_element(By.ID, value="vorlesenbutton").click()
        sleep(10)
        driver.find_element(By.ID, "voicetext").clear()
        if lengthoftext >= 30:
            sleep(7)
        elif lengthoftext >= 40:
            sleep(8)
        elif lengthoftext >= 55:
            sleep(12)
        elif lengthoftext >= 70:
            sleep(14)
        elif lengthoftext >= 108:
            sleep(16)
        elif lengthoftext >= 120:
            sleep(18)
        else:
            sleep(2)
speak("Hi i'm dhela didi!")