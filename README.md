Selenium Text-to-Speech Bot
This project contains a Python script that uses Selenium WebDriver to interact with the ttsmp3.com text-to-speech service. The script allows you to input text and convert it to speech using the "British English / Brian" voice, running in a headless Chrome browser.

Features
Automated Text-to-Speech: Convert text to speech using the selected voice on ttsmp3.com.
Headless Browser: Operates without a GUI, suitable for server environments.
Dynamic Text Handling: Adjusts sleep times based on the text length to ensure proper speech conversion.
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/selenium-tts-bot.git
cd selenium-tts-bot
Install Dependencies:
Ensure you have Python installed. Then, install the required packages:

bash
Copy code
pip install selenium
Download WebDriver:
Download the appropriate ChromeDriver for your Chrome version from here and ensure it is in your system's PATH.

Usage
Run the Script:

bash
Copy code
python tts_bot.py
Function:

The speak() function takes a string as input, sends it to the ttsmp3.com service, and plays the speech output.
Example:
python
Copy code
speak("Hi, I'm Dhela Didi!")
Code Explanation
python
Copy code
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

# Setting up Chrome in headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.headless = True

# Initializing the WebDriver
driver = webdriver.Chrome(options=chrome_options)
website = r"https://ttsmp3.com/"
driver.get(website)
driver.maximize_window()

# Selecting the voice
buttonselection = Select(driver.find_element(by=By.ID, value='sprachwahl'))
buttonselection.select_by_visible_text("British English / Brian")

# Function to convert text to speech
def speak(Text):
    lengthoftext = len(str(Text))
    if lengthoftext == 0:
        pass
    else:
        print(f"\nAI: {Text}.\n")
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

# Example usage
speak("Hi, I'm Ayush Ranjan!")
Contributing
We welcome contributions! Feel free to fork this repository, create a branch, and submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Special thanks to the developers of ttsmp3.com for their excellent text-to-speech service.
