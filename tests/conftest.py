import os
import re
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page
from pages.login_pages import LoginPage
from pages.admin_pages import AdminPage

# Muat variabel dari file .env (jika ada di lokal)
load_dotenv()

ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")


@pytest.fixture
def login_to_admin(page: Page):
    """
    Fixture ini bertugas melakukan login sebelum test dijalankan.
    Menggunakan kredensial dari Environment Variable / Secrets.
    """
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    # Assertion / tunggu hingga berpindah ke dashboard /admin
    page.wait_for_url(re.compile("/admin"))

    # YIELD: mengembalikan page yang sudah login
    yield page


@pytest.fixture
def admin_page(login_to_admin: Page) -> AdminPage:
    """
    Fixture pembantu yang langsung mengembalikan instance AdminPage
    dalam keadaan sudah login ke dashboard admin.
    """
    return AdminPage(login_to_admin)