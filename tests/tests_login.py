import os
import re
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page, expect
from pages.login_pages import LoginPage

# Muat variabel environment
load_dotenv()

ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "")


def test_login_page_loads(page: Page):
    """
    Test 1: Memverifikasi halaman login berhasil dimuat
    dan elemen judul serta tombol submit tampil.
    """
    login_page = LoginPage(page)
    login_page.navigate()

    # Verifikasi Title dan Heading
    expect(page).to_have_title(re.compile("Admin Login"))
    expect(page.get_by_role("heading", name="Admin Portal")).to_be_visible()

    # Verifikasi elemen input dan tombol submit tampil
    expect(login_page.input_email).to_be_visible()
    expect(login_page.input_password).to_be_visible()
    expect(login_page.button_submit).to_be_visible()


def test_login_with_valid_crendial(page: Page):
    """
    Test 2: Positive Test - Login berhasil dan redirect ke dashboard.
    """
    login_page = LoginPage(page)
    login_page.navigate()

    # Isi email dan password dari Environment Variables
    login_page.login(ADMIN_EMAIL, ADMIN_PASSWORD)

    # Assert url berpindah ke dashboard /admin
    expect(page).to_have_url(re.compile("/admin"))


def test_login_empty_inputs_validation(page: Page):
    """
    Test 3: Validasi ketika form di-submit dalam keadaan kosong.
    Harus memunculkan pesan peringatan 'Please enter both email and password'.
    """
    login_page = LoginPage(page)
    login_page.navigate()

    # Langsung klik tombol submit tanpa mengisi email/password
    login_page.button_submit.click()

    # Assert banner feedback muncul dengan pesan yang sesuai
    expect(login_page.feedback_alert).to_be_visible()
    expect(login_page.feedback_alert).to_contain_text("Please enter both email and password")


def test_login_invalid_email_format(page: Page):
    """
    Test 4: Validasi format email tidak valid.
    Harus memunculkan pesan 'Please enter a valid email'.
    """
    login_page = LoginPage(page)
    login_page.navigate()

    # Isi email dengan format salah
    login_page.login("format_email_salah", "Password123")

    # Assert banner feedback muncul
    expect(login_page.feedback_alert).to_be_visible()
    expect(login_page.feedback_alert).to_contain_text("Please enter a valid email")


def test_login_invalid_credentials(page: Page):
    """
    Test 5: Negative Test - Login dengan kombinasi email/password yang salah.
    Harus memunculkan pesan 'Invalid email or password'.
    """
    login_page = LoginPage(page)
    login_page.navigate()

    # Isi dengan email dan password sembarang
    login_page.login("user.ngasal@gmail.com", "PasswordSalah123")

    # Assert banner feedback muncul dengan notifikasi gagal
    expect(login_page.feedback_alert).to_be_visible()
    expect(login_page.feedback_alert).to_contain_text("Invalid email or password")


