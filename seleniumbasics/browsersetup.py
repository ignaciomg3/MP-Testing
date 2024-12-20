from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# # Configurar las opciones del navegador
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

ruta = "C:/Users/admin/Desktop/chromedriver/chromedriver.exe"
driver =  webdriver.Chrome(service= Service(ruta))
#driver.get("https://morpheuscapital.com.ar/login")
driver.get("http://localhost:3000/login")


# Esperar a que un elemento específico esté presente en la página
# Esto indica que la página se ha cargado completamente
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    print("La página se ha cargado completamente.")
except Exception as e:
    print(f"Se produjo un error al esperar la carga de la página: {e}")


# Localizar el campo de entrada por el atributo 'name'
email_input = driver.find_element(By.NAME, "loginEmail")

# Rellenar el campo de entrada con el correo electrónico
email_input.send_keys("ignacioandres_mongi@epam.com")

# Esperar 2 segundos antes de continuar
time.sleep(2)

# Localizar el campo de entrada de contraseña por el atributo 'name'
password_input = driver.find_element(By.NAME, "password")

# Rellenar el campo de entrada con la contraseña
password_input.send_keys("test1234")

# Esperar 2 segundos antes de continuar
time.sleep(2)


# Localizar el botón por su texto y hacer clic
login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Iniciar sesión')]")
login_button.click()

time.sleep(3)


# Esperar y verificar si un elemento esperado está presente después del clic
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[1]/nav/div/ul/li[2]/a/div[2]/img"))
    )
    print("El test fue exitoso, el clic en el botón 'Iniciar sesión' funcionó correctamente.")
except Exception as e:
    print("El test falló, el clic en el botón 'Iniciar sesión' no produjo el resultado esperado.")



#Cerrar el navegador
driver.quit()
