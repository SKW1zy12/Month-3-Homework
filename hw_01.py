from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Получаем логин и пароль через терминал
username = "BIGOMORI"
password = "Abu20075"

# Настройка Selenium для работы в headless режиме
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

# Устанавливаем время ожидания
wait = WebDriverWait(driver, 20)

# Переходим на сайт csgoad.run
driver.get("https://cs2a.run/")

# Ожидаем загрузки страницы
time.sleep(10)

# Ищем и нажимаем на кнопку "Авторизация"
auth_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn--green') and contains(text(), 'Авторизация')]")))
auth_button.click()

# Ожидаем, чтобы появилось окно авторизации
time.sleep(5)

# Ищем и нажимаем на кнопку "Steam"
steam_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.w-full.overflow-hidden.justify-start')))
steam_button.click()

# Ожидаем загрузки страницы Steam
time.sleep(10)

# Вводим логин
login_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='text' and contains(@class, '_2GBWeup5cttgbTw8FM3tfx')]")))
login_input.send_keys(username)

# Вводим пароль
password_input = driver.find_element(By.XPATH, "//input[@type='password' and contains(@class, '_2GBWeup5cttgbTw8FM3tfx')]")
password_input.send_keys(password)

# Нажимаем Enter для входа
password_input.send_keys(Keys.RETURN)

# Ожидаем 1 минуту
time.sleep(60)

# Нажимаем на кнопку "Войти"
login_button = wait.until(EC.element_to_be_clickable((By.ID, "imageLogin")))
login_button.click()
time.sleep(60)

# Переходим на страницу https://csgoad.run/raffles
driver.get("https://cs2a.run/raffles")

# Функция для нажатия на кнопку "Принять участие" и получения номера билета
def click_participate_button():
    while True:
        try:
            # Находим кнопку "Принять участие"
            button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn--gold') and contains(text(), 'Принять участие')]")))
            
            # Кликаем по кнопке
            ActionChains(driver).move_to_element(button).click(button).perform()
            print("Кнопка 'Принять участие' нажата.")

            # Ожидаем изменения кнопки на элемент с номером билета
            ticket_number_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Ваш билет в розыгрыше:')]")))
            ticket_number = ticket_number_element.text.split(":")[-1].strip()
            print(f"Ваш билет в розыгрыше: {ticket_number}")
            break  # Если номер билета получен, выходим из цикла
        except Exception as e:
            print(f"Ошибка: {e}")
            time.sleep(5)  # Ждем 5 секунд перед повторной попыткой

# Запускаем процесс получения билета
click_participate_button()

# Скрипт продолжит работать, нажимая кнопку каждые 35 минут
try:
    while True:
        time.sleep(2100)  # Ждем 35 минут
        click_participate_button()
except KeyboardInterrupt:
    print("Скрипт завершен пользователем.")
finally:
    driver.quit()  # Закрываем браузер при завершении работы
