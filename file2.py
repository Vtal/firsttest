from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    # Открываем страницу
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем текстовые поля: имя, фамилия, email
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Иван")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Петров")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("test@example.com")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))  # Получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # Формируем путь к файлу

    # Загружаем файл
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    # Нажимаем кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
    # Ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # Закрываем браузер после всех манипуляций
    browser.quit()
