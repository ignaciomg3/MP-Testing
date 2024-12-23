from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        """Inicializa el drivers y los selectores de la página."""
        self.driver = driver
        self.url = "http://localhost:3000/login"  # URL del login
        self.username_input = (By.NAME, "loginEmail")
        #self.username_input = (By.ID, "username")  # Selector del campo usuario

        self.password_input = (By.NAME, "password")  # Selector del campo contraseña

        #self.login_button = (By.ID, "login-btn")  # Selector del botón login
        self.login_button = (By.CSS_SELECTOR, 'button[type="submit"]')

    def load(self):
        """Carga la página de login."""
        self.driver.get(self.url)

    def login(self, username, password):
        """Rellena el formulario de login y envía los datos."""
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
