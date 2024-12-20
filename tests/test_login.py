import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from utils.browser import get_driver
from pages.login_page import LoginPage

@pytest.fixture
def driver():
    """Fixture para inicializar y cerrar el WebDriver."""
    driver = get_driver("chrome")  # Cambia "edge" por el navegador que prefieras
    yield driver
    driver.quit()

def test_login(driver):
    """Prueba de inicio de sesión."""
    login_page = LoginPage(driver)
    login_page.load()  # Navega al login
    login_page.login("ignacioandres_mongi@epam.com", "test1234")  # Credenciales de prueba
    login_button = driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary') and text()='Iniciar sesión']")
    login_button.click()  # Hacer clic en el botón

    """Verifica mediante un assert si el avatar está presente en la página."""
    try:
        driver.find_element(By.XPATH, "//img[@class='' and contains(@src, 'photo/get_photo') and @alt='avatarImg']")
        assert True, "El avatar está presente en la página."
    except NoSuchElementException:
        assert False, "El avatar no está presente en la página."
