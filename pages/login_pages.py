class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://www.irfanlab.my.id/login"
        self.input_email = page.locator("#login-email")
        self.input_password = page.locator("#login-password")
        self.button_submit = page.locator("#login-submit-btn")
        self.feedback_alert = page.locator("#login-feedback")

    def navigate(self):
        self.page.goto(self.url)

    def login(self, email: str, password: str):
        self.input_email.fill(email)
        self.input_password.fill(password)
        self.button_submit.click()