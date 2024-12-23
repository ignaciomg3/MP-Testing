from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService


def get_driver(browser_name="chrome"):
    """Inicializa el WebDriver según el navegador especificado."""
    if browser_name.lower() == "chrome":
        service = Service("drivers/chromedriver.exe")
        driver = webdriver.Chrome(service=service)
    elif browser_name.lower() == "firefox":
        service = FirefoxService("drivers/geckodriver.exe")
        driver = webdriver.Firefox(service=service)
    elif browser_name.lower() == "edge":
        service = EdgeService("drivers/msedgedriver.exe")
        driver = webdriver.Edge(service=service)
    else:
        raise ValueError(f"Navegador no soportado: {browser_name}")

    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver
