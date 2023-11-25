import json
import os.path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# will need to update everytime the browser and driver version don't match ,so using ChromeDriverManager(),
# it automatically installs the compatible version of ChromeDriver for your installed Chrome Browser. :
#
# chrome_driver_path = "C:\Development\chromedriver-win64\chromedriver.exe"
# driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_driver_path)


def get_morse_data():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=Service(executable_path=ChromeDriverManager().install()))
    driver.get("https://en.wikipedia.org/wiki/Morse_code")

    str_keys = driver.find_elements(By.CSS_SELECTOR, 'tbody td b a')
    str_values = driver.find_elements(By.CSS_SELECTOR, 'td div div div div div a span span')
    my_dict = {key.text: value.text for (key, value) in zip(str_keys, str_values)}

    with open('morse_keys.json', mode='w', encoding='utf-8') as file:
        json.dump(my_dict, file, indent=2, ensure_ascii=False)

    driver.quit()

# executes only if morse_keys.json does not already exists, so only need to execute once
if not os.path.exists('morse_keys.json'):
    get_morse_data()


def method1():
    morse_str = ''
    for char in input_str:
        found = False
        for key in my_dict.keys():
            if char in key:
                morse_str += my_dict[key]
                found = True
                break
        if not found:
            morse_str += char
    return morse_str


# METHOD #2
def method2():
    uppercase_dict = {k[0].upper(): v for (k, v) in my_dict.items()}
    morse_str = ''

    for char in input_str.upper():
        if char in uppercase_dict:
            morse_str += uppercase_dict[char]
        else:
            morse_str += char

    return morse_str


input_str = input('Enter your String: ')
with open('morse_keys.json', encoding='utf-8') as my_file:
    my_dict = json.load(my_file)

print(f'\nUSING METHOD1:\nYour morse coded string is:\n{method1()}\n')

print(f'\nUSING METHOD2:\nYour morse codes string is:\n{method2()}')
