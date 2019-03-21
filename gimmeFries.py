from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


def open_page(url):
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    return driver


def input_code(driver, code):
    boxes = driver.find_elements_by_css_selector("input[type='text']")
    input = code.split("-")
    for x in range(len(boxes)):
        boxes[x].send_keys(input[x])

    submit = driver.find_element_by_id("NextButton")
    submit.click()

def first_page(driver):
    buttons = driver.find_elements_by_css_selector("div[class^=Opt")
    for button in buttons:
        txt = str(button.text)
        print(txt)
        if "Dine" in txt:
            button.find_element_by_class_name("radioButtonHolder").click()
    submit = driver.find_element_by_css_selector("input[type='submit']")
    
    submit.click()

def second_page(driver):
    highly_satisfied = driver.find_element_by_class_name("radioBranded")
    highly_satisfied.click()
    submit = driver.find_element_by_css_selector("input[type='submit']")
    
    submit.click()

def third_forth_eigth_page(driver):
    rows = driver.find_elements_by_css_selector("tr[class^=Input")
    for r in rows:
        radio = r.find_element_by_css_selector("td[class^=Opt")
        radio.click()
    submit = driver.find_element_by_css_selector("input[type='submit']")
    
    submit.click()

def fifth_page(driver):
    boxes = driver.find_elements_by_class_name("cataOption")
    for box in boxes:
        txt = box.text
        if "Fries" in txt:
            box.find_element_by_class_name("checkboxholder").click()

    submit = driver.find_element_by_css_selector("input[type='submit']")
    
    submit.click()

def decline_option(driver):
    no = driver.find_elements_by_class_name("radioBranded")[1]
    no.click()
    submit = driver.find_element_by_css_selector("input[type='submit']")
    
    submit.click()

# def seventh_page(driver):
#     radios = driver.find_element_by_class_name("radioBranded")
#     radios.click()
#     submit = driver.find_element_by_css_selector("input[type='submit']")
#     
#     submit.click()

def ninth_page(driver):
    text_box = driver.find_element_by_name("S081000")
    text_box.send_keys("The meal was very good, my kids loved it")
    submit = driver.find_element_by_css_selector("input[type='submit']")
    
    submit.click()

def tenth_page(driver):
    radio = driver.find_element_by_class_name("radioBranded")
    radio.click()
    submit = driver.find_element_by_css_selector("input[type='submit']")
    
    submit.click()

def eleventh_page(driver):
    buttons = driver.find_elements_by_class_name("radioBranded")
    buttons[len(buttons)-1].click()
    submit = driver.find_element_by_css_selector("input[type='submit']")
    
    submit.click()

def favorite(driver):
    mcd = driver.find_element_by_class_name("Opt4")
    bttn = mcd.find_element_by_class_name("radioButtonHolder")
    bttn.click()
    submit = driver.find_element_by_css_selector("input[type='submit']")
    
    submit.click()



def optional_page(driver):
    check = "The following information is optional and for demographic purposes only."
    if (driver.page_source.__contains__(check)):
        submit = driver.find_element_by_css_selector("input[type='submit']")
        submit.click()
    else:
        return

def final(driver):
    code = str(driver.find_element_by_class_name("ValCode").text)
    print(code)
    with open("TwitterBot/testfile.txt", 'a') as f:
        f.write(code[17:]+"\n")


def get_fries(driver):
    first_page(driver)
    second_page(driver)
    third_forth_eigth_page(driver)
    third_forth_eigth_page(driver)
    fifth_page(driver)
    third_forth_eigth_page(driver)
    decline_option(driver)
    third_forth_eigth_page(driver)
    ninth_page(driver)
    tenth_page(driver)
    eleventh_page(driver)
    decline_option(driver)
    favorite(driver)
    optional_page(driver)
    final(driver)


def main():
    code = "02290-06660-31819-14299-00066-6"
    driver = open_page('https://www.mcdvoice.com/')
    for x in range(0,200):
        input_code(driver, code)
        time.sleep(0.5)
        get_fries(driver)
        driver.get('https://www.mcdvoice.com/')
        time.sleep(0.5)

main()
