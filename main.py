import unittest
import tkinter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

pady=6
padx=10

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.minimize_window()

window = tkinter.Tk()
window.title("Calculate Roman Number")
window.minsize(width=400, height=300)

title_label = tkinter.Label(text="ROMAN NUMBER TO ARABİC NUMBER", font=("Arial",13, "bold"),bg="lightgray",fg="blue")
title_label.pack(pady=15)

label_roman_number = tkinter.Label(text="Roman/Arabic Number",bg="lightgray", font=("Arial",11, "bold"))
label_roman_number.pack(pady=pady)

entry_roman_number = tkinter.Entry(width=10)
entry_roman_number.pack(pady=pady)

def calculate():
    if len(entry_roman_number.get()) == 0:
        result_label_arabic_number.config(text="Please Do Not Leave Empty!!!")
    else:
        try:
            first_roman_data = entry_roman_number.get().upper()
            entry_roman_number.delete(0,tkinter.END)
            entry_roman_number.insert(0, first_roman_data)
            second_roman_data = entry_roman_number.get()
            calculate_roman_numbers(second_roman_data)
        except:
            result_label_arabic_number.config(text="Please Enter A Valid Roman Number")


button_calculate = tkinter.Button(text="CALCULATE", bg="black", fg="white", font=("Arial",12, "bold"), command=calculate)
button_calculate.pack(pady=pady)

label_arabic_number = tkinter.Label(text="Arabic/Roman Number",bg="lightgray", font=("Arial",11, "bold"))
label_arabic_number.pack(pady=pady)

result_label_arabic_number = tkinter.Label(text="")
result_label_arabic_number.pack(pady=pady)


def calculate_roman_numbers(second_roman_data):
    driver.get("https://www.calculatorsoup.com/calculators/conversions/roman-numeral-converter.php")

    WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "num")))
    driver.find_element(By.NAME, "reset").click()
    driver.find_element(By.NAME, "num").send_keys(second_roman_data)
    WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable((By.NAME, "calculateButton")))
    driver.find_element(By.NAME, "calculateButton").click()

    WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[3]/div[1]/div[2]/form/div[6]/div")))
    result = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[3]/div[1]/div[2]/form/div[6]/div").text.splitlines()[0]
    result_label_arabic_number.config(text=result, font=("Arial",11, "bold"), fg="darkblue")

    return result

    driver.close()

window.mainloop()


'''
class TestCalculateRomanNumbers(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def test_calculate_roman_numbers(self):
        driver = self.driver
        driver.get("https://www.calculatorsoup.com/calculators/conversions/roman-numeral-converter.php")
        self.assertIn("Roman Numeral Converter", driver.title)

        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME,"num")))
        driver.find_element(By.NAME, "reset").click()
        driver.find_element(By.NAME,"num").send_keys("W")
        WebDriverWait(driver, 4).until(expected_conditions.element_to_be_clickable((By.NAME,"calculateButton")))
        driver.find_element(By.NAME, "calculateButton").click()

        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div[1]/div/main/div[3]/div[1]/div[2]/form/div[6]/div")))
        result = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div[3]/div[1]/div[2]/form/div[6]/div").text.splitlines()[0]

        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div[3]/div[1]/div[2]/form/div[6]/div/div")))
        alertMessage = driver.find_element(By.XPATH,"/html/body/div[1]/div/main/div[3]/div[1]/div[2]/form/div[6]/div/div").text.splitlines()[0]

        assert "Enter a valid Roman Numeral or Integer from 1 to 3,999,999." in alertMessage

    def tearDown(self) -> None:
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
'''

